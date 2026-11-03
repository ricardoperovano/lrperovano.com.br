#!/usr/bin/env python3
"""Gera o blog estático da PEROVANO a partir de _conteudo/artigos/*.md.

Saídas:
  blog/index.html, blog/<slug>/index.html, blog/feed.xml,
  sitemap.xml, robots.txt e o bloco "artigos recentes" do index.html
  (entre os marcadores <!-- artigos:inicio --> e <!-- artigos:fim -->).

Uso:
  python3 scripts/build_blog.py          # gera tudo
  python3 scripts/build_blog.py --og     # também gera as imagens de compartilhamento
                                         # (precisa do google-chrome-stable ou chromium)

Sem dependências externas: o Markdown aceito é um subconjunto documentado no README.
"""
from __future__ import annotations

import html
import json
import math
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "_conteudo" / "artigos"
OUT = ROOT / "blog"
SITE = "https://lrperovano.com.br"
AUTHOR = "Ricardo Perovano"
WHATSAPP = "5527998553591"
EMAIL = "contato@lrperovano.com.br"
CATEGORIES = ["Sites", "Sistemas", "Automação", "Inteligência artificial", "Gestão de projetos"]
# Artigos com data futura ficam fora até o dia da publicação (rode o build de novo nesse dia).
SCHEDULED: list["Article"] = []
PUBLISHED: set[str] = set()
MONTHS = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
          "agosto", "setembro", "outubro", "novembro", "dezembro"]


# ---------------------------------------------------------------------------
# Modelo
# ---------------------------------------------------------------------------
@dataclass
class Article:
    slug: str
    title: str
    description: str
    date: date
    updated: date
    category: str
    keywords: str
    body_md: str
    body_html: str = ""
    toc: list[tuple[str, str]] = field(default_factory=list)
    faq: list[tuple[str, str]] = field(default_factory=list)
    words: int = 0

    @property
    def url(self) -> str:
        return f"/blog/{self.slug}/"

    @property
    def reading_minutes(self) -> int:
        return max(1, math.ceil(self.words / 200))

    @property
    def og_image(self) -> str:
        if (OUT / self.slug / "og.png").exists():
            return f"{SITE}/blog/{self.slug}/og.png"
        return f"{SITE}/og-image.png"


def fail(msg: str) -> None:
    print(f"erro: {msg}", file=sys.stderr)
    sys.exit(1)


def parse_front_matter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        fail(f"{path.name}: front matter ausente")
    meta: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if not line.strip():
            continue
        key, _, value = line.partition(":")
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        meta[key.strip()] = value
    return meta, m.group(2).strip() + "\n"


def load_articles() -> list[Article]:
    articles = []
    for path in sorted(SRC.glob("*.md")):
        meta, body = parse_front_matter(path)
        for key in ("title", "description", "date", "category"):
            if not meta.get(key):
                fail(f"{path.name}: campo '{key}' obrigatório")
        if meta["category"] not in CATEGORIES:
            fail(f"{path.name}: categoria '{meta['category']}' fora da lista {CATEGORIES}")
        published = date.fromisoformat(meta["date"])
        art = Article(
            slug=path.stem,
            title=meta["title"],
            description=meta["description"],
            date=published,
            updated=date.fromisoformat(meta.get("updated") or meta["date"]),
            category=meta["category"],
            keywords=meta.get("keywords", ""),
            body_md=body,
        )
        if meta.get("draft", "").lower() in ("true", "sim", "yes"):
            continue
        if published > date.today():
            SCHEDULED.append(art)
            continue
        articles.append(art)
    articles.sort(key=lambda a: (a.date, a.title), reverse=True)
    return articles


# ---------------------------------------------------------------------------
# Markdown (subconjunto)
# ---------------------------------------------------------------------------
def slugify(text: str) -> str:
    import unicodedata
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def inline(text: str) -> str:
    codes: list[str] = []

    def keep_code(m: re.Match) -> str:
        codes.append(f"<code>{html.escape(m.group(1))}</code>")
        return f"\x00{len(codes) - 1}\x00"

    text = re.sub(r"`([^`]+)`", keep_code, text)
    text = html.escape(text, quote=False)

    def link(m: re.Match) -> str:
        label, href = m.group(1), html.unescape(m.group(2))
        target = re.match(r"^/blog/([a-z0-9-]+)/$", href)
        if target and PUBLISHED and target.group(1) not in PUBLISHED:
            return label
        attrs = f'href="{html.escape(href)}"'
        if re.match(r"https?://", href) and not href.startswith(SITE):
            attrs += ' target="_blank" rel="noopener"'
        return f"<a {attrs}>{label}</a>"

    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", text)
    return re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m.group(1))], text)


def strip_tags(s: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", s))


def render_markdown(art: Article) -> None:
    out: list[str] = []
    para: list[str] = []
    list_kind: str | None = None
    quote: list[str] = []
    used_ids: set[str] = set()
    in_faq = False
    faq_q: str | None = None
    faq_a: list[str] = []

    def flush_faq_answer() -> None:
        nonlocal faq_q, faq_a
        if faq_q and faq_a:
            art.faq.append((faq_q, " ".join(faq_a)))
        faq_q, faq_a = None, []

    def flush() -> None:
        nonlocal para, list_kind, quote
        if para:
            rendered = inline(" ".join(para))
            out.append(f"<p>{rendered}</p>")
            if in_faq and faq_q:
                faq_a.append(strip_tags(rendered))
            para = []
        if list_kind:
            out.append(f"</{list_kind}>")
            list_kind = None
        if quote:
            out.append(f"<blockquote><p>{inline(' '.join(quote))}</p></blockquote>")
            quote = []

    def heading_id(text: str) -> str:
        base = slugify(text) or "secao"
        hid, n = base, 2
        while hid in used_ids:
            hid, n = f"{base}-{n}", n + 1
        used_ids.add(hid)
        return hid

    for raw in art.body_md.splitlines():
        line = raw.rstrip()
        if not line.strip():
            flush()
            continue
        if line.startswith("# "):
            fail(f"{art.slug}: use ## e ###; o H1 vem do título")
        m = re.match(r"^(#{2,3})\s+(.*)$", line)
        if m:
            flush()
            level, text = len(m.group(1)), m.group(2).strip()
            hid = heading_id(text)
            if level == 2:
                flush_faq_answer()
                in_faq = slugify(text).startswith("perguntas-frequentes")
                art.toc.append((hid, strip_tags(inline(text))))
            elif in_faq:
                flush_faq_answer()
                faq_q = strip_tags(inline(text))
            out.append(f'<h{level} id="{hid}">{inline(text)}</h{level}>')
            continue
        m = re.match(r"^(?:[-*]|(\d+)\.)\s+(.*)$", line)
        if m:
            kind = "ol" if m.group(1) else "ul"
            if para or quote:
                flush()
            if list_kind != kind:
                if list_kind:
                    out.append(f"</{list_kind}>")
                out.append(f"<{kind}>")
                list_kind = kind
            out.append(f"<li>{inline(m.group(2))}</li>")
            if in_faq and faq_q:
                faq_a.append(strip_tags(inline(m.group(2))))
            continue
        if line.startswith(">"):
            if para or list_kind:
                flush()
            quote.append(line.lstrip("> ").strip())
            continue
        if list_kind and raw.startswith(("  ", "\t")):
            # continuação de item de lista
            out[-1] = out[-1][:-5] + " " + inline(line.strip()) + "</li>"
            continue
        if list_kind or quote:
            flush()
        para.append(line.strip())
    flush()
    flush_faq_answer()
    art.body_html = "\n".join(out)
    art.words = len(re.findall(r"\w+", strip_tags(art.body_html)))


# ---------------------------------------------------------------------------
# Templates
# ---------------------------------------------------------------------------
def e(s: str) -> str:
    return html.escape(s, quote=True)


def fmt_date(d: date) -> str:
    return f"{d.day} de {MONTHS[d.month - 1]} de {d.year}"


GA_TAG = """  <!-- Google tag (gtag.js) com consentimento: o Analytics só carrega após "Aceitar" no aviso de cookies (ver assets/js/site.js). -->
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('consent', 'default', {
      analytics_storage: 'denied',
      ad_storage: 'denied',
      ad_user_data: 'denied',
      ad_personalization: 'denied'
    });
    window.loadAnalytics = function () {
      if (window.__gaLoaded) return;
      window.__gaLoaded = true;
      gtag('consent', 'update', { analytics_storage: 'granted' });
      gtag('js', new Date());
      gtag('config', 'G-KGNMPTML28');
      var s = document.createElement('script');
      s.async = true;
      s.src = 'https://www.googletagmanager.com/gtag/js?id=G-KGNMPTML28';
      document.head.appendChild(s);
    };
    try { if (localStorage.getItem('perovano-cookies') === 'aceito') window.loadAnalytics(); } catch (e) {}
  </script>
"""


def head(title: str, description: str, canonical: str, *, og_type: str = "website",
         og_image: str = f"{SITE}/og-image.png", extra: str = "") -> str:
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
{GA_TAG}  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{e(title)}</title>
  <meta name="description" content="{e(description)}">
  <meta name="theme-color" content="#143C3A">
  <link rel="canonical" href="{e(canonical)}">
  <link rel="icon" type="image/svg+xml" href="/assets/img/favicon.svg">
  <link rel="icon" type="image/x-icon" href="/favicon.ico" sizes="32x32">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="alternate" type="application/rss+xml" title="Blog da PEROVANO" href="/blog/feed.xml">
  <meta property="og:site_name" content="PEROVANO">
  <meta property="og:title" content="{e(title)}">
  <meta property="og:description" content="{e(description)}">
  <meta property="og:type" content="{og_type}">
  <meta property="og:locale" content="pt_BR">
  <meta property="og:url" content="{e(canonical)}">
  <meta property="og:image" content="{e(og_image)}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="{e(og_image)}">
{extra}  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,400..700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/css/site.css">
  <script>document.documentElement.classList.add('js');</script>
  <script src="/assets/js/site.js" defer></script>
</head>
<body>
  <a class="skip-link" href="#conteudo">Pular para o conteúdo</a>
"""


HEADER = """  <header class="site-header">
    <div class="container site-header__inner">
      <a class="brand" href="/" aria-label="PEROVANO — Engenharia de software, página inicial">
        <span class="brand__name">PEROVANO</span>
        <span class="brand__descriptor">Engenharia de software</span>
      </a>

      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="menu-principal">
        <span class="sr-only">Abrir menu</span>
        <span class="nav-toggle__bars" aria-hidden="true"><span></span><span></span><span></span></span>
      </button>

      <nav class="site-nav" id="menu-principal" aria-label="Principal">
        <ul class="site-nav__list">
          <li><a href="/#projetos">Projetos</a></li>
          <li><a href="/#solucoes">Soluções</a></li>
          <li><a href="/#como-trabalhamos">Como trabalhamos</a></li>
          <li><a href="/blog/"{blog_current}>Blog</a></li>
          <li><a href="/#contato">Contato</a></li>
        </ul>
        <a class="lang-switch" href="/en/" hreflang="en" lang="en" data-lang="en"><span aria-hidden="true">EN</span><span class="sr-only">English version (home page)</span></a>
        <a class="btn btn--accent btn--small" href="/#contato">Vamos conversar</a>
      </nav>
    </div>
  </header>
"""

FOOTER = f"""  <footer class="site-footer">
    <div class="container">
      <div class="site-footer__top">
        <div>
          <a class="brand brand--footer" href="/" aria-label="PEROVANO — Engenharia de software, página inicial">
            <span class="brand__name">PEROVANO</span>
            <span class="brand__descriptor">Engenharia de software</span>
          </a>
          <p class="site-footer__legal">L R PEROVANO LTDA</p>
        </div>

        <nav aria-label="Rodapé">
          <h2>Navegação</h2>
          <ul>
            <li><a href="/#projetos">Projetos</a></li>
            <li><a href="/#solucoes">Soluções</a></li>
            <li><a href="/#como-trabalhamos">Como trabalhamos</a></li>
            <li><a href="/blog/">Blog</a></li>
            <li><a href="/#contato">Contato</a></li>
            <li><a href="/privacy.html">Política de Privacidade</a></li>
          </ul>
        </nav>

        <div>
          <h2>Contato</h2>
          <ul>
            <li><a href="https://wa.me/{WHATSAPP}" target="_blank" rel="noopener">WhatsApp: +55 27 99855-3591<span class="sr-only"> (abre em nova aba)</span></a></li>
            <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
            <li><a href="https://www.linkedin.com/in/xhricardo/" target="_blank" rel="noopener">LinkedIn<span class="sr-only"> (abre em nova aba)</span></a></li>
            <li><a href="https://github.com/ricardoperovano" target="_blank" rel="noopener">GitHub<span class="sr-only"> (abre em nova aba)</span></a></li>
          </ul>
        </div>
      </div>

      <div class="site-footer__bottom">
        <p>© <span data-year>{date.today().year}</span> L R PEROVANO LTDA</p>
        <p>lrperovano.com.br</p>
      </div>
    </div>
  </footer>
</body>
</html>
"""


def json_ld(data: object) -> str:
    payload = json.dumps(data, ensure_ascii=False, indent=2).replace("</", "<\\/")
    return f'  <script type="application/ld+json">\n{payload}\n  </script>\n'


ORG = {
    "@type": "Organization",
    "@id": f"{SITE}/#organizacao",
    "name": "PEROVANO",
    "legalName": "L R PEROVANO LTDA",
    "url": f"{SITE}/",
    "logo": f"{SITE}/apple-touch-icon.png",
}


def category_url(category: str) -> str:
    return f"/blog/categoria/{slugify(category)}/"


CATEGORY_INTRO = {
    "Sites": "Sites institucionais, landing pages, SEO, velocidade e tudo o que faz um site gerar contatos.",
    "Sistemas": "Sistemas sob medida, aplicativos, SaaS e as decisões para tirar um software do papel.",
    "Automação": "Integrações entre sistemas, APIs, pagamentos e automações que eliminam trabalho repetitivo.",
    "Inteligência artificial": "Como aplicar IA na empresa com critério: assistentes, agentes, chatbots e busca em documentos.",
    "Gestão de projetos": "Como contratar, acompanhar e manter um projeto de software sem surpresas.",
}


def article_card(art: Article, heading: str = "h3") -> str:
    return f"""          <article class="post-card" data-category="{e(art.category)}" data-search="{e((art.title + ' ' + art.description + ' ' + art.keywords).lower())}">
            <p class="post-card__meta"><span>{e(art.category)}</span><span>{art.reading_minutes} min de leitura</span></p>
            <{heading} class="post-card__title"><a href="{art.url}">{e(art.title)}</a></{heading}>
            <p class="post-card__excerpt">{e(art.description)}</p>
          </article>"""


def related(art: Article, articles: list[Article], n: int = 3) -> list[Article]:
    linked = set(re.findall(r"\(/blog/([a-z0-9-]+)/\)", art.body_md))
    others = [a for a in articles if a.slug != art.slug]
    others.sort(key=lambda a: (a.category != art.category, a.slug in linked, a.title))
    return others[:n]


def render_article(art: Article, articles: list[Article]) -> str:
    canonical = f"{SITE}{art.url}"
    ld = [
        {
            "@context": "https://schema.org",
            "@type": "BlogPosting",
            "headline": art.title,
            "description": art.description,
            "datePublished": art.date.isoformat(),
            "dateModified": art.updated.isoformat(),
            "inLanguage": "pt-BR",
            "articleSection": art.category,
            "keywords": art.keywords,
            "wordCount": art.words,
            "image": art.og_image,
            "mainEntityOfPage": canonical,
            "url": canonical,
            "author": {"@type": "Person", "name": AUTHOR, "url": f"{SITE}/#sobre"},
            "publisher": ORG,
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Início", "item": f"{SITE}/"},
                {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{SITE}/blog/"},
                {"@type": "ListItem", "position": 3, "name": art.category, "item": f"{SITE}{category_url(art.category)}"},
                {"@type": "ListItem", "position": 4, "name": art.title, "item": canonical},
            ],
        },
    ]
    if art.faq:
        ld.append({
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                for q, a in art.faq
            ],
        })
    extra = (
        f'  <meta property="article:published_time" content="{art.date.isoformat()}">\n'
        f'  <meta property="article:modified_time" content="{art.updated.isoformat()}">\n'
        f'  <meta property="article:section" content="{e(art.category)}">\n'
        + "".join(json_ld(x) for x in ld)
    )
    toc = "\n".join(f'              <li><a href="#{hid}">{e(t)}</a></li>' for hid, t in art.toc)
    cards = "\n".join(article_card(a) for a in related(art, articles))
    wa_text = f"Olá! Li o artigo \"{art.title}\" e gostaria de conversar sobre um projeto."
    from urllib.parse import quote
    updated = (f' <span>Atualizado em <time datetime="{art.updated.isoformat()}">{fmt_date(art.updated)}</time></span>'
               if art.updated != art.date else "")
    return (
        head(f"{art.title} | PEROVANO", art.description, canonical, og_type="article",
             og_image=art.og_image, extra=extra)
        + HEADER.replace("{blog_current}", ' aria-current="page"')
        + f"""
  <main id="conteudo">
    <article class="post">
      <header class="post__header">
        <div class="container">
          <nav class="breadcrumb" aria-label="Você está em">
            <ol>
              <li><a href="/">Início</a></li>
              <li><a href="/blog/">Blog</a></li>
              <li><a href="{category_url(art.category)}">{e(art.category)}</a></li>
            </ol>
          </nav>
          <h1 class="post__title">{e(art.title)}</h1>
          <p class="post__lead">{e(art.description)}</p>
          <p class="post__meta">
            <span>Por {e(AUTHOR)}</span>
            <span><time datetime="{art.date.isoformat()}">{fmt_date(art.date)}</time></span>{updated}
            <span>{art.reading_minutes} min de leitura</span>
          </p>
        </div>
      </header>

      <div class="container post__layout">
        <aside class="post__toc" aria-labelledby="toc-titulo">
          <h2 id="toc-titulo">Neste artigo</h2>
          <ol>
{toc}
          </ol>
        </aside>

        <div class="post__body prose-article">
{art.body_html}
        </div>
      </div>
    </article>

    <section class="post-cta on-dark" aria-labelledby="cta-titulo">
      <div class="container post-cta__inner">
        <div>
          <h2 id="cta-titulo">Quer aplicar isso na sua empresa?</h2>
          <p>Conte o seu desafio. A primeira conversa serve para entender o contexto e indicar o melhor caminho — seja um site, um sistema ou uma automação.</p>
        </div>
        <div class="post-cta__actions">
          <a class="btn btn--accent" href="https://wa.me/{WHATSAPP}?text={quote(wa_text)}" target="_blank" rel="noopener">Conversar pelo WhatsApp<span class="sr-only"> (abre em nova aba)</span></a>
          <a class="btn btn--outline-light" href="/#projetos">Ver projetos no ar</a>
        </div>
      </div>
    </section>

    <section class="section related" aria-labelledby="relacionados-titulo">
      <div class="container">
        <h2 id="relacionados-titulo" class="related__title">Continue lendo</h2>
        <div class="post-grid">
{cards}
        </div>
      </div>
    </section>
  </main>

"""
        + FOOTER
    )


def chips_nav(used: list[str], current: str | None, *, filters: bool) -> str:
    """Chips de categoria. No índice (filters=True) também filtram a lista sem recarregar."""
    def chip(label: str, href: str, value: str, anchor: str) -> str:
        attrs = f' data-filter="{e(value)}" data-anchor="{anchor}"' if filters else ""
        cur = ' aria-current="page"' if (current == value or (current is None and value == "" and not filters)) else ""
        return f'          <a class="chip" href="{href}"{attrs}{cur}>{e(label)}</a>'
    items = [chip("Todos", "/blog/", "", "#todos")]
    items += [chip(c, category_url(c), c, f"#{slugify(c)}") for c in used]
    return '        <nav class="chips" aria-label="Categorias">\n' + "\n".join(items) + "\n        </nav>"


SEARCH = """        <div class="blog-search" hidden>
          <label for="busca-artigos">Buscar artigos</label>
          <input id="busca-artigos" type="search" autocomplete="off" placeholder="Ex.: aplicativo, Pix, chatbot, SEO">
        </div>"""


def render_index(articles: list[Article]) -> str:
    canonical = f"{SITE}/blog/"
    title = "Blog | PEROVANO — sites, sistemas, automação e IA"
    description = ("Artigos práticos sobre sites, sistemas sob medida, aplicativos, integrações, automação e "
                   "inteligência artificial para quem precisa decidir e contratar tecnologia.")
    ld = {
        "@context": "https://schema.org",
        "@type": "Blog",
        "name": "Blog da PEROVANO",
        "url": canonical,
        "inLanguage": "pt-BR",
        "publisher": ORG,
        "blogPost": [
            {"@type": "BlogPosting", "headline": a.title, "url": f"{SITE}{a.url}",
             "datePublished": a.date.isoformat()}
            for a in articles
        ],
    }
    used = [c for c in CATEGORIES if any(a.category == c for a in articles)]
    groups = []
    for c in used:
        items = [a for a in articles if a.category == c]
        cards = "\n".join(article_card(a, "h3") for a in items)
        groups.append(f"""      <section class="blog-group" id="{slugify(c)}" data-category="{e(c)}" aria-labelledby="cat-{slugify(c)}">
        <div class="blog-group__head">
          <h2 class="blog-group__title" id="cat-{slugify(c)}">{e(c)}</h2>
          <a class="text-link" href="{category_url(c)}">{len(items)} artigos sobre {e(c.lower() if c != "Inteligência artificial" else c)}</a>
        </div>
        <div class="post-grid">
{cards}
        </div>
      </section>""")
    return (
        head(title, description, canonical, extra=json_ld(ld))
        + HEADER.replace("{blog_current}", ' aria-current="page"')
        + f"""
  <main id="conteudo">
    <header class="blog-hero on-dark">
      <div class="container">
        <h1 class="blog-hero__title">Tecnologia explicada para quem decide.</h1>
        <p class="blog-hero__lead">{len(articles)} artigos práticos sobre sites, sistemas sob medida, aplicativos, integrações, automação e inteligência artificial — com critérios para decidir, contratar e acompanhar um projeto.</p>
{SEARCH}
{chips_nav(used, "", filters=True)}
      </div>
    </header>

    <div class="container blog-list" id="todos">
      <p class="blog-empty" role="status" hidden></p>
{chr(10).join(groups)}
    </div>
  </main>

"""
        + FOOTER
    )


def render_category(category: str, articles: list[Article]) -> str:
    items = [a for a in articles if a.category == category]
    canonical = f"{SITE}{category_url(category)}"
    intro = CATEGORY_INTRO.get(category, "")
    title = f"{category}: artigos e guias práticos | PEROVANO"
    description = f"{intro} {len(items)} artigos da PEROVANO sobre {category.lower() if category != 'Inteligência artificial' else category}."
    ld = [
        {
            "@context": "https://schema.org",
            "@type": "CollectionPage",
            "name": f"{category} — Blog da PEROVANO",
            "url": canonical,
            "inLanguage": "pt-BR",
            "publisher": ORG,
            "mainEntity": {
                "@type": "ItemList",
                "itemListElement": [
                    {"@type": "ListItem", "position": i + 1, "url": f"{SITE}{a.url}", "name": a.title}
                    for i, a in enumerate(items)
                ],
            },
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Início", "item": f"{SITE}/"},
                {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{SITE}/blog/"},
                {"@type": "ListItem", "position": 3, "name": category, "item": canonical},
            ],
        },
    ]
    used = [c for c in CATEGORIES if any(a.category == c for a in articles)]
    cards = "\n".join(article_card(a, "h2") for a in items)
    return (
        head(title, description, canonical, extra="".join(json_ld(x) for x in ld))
        + HEADER.replace("{blog_current}", ' aria-current="page"')
        + f"""
  <main id="conteudo">
    <header class="blog-hero on-dark">
      <div class="container">
        <nav class="breadcrumb breadcrumb--dark" aria-label="Você está em">
          <ol>
            <li><a href="/">Início</a></li>
            <li><a href="/blog/">Blog</a></li>
          </ol>
        </nav>
        <h1 class="blog-hero__title">{e(category)}</h1>
        <p class="blog-hero__lead">{e(intro)}</p>
{chips_nav(used, category, filters=False)}
      </div>
    </header>

    <div class="container blog-list">
      <div class="post-grid">
{cards}
      </div>
    </div>
  </main>

"""
        + FOOTER
    )


def render_home_block(articles: list[Article]) -> str:
    cards = "\n".join(article_card(a) for a in articles[:3])
    return f"""<!-- artigos:inicio -->
    <section class="section section--surface" id="blog" aria-labelledby="titulo-blog">
      <div class="container">
        <div class="home-blog__head">
          <div>
            <span class="kicker">Blog</span>
            <h2 id="titulo-blog">Tecnologia explicada para quem decide.</h2>
          </div>
          <a class="btn btn--secondary" href="/blog/">Ver todos os artigos</a>
        </div>
        <div class="post-grid">
{cards}
        </div>
      </div>
    </section>
    <!-- artigos:fim -->"""


def render_feed(articles: list[Article]) -> str:
    from email.utils import format_datetime
    from datetime import datetime, timezone

    def rfc(d: date) -> str:
        return format_datetime(datetime(d.year, d.month, d.day, 9, tzinfo=timezone.utc))

    items = "\n".join(f"""    <item>
      <title>{e(a.title)}</title>
      <link>{SITE}{a.url}</link>
      <guid isPermaLink="true">{SITE}{a.url}</guid>
      <pubDate>{rfc(a.date)}</pubDate>
      <category>{e(a.category)}</category>
      <description>{e(a.description)}</description>
    </item>""" for a in articles)
    last = max((a.updated for a in articles), default=date.today())
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>Blog da PEROVANO</title>
    <link>{SITE}/blog/</link>
    <atom:link href="{SITE}/blog/feed.xml" rel="self" type="application/rss+xml"/>
    <description>Sites, sistemas sob medida, integrações, automação e inteligência artificial para empresas.</description>
    <language>pt-BR</language>
    <lastBuildDate>{rfc(last)}</lastBuildDate>
{items}
  </channel>
</rss>
"""


def render_sitemap(articles: list[Article]) -> str:
    last = max((a.updated for a in articles), default=date.today()).isoformat()
    # Páginas com versão em inglês: (pt, en). Cada uma declara a outra como alternativa.
    pairs = [(f"{SITE}/", f"{SITE}/en/"), (f"{SITE}/privacy.html", f"{SITE}/en/privacy.html")]

    def alternates(pt: str, en: str) -> str:
        return (f'<xhtml:link rel="alternate" hreflang="pt-BR" href="{pt}"/>'
                f'<xhtml:link rel="alternate" hreflang="en" href="{en}"/>'
                f'<xhtml:link rel="alternate" hreflang="x-default" href="{en}"/>')

    entries = []
    for pt, en in pairs:
        lm = f"<lastmod>{last}</lastmod>" if pt == f"{SITE}/" else ""
        entries.append(f"  <url><loc>{pt}</loc>{lm}{alternates(pt, en)}</url>")
        entries.append(f"  <url><loc>{en}</loc>{lm}{alternates(pt, en)}</url>")
    urls = [(f"{SITE}/blog/", last)]
    for c in CATEGORIES:
        dates = [a.updated for a in articles if a.category == c]
        if dates:
            urls.append((f"{SITE}{category_url(c)}", max(dates).isoformat()))
    urls += [(f"{SITE}{a.url}", a.updated.isoformat()) for a in articles]
    entries += [f"  <url><loc>{loc}</loc><lastmod>{lm}</lastmod></url>" for loc, lm in urls]
    body = "\n".join(entries)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
            f"{body}\n</urlset>\n")


# ---------------------------------------------------------------------------
# Imagens de compartilhamento (opcional)
# ---------------------------------------------------------------------------
OG_TEMPLATE = """<!DOCTYPE html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,400..700&display=swap" rel="stylesheet">
<style>
html,body{{margin:0;width:1200px;height:630px;overflow:hidden;background:#143C3A;color:#F4F2EB;font-family:Inter,sans-serif}}
.b{{position:absolute;left:88px;top:76px}} .n{{font-weight:700;font-size:34px;letter-spacing:.04em;line-height:1}}
.d{{font-weight:600;font-size:13px;letter-spacing:.24em;text-transform:uppercase;margin-top:9px;color:#D7E6A5}}
.c{{position:absolute;right:88px;top:80px;font-weight:600;font-size:22px;color:#D7E6A5}}
h1{{position:absolute;left:88px;right:300px;bottom:84px;margin:0;font-size:{size}px;line-height:1.06;letter-spacing:-.035em;font-weight:700}}
svg{{position:absolute;right:0;bottom:0;width:260px;height:164px}}
</style></head><body>
<div class="b"><div class="n">PEROVANO</div><div class="d">Engenharia de software</div></div>
<div class="c">{category}</div>
<h1>{title}</h1>
<svg viewBox="0 0 380 240"><path fill="#D7E6A5" d="M0 240V110Q0 0 110 0H380V240Z"/></svg>
</body></html>"""


def build_og(articles: list[Article]) -> None:
    chrome = shutil.which("google-chrome-stable") or shutil.which("chromium") or shutil.which("google-chrome")
    if not chrome:
        print("aviso: Chrome não encontrado; imagens de compartilhamento não geradas")
        return
    with tempfile.TemporaryDirectory() as tmp:
        for a in articles:
            size = 64 if len(a.title) <= 48 else 56 if len(a.title) <= 64 else 50
            page = Path(tmp) / f"{a.slug}.html"
            page.write_text(OG_TEMPLATE.format(title=e(a.title), category=e(a.category), size=size), encoding="utf-8")
            target = OUT / a.slug / "og.png"
            target.parent.mkdir(parents=True, exist_ok=True)
            subprocess.run([chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                            "--window-size=1200,630", "--virtual-time-budget=6000",
                            f"--screenshot={target}", page.as_uri()],
                           check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"og: {target.relative_to(ROOT)}")


# ---------------------------------------------------------------------------
def check_links(articles: list[Article]) -> list[str]:
    slugs = {a.slug for a in articles}
    problems = []
    for a in articles:
        for target in re.findall(r"\]\((/blog/[^)]*)\)", a.body_md):
            m = re.match(r"^/blog/([a-z0-9-]+)/$", target)
            scheduled = {x.slug for x in SCHEDULED}
            if m and m.group(1) in scheduled:
                continue  # vira texto simples até o artigo ser publicado
            if not m or m.group(1) not in slugs:
                problems.append(f"{a.slug}: link interno quebrado {target}")
        for target in re.findall(r"\]\((/[^)]*)\)", a.body_md):
            if not target.startswith(("/blog/", "/#", "/privacy.html")) and target != "/":
                problems.append(f"{a.slug}: link interno desconhecido {target}")
    return problems


def main() -> None:
    articles = load_articles()
    if not articles:
        fail("nenhum artigo em _conteudo/artigos")
    PUBLISHED.update(a.slug for a in articles)
    for a in articles:
        render_markdown(a)

    problems = check_links(articles)
    for p in problems:
        print(f"aviso: {p}")

    if "--og" in sys.argv:
        build_og(articles)

    # limpa páginas de artigos removidos (preserva og.png de artigos existentes)
    slugs = {a.slug for a in articles}
    if OUT.exists():
        for d in OUT.iterdir():
            if d.is_dir() and d.name not in slugs and d.name != "categoria":
                shutil.rmtree(d)
    for a in articles:
        target = OUT / a.slug / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(render_article(a, articles), encoding="utf-8")
    (OUT / "index.html").write_text(render_index(articles), encoding="utf-8")
    used = [c for c in CATEGORIES if any(x.category == c for x in articles)]
    cat_root = OUT / "categoria"
    if cat_root.exists():
        shutil.rmtree(cat_root)
    for c in used:
        target = cat_root / slugify(c) / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(render_category(c, articles), encoding="utf-8")
    (OUT / "feed.xml").write_text(render_feed(articles), encoding="utf-8")
    (ROOT / "sitemap.xml").write_text(render_sitemap(articles), encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")

    home = ROOT / "index.html"
    text = home.read_text(encoding="utf-8")
    block = render_home_block(articles)
    new, n = re.subn(r"<!-- artigos:inicio -->.*?<!-- artigos:fim -->", lambda _: block, text, flags=re.S)
    if n != 1:
        fail("marcadores <!-- artigos:inicio --> / <!-- artigos:fim --> não encontrados no index.html")
    home.write_text(new, encoding="utf-8")

    for a in articles:
        print(f"{a.url}  {a.words} palavras  {a.reading_minutes} min  {len(a.toc)} seções  {len(a.faq)} FAQ")
    for a in sorted(SCHEDULED, key=lambda x: x.date):
        print(f"agendado: {a.url} para {a.date.isoformat()} (rode o build nesse dia)")
    print(f"{len(articles)} artigos gerados; {len(SCHEDULED)} agendados; {len(problems)} avisos")


if __name__ == "__main__":
    main()
