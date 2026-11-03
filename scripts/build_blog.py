#!/usr/bin/env python3
"""Gera o blog estático da PEROVANO, em português e em inglês.

Fontes:
  _conteudo/artigos/*.md      → /blog/<slug>/        (português)
  _conteudo/en/articles/*.md  → /en/blog/<slug>/     (inglês; front matter `pt:` aponta o original)

Saídas, para cada idioma: índice do blog, artigos, páginas de categoria, feed RSS e o
bloco "artigos recentes" da home (entre <!-- artigos:inicio --> e <!-- artigos:fim -->).
Também gera sitemap.xml (com hreflang ligando as traduções) e robots.txt.

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
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://lrperovano.com.br"
AUTHOR = "Ricardo Perovano"
WHATSAPP = "5527998553591"
EMAIL = "contato@lrperovano.com.br"


# ---------------------------------------------------------------------------
# Idiomas
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Lang:
    code: str
    html_lang: str
    og_locale: str
    src: Path
    out: Path
    blog: str
    home: str
    home_file: Path
    privacy: str
    category_dir: str
    categories: tuple[str, ...]
    category_intro: dict
    anchors: dict
    t: dict
    months: tuple[str, ...]

    def fmt_date(self, d: date) -> str:
        if self.code == "en":
            return f"{self.months[d.month - 1]} {d.day}, {d.year}"
        return f"{d.day} de {self.months[d.month - 1]} de {d.year}"

    def category_url(self, category: str) -> str:
        return f"{self.blog}{self.category_dir}/{slugify(category)}/"

    def category_phrase(self, category: str) -> str:
        return category if category == "Inteligência artificial" else category.lower()


PT = Lang(
    code="pt", html_lang="pt-BR", og_locale="pt_BR",
    src=ROOT / "_conteudo" / "artigos", out=ROOT / "blog",
    blog="/blog/", home="/", home_file=ROOT / "index.html", privacy="/privacy.html",
    category_dir="categoria",
    categories=("Sites", "Sistemas", "Automação", "Inteligência artificial", "Gestão de projetos"),
    category_intro={
        "Sites": "Sites institucionais, landing pages, SEO, velocidade e tudo o que faz um site gerar contatos.",
        "Sistemas": "Sistemas sob medida, aplicativos, SaaS e as decisões para tirar um software do papel.",
        "Automação": "Integrações entre sistemas, APIs, pagamentos e automações que eliminam trabalho repetitivo.",
        "Inteligência artificial": "Como aplicar IA na empresa com critério: assistentes, agentes, chatbots e busca em documentos.",
        "Gestão de projetos": "Como contratar, acompanhar e manter um projeto de software sem surpresas.",
    },
    anchors={"content": "conteudo", "projects": "projetos", "solutions": "solucoes",
             "how": "como-trabalhamos", "about": "sobre", "contact": "contato"},
    months=("janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
            "agosto", "setembro", "outubro", "novembro", "dezembro"),
    t={
        "skip": "Pular para o conteúdo",
        "brand_desc": "Engenharia de software",
        "brand_label": "PEROVANO — Engenharia de software, página inicial",
        "open_menu": "Abrir menu",
        "nav_main": "Principal",
        "nav_projects": "Projetos", "nav_solutions": "Soluções", "nav_how": "Como trabalhamos",
        "nav_contact": "Contato",
        "cta": "Vamos conversar",
        "footer_nav": "Rodapé", "navigation": "Navegação", "contact": "Contato",
        "privacy": "Política de Privacidade",
        "new_tab": " (abre em nova aba)",
        "reading": "{n} min de leitura",
        "by": "Por",
        "updated": "Atualizado em",
        "breadcrumb": "Você está em",
        "home": "Início",
        "toc": "Neste artigo",
        "cta_title": "Quer aplicar isso na sua empresa?",
        "cta_text": "Conte o seu desafio. A primeira conversa serve para entender o contexto e indicar o melhor caminho — seja um site, um sistema ou uma automação.",
        "wa_button": "Conversar pelo WhatsApp",
        "wa_text": "Olá! Li o artigo \"{title}\" e gostaria de conversar sobre um projeto.",
        "see_projects": "Ver projetos no ar",
        "related": "Continue lendo",
        "all": "Todos",
        "categories": "Categorias",
        "search_label": "Buscar artigos",
        "search_placeholder": "Ex.: aplicativo, Pix, chatbot, SEO",
        "blog_name": "Blog da PEROVANO",
        "index_title": "Blog | PEROVANO — sites, sistemas, automação e IA",
        "index_description": "Artigos práticos sobre sites, sistemas sob medida, aplicativos, integrações, automação e inteligência artificial para quem precisa decidir e contratar tecnologia.",
        "index_h1": "Tecnologia explicada para quem decide.",
        "index_lead": "{n} artigos práticos sobre sites, sistemas sob medida, aplicativos, integrações, automação e inteligência artificial — com critérios para decidir, contratar e acompanhar um projeto.",
        "group_link": "{n} artigos sobre {c}",
        "category_title": "{c}: artigos e guias práticos | PEROVANO",
        "category_description": "{intro} {n} artigos da PEROVANO sobre {c}.",
        "see_all": "Ver todos os artigos",
        "home_blog_id": "titulo-blog",
        "feed_description": "Sites, sistemas sob medida, integrações, automação e inteligência artificial para empresas.",
        "switch_code": "EN",
        "switch_label": "English version",
    },
)

EN = Lang(
    code="en", html_lang="en", og_locale="en_US",
    src=ROOT / "_conteudo" / "en" / "articles", out=ROOT / "en" / "blog",
    blog="/en/blog/", home="/en/", home_file=ROOT / "en" / "index.html", privacy="/en/privacy.html",
    category_dir="category",
    categories=("Websites", "Software", "Automation", "Artificial intelligence", "Project management"),
    category_intro={
        "Websites": "Business websites, landing pages, SEO, speed and everything that makes a website generate inquiries.",
        "Software": "Custom software, apps, SaaS and the decisions behind turning a software idea into a product.",
        "Automation": "System integrations, APIs, payments and automation that remove repetitive work.",
        "Artificial intelligence": "How to apply AI in business with judgment: assistants, agents, chatbots and document search.",
        "Project management": "How to hire, follow and maintain a software project without surprises.",
    },
    anchors={"content": "content", "projects": "projects", "solutions": "solutions",
             "how": "how-we-work", "about": "about", "contact": "contact"},
    months=("January", "February", "March", "April", "May", "June", "July",
            "August", "September", "October", "November", "December"),
    t={
        "skip": "Skip to content",
        "brand_desc": "Software engineering",
        "brand_label": "PEROVANO — Software engineering, home page",
        "open_menu": "Open menu",
        "nav_main": "Main",
        "nav_projects": "Projects", "nav_solutions": "Solutions", "nav_how": "How we work",
        "nav_contact": "Contact",
        "cta": "Let's talk",
        "footer_nav": "Footer", "navigation": "Navigation", "contact": "Contact",
        "privacy": "Privacy Policy",
        "new_tab": " (opens in a new tab)",
        "reading": "{n} min read",
        "by": "By",
        "updated": "Updated",
        "breadcrumb": "Breadcrumb",
        "home": "Home",
        "toc": "In this article",
        "cta_title": "Want to apply this to your business?",
        "cta_text": "Tell us about your challenge. The first conversation is about understanding your context and pointing to the best path — whether it's a website, a software system or an automation. We work remotely and run projects in English.",
        "wa_button": "Chat on WhatsApp",
        "wa_text": "Hi! I read the article \"{title}\" and would like to talk about a project.",
        "see_projects": "See live projects",
        "related": "Keep reading",
        "all": "All",
        "categories": "Categories",
        "search_label": "Search articles",
        "search_placeholder": "E.g. app, chatbot, SEO, API",
        "blog_name": "PEROVANO Blog",
        "index_title": "Blog | PEROVANO — websites, software, automation and AI",
        "index_description": "Practical articles on websites, custom software, apps, integrations, automation and artificial intelligence for people who need to decide on and hire technology.",
        "index_h1": "Technology explained for decision-makers.",
        "index_lead": "{n} practical articles on websites, custom software, apps, integrations, automation and artificial intelligence — with criteria to decide, hire and follow a project.",
        "group_link": "{n} articles on {c}",
        "category_title": "{c}: articles and practical guides | PEROVANO",
        "category_description": "{intro} {n} PEROVANO articles on {c}.",
        "see_all": "See all articles",
        "home_blog_id": "blog-title",
        "feed_description": "Websites, custom software, integrations, automation and artificial intelligence for businesses.",
        "switch_code": "PT",
        "switch_label": "Versão em português",
    },
)

LANGS = (PT, EN)
OTHER = {"pt": EN, "en": PT}


# ---------------------------------------------------------------------------
# Modelo
# ---------------------------------------------------------------------------
@dataclass
class Article:
    lang: Lang
    slug: str
    title: str
    description: str
    date: date
    updated: date
    category: str
    keywords: str
    body_md: str
    pt_slug: str = ""
    body_html: str = ""
    toc: list[tuple[str, str]] = field(default_factory=list)
    faq: list[tuple[str, str]] = field(default_factory=list)
    words: int = 0
    translation: "Article | None" = None

    @property
    def url(self) -> str:
        return f"{self.lang.blog}{self.slug}/"

    @property
    def reading_minutes(self) -> int:
        return max(1, math.ceil(self.words / 200))

    @property
    def og_image(self) -> str:
        if (self.lang.out / self.slug / "og.png").exists():
            return f"{SITE}{self.url}og.png"
        return f"{SITE}/og-image{'-en' if self.lang.code == 'en' else ''}.png"


# Artigos com data futura ficam fora até o dia da publicação (rode o build de novo nesse dia).
SCHEDULED: list[Article] = []
# Contexto de renderização: links para artigos ainda não publicados viram texto simples.
CTX: dict = {"blog": "/blog/", "published": set()}


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


def load_articles(lang: Lang) -> list[Article]:
    articles = []
    for path in sorted(lang.src.glob("*.md")):
        meta, body = parse_front_matter(path)
        for key in ("title", "description", "date", "category"):
            if not meta.get(key):
                fail(f"{path.name}: campo '{key}' obrigatório")
        if meta["category"] not in lang.categories:
            fail(f"{path.name}: categoria '{meta['category']}' fora da lista {lang.categories}")
        published = date.fromisoformat(meta["date"])
        art = Article(
            lang=lang,
            slug=path.stem,
            title=meta["title"],
            description=meta["description"],
            date=published,
            updated=date.fromisoformat(meta.get("updated") or meta["date"]),
            category=meta["category"],
            keywords=meta.get("keywords", ""),
            body_md=body,
            pt_slug=meta.get("pt", "") if lang.code == "en" else path.stem,
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
        target = re.match(rf"^{re.escape(CTX['blog'])}([a-z0-9-]+)/$", href)
        if target and CTX["published"] and target.group(1) not in CTX["published"]:
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


FAQ_HEADINGS = ("perguntas-frequentes", "frequently-asked-questions")


def render_markdown(art: Article) -> None:
    out: list[str] = []
    para: list[str] = []
    list_kind: str | None = None
    quote_lines: list[str] = []
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
        nonlocal para, list_kind, quote_lines
        if para:
            rendered = inline(" ".join(para))
            out.append(f"<p>{rendered}</p>")
            if in_faq and faq_q:
                faq_a.append(strip_tags(rendered))
            para = []
        if list_kind:
            out.append(f"</{list_kind}>")
            list_kind = None
        if quote_lines:
            out.append(f"<blockquote><p>{inline(' '.join(quote_lines))}</p></blockquote>")
            quote_lines = []

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
                in_faq = slugify(text).startswith(FAQ_HEADINGS)
                art.toc.append((hid, strip_tags(inline(text))))
            elif in_faq:
                flush_faq_answer()
                faq_q = strip_tags(inline(text))
            out.append(f'<h{level} id="{hid}">{inline(text)}</h{level}>')
            continue
        m = re.match(r"^(?:[-*]|(\d+)\.)\s+(.*)$", line)
        if m:
            kind = "ol" if m.group(1) else "ul"
            if para or quote_lines:
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
            quote_lines.append(line.lstrip("> ").strip())
            continue
        if list_kind and raw.startswith(("  ", "\t")):
            # continuação de item de lista
            out[-1] = out[-1][:-5] + " " + inline(line.strip()) + "</li>"
            continue
        if list_kind or quote_lines:
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


def lang_redirect(target: str) -> str:
    """Páginas em português: navegador em outro idioma vai para a tradução.
    Robôs não são redirecionados; a escolha manual (perovano-lang ou ?lang=pt) prevalece."""
    return f"""  <script>
    (function () {{
      try {{
        var KEY = 'perovano-lang';
        if (/[?&]lang=pt(&|$)/.test(location.search)) {{ localStorage.setItem(KEY, 'pt'); return; }}
        var pref = localStorage.getItem(KEY);
        if (pref === 'pt') return;
        if (/bot|crawl|spider|slurp|preview|facebookexternalhit|whatsapp|telegram|lighthouse/i.test(navigator.userAgent)) return;
        var langs = navigator.languages && navigator.languages.length ? navigator.languages : [navigator.language || ''];
        var readsPt = langs.some(function (l) {{ return /^pt(-|$)/i.test(l); }});
        if (pref === 'en' || !readsPt) location.replace('{target}');
      }} catch (e) {{}}
    }})();
  </script>
"""


def alternates(pt_url: str | None, en_url: str | None) -> str:
    """<link rel="alternate" hreflang> recíprocos; x-default aponta para o inglês."""
    if not (pt_url and en_url):
        return ""
    return (f'  <link rel="alternate" hreflang="pt-BR" href="{SITE}{pt_url}">\n'
            f'  <link rel="alternate" hreflang="en" href="{SITE}{en_url}">\n'
            f'  <link rel="alternate" hreflang="x-default" href="{SITE}{en_url}">\n')


def page_pair(lang: Lang, own: str, other: str | None) -> tuple[str | None, str | None]:
    return (own, other) if lang.code == "pt" else (other, own)


def head(lang: Lang, title: str, description: str, path: str, *, other_path: str | None,
         og_type: str = "website", og_image: str | None = None, extra: str = "") -> str:
    canonical = f"{SITE}{path}"
    og_image = og_image or f"{SITE}/og-image{'-en' if lang.code == 'en' else ''}.png"
    pt_url, en_url = page_pair(lang, path, other_path)
    redirect = lang_redirect(en_url) if lang.code == "pt" and en_url else ""
    alt_locale = "en_US" if lang.code == "pt" else "pt_BR"
    return f"""<!DOCTYPE html>
<html lang="{lang.html_lang}">
<head>
{redirect}{GA_TAG}  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{e(title)}</title>
  <meta name="description" content="{e(description)}">
  <meta name="theme-color" content="#143C3A">
  <link rel="canonical" href="{e(canonical)}">
{alternates(pt_url, en_url)}  <link rel="icon" type="image/svg+xml" href="/assets/img/favicon.svg">
  <link rel="icon" type="image/x-icon" href="/favicon.ico" sizes="32x32">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="alternate" type="application/rss+xml" title="{e(lang.t['blog_name'])}" href="{lang.blog}feed.xml">
  <meta property="og:site_name" content="PEROVANO">
  <meta property="og:title" content="{e(title)}">
  <meta property="og:description" content="{e(description)}">
  <meta property="og:type" content="{og_type}">
  <meta property="og:locale" content="{lang.og_locale}">
  <meta property="og:locale:alternate" content="{alt_locale}">
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
  <a class="skip-link" href="#{lang.anchors['content']}">{lang.t['skip']}</a>
"""


def header(lang: Lang, other_path: str | None) -> str:
    t, a, home = lang.t, lang.anchors, lang.home
    other = OTHER[lang.code]
    target = other_path or other.home
    if other.code == "pt":
        target += "?lang=pt"
    return f"""  <header class="site-header">
    <div class="container site-header__inner">
      <a class="brand" href="{home}" aria-label="{e(t['brand_label'])}">
        <span class="brand__name">PEROVANO</span>
        <span class="brand__descriptor">{t['brand_desc']}</span>
      </a>

      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="menu-principal">
        <span class="sr-only">{t['open_menu']}</span>
        <span class="nav-toggle__bars" aria-hidden="true"><span></span><span></span><span></span></span>
      </button>

      <nav class="site-nav" id="menu-principal" aria-label="{t['nav_main']}">
        <ul class="site-nav__list">
          <li><a href="{home}#{a['projects']}">{t['nav_projects']}</a></li>
          <li><a href="{home}#{a['solutions']}">{t['nav_solutions']}</a></li>
          <li><a href="{home}#{a['how']}">{t['nav_how']}</a></li>
          <li><a href="{lang.blog}" aria-current="page">Blog</a></li>
          <li><a href="{home}#{a['contact']}">{t['nav_contact']}</a></li>
        </ul>
        <a class="lang-switch" href="{target}" hreflang="{other.html_lang}" lang="{other.html_lang}" data-lang="{other.code}"><span aria-hidden="true">{t['switch_code']}</span><span class="sr-only">{t['switch_label']}</span></a>
        <a class="btn btn--accent btn--small" href="{home}#{a['contact']}">{t['cta']}</a>
      </nav>
    </div>
  </header>
"""


def footer(lang: Lang) -> str:
    t, a, home = lang.t, lang.anchors, lang.home
    return f"""  <footer class="site-footer">
    <div class="container">
      <div class="site-footer__top">
        <div>
          <a class="brand brand--footer" href="{home}" aria-label="{e(t['brand_label'])}">
            <span class="brand__name">PEROVANO</span>
            <span class="brand__descriptor">{t['brand_desc']}</span>
          </a>
          <p class="site-footer__legal">L R PEROVANO LTDA</p>
        </div>

        <nav aria-label="{t['footer_nav']}">
          <h2>{t['navigation']}</h2>
          <ul>
            <li><a href="{home}#{a['projects']}">{t['nav_projects']}</a></li>
            <li><a href="{home}#{a['solutions']}">{t['nav_solutions']}</a></li>
            <li><a href="{home}#{a['how']}">{t['nav_how']}</a></li>
            <li><a href="{lang.blog}">Blog</a></li>
            <li><a href="{home}#{a['contact']}">{t['nav_contact']}</a></li>
            <li><a href="{lang.privacy}">{t['privacy']}</a></li>
          </ul>
        </nav>

        <div>
          <h2>{t['contact']}</h2>
          <ul>
            <li><a href="https://wa.me/{WHATSAPP}" target="_blank" rel="noopener">WhatsApp: +55 27 99855-3591<span class="sr-only">{t['new_tab']}</span></a></li>
            <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
            <li><a href="https://www.linkedin.com/in/xhricardo/" target="_blank" rel="noopener">LinkedIn<span class="sr-only">{t['new_tab']}</span></a></li>
            <li><a href="https://github.com/ricardoperovano" target="_blank" rel="noopener">GitHub<span class="sr-only">{t['new_tab']}</span></a></li>
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


def other_category(lang: Lang, category: str) -> str:
    return OTHER[lang.code].categories[lang.categories.index(category)]


def article_card(art: Article, heading: str = "h3") -> str:
    reading = art.lang.t["reading"].format(n=art.reading_minutes)
    search = (art.title + " " + art.description + " " + art.keywords).lower()
    return f"""          <article class="post-card" data-category="{e(art.category)}" data-search="{e(search)}">
            <p class="post-card__meta"><span>{e(art.category)}</span><span>{reading}</span></p>
            <{heading} class="post-card__title"><a href="{art.url}">{e(art.title)}</a></{heading}>
            <p class="post-card__excerpt">{e(art.description)}</p>
          </article>"""


def related(art: Article, articles: list[Article], n: int = 3) -> list[Article]:
    linked = set(re.findall(rf"\({re.escape(art.lang.blog)}([a-z0-9-]+)/\)", art.body_md))
    others = [a for a in articles if a.slug != art.slug]
    others.sort(key=lambda a: (a.category != art.category, a.slug in linked, a.title))
    return others[:n]


def render_article(art: Article, articles: list[Article]) -> str:
    lang, t = art.lang, art.lang.t
    canonical = f"{SITE}{art.url}"
    other_path = art.translation.url if art.translation else None
    ld = [
        {
            "@context": "https://schema.org",
            "@type": "BlogPosting",
            "headline": art.title,
            "description": art.description,
            "datePublished": art.date.isoformat(),
            "dateModified": art.updated.isoformat(),
            "inLanguage": lang.html_lang,
            "articleSection": art.category,
            "keywords": art.keywords,
            "wordCount": art.words,
            "image": art.og_image,
            "mainEntityOfPage": canonical,
            "url": canonical,
            "author": {"@type": "Person", "name": AUTHOR, "url": f"{SITE}{lang.home}#{lang.anchors['about']}"},
            "publisher": ORG,
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": t["home"], "item": f"{SITE}{lang.home}"},
                {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{SITE}{lang.blog}"},
                {"@type": "ListItem", "position": 3, "name": art.category, "item": f"{SITE}{lang.category_url(art.category)}"},
                {"@type": "ListItem", "position": 4, "name": art.title, "item": canonical},
            ],
        },
    ]
    if art.translation:
        ld[0]["translationOfWork" if lang.code == "en" else "workTranslation"] = {"@id": f"{SITE}{art.translation.url}"}
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
    toc = "\n".join(f'              <li><a href="#{hid}">{e(title)}</a></li>' for hid, title in art.toc)
    cards = "\n".join(article_card(a) for a in related(art, articles))
    wa_text = t["wa_text"].format(title=art.title)
    updated = (f' <span>{t["updated"]} <time datetime="{art.updated.isoformat()}">{lang.fmt_date(art.updated)}</time></span>'
               if art.updated != art.date else "")
    return (
        head(lang, f"{art.title} | PEROVANO", art.description, art.url, other_path=other_path,
             og_type="article", og_image=art.og_image, extra=extra)
        + header(lang, other_path)
        + f"""
  <main id="{lang.anchors['content']}">
    <article class="post">
      <header class="post__header">
        <div class="container">
          <nav class="breadcrumb" aria-label="{t['breadcrumb']}">
            <ol>
              <li><a href="{lang.home}">{t['home']}</a></li>
              <li><a href="{lang.blog}">Blog</a></li>
              <li><a href="{lang.category_url(art.category)}">{e(art.category)}</a></li>
            </ol>
          </nav>
          <h1 class="post__title">{e(art.title)}</h1>
          <p class="post__lead">{e(art.description)}</p>
          <p class="post__meta">
            <span>{t['by']} {e(AUTHOR)}</span>
            <span><time datetime="{art.date.isoformat()}">{lang.fmt_date(art.date)}</time></span>{updated}
            <span>{t['reading'].format(n=art.reading_minutes)}</span>
          </p>
        </div>
      </header>

      <div class="container post__layout">
        <aside class="post__toc" aria-labelledby="toc-titulo">
          <h2 id="toc-titulo">{t['toc']}</h2>
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
          <h2 id="cta-titulo">{t['cta_title']}</h2>
          <p>{t['cta_text']}</p>
        </div>
        <div class="post-cta__actions">
          <a class="btn btn--accent" href="https://wa.me/{WHATSAPP}?text={quote(wa_text)}" target="_blank" rel="noopener">{t['wa_button']}<span class="sr-only">{t['new_tab']}</span></a>
          <a class="btn btn--outline-light" href="{lang.home}#{lang.anchors['projects']}">{t['see_projects']}</a>
        </div>
      </div>
    </section>

    <section class="section related" aria-labelledby="relacionados-titulo">
      <div class="container">
        <h2 id="relacionados-titulo" class="related__title">{t['related']}</h2>
        <div class="post-grid">
{cards}
        </div>
      </div>
    </section>
  </main>

"""
        + footer(lang)
    )


def chips_nav(lang: Lang, used: list[str], current: str | None, *, filters: bool) -> str:
    """Chips de categoria. No índice (filters=True) também filtram a lista sem recarregar."""
    def chip(label: str, href: str, value: str, anchor: str) -> str:
        attrs = f' data-filter="{e(value)}" data-anchor="{anchor}"' if filters else ""
        cur = ' aria-current="page"' if (current == value or (current is None and value == "" and not filters)) else ""
        return f'          <a class="chip" href="{href}"{attrs}{cur}>{e(label)}</a>'
    items = [chip(lang.t["all"], lang.blog, "", "#todos")]
    items += [chip(c, lang.category_url(c), c, f"#{slugify(c)}") for c in used]
    return f'        <nav class="chips" aria-label="{lang.t["categories"]}">\n' + "\n".join(items) + "\n        </nav>"


def search_box(lang: Lang) -> str:
    return f"""        <div class="blog-search" hidden>
          <label for="busca-artigos">{lang.t['search_label']}</label>
          <input id="busca-artigos" type="search" autocomplete="off" placeholder="{e(lang.t['search_placeholder'])}">
        </div>"""


def render_index(lang: Lang, articles: list[Article]) -> str:
    t = lang.t
    other = OTHER[lang.code]
    ld = {
        "@context": "https://schema.org",
        "@type": "Blog",
        "name": t["blog_name"],
        "url": f"{SITE}{lang.blog}",
        "inLanguage": lang.html_lang,
        "publisher": ORG,
        "blogPost": [
            {"@type": "BlogPosting", "headline": a.title, "url": f"{SITE}{a.url}",
             "datePublished": a.date.isoformat()}
            for a in articles
        ],
    }
    used = [c for c in lang.categories if any(a.category == c for a in articles)]
    groups = []
    for c in used:
        items = [a for a in articles if a.category == c]
        cards = "\n".join(article_card(a, "h3") for a in items)
        link_text = t["group_link"].format(n=len(items), c=e(lang.category_phrase(c)))
        groups.append(f"""      <section class="blog-group" id="{slugify(c)}" data-category="{e(c)}" aria-labelledby="cat-{slugify(c)}">
        <div class="blog-group__head">
          <h2 class="blog-group__title" id="cat-{slugify(c)}">{e(c)}</h2>
          <a class="text-link" href="{lang.category_url(c)}">{link_text}</a>
        </div>
        <div class="post-grid">
{cards}
        </div>
      </section>""")
    return (
        head(lang, t["index_title"], t["index_description"], lang.blog, other_path=other.blog, extra=json_ld(ld))
        + header(lang, other.blog)
        + f"""
  <main id="{lang.anchors['content']}">
    <header class="blog-hero on-dark">
      <div class="container">
        <h1 class="blog-hero__title">{t['index_h1']}</h1>
        <p class="blog-hero__lead">{t['index_lead'].format(n=len(articles))}</p>
{search_box(lang)}
{chips_nav(lang, used, "", filters=True)}
      </div>
    </header>

    <div class="container blog-list" id="todos">
      <p class="blog-empty" role="status" hidden></p>
{chr(10).join(groups)}
    </div>
  </main>

"""
        + footer(lang)
    )


def render_category(lang: Lang, category: str, articles: list[Article]) -> str:
    t = lang.t
    other = OTHER[lang.code]
    items = [a for a in articles if a.category == category]
    path = lang.category_url(category)
    canonical = f"{SITE}{path}"
    intro = lang.category_intro.get(category, "")
    title = t["category_title"].format(c=category)
    description = t["category_description"].format(intro=intro, n=len(items), c=lang.category_phrase(category))
    other_path = other.category_url(other_category(lang, category))
    ld = [
        {
            "@context": "https://schema.org",
            "@type": "CollectionPage",
            "name": f"{category} — {t['blog_name']}",
            "url": canonical,
            "inLanguage": lang.html_lang,
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
                {"@type": "ListItem", "position": 1, "name": t["home"], "item": f"{SITE}{lang.home}"},
                {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{SITE}{lang.blog}"},
                {"@type": "ListItem", "position": 3, "name": category, "item": canonical},
            ],
        },
    ]
    used = [c for c in lang.categories if any(a.category == c for a in articles)]
    cards = "\n".join(article_card(a, "h2") for a in items)
    return (
        head(lang, title, description, path, other_path=other_path, extra="".join(json_ld(x) for x in ld))
        + header(lang, other_path)
        + f"""
  <main id="{lang.anchors['content']}">
    <header class="blog-hero on-dark">
      <div class="container">
        <nav class="breadcrumb breadcrumb--dark" aria-label="{t['breadcrumb']}">
          <ol>
            <li><a href="{lang.home}">{t['home']}</a></li>
            <li><a href="{lang.blog}">Blog</a></li>
          </ol>
        </nav>
        <h1 class="blog-hero__title">{e(category)}</h1>
        <p class="blog-hero__lead">{e(intro)}</p>
{chips_nav(lang, used, category, filters=False)}
      </div>
    </header>

    <div class="container blog-list">
      <div class="post-grid">
{cards}
      </div>
    </div>
  </main>

"""
        + footer(lang)
    )


def render_home_block(lang: Lang, articles: list[Article]) -> str:
    t = lang.t
    cards = "\n".join(article_card(a) for a in articles[:3])
    return f"""<!-- artigos:inicio -->
    <section class="section section--surface" id="blog" aria-labelledby="{t['home_blog_id']}">
      <div class="container">
        <div class="home-blog__head">
          <div>
            <span class="kicker">Blog</span>
            <h2 id="{t['home_blog_id']}">{t['index_h1']}</h2>
          </div>
          <a class="btn btn--secondary" href="{lang.blog}">{t['see_all']}</a>
        </div>
        <div class="post-grid">
{cards}
        </div>
      </div>
    </section>
    <!-- artigos:fim -->"""


def render_feed(lang: Lang, articles: list[Article]) -> str:
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
    <title>{e(lang.t['blog_name'])}</title>
    <link>{SITE}{lang.blog}</link>
    <atom:link href="{SITE}{lang.blog}feed.xml" rel="self" type="application/rss+xml"/>
    <description>{e(lang.t['feed_description'])}</description>
    <language>{lang.html_lang}</language>
    <lastBuildDate>{rfc(last)}</lastBuildDate>
{items}
  </channel>
</rss>
"""


def render_sitemap(by_lang: dict[str, list[Article]]) -> str:
    pt_articles, en_articles = by_lang["pt"], by_lang["en"]
    all_articles = pt_articles + en_articles
    last = max((a.updated for a in all_articles), default=date.today()).isoformat()

    def alt_links(pt: str | None, en: str | None) -> str:
        if not (pt and en):
            return ""
        return (f'<xhtml:link rel="alternate" hreflang="pt-BR" href="{SITE}{pt}"/>'
                f'<xhtml:link rel="alternate" hreflang="en" href="{SITE}{en}"/>'
                f'<xhtml:link rel="alternate" hreflang="x-default" href="{SITE}{en}"/>')

    # (url pt, url en, lastmod) — cada URL entra uma vez e declara a sua tradução.
    rows: list[tuple[str | None, str | None, str | None]] = [
        ("/", "/en/", last),
        ("/privacy.html", "/en/privacy.html", None),
        ("/blog/", "/en/blog/", last),
    ]
    for c_pt, c_en in zip(PT.categories, EN.categories):
        dates = [a.updated for a in all_articles if a.category in (c_pt, c_en)]
        if dates:
            rows.append((PT.category_url(c_pt), EN.category_url(c_en), max(dates).isoformat()))
    for a in pt_articles:
        lm = max(a.updated, a.translation.updated) if a.translation else a.updated
        rows.append((a.url, a.translation.url if a.translation else None, lm.isoformat()))
    for a in en_articles:
        if not a.translation:
            rows.append((None, a.url, a.updated.isoformat()))

    entries = []
    for pt, en, lm in rows:
        lastmod = f"<lastmod>{lm}</lastmod>" if lm else ""
        for loc in (pt, en):
            if loc:
                entries.append(f"  <url><loc>{SITE}{loc}</loc>{lastmod}{alt_links(pt, en)}</url>")
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
<div class="b"><div class="n">PEROVANO</div><div class="d">{descriptor}</div></div>
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
            page = Path(tmp) / f"{a.lang.code}-{a.slug}.html"
            page.write_text(OG_TEMPLATE.format(title=e(a.title), category=e(a.category), size=size,
                                               descriptor=e(a.lang.t["brand_desc"])), encoding="utf-8")
            target = a.lang.out / a.slug / "og.png"
            target.parent.mkdir(parents=True, exist_ok=True)
            subprocess.run([chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                            "--window-size=1200,630", "--virtual-time-budget=6000",
                            f"--screenshot={target}", page.as_uri()],
                           check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"og: {target.relative_to(ROOT)}")


# ---------------------------------------------------------------------------
def check_links(lang: Lang, articles: list[Article]) -> list[str]:
    slugs = {a.slug for a in articles}
    scheduled = {x.slug for x in SCHEDULED if x.lang is lang}
    allowed = (lang.blog, f"{lang.home}#", lang.privacy)
    problems = []
    for a in articles:
        for target in re.findall(r"\]\((/[^)]*)\)", a.body_md):
            m = re.match(rf"^{re.escape(lang.blog)}([a-z0-9-]+)/$", target)
            if m:
                if m.group(1) in scheduled:
                    continue  # vira texto simples até o artigo ser publicado
                if m.group(1) not in slugs:
                    problems.append(f"{lang.code}/{a.slug}: link interno quebrado {target}")
            elif not target.startswith(allowed) and target != lang.home:
                problems.append(f"{lang.code}/{a.slug}: link interno desconhecido ou de outro idioma {target}")
    return problems


def write_home_block(lang: Lang, articles: list[Article]) -> None:
    if not lang.home_file.exists():
        return
    text = lang.home_file.read_text(encoding="utf-8")
    block = render_home_block(lang, articles)
    new, n = re.subn(r"<!-- artigos:inicio -->.*?<!-- artigos:fim -->", lambda _: block, text, flags=re.S)
    if n != 1:
        fail(f"marcadores <!-- artigos:inicio --> / <!-- artigos:fim --> não encontrados em {lang.home_file.relative_to(ROOT)}")
    lang.home_file.write_text(new, encoding="utf-8")


def main() -> None:
    by_lang = {lang.code: load_articles(lang) for lang in LANGS}
    if not by_lang["pt"]:
        fail("nenhum artigo em _conteudo/artigos")

    # Liga cada tradução ao original pelo campo `pt:` do artigo em inglês.
    pt_by_slug = {a.slug: a for a in by_lang["pt"]}
    for en_art in by_lang["en"]:
        original = pt_by_slug.get(en_art.pt_slug)
        if not original:
            print(f"aviso: en/{en_art.slug}: original '{en_art.pt_slug}' não encontrado (sem hreflang)")
            continue
        en_art.translation, original.translation = original, en_art
        if other_category(EN, en_art.category) != original.category:
            print(f"aviso: en/{en_art.slug}: categoria '{en_art.category}' não corresponde a '{original.category}'")

    problems: list[str] = []
    for lang in LANGS:
        articles = by_lang[lang.code]
        CTX["blog"], CTX["published"] = lang.blog, {a.slug for a in articles}
        for a in articles:
            render_markdown(a)
        problems += check_links(lang, articles)
    for p in problems:
        print(f"aviso: {p}")

    if "--og" in sys.argv:
        build_og(by_lang["pt"] + by_lang["en"])

    for lang in LANGS:
        articles = by_lang[lang.code]
        if not articles:
            continue
        out = lang.out
        out.mkdir(parents=True, exist_ok=True)
        # limpa páginas de artigos removidos (preserva og.png de artigos existentes)
        slugs = {a.slug for a in articles}
        for d in out.iterdir():
            if d.is_dir() and d.name not in slugs and d.name != lang.category_dir:
                shutil.rmtree(d)
        CTX["blog"], CTX["published"] = lang.blog, slugs
        for a in articles:
            target = out / a.slug / "index.html"
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(render_article(a, articles), encoding="utf-8")
        (out / "index.html").write_text(render_index(lang, articles), encoding="utf-8")
        cat_root = out / lang.category_dir
        if cat_root.exists():
            shutil.rmtree(cat_root)
        for c in lang.categories:
            if any(x.category == c for x in articles):
                target = cat_root / slugify(c) / "index.html"
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(render_category(lang, c, articles), encoding="utf-8")
        (out / "feed.xml").write_text(render_feed(lang, articles), encoding="utf-8")
        write_home_block(lang, articles)

    (ROOT / "sitemap.xml").write_text(render_sitemap(by_lang), encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")

    for lang in LANGS:
        for a in by_lang[lang.code]:
            mark = "" if a.translation else "  (sem tradução)"
            print(f"{a.url}  {a.words} palavras  {a.reading_minutes} min  {len(a.toc)} seções  {len(a.faq)} FAQ{mark}")
    for a in sorted(SCHEDULED, key=lambda x: x.date):
        print(f"agendado: {a.url} para {a.date.isoformat()} (rode o build nesse dia)")
    counts = ", ".join(f"{len(by_lang[l.code])} em {l.code}" for l in LANGS)
    print(f"artigos gerados: {counts}; {len(SCHEDULED)} agendados; {len(problems)} avisos")


if __name__ == "__main__":
    main()
