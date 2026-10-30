---
title: "WordPress ou site sob medida: como escolher"
description: "WordPress ou site sob medida? Veja quando cada um faz sentido, os cuidados com plugins, segurança e desempenho, e as opções intermediárias, como CMS headless."
date: 2026-10-30
category: "Sites"
keywords: "wordpress ou site sob medida, site em wordpress vale a pena, site personalizado ou wordpress, cms headless"
---

WordPress costuma ser a melhor escolha quando o site depende de conteúdo publicado com frequência, como um blog, uma área de notícias ou um catálogo editado pela própria equipe, e quando o orçamento pede uma base pronta com temas e plugins já existentes. A empresa ganha um painel conhecido, muitos profissionais no mercado e liberdade para editar sem chamar o desenvolvedor a cada mudança.

Um site sob medida ou estático faz mais sentido quando o conteúdo muda pouco, quando o desempenho e o design próprio pesam na decisão ou quando o site precisa conversar com sistemas da empresa. Nesse caso, o site carrega só o que usa, tem menos peças para manter atualizadas e fica mais fácil de proteger.

Entre os dois extremos existem caminhos intermediários, como o CMS headless e os construtores de páginas. A escolha certa depende menos da tecnologia e mais de quatro perguntas: quem vai editar, com que frequência, o que o site precisa integrar e quem vai cuidar dele depois de publicado.

## O que é o WordPress

WordPress é um sistema de gerenciamento de conteúdo, ou CMS (do inglês *content management system*), de código aberto. Na prática, é um software instalado em um servidor que oferece um painel administrativo para criar páginas, publicar posts, organizar menus e enviar imagens, sem mexer em código.

Ele funciona com duas peças principais:

- **Temas**, que definem a aparência do site: cores, tipografia, layout das páginas.
- **Plugins**, que acrescentam funções: formulários, SEO, loja virtual, cache, backup, multilíngue e muito mais.

O WordPress pode ser instalado em uma hospedagem própria, com controle total e responsabilidade total pelas atualizações, ou usado em serviços que o hospedam por você, com menos trabalho e mais limites sobre o que pode ser instalado. Confira as condições atuais de cada plano antes de decidir.

## Quando o WordPress é a melhor escolha

- **Blog ou área de conteúdo ativa.** Se a estratégia inclui publicar artigos com regularidade para atrair visitas do Google, o editor do WordPress foi feito para isso. O artigo sobre [SEO para sites de empresas](/blog/seo-para-sites-de-empresas/) explica por que esse conteúdo importa.
- **Conteúdo editado com frequência pela equipe.** Cardápios, vagas, eventos, notícias, catálogo de produtos. Quando várias pessoas precisam atualizar o site toda semana, um painel de edição deixa de ser luxo.
- **Orçamento enxuto.** Com um tema bem escolhido e poucos plugins, é possível colocar no ar um site funcional com investimento menor do que o de um projeto desenhado do zero. O artigo sobre [quanto custa um site profissional](/blog/quanto-custa-um-site-profissional/) detalha o que entra nessa conta.
- **Autonomia em relação ao fornecedor.** Como o WordPress é muito difundido, encontrar outro profissional para dar continuidade costuma ser simples.

## Limites e cuidados com o WordPress

O WordPress é uma boa ferramenta, mas não é "instalar e esquecer". Os problemas mais comuns aparecem depois da entrega.

### Atualizações constantes

O núcleo do WordPress, os temas e os plugins recebem atualizações frequentes, muitas delas de segurança, e cada uma pode gerar incompatibilidade entre peças de autores diferentes. Alguém precisa ser responsável por atualizar, testar e manter backups. O artigo sobre [manutenção de software](/blog/manutencao-de-software/) aprofunda esse ponto.

### Segurança dos plugins

Cada plugin é código de terceiros rodando no seu servidor. Plugins abandonados pelo autor, baixados de fontes não oficiais ou mantidos desatualizados são uma porta de entrada comum para invasões. Alguns cuidados básicos:

- Instalar só o necessário e remover o que não é usado.
- Preferir plugins com atualizações recentes e boa reputação.
- Nunca usar versões "pirateadas" de plugins ou temas pagos.
- Usar senhas fortes e autenticação em dois fatores no painel.
- Manter backups automáticos guardados fora do servidor do site.

### Desempenho de temas pesados

Temas "multiuso", que prometem servir para qualquer tipo de negócio, costumam carregar muitos scripts, fontes e estilos que o site nunca usa. Somados a vários plugins, o resultado é um site lento, especialmente no celular. Isso afeta a experiência do visitante e as métricas que o Google acompanha, explicadas no artigo sobre [velocidade do site e Core Web Vitals](/blog/velocidade-do-site-core-web-vitals/). Um WordPress rápido é possível, mas exige tema leve, poucos plugins e cache bem configurado.

### Hospedagem

O WordPress depende de PHP e de um banco de dados, o que pede uma hospedagem com recursos adequados. Planos muito baratos e superlotados deixam qualquer site lento, por melhor que seja o tema. Também vale saber quem cuida das atualizações do servidor e dos backups. O artigo sobre [domínio e hospedagem](/blog/dominio-e-hospedagem/) ajuda a entender o que contratar.

## Quando um site sob medida ou estático faz mais sentido

Site sob medida é aquele cujo código é escrito para o projeto, a partir de um design próprio. Uma variação comum é o **site estático**: as páginas são geradas antecipadamente como arquivos prontos e entregues ao visitante sem consultar banco de dados a cada acesso. Isso reduz o tempo de carregamento e elimina boa parte das brechas de segurança típicas de um painel exposto na internet.

Esse caminho tende a ser melhor quando:

- **O desempenho é prioridade.** O site carrega apenas o código que usa. Não há tema genérico nem dezenas de plugins competindo por recursos.
- **O design precisa ser próprio.** A identidade visual da empresa é desenhada do zero, sem as limitações de adaptar um tema existente.
- **Há integrações.** O site precisa consultar estoque, enviar leads direto para o CRM, mostrar dados de um sistema interno ou conectar com pagamentos. Integrações bem feitas, como as descritas no artigo sobre [integração de sistemas via API](/blog/integracao-de-sistemas-api/), são mais simples de controlar em código próprio.
- **O conteúdo muda pouco.** Um site institucional que recebe ajustes algumas vezes por ano não precisa de um painel de edição que exige atualizações toda semana.

Um exemplo é o site institucional da Safe Offshore, empresa de serviços marítimos, que está entre os [projetos da PEROVANO](/#projetos).

O ponto de atenção é a edição: sem painel, cada mudança de texto passa pelo desenvolvedor. Para quem edita pouco, é aceitável. Para quem publica toda semana, vira gargalo.

## Opções intermediárias

### CMS headless

Em um **CMS headless**, o painel de edição fica separado do site. A equipe edita o conteúdo em um painel, e o site, construído sob medida, busca esse conteúdo por API (uma interface que permite que sistemas troquem dados). O próprio WordPress pode ser usado assim, e também existem CMS criados especificamente para esse modelo.

A vantagem é juntar o melhor dos dois lados: design próprio e desempenho de um site sob medida, com a autonomia de edição de um CMS. A desvantagem é a complexidade maior, já que são duas peças para hospedar e manter. Faz sentido em sites com bastante conteúdo e exigência alta de desempenho ou integração.

### Construtor de páginas

Os **construtores de páginas** permitem montar o layout arrastando blocos, seja como plugin dentro do WordPress, seja como plataforma de criação de sites hospedada. São rápidos para começar e dão autonomia para quem não programa.

Em troca, costumam gerar páginas mais pesadas, prendem o site à ferramenta e limitam integrações. Servem bem para validar uma ideia ou para uma página de campanha simples, como as descritas no artigo sobre [landing page](/blog/o-que-e-landing-page/). O artigo sobre [no-code, low-code ou desenvolvimento](/blog/no-code-low-code-ou-desenvolvimento/) compara esses caminhos com mais detalhe.

## Perguntas para decidir

1. Quem vai editar o site e com que frequência? Toda semana ou algumas vezes por ano?
2. O site terá blog ou outra área de conteúdo publicada com regularidade?
3. O design precisa ser exclusivo ou um tema adaptado atende?
4. O site precisa se integrar a CRM, ERP, pagamentos ou outros sistemas da empresa?
5. Quem vai cuidar das atualizações, da segurança e dos backups depois da entrega?
6. Se trocar de fornecedor, quem fica com o código, o domínio e a hospedagem?

Ao pedir orçamentos, pergunte ao fornecedor qual tecnologia ele propõe e por quê, quantos plugins serão usados, como será a manutenção e o que acontece se o contrato terminar. Uma boa proposta explica a escolha em função das respostas acima, não da preferência de quem desenvolve. O guia sobre [como escolher uma empresa de desenvolvimento](/blog/como-escolher-empresa-de-desenvolvimento/) traz outros critérios.

## Perguntas frequentes

### Site em WordPress é inseguro?

Não por natureza. O núcleo do WordPress é mantido ativamente e recebe correções de segurança. O risco aparece quando o site acumula plugins desatualizados, senhas fracas e nenhuma rotina de manutenção. Com cuidados básicos e atualizações em dia, o WordPress pode ser bastante seguro.

### Site sob medida é sempre mais caro que WordPress?

No investimento inicial, geralmente sim, porque o design e o código são feitos para o projeto. Ao longo do tempo, a diferença tende a diminuir: um site estático costuma exigir menos manutenção, enquanto um WordPress com muitos plugins pede atualizações e testes contínuos, e alguns plugins são pagos por assinatura.

### Dá para migrar de WordPress para um site sob medida depois?

Dá. O conteúdo pode ser exportado e reaproveitado. O cuidado principal é manter os mesmos endereços das páginas ou configurar redirecionamentos, para não perder o posicionamento já conquistado no Google.

### WordPress é bom para SEO?

Ele oferece uma boa base, e há plugins que facilitam títulos, descrições e sitemap. Mas SEO depende mais de conteúdo útil, estrutura e velocidade do que da plataforma.

Se você está decidindo entre WordPress e um site sob medida, vale começar pelo uso que o site vai ter no dia a dia, e não pela tecnologia. A PEROVANO desenvolve sites e pode ajudar a avaliar qual caminho faz sentido para a sua empresa. [Fale conosco](/#contato) para conversar sobre o projeto.
