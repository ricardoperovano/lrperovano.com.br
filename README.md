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
| `privacy.html` | Política de privacidade (endereço preservado; usada pelo app TOON Converter) |
| `assets/css/site.css` | Tokens da identidade (`--brand-*`) e todos os estilos |
| `assets/js/site.js` | Menu mobile, ano do rodapé, âncoras antigas, entrada das seções |
| `assets/img/favicon.svg` | Ícone provisório neutro (origem de `favicon.ico`, `favicon-*.png`, `apple-touch-icon.png`) |
| `og-image.png` | Imagem de compartilhamento 1200×630 |
| `modern.html`, `toon-converter.js` | Conversor JSON → TOON (preservados, sem alteração) |

Contatos (WhatsApp, e-mail, LinkedIn, GitHub) aparecem em dois blocos do `index.html`: seção `#contato` e rodapé.
Ao alterar um contato, busque pelo valor antigo no projeto para atualizar todas as ocorrências (inclusive `privacy.html`).

Âncoras do site anterior: `#projetos`, `#sobre` e `#contato` continuam existindo; `#servicos` e `#top` são redirecionadas por `site.js`.

## Pendências

1. **Logo definitivo.** O guia (proposta inicial v1) informa que SVG, versões monocromáticas e PNGs isolados ainda serão finalizados.
   O site usa uma assinatura textual provisória ("PEROVANO" + "Engenharia de software"). Ao receber os arquivos:
   - salvar em `assets/brand/` e trocar o conteúdo dos `<a class="brand">` (cabeçalho e rodapé de `index.html`, cabeçalho de `privacy.html`) por `<img>` — o CSS `.brand img` já está previsto;
   - regenerar favicons e `apple-touch-icon.png` a partir do símbolo, validando em 16, 24 e 32 px;
   - refazer `og-image.png` com o logo.
2. **Favicon provisório.** O ícone atual é um bloco neutro nas cores da marca; não é o símbolo "P".
3. **Projetos e casos.** Só há material verificável sobre o TOON Converter (produto próprio). Para uma seção de projetos faltam, por caso: desafio, solução, participação, resultado comprovável e autorização para citar nomes, telas e depoimentos. Os dois cartões genéricos do site anterior foram removidos por não serem casos reais.
4. **Processo comercial.** As etapas de "Como trabalhamos" seguem o roteiro do briefing; o item "O que você recebe" de cada etapa deve ser validado contra o processo real.
5. **Sobre.** O nome "Ricardo Perovano" e os perfis vêm do site anterior e do guia. Tempo de mercado, formação, equipe e stack não foram publicados por falta de confirmação.
6. **E-mail no domínio.** O guia recomenda um e-mail @lrperovano.com.br; o site mantém o endereço Gmail existente.
7. **Política de privacidade.** O nome "Perovano Labs" foi trocado por "PEROVANO (L R PEROVANO LTDA)" e o visual foi atualizado; o restante do texto e a data de "Última atualização" não foram alterados. Conferir se o nome do desenvolvedor na loja do app deve acompanhar a mudança e se a data deve ser atualizada.
8. **Arquivos da marca anterior.** `logo.png` e `icon.png` ("Perovano Labs") não são mais referenciados e podem ser removidos.
9. **`modern.html`** mantém o visual antigo (roxo) e não é linkado pelo site.
