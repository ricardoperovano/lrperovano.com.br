---
title: "O que é PWA (Progressive Web App) e quando vale a pena"
description: "Entenda o que é PWA, o site que se instala como aplicativo e funciona offline. Veja vantagens, limitações no Android e no iPhone e quando escolher app nativo."
date: 2026-10-30
category: "Sistemas"
keywords: "o que é PWA, progressive web app, PWA ou app nativo, aplicativo web progressivo"
---

PWA, sigla em inglês para Progressive Web App (aplicativo web progressivo), é um site construído para se comportar como aplicativo. O usuário acessa pelo navegador e, se quiser, instala na tela inicial do celular ou do computador. A partir daí, o PWA abre com ícone próprio, em tela cheia, sem a barra de endereço, e pode continuar funcionando mesmo sem internet.

Na prática, é um único produto que serve como site e como aplicativo. Não é preciso baixar nada de uma loja para começar a usar, e quem preferir pode instalar com um toque. As atualizações chegam assim que são publicadas no servidor, sem esperar aprovação de loja nem que o usuário clique em "atualizar".

Um PWA costuma ser uma boa escolha para sistemas de uso frequente, áreas de cliente, ferramentas internas e produtos que precisam ser encontrados no Google. Ele perde para o app nativo quando o projeto depende de recursos avançados do aparelho, de processamento pesado ou de presença forte nas lojas de aplicativos.

## Como um PWA funciona

Três peças transformam um site comum em PWA:

- **HTTPS**: o site precisa ser servido com conexão segura, o que já é padrão em qualquer projeto sério.
- **Manifesto**: um arquivo que informa ao aparelho o nome do aplicativo, o ícone, as cores e como ele deve abrir, por exemplo em tela cheia.
- **Service worker**: um script que roda em segundo plano no navegador, entre o aplicativo e a internet. Ele guarda telas e dados no aparelho, permite abrir o app sem conexão e recebe notificações.

Com essas peças, o navegador reconhece o site como instalável. No Android, navegadores como o Chrome costumam oferecer a instalação diretamente. No iPhone, o caminho é pelo menu de compartilhar do navegador, na opção de adicionar à tela de início.

O funcionamento offline não é automático. Cabe ao projeto decidir o que fica disponível sem internet: só as telas já visitadas, um catálogo inteiro, ou formulários que o usuário preenche offline e que são enviados quando a conexão volta. Cada nível exige mais trabalho de desenvolvimento e testes.

## Vantagens do PWA

### Um código para todos os aparelhos

O mesmo PWA roda no Android, no iPhone, no computador e no tablet. Em vez de manter um app para Android, outro para iOS e um site separado, a equipe mantém uma base de código. Isso reduz o esforço de desenvolvimento, de testes e de manutenção ao longo dos anos.

### Atualização sem loja

Correções e novas funcionalidades entram no ar assim que são publicadas. Não há fila de revisão das lojas nem usuários presos em versões antigas. Para sistemas com regras de negócio que mudam com frequência, isso faz diferença.

### Custo menor que dois apps nativos

Desenvolver dois aplicativos nativos significa, em geral, duas bases de código, duas rotinas de publicação e, muitas vezes, profissionais com especialidades diferentes. Um PWA tende a custar menos por concentrar tudo em um projeto web. O artigo sobre [quanto custa desenvolver um aplicativo](/blog/quanto-custa-desenvolver-um-aplicativo/) detalha os fatores que mais pesam no orçamento.

### Pode ser encontrado no Google

Como o PWA é um site, suas páginas públicas podem ser indexadas pelos buscadores. Um app nativo vive dentro da loja; o conteúdo dele não aparece na busca do mesmo jeito. Para produtos que dependem de tráfego orgânico, isso pesa. As boas práticas de [SEO para sites de empresas](/blog/seo-para-sites-de-empresas/) e de [velocidade do site e Core Web Vitals](/blog/velocidade-do-site-core-web-vitals/) se aplicam diretamente.

### Sem atrito para começar

O usuário pode experimentar o produto pelo link, sem baixar nada. A instalação vira uma escolha posterior, para quem já viu valor. Em produtos novos, isso reduz a barreira de entrada.

## Limitações que precisam entrar na conta

### Acesso a recursos do aparelho

Navegadores modernos permitem usar câmera, microfone, geolocalização, notificações e compartilhamento. Mas alguns recursos ainda são restritos ou indisponíveis para aplicações web, principalmente fora do Android: comunicação com certos acessórios por Bluetooth, leitura de NFC, tarefas longas em segundo plano e integração profunda com o sistema operacional. Se o produto depende de algo assim, vale confirmar a compatibilidade antes de decidir.

### Diferenças entre Android e iPhone

O Android, com o Chrome, costuma oferecer suporte mais amplo a recursos de PWA. No iPhone, os navegadores em geral usam o mesmo mecanismo do Safari, e a Apple historicamente libera recursos web com mais cautela.

Um exemplo é a notificação push. O iOS passou a aceitar notificações push para PWAs instalados na tela inicial a partir da versão 16.4. Ou seja, no iPhone o usuário precisa instalar o PWA e autorizar as notificações; um site aberto apenas no navegador não as recebe. Esse tipo de detalhe muda com novas versões do sistema, por isso o ideal é testar nos aparelhos reais do público antes de prometer uma funcionalidade.

### Presença nas lojas

Muita gente procura aplicativos diretamente na Google Play ou na App Store. Um PWA não aparece lá por padrão. É possível empacotar um PWA para publicar na Google Play, e existem caminhos para a App Store, mas a Apple tende a exigir que o aplicativo ofereça mais do que um site dentro de uma moldura. Se estar nas lojas é parte da estratégia de marketing, isso precisa ser planejado desde o início.

### Desempenho em casos extremos

Para a maioria dos sistemas de negócio, como cadastros, agendamentos, painéis e pedidos, um PWA bem feito é rápido o suficiente. Jogos com gráficos pesados, edição de vídeo e processamento intenso no aparelho continuam sendo território dos apps nativos.

## PWA, app nativo ou multiplataforma: como escolher

Existem três caminhos principais, e cada um resolve um conjunto diferente de necessidades.

**PWA** é indicado quando:

- o produto precisa funcionar bem no celular e no computador;
- ser encontrado no Google é importante;
- as regras mudam com frequência e as atualizações precisam ser imediatas;
- os recursos do aparelho exigidos são os comuns, como câmera, localização e notificações;
- o orçamento pede uma base de código só.

**App nativo**, desenvolvido separadamente para Android e iOS com as ferramentas de cada plataforma, é indicado quando:

- o desempenho é crítico, como em jogos ou processamento de mídia;
- o app depende de recursos específicos do sistema ou de acessórios;
- a experiência precisa seguir à risca os padrões visuais de cada plataforma.

**Multiplataforma**, com tecnologias como React Native ou Flutter, gera apps instaláveis pelas lojas para Android e iOS a partir de um código compartilhado. É indicado quando:

- a presença nas lojas é obrigatória;
- o app precisa de recursos do aparelho que a web não oferece bem no iPhone;
- o orçamento não comporta dois apps nativos.

> A pergunta central não é qual tecnologia é melhor, e sim quais recursos o produto precisa no primeiro ano e onde o público vai procurá-lo.

Uma estratégia comum é começar com um PWA para validar o produto com usuários reais, no espírito de um [MVP](/blog/mvp-como-tirar-ideia-de-sistema-do-papel/), e partir para um app de loja só quando houver demanda clara. Como o back-end (a parte do sistema que roda no servidor, com regras e banco de dados) pode ser reaproveitado, a migração não significa começar do zero. O guia sobre [como criar um aplicativo](/blog/como-criar-um-aplicativo/) mostra as etapas do projeto em qualquer um dos caminhos.

## O que perguntar ao fornecedor

- Quais funcionalidades vão funcionar offline e o que acontece com dados preenchidos sem conexão?
- As notificações vão funcionar no iPhone e no Android? Com quais condições?
- Em quais aparelhos e navegadores o PWA será testado?
- Há plano para publicar nas lojas, se isso for necessário no futuro?
- Como o back-end será construído para servir também a um eventual app nativo?

A PEROVANO desenvolve sistemas web, PWAs e aplicativos, e as [soluções](/#solucoes) descrevem cada frente de trabalho.

## Perguntas frequentes

### PWA é a mesma coisa que site responsivo?

Não. Site responsivo é o que se adapta a diferentes tamanhos de tela. Um PWA também é responsivo, mas vai além: pode ser instalado, abrir em tela cheia, funcionar offline e enviar notificações.

### Um PWA funciona no iPhone?

Funciona. O usuário instala pelo menu de compartilhar do navegador. Algumas funcionalidades têm restrições no iOS, e as notificações push só funcionam com o PWA instalado na tela inicial, a partir do iOS 16.4.

### Dá para transformar o site atual em PWA?

Em muitos casos, sim. Adicionar manifesto e service worker é relativamente simples. O trabalho maior está em adaptar a navegação para parecer aplicativo e decidir o que funciona offline. Sites muito antigos ou lentos podem exigir uma reformulação antes.

### PWA substitui um aplicativo de loja?

Para muitos sistemas de negócio, sim. Para produtos que dependem de presença nas lojas ou de recursos avançados do aparelho, não. Nesses casos, o PWA pode ser o primeiro passo, e o app de loja vem depois.

Se a dúvida é entre PWA, app nativo ou multiplataforma, o caminho mais seguro é partir dos recursos que o produto realmente precisa. A PEROVANO pode ajudar a avaliar o seu caso e indicar a opção mais adequada. [Fale conosco](/#contato) para conversar sobre o projeto.
