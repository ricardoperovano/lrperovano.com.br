---
title: "Velocidade do site e Core Web Vitals: o que corrigir"
description: "Entenda como a velocidade do site afeta vendas e SEO, o que medem LCP, INP e CLS, como avaliar no PageSpeed Insights e quais correções priorizar."
date: 2026-10-30
category: "Sites"
keywords: "velocidade do site, core web vitals, site lento, pagespeed insights"
---

A velocidade do site afeta duas coisas que importam para quem vende: a experiência de quem chega e a forma como o Google avalia a página. Um site que demora a mostrar o conteúdo, trava ao tocar em um botão ou "pula" enquanto carrega perde visitantes antes que eles leiam a oferta. E cada visitante perdido é um contato que não acontece.

O Google mede essa experiência com os Core Web Vitals, um conjunto de três métricas: **LCP** (quanto tempo o conteúdo principal leva para aparecer), **INP** (quanto tempo a página leva para responder a uma ação) e **CLS** (quanto o layout se mexe sozinho). Elas fazem parte dos sinais de experiência da página considerados na busca. Não substituem conteúdo relevante, mas podem pesar a favor ou contra quando há páginas concorrentes parecidas.

As causas de lentidão costumam ser conhecidas: imagens pesadas, scripts de terceiros em excesso, hospedagem fraca e temas inchados. Dá para medir com ferramentas gratuitas e corrigir em ordem, começando pelo que tem mais impacto.

## Por que a velocidade afeta conversão e SEO

Conversão é quando o visitante faz o que a página propõe: pedir orçamento, chamar no WhatsApp, comprar. Para isso, ele precisa ver a oferta e conseguir agir sem atrito. Pense em quem chega pelo celular, com sinal instável, a partir de um anúncio pago. Se a primeira tela fica em branco por vários segundos, parte dessas pessoas volta para a busca. A empresa pagou pelo clique e não teve a chance de apresentar o serviço.

No SEO (o conjunto de práticas para aparecer no Google), a velocidade entra pelos Core Web Vitals como sinal de experiência. O guia de [SEO para sites de empresas](/blog/seo-para-sites-de-empresas/) mostra como a parte técnica se combina com conteúdo e autoridade.

Em [landing pages](/blog/o-que-e-landing-page/), páginas criadas para uma única ação, o efeito costuma ser ainda mais visível, porque quase todo o tráfego vem de campanhas e cada segundo de espera tem custo direto.

## O que são LCP, INP e CLS, em linguagem de gestor

### LCP: o conteúdo principal apareceu?

LCP significa *Largest Contentful Paint*. Mede quanto tempo leva para o maior elemento visível da primeira tela aparecer, geralmente a imagem de destaque ou o título principal. É a métrica que traduz a sensação de "o site abriu".

**Bom:** até 2,5 segundos. Acima de 4 segundos, o Google considera ruim.

### INP: o site respondeu quando cliquei?

INP significa *Interaction to Next Paint*. Mede o tempo entre uma ação do usuário, como tocar em um botão, abrir um menu ou digitar em um campo, e a resposta visual da página. Em 2024, o INP substituiu o FID, uma métrica anterior que avaliava apenas a primeira interação.

**Bom:** até 200 milissegundos. Um INP alto aparece como aquele botão que parece não funcionar e faz a pessoa tocar de novo.

### CLS: a página ficou parada?

CLS significa *Cumulative Layout Shift*. Mede quanto os elementos mudam de lugar sozinhos durante o carregamento. O exemplo clássico: a pessoa vai tocar em um link, um banner carrega em cima e ela acaba clicando em outra coisa.

**Bom:** até 0,1. É um índice sem unidade; quanto menor, mais estável a página.

> As três métricas respondem a perguntas simples: o conteúdo apareceu rápido, o site respondeu quando toquei, a página ficou parada enquanto eu lia?

## Como medir a velocidade do site

### PageSpeed Insights

O PageSpeed Insights é uma ferramenta gratuita do Google. Basta colar o endereço da página. O relatório mostra dois tipos de dado, e a diferença entre eles é importante:

- **Dados de campo:** vêm de usuários reais do Chrome que visitaram a página nos últimos 28 dias. É o que o Google usa para avaliar os Core Web Vitals. Sites com pouco tráfego podem não ter esses dados.
- **Dados de laboratório:** uma simulação feita na hora, em condições controladas. Servem para diagnosticar problemas e testar correções, mas não refletem exatamente a experiência real.

Abaixo da nota, a ferramenta lista oportunidades de melhoria, como imagens grandes demais. Não persiga a nota 100 de laboratório; o que importa é que os dados de campo fiquem na faixa "bom". Teste a versão para celular, que costuma ser mais exigente, e várias páginas, não só a inicial.

### Google Search Console

O Search Console é o painel gratuito do Google para acompanhar como o site aparece na busca. Ele tem um relatório de Core Web Vitals que agrupa as páginas do site em "boas", "precisam de melhoria" e "ruins", separando celular e computador. Serve para ver o problema em escala e acompanhar o efeito das correções.

## Causas comuns de lentidão

### Imagens pesadas

É uma das causas mais frequentes. Fotos são publicadas no tamanho original, muito maiores do que a tela vai exibir. As correções são conhecidas: redimensionar para o tamanho de uso, usar formatos modernos como WebP ou AVIF, servir versões diferentes para celular e computador e adiar o carregamento de imagens que estão fora da primeira tela.

Um cuidado: a imagem principal, que define o LCP, não deve ter carregamento adiado. Ela precisa chegar o quanto antes.

### Scripts de terceiros

Chat, pixels de anúncios, mapas incorporados, vídeos, ferramentas de mapa de calor, widgets de avaliação. Cada um adiciona código que o navegador precisa baixar e executar, e muitos afetam diretamente o INP. É comum encontrar ferramentas instaladas para uma campanha antiga que ninguém usa mais.

Faça um inventário: o que está instalado, quem usa e para quê. O que não tem dono pode sair. O que fica pode ser carregado depois do conteúdo principal ou só quando o usuário interage.

### Hospedagem

Se o servidor demora para começar a responder, todo o resto atrasa. Hospedagens compartilhadas muito baratas, servidores distantes do público e ausência de cache (cópias prontas das páginas para entregar mais rápido) são causas típicas. Uma CDN, rede de servidores que entrega os arquivos a partir do ponto mais próximo do visitante, costuma ajudar.

### Temas e construtores inchados

Temas prontos e construtores visuais trazem recursos para atender qualquer tipo de site, e muitos carregam todo esse código em todas as páginas. Somam-se a isso plugins acumulados ao longo dos anos.

Nesses casos, otimizar tem limite. Às vezes a correção mais eficiente é reconstruir o site com uma base mais enxuta, e essa decisão entra no cálculo de [quanto custa um site profissional](/blog/quanto-custa-um-site-profissional/).

### Fontes e elementos sem espaço reservado

Fontes personalizadas mal configuradas atrasam a exibição do texto. Imagens, anúncios e banners sem dimensões definidas provocam deslocamentos de layout e pioram o CLS. São correções pequenas, mas fazem diferença.

## O que corrigir primeiro

Com o diagnóstico em mãos, a ordem abaixo costuma trazer o melhor retorno para o esforço:

1. **Comece pelas páginas que geram negócio.** Home, páginas de serviço e landing pages de campanha vêm antes do blog ou da página institucional.
2. **Otimize as imagens.** É a correção mais barata e geralmente a de maior efeito no LCP.
3. **Corte scripts de terceiros sem uso** e adie o carregamento dos que ficam. Isso ajuda principalmente o INP.
4. **Reserve espaço para imagens, vídeos e banners** definindo dimensões. Isso resolve a maior parte dos problemas de CLS.
5. **Revise hospedagem, cache e CDN** se o servidor demora para responder mesmo com as páginas leves.
6. **Avalie a base do site.** Se as etapas anteriores não bastaram, o problema pode estar no tema ou na plataforma.

Depois de cada mudança, confira no PageSpeed Insights e acompanhe no Search Console. Lembre que os dados de campo consideram um período de 28 dias, então a melhora leva algumas semanas para aparecer por completo.

Velocidade não é um ajuste feito uma vez: cada nova ferramenta de marketing ou plugin pode desfazer o trabalho. Vale incluir uma checagem periódica na manutenção do site. Entre as [soluções](/#solucoes) que oferecemos estão a criação de sites com essa base de desempenho e a revisão de sites existentes.

## Perguntas frequentes

### Nota baixa no PageSpeed Insights significa que o site é lento?

Não necessariamente. A nota de 0 a 100 vem do teste de laboratório, uma simulação em condições específicas. O que o Google usa para avaliar a experiência são os dados de campo, de usuários reais.

Um site pode ter nota mediana no laboratório e Core Web Vitals bons no campo, e vice-versa. Use a nota como diagnóstico, não como meta.

### Melhorar a velocidade garante subir no Google?

Não. Os Core Web Vitals são um dos sinais considerados, e a relevância do conteúdo continua pesando mais. Um site rápido com conteúdo fraco dificilmente supera uma página que responde melhor à busca.

O ganho mais direto está na conversão: mais pessoas veem a oferta e conseguem agir.

### Trocar de hospedagem resolve tudo?

Raramente. A hospedagem afeta o tempo de resposta do servidor, mas imagens pesadas, scripts de terceiros e temas inchados continuam pesando no navegador do visitante. Vale trocar quando o diagnóstico mostra que o servidor é o gargalo.

Se o seu site está lento e não está claro onde está o problema, uma análise técnica ajuda a separar o que é ajuste rápido do que exige mudança de base. [Fale com a PEROVANO](/#contato) e conte como o site está hoje.
