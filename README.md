# lrperovano.com.br — site institucional da PEROVANO

Site estático (HTML, CSS e JavaScript, sem build), publicado via GitHub Pages com o domínio definido em `CNAME`.
Este arquivo é documentação técnica e não é publicado (`_config.yml` o exclui).

## Executar localmente

```sh
python3 -m http.server 8080
# abrir http://localhost:8080/
```

Os caminhos são absolutos (`/assets/...`), então abra pelo servidor, não por `file://`.

## Estrutura

| Arquivo | Função |
| --- | --- |
| `index.html` | Página institucional (conteúdo e marcação) |
| `privacy.html` | Política de privacidade (endereço preservado; também cobre o app Android TOON Converter) |
| `assets/css/site.css` | Tokens da identidade (`--brand-*`) e todos os estilos |
| `assets/js/site.js` | Menu mobile, ano do rodapé, âncoras antigas, entrada das seções |
| `assets/img/favicon.svg` | Ícone provisório neutro (origem de `favicon.ico`, `favicon-*.png`, `apple-touch-icon.png`) |
| `og-image.png` | Imagem de compartilhamento 1200×630 |
| `assets/img/portfolio/` | Capturas dos sites do portfólio (`*-hero.webp` na abertura, `*-full.webp` nas janelas) |
| `_conteudo/artigos/*.md` | Fonte dos artigos do blog (não é publicada) |
| `scripts/build_blog.py` | Gera `blog/`, `sitemap.xml`, `robots.txt`, `blog/feed.xml` e o bloco de artigos da home |
| `blog/` | Saída gerada — não edite à mão |

Contatos (WhatsApp, e-mail, LinkedIn, GitHub) aparecem em dois blocos do `index.html`: seção `#contato` e rodapé.
Ao alterar um contato, busque pelo valor antigo no projeto para atualizar todas as ocorrências (inclusive `privacy.html`).

Âncoras do site anterior: `#projetos`, `#sobre` e `#contato` continuam existindo; `#servicos` e `#top` são redirecionadas por `site.js`.

## Blog

Para publicar ou alterar um artigo:

1. Crie ou edite `_conteudo/artigos/<slug>.md` (o nome do arquivo vira a URL `/blog/<slug>/`).
2. Rode `python3 scripts/build_blog.py --og` (o `--og` gera a imagem de compartilhamento do artigo; precisa do Chrome).
3. Confira em `python3 -m http.server 8080` e faça commit de `_conteudo/`, `blog/`, `sitemap.xml` e `index.html`.

Front matter obrigatório:

```
---
title: "Título com a palavra-chave (até ~60 caracteres)"
description: "Meta description de 140 a 160 caracteres"
date: 2026-10-30
category: "Sites | Sistemas | Automação | Inteligência artificial | Gestão de projetos"
keywords: "principal, variação 1, variação 2"
updated: 2026-11-15   # opcional, quando revisar o texto
draft: true           # opcional, para não publicar ainda
---
```

Markdown aceito: `##`, `###`, parágrafos, listas `-` e `1.`, `**negrito**`, `*itálico*`, `` `código` ``, `[link](/caminho/)` e `> citação`.
Uma seção `## Perguntas frequentes` com perguntas em `###` vira dados estruturados de FAQ automaticamente.
O gerador avisa sobre links internos quebrados.

O gerador também cria uma página por categoria (`/blog/categoria/<categoria>/`), com breadcrumb e dados estruturados, e a busca do índice do blog.

**Agendamento:** um artigo com `date` no futuro fica fora do site, do sitemap e do RSS até essa data. Links de outros artigos para ele aparecem como texto simples até lá. No dia, rode o build de novo e publique.

## Pendências

1. **Logo definitivo.** O guia (proposta inicial v1) informa que SVG, versões monocromáticas e PNGs isolados ainda serão finalizados.
   O site usa uma assinatura textual provisória ("PEROVANO" + "Engenharia de software"). Ao receber os arquivos:
   - salvar em `assets/brand/` e trocar o conteúdo dos `<a class="brand">` (cabeçalho e rodapé de `index.html`, cabeçalho de `privacy.html` e os templates `HEADER`/`FOOTER` de `scripts/build_blog.py`) por `<img>` — o CSS `.brand img` já está previsto;
   - regenerar favicons e `apple-touch-icon.png` a partir do símbolo, validando em 16, 24 e 32 px;
   - refazer `og-image.png` com o logo.
2. **Favicon provisório.** O ícone atual é um bloco neutro nas cores da marca; não é o símbolo "P".
3. **Casos detalhados.** O portfólio mostra os sites no ar com a descrição de cada um. Para casos completos faltam, por projeto: desafio, solução, participação da PEROVANO, resultado comprovável e autorização para citar nomes e depoimentos.
4. **Processo comercial.** As etapas de "Como trabalhamos" seguem o roteiro do briefing; o item "O que você recebe" de cada etapa deve ser validado contra o processo real.
5. **Sobre.** O nome "Ricardo Perovano" e os perfis vêm do site anterior e do guia. Tempo de mercado, formação, equipe e stack não foram publicados por falta de confirmação.
6. **Contato.** E-mail `contato@lrperovano.com.br` e WhatsApp/telefone +55 27 99855-3591 (atualizados em 30/10/2026). Confirmar que a caixa de e-mail do domínio está recebendo mensagens e que o número tem WhatsApp.
7. **Política de privacidade.** O nome "Perovano Labs" foi trocado por "PEROVANO (L R PEROVANO LTDA)" e o visual foi atualizado; o restante do texto e a data de "Última atualização" não foram alterados. Conferir se o nome do desenvolvedor na loja do app deve acompanhar a mudança e se a data deve ser atualizada.
8. **Arquivos da marca anterior.** `logo.png` e `icon.png` ("Perovano Labs") não são mais referenciados e podem ser removidos.
9. **Conversor JSON → TOON removido.** `modern.html` e `toon-converter.js` saíram do site em 30/10/2026. A `privacy.html` ainda descreve o app Android TOON Converter; se o app não estiver mais publicado, essa seção pode sair da política.
10. **Portfólio.** Confirmar, para cada site (PaceOn, VipDesk, Portal da Igreja, Estudatta, MinhaOS App, Safe Offshore), se é produto próprio ou projeto de cliente, e se há autorização para exibir. As capturas são de 30/10/2026; quando os sites mudarem, refaça as imagens em `assets/img/portfolio/`.
11. **Google Search Console.** Verificar a propriedade `lrperovano.com.br` e enviar `https://lrperovano.com.br/sitemap.xml`. Opcional: Bing Webmaster Tools.
12. **Artigos (30).** Revisar os textos antes de publicar — em especial LGPD, WhatsApp, Pix, domínio/Registro.br, SEO local e os pontos jurídicos de escopo/contratação, cujas regras de terceiros mudam com o tempo e manter um ritmo de publicação (ex.: 1 artigo por semana) — conteúdo novo e atualizado pesa mais que volume publicado de uma vez.
13. **Google Analytics (G-KGNMPTML28).** Só carrega depois de "Aceitar" no aviso de cookies (Consent Mode do Google, com padrão negado). A escolha fica em `localStorage` (`perovano-cookies`) e pode ser revista em "Preferências de cookies", no rodapé. Cliques em WhatsApp e e-mail geram o evento `generate_lead`; marque-o como evento-chave no GA4 para medir conversões. O código do GA está no `<head>` de `index.html`, `privacy.html` e em `GA_TAG` de `scripts/build_blog.py`. A política de privacidade foi atualizada para refletir isso — vale uma revisão jurídica.
