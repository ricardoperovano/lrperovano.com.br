---
title: "LGPD em sites e sistemas: o que a lei exige na prática"
description: "O que a LGPD exige de sites e sistemas: bases legais, coleta mínima, política de privacidade, cookies, direitos do titular, segurança, incidentes e terceiros."
date: 2026-10-30
category: "Sistemas"
keywords: "LGPD em sites e sistemas, LGPD para sites, adequação à LGPD, LGPD no desenvolvimento de software"
---

A LGPD (Lei Geral de Proteção de Dados Pessoais, Lei nº 13.709/2018) se aplica aos sites e sistemas de empresas que coletem ou usem dados de pessoas físicas, como nome, e-mail, telefone, CPF, endereço ou histórico de compras. Na prática, ela exige que a empresa saiba quais dados coleta, por que coleta, com qual justificativa legal, por quanto tempo guarda, com quem compartilha e como protege essas informações.

Para um site, isso significa formulários que pedem só o necessário, política de privacidade clara, banner de cookies que funcione de verdade e um canal para o titular exercer seus direitos. Para um sistema, entram também controle de acesso, registro de quem acessa o quê, plano para incidentes e contratos com fornecedores que tratam dados em nome da empresa.

Este artigo tem caráter informativo e técnico. Ele não substitui a orientação de um profissional jurídico, que deve avaliar o caso concreto da sua empresa.

## Conceitos básicos para entender a lei

Alguns termos aparecem o tempo todo quando se fala de LGPD:

- **Dado pessoal:** qualquer informação que identifique ou permita identificar uma pessoa.
- **Dado pessoal sensível:** dados sobre saúde, origem racial ou étnica, religião, opinião política, filiação sindical, vida sexual, dados genéticos ou biométricos. Exigem cuidado redobrado.
- **Titular:** a pessoa a quem os dados se referem.
- **Tratamento:** qualquer operação com dados, como coletar, armazenar, consultar, compartilhar ou excluir.
- **Controlador:** quem decide sobre o tratamento. Em geral, a empresa dona do site ou do sistema.
- **Operador:** quem trata os dados em nome do controlador, como a empresa de hospedagem, a plataforma de e-mail marketing ou o fornecedor do software.

## Bases legais: toda coleta precisa de uma justificativa

A LGPD lista hipóteses que autorizam o tratamento de dados, chamadas de **bases legais**. Entre elas estão o consentimento do titular, a execução de um contrato, o cumprimento de obrigação legal ou regulatória e o legítimo interesse do controlador, além de outras previstas na lei.

O ponto prático é este: cada finalidade de uso precisa estar ligada a uma base legal adequada. O endereço de entrega de um pedido se justifica pela execução do contrato. A emissão de nota fiscal, por obrigação legal. O envio de newsletter costuma depender de consentimento. A escolha da base legal certa para cada caso é uma decisão que deve envolver orientação jurídica.

Um erro comum é tratar o consentimento como resposta para tudo. Ele é uma das bases, nem sempre a mais adequada.

## Coletar só o necessário

O princípio da necessidade pede que se colete o mínimo de dados para cumprir a finalidade. Em um site, isso significa revisar cada formulário:

- Um formulário de contato precisa de CPF? Quase nunca.
- Data de nascimento é usada para alguma coisa? Se não for, retire do formulário.
- O telefone é obrigatório ou opcional?

Menos dados coletados significa menos risco em caso de vazamento. Essa revisão é mais fácil no planejamento, por isso vale incluí-la no [briefing do projeto](/blog/como-fazer-briefing-de-software/).

## Política de privacidade clara

A política de privacidade explica ao titular, em linguagem compreensível, como os dados são tratados. Ela deve dizer, no mínimo:

- quais dados são coletados e de que forma;
- para quais finalidades;
- com quem são compartilhados, como fornecedores e parceiros;
- por quanto tempo são guardados;
- quais são os direitos do titular e como exercê-los;
- quem é o controlador e como entrar em contato com o encarregado.

Copiar a política de outro site é um problema: ela precisa descrever o que o seu site faz de fato, incluindo ferramentas de análise de tráfego e pixels de anúncios.

## Consentimento e banner de cookies

Quando o consentimento for a base legal aplicável, ele precisa ser livre, informado e inequívoco, para uma finalidade específica. Caixas já marcadas e textos vagos como "aceito tudo" não atendem a esse padrão. O titular também precisa conseguir revogar o consentimento com facilidade.

Cookies são pequenos arquivos que o site grava no navegador. Alguns são necessários ao funcionamento, como manter o usuário logado. Outros servem para análise de audiência ou publicidade e, em geral, dependem de consentimento.

Um banner de cookies que funciona de verdade:

- separa os cookies por categoria (necessários, análise, marketing);
- só carrega os scripts opcionais depois que o visitante aceita;
- permite recusar com a mesma facilidade com que permite aceitar;
- deixa o visitante mudar a escolha depois.

O erro mais frequente é o banner decorativo, que aparece quando os scripts de rastreamento já foram carregados. Controlar esses scripts também ajuda na [velocidade do site](/blog/velocidade-do-site-core-web-vitals/).

## Direitos do titular

A lei garante ao titular uma série de direitos, entre eles: confirmar se a empresa trata seus dados, acessar esses dados, corrigir informações incorretas, pedir a eliminação de dados tratados com base em consentimento, solicitar a portabilidade, saber com quem os dados foram compartilhados e revogar o consentimento.

Para o sistema, isso significa conseguir localizar todos os dados de uma pessoa, exportá-los, corrigi-los e excluí-los ou anonimizá-los quando for o caso. Com dados espalhados em planilhas e sistemas sem ligação, um pedido simples vira trabalho manual demorado. Uma boa [integração de sistemas via API](/blog/integracao-de-sistemas-api/) ajuda a manter os dados organizados e rastreáveis.

## Segurança e controle de acesso

A LGPD exige medidas técnicas e administrativas para proteger os dados. Em um sistema, isso inclui, entre outros pontos:

- **Controle de acesso por perfil:** cada pessoa vê só o que precisa para o seu trabalho. O atendente não precisa ver dados financeiros, por exemplo.
- **Autenticação forte:** senhas armazenadas com hash, usando algoritmos próprios para isso (nunca em texto puro) e, para acessos administrativos, verificação em duas etapas.
- **Criptografia em trânsito:** HTTPS em todo o site e em todas as integrações.
- **Backups protegidos** e testados.
- **Atualizações de segurança** do servidor, do framework e das bibliotecas.

### Registro de quem acessa

Manter **logs de acesso**, ou seja, registros de quem consultou ou alterou determinado dado e quando, ajuda a investigar incidentes, identificar acessos indevidos e comprovar boas práticas. Esses registros também precisam ser protegidos.

## Incidentes de segurança

Incidente é qualquer evento que comprometa a confidencialidade, a integridade ou a disponibilidade dos dados, como um vazamento, um acesso não autorizado ou a perda de um banco de dados.

Quando um incidente pode causar risco ou dano relevante aos titulares, a lei prevê a comunicação à ANPD (Autoridade Nacional de Proteção de Dados) e aos titulares afetados. Por isso, o plano precisa existir antes: quem é acionado, como conter o problema, como avaliar o impacto e como registrar o ocorrido.

## O papel do encarregado (DPO)

O **encarregado**, também chamado de DPO (*Data Protection Officer*), é a pessoa ou empresa indicada pelo controlador como canal de comunicação com os titulares e com a ANPD. Ele recebe pedidos e reclamações e orienta a equipe sobre boas práticas.

A identidade e o contato do encarregado devem estar disponíveis de forma clara, normalmente na política de privacidade. Existem regras específicas e simplificadas para empresas de pequeno porte, que devem ser verificadas com orientação jurídica.

## Operadores e fornecedores

Quase todo site e sistema depende de terceiros: hospedagem, e-mail, gateway de pagamento, CRM, serviço de IA. Cada um que trata dados em nome da empresa é um operador.

Na prática, é preciso:

- mapear quais fornecedores recebem dados pessoais;
- verificar onde esses dados ficam armazenados e se há transferência para outros países;
- ter cláusulas contratuais sobre proteção de dados;
- confirmar as medidas de segurança do fornecedor.

O mesmo vale para quem desenvolve o software. Ao escolher entre [sistema sob medida ou software pronto](/blog/sistema-sob-medida-ou-software-pronto/), pergunte quem tem acesso ao ambiente de produção e como funcionam os backups. Projetos com [inteligência artificial](/blog/inteligencia-artificial-nas-empresas/) pedem o mesmo cuidado.

## Privacidade desde o projeto

Adequar um sistema pronto costuma ser mais trabalhoso do que construir já com a privacidade em mente. Definir perfis de acesso, prazos de retenção e logs na fase de desenho evita retrabalho. Conheça as [soluções](/#solucoes) que desenvolvemos para sites e sistemas.

> Adequação à LGPD não é um documento publicado no rodapé do site. É a soma de decisões técnicas e de processo que precisam se sustentar no dia a dia.

## Perguntas frequentes

### Um site institucional simples precisa se adequar à LGPD?

Sim, se ele coleta qualquer dado pessoal, mesmo que seja só nome e e-mail em um formulário de contato, ou se usa cookies de análise e publicidade. O esforço é menor do que em um sistema, mas política de privacidade, coleta mínima e banner de cookies continuam necessários.

### Basta publicar uma política de privacidade?

Não. A política descreve o que acontece, mas o site e o sistema precisam funcionar de acordo com ela. Se a política diz que os cookies de marketing dependem de consentimento, eles não podem ser carregados antes do aceite.

### Quem é responsável se o fornecedor do sistema vazar os dados?

A lei distribui responsabilidades entre controlador e operador conforme o papel de cada um. Por isso, contratos claros e fornecedores com boas práticas são importantes. A análise de um caso concreto deve ser feita com orientação jurídica.

### Preciso apagar todos os dados quando o cliente pedir?

Nem sempre. Alguns dados precisam ser mantidos por obrigação legal, como registros fiscais. O sistema deve excluir ou anonimizar o que pode ser eliminado e guardar, protegido, o que a lei exige.

Se você está planejando um site ou sistema e quer que a proteção de dados esteja no desenho desde o início, podemos conversar sobre o projeto. [Fale conosco](/#contato) e conte o que precisa ser construído.
