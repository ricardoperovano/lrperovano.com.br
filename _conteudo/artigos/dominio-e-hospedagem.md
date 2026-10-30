---
title: "Domínio e hospedagem: o que são e como escolher"
description: "Entenda a diferença entre domínio e hospedagem, como registrar um .com.br no nome da empresa, o que é DNS e quais cuidados exigir do fornecedor do site."
date: 2026-10-30
category: "Sites"
keywords: "domínio e hospedagem, diferença entre domínio e hospedagem, como registrar domínio com.br, tipos de hospedagem de site"
---

Domínio é o endereço do site, como `suaempresa.com.br`. Hospedagem é o servidor onde os arquivos do site ficam guardados e de onde são entregues a quem visita. Um é o nome na placa; o outro é o imóvel. São contratados separadamente, podem estar em empresas diferentes e cada um tem a sua renovação.

Para escolher bem, a regra principal é simples: o domínio deve estar registrado no nome da sua empresa, com acesso controlado por alguém de dentro. A hospedagem deve combinar com o tipo de site, ter HTTPS, backup e suporte. Preço importa, mas vem depois desses pontos.

Os problemas mais comuns não são técnicos: domínio no nome de um ex-funcionário ou de uma agência antiga, renovação esquecida, senhas que ninguém sabe onde estão.

## Qual a diferença entre domínio e hospedagem

O **domínio** é um nome registrado por um período, que a empresa precisa renovar para continuar usando. Ele não guarda nenhum arquivo. Sozinho, só aponta para algum lugar.

A **hospedagem** é o serviço que mantém o site funcionando: um computador ligado o tempo todo, conectado à internet, que responde quando alguém digita o endereço. Também pode guardar banco de dados, formulários e, em alguns planos, e-mails.

Os dois se conectam pelo DNS, explicado mais abaixo. Por isso é possível trocar de hospedagem sem trocar de domínio, e o endereço que os clientes conhecem continua o mesmo.

## Domínio .com.br: como registrar

Domínios terminados em `.br`, como `.com.br`, são registrados no Registro.br, a entidade responsável pelo domínio do Brasil. O registro pode ser feito diretamente lá ou por meio de empresas que oferecem o serviço. O titular precisa informar CPF ou CNPJ.

Alguns cuidados no registro:

- **Registre no CNPJ da empresa.** O domínio é um ativo do negócio. Se ficar no CPF de um sócio, de um funcionário ou do fornecedor, a transferência depende da boa vontade de quem é o titular.
- **Use um e-mail de contato que a empresa controla.** Avisos de vencimento e pedidos de confirmação chegam nesse e-mail. Se ele for de uma pessoa que saiu, os avisos se perdem.
- **Guarde o acesso em local seguro.** Login, senha e autenticação em dois fatores, quando disponível, devem ficar com a empresa. O fornecedor pode receber permissão técnica para configurar, sem ser o titular.

Domínios como `.com` são registrados por outras empresas credenciadas, com regras próprias. Confira as condições atuais antes de contratar.

## Renovação e o risco de perder o domínio

O domínio é registrado por um período e precisa ser renovado. Quando a renovação não acontece, o site e os e-mails param de funcionar. Se a situação não for resolvida dentro do prazo previsto pelas regras do registro, o domínio pode voltar a ficar disponível e ser registrado por outra pessoa.

Recuperar um domínio que já foi registrado por terceiros pode ser difícil, demorado ou impossível. Por isso:

- ative a renovação automática quando o registrador oferecer;
- registre por mais de um ano, se fizer sentido para o orçamento;
- coloque o vencimento no calendário de alguém responsável;
- revise uma vez por ano se os dados do titular e do contato estão corretos.

## DNS em linguagem simples

DNS (sistema de nomes de domínio) é a lista de contatos da internet. Ele traduz o nome `suaempresa.com.br` para o endereço numérico do servidor onde o site está. Essas informações ficam em registros, e os mais comuns são:

- **A:** aponta o domínio para o endereço do servidor do site.
- **CNAME:** aponta um nome para outro nome, como `www` apontando para o domínio principal.
- **MX:** indica qual serviço recebe os e-mails do domínio.
- **TXT:** guarda textos de verificação e configurações de segurança do e-mail.

Quem gerencia o DNS pode mudar para onde o site e os e-mails apontam. Uma alteração errada derruba os dois. Por isso, o acesso ao DNS merece o mesmo cuidado que o acesso ao domínio. Depois de uma alteração, ela pode levar de minutos a algumas horas para valer em todos os lugares, porque os servidores guardam as respostas por um tempo.

## Tipos de hospedagem

### Compartilhada

Vários sites dividem o mesmo servidor. É a opção mais simples de contratar e costuma vir com painel de controle pronto. Atende bem sites pequenos com pouco tráfego. A desvantagem é que o desempenho pode ser afetado por outros sites no mesmo servidor, e as configurações possíveis são limitadas.

### VPS

VPS (servidor virtual privado) é uma fatia de um servidor com recursos reservados para o seu site. Há mais controle e desempenho mais previsível. Em compensação, alguém precisa configurar e manter o sistema operacional, as atualizações de segurança e o monitoramento. Se ninguém fizer isso, o VPS fica pior do que uma hospedagem compartilhada bem administrada.

### Nuvem

Na hospedagem em nuvem, os recursos podem crescer ou diminuir conforme a demanda, e há serviços gerenciados de banco de dados, armazenamento e filas. É a escolha comum para sistemas web, lojas com variação de tráfego e aplicações que precisam de alta disponibilidade. Exige conhecimento técnico para configurar e acompanhar custos.

### Hospedagem para sites estáticos

Site estático é aquele em que as páginas são geradas antes e entregues prontas, sem banco de dados a cada visita. Para esse tipo, existem serviços especializados que distribuem os arquivos por servidores em várias regiões. O resultado costuma ser um site rápido, com pouca manutenção e menos pontos de ataque. Sites institucionais e blogs se encaixam bem nesse modelo. A velocidade também ajuda no Google, como mostra o artigo sobre [Core Web Vitals](/blog/velocidade-do-site-core-web-vitals/).

A escolha entre esses modelos depende de como o site é construído. Um site em WordPress precisa de servidor com PHP e banco de dados; um site estático não. O comparativo [WordPress ou site sob medida](/blog/wordpress-ou-site-sob-medida/) ajuda a entender essa parte.

## E-mail no domínio

E-mail como `contato@suaempresa.com.br` transmite mais confiança do que um endereço gratuito e fica com a empresa quando um funcionário sai. Ele pode estar no mesmo lugar da hospedagem ou em um serviço de e-mail separado, apontado pelo registro MX.

Separar e-mail e site costuma ser uma boa prática. Uma troca de hospedagem ou um problema no servidor do site não afeta os e-mails. Também vale configurar os registros de autenticação de e-mail (SPF, DKIM e DMARC), que ajudam a evitar que as mensagens caiam no spam e dificultam o uso do domínio por golpistas.

## HTTPS e certificado

HTTPS é a versão segura do protocolo da web. Ele protege os dados entre o navegador do visitante e o servidor, e o navegador mostra o cadeado na barra de endereço. Para isso, o site precisa de um certificado digital válido.

Hoje, HTTPS é obrigatório na prática para qualquer site. Navegadores alertam o visitante quando ele falta, e formulários sem proteção expõem dados pessoais, o que também é tema da [LGPD em sites e sistemas](/blog/lgpd-em-sites-e-sistemas/). Muitas hospedagens oferecem certificados gratuitos com renovação automática. Confirme que a renovação está funcionando, porque um certificado vencido gera alerta de segurança para todos os visitantes.

## Backups

Backup é uma cópia do site e dos dados guardada em outro lugar, que permite restaurar tudo após uma falha, invasão ou erro humano. Pergunte:

- Com que frequência o backup é feito?
- Por quanto tempo as cópias ficam guardadas?
- Elas ficam em local separado do servidor principal?
- Quem faz a restauração e em quanto tempo?
- Já foi feito um teste de restauração?

Backup que nunca foi testado é uma suposição.

## O que exigir do fornecedor

Ao contratar o site, peça por escrito:

1. Domínio registrado no CNPJ da empresa, com acesso de titular sob controle de vocês.
2. Conta de hospedagem em nome da empresa, ou acesso administrativo garantido.
3. Lista de todos os serviços contratados, com vencimentos e responsáveis.
4. HTTPS configurado com renovação automática.
5. Política de backup com frequência, retenção e teste de restauração.
6. Documentação das configurações de DNS e e-mail.
7. Previsão de manutenção e atualizações de segurança após a entrega.

Esses itens entram na comparação de propostas tanto quanto o design. O artigo sobre [quanto custa um site profissional](/blog/quanto-custa-um-site-profissional/) explica os custos recorrentes, e o guia sobre [o que um site institucional precisa ter](/blog/o-que-um-site-institucional-precisa-ter/) mostra o restante da lista.

> Se o fornecedor desaparecer amanhã, a empresa consegue continuar com o site e os e-mails? Se a resposta for não, há algo para corrigir.

## Perguntas frequentes

### Posso ter o domínio em uma empresa e a hospedagem em outra?

Pode, e é comum. Basta configurar o DNS para apontar o domínio para a hospedagem. Essa separação até facilita trocar de hospedagem no futuro.

### Meu domínio está no nome da agência antiga. O que fazer?

Peça a transferência de titularidade para o CNPJ da empresa. O processo depende do registrador e normalmente exige a autorização do titular atual. Quanto antes for resolvido, melhor, porque a dificuldade cresce se o contato com o fornecedor se perder.

### Hospedagem mais barata serve para minha empresa?

Depende do site. Um site institucional simples pode funcionar bem em planos de entrada ou em hospedagem para sites estáticos. Sistemas, lojas e sites com muito tráfego precisam de mais recursos e de suporte técnico que atenda rápido.

Se a sua empresa quer organizar domínio, hospedagem e e-mail ou está planejando um site novo, vale fazer isso desde o início com tudo em nome de vocês. A PEROVANO desenvolve [sites e sistemas](/#solucoes) e entrega a estrutura documentada. [Fale conosco](/#contato) para conversar sobre o seu caso.
