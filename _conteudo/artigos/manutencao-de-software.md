---
title: "Manutenção de software: o que inclui e por que é necessária"
description: "Manutenção de software: tipos (corretiva, adaptativa, evolutiva e preventiva), monitoramento, backups, modelos de contrato e o que definir no acordo."
date: 2026-10-30
category: "Gestão de projetos"
keywords: "manutenção de software, manutenção de sistemas, contrato de manutenção de software, suporte de sistema, manutenção de site"
---

Manutenção de software é o trabalho contínuo que mantém um site, sistema ou aplicativo funcionando, seguro e útil depois que ele entra no ar. Inclui corrigir defeitos, atualizar bibliotecas e componentes, adaptar o sistema a mudanças em navegadores, sistemas operacionais e serviços de terceiros, aplicar correções de segurança, acompanhar o funcionamento e garantir backups.

Ela é necessária porque o software não vive isolado. Ele depende de dezenas de componentes que mudam o tempo todo, e o próprio negócio muda. Um sistema que ninguém atualiza não fica parado: ele envelhece, acumula falhas de segurança conhecidas e, cedo ou tarde, deixa de funcionar em algum ponto.

Para quem contrata, a pergunta prática não é se haverá manutenção, mas como ela será organizada: quem faz, o que está incluído, em quanto tempo os problemas são atendidos e como isso é cobrado.

## Os quatro tipos de manutenção

### Corretiva

É a correção de defeitos: um botão que não responde, um cálculo errado, um relatório que trava com muitos dados. Alguns aparecem logo após a entrega, outros só quando o uso cresce ou surge uma combinação de dados que ninguém previu. Defeitos encontrados no período de garantia costumam ser corrigidos sem custo, conforme o contrato do projeto.

### Adaptativa

É a manutenção que ajusta o sistema a mudanças externas, mesmo que nada tenha mudado no negócio. Exemplos comuns:

- **Bibliotecas e frameworks.** Quase todo software usa componentes prontos, chamados dependências. Eles recebem versões novas, com correções, e versões antigas deixam de ser mantidas.
- **Navegadores.** Chrome, Safari, Firefox e Edge são atualizados com frequência. Recursos mudam de comportamento ou deixam de existir.
- **Sistemas operacionais.** Novas versões de Android e iOS trazem regras de permissão e privacidade diferentes. As lojas de aplicativos também atualizam periodicamente as exigências para publicar e manter apps.
- **APIs de terceiros.** API é a interface pela qual um sistema conversa com outro. Gateways de pagamento, plataformas de mensagem, serviços de mapas e redes sociais lançam novas versões e desativam as antigas. Quando isso acontece, a integração precisa ser ajustada. O artigo sobre [integração de sistemas via API](/blog/integracao-de-sistemas-api/) explica esse funcionamento.
- **Regras legais e fiscais.** Mudanças em obrigações, como a forma de emitir documentos ou de tratar dados pessoais, podem exigir ajustes.

### Evolutiva

É a inclusão de novas funcionalidades ou a alteração das existentes para acompanhar o negócio: um novo relatório, uma etapa a mais no fluxo de aprovação, uma integração com outro sistema. É a parte da manutenção que gera valor novo, e normalmente é tratada como pequenos projetos, com estimativa e aprovação prévia.

### Preventiva e de segurança

É o trabalho feito antes que o problema apareça: aplicar correções de segurança, revisar permissões de acesso, melhorar trechos de código frágeis, otimizar consultas lentas ao banco de dados, renovar certificados. Tem pouca visibilidade para o usuário, mas é o que evita incidentes.

## Monitoramento e backups

Monitorar é acompanhar o sistema em produção para saber de um problema antes que o cliente reclame. O básico inclui:

- Verificação de disponibilidade, que avisa quando o site ou a API sai do ar.
- Registro de erros, com alerta quando eles aumentam.
- Acompanhamento de uso de servidor, banco de dados e armazenamento.
- Alertas de vencimento do domínio e do certificado de segurança, responsável pelo cadeado que aparece no navegador.

Backup é a cópia de segurança dos dados e, quando aplicável, dos arquivos enviados pelos usuários. Um bom plano de backup define a frequência, por quanto tempo as cópias são guardadas, onde ficam (de preferência em local separado do servidor principal) e, principalmente, quando a restauração é testada. Backup que nunca foi restaurado é uma suposição, não uma garantia.

## O que acontece com um sistema sem manutenção

- **Vulnerabilidades conhecidas.** Falhas de segurança em bibliotecas populares são publicadas e corrigidas. Quem não atualiza fica exposto justamente às falhas que já são de conhecimento público, as mais fáceis de explorar.
- **Incompatibilidades.** Uma atualização de navegador ou do sistema operacional do celular quebra uma tela. Uma API de pagamento desativa a versão usada e a cobrança para de funcionar.
- **Dependências sem suporte.** Versões antigas de linguagens e frameworks deixam de receber correções. Com o tempo, atualizar exige saltos grandes, que custam bem mais do que pequenas atualizações regulares.
- **Lentidão e custos crescentes.** O volume de dados aumenta, consultas ficam lentas e o servidor precisa de mais recursos.
- **Perda de conhecimento.** Sem ninguém acompanhando o sistema, quem conhecia os detalhes se afasta. Quando um problema aparece, alguém precisa reaprender tudo às pressas.

Em sites, o efeito também aparece no Google: páginas lentas ou com erros perdem desempenho, como explica o artigo sobre [velocidade do site e Core Web Vitals](/blog/velocidade-do-site-core-web-vitals/).

> A manutenção adiada não desaparece: ela se acumula e volta mais cara, geralmente em um momento pior.

## Modelos comuns de contrato

Os modelos variam entre fornecedores, mas três aparecem com frequência:

- **Pacote de horas.** A empresa contrata uma quantidade de horas por mês ou por período, usadas em correções, ajustes e pequenas evoluções. É importante definir o que acontece com horas não usadas e com o que exceder o pacote.
- **Mensalidade com escopo definido.** Um valor fixo cobre atividades combinadas, como monitoramento, backups, atualizações de segurança e um volume de correções. Evoluções costumam ser orçadas à parte.
- **Sob demanda.** Cada necessidade é orçada e aprovada separadamente. Funciona para sistemas simples e estáveis, mas não oferece tempo de resposta garantido nem acompanhamento preventivo.

Muitos contratos combinam os modelos: uma mensalidade para o básico e horas ou orçamentos para evolução. O modelo de cobrança se parece com o da contratação do projeto, discutido em [escopo fechado ou por hora](/blog/escopo-fechado-ou-por-hora/).

## O que definir no acordo

- **O que está incluído e o que não está.** Monitoramento, backups, atualizações de dependências, correções, pequenos ajustes, evoluções, suporte a usuários.
- **Prioridades.** Uma classificação simples, por exemplo: crítico (sistema fora do ar ou cobrança parada), alto (função importante com falha, sem alternativa), normal e baixo.
- **Tempo de resposta e de solução por prioridade.** Tempo de resposta é quanto se leva para começar a tratar o chamado. Tempo de solução é quanto se leva para resolver. São coisas diferentes e devem estar separadas.
- **Horário de atendimento.** Dias úteis, horário comercial ou plantão para casos críticos.
- **Canal de abertura de chamados** e como o histórico fica registrado.
- **Responsabilidades da empresa contratante**, como manter contas de terceiros ativas e informar mudanças no negócio.
- **Acessos e propriedade.** Quem tem acesso ao servidor, ao repositório e aos backups, e como isso é devolvido se o contrato terminar.
- **Relatório periódico** com o que foi feito, as horas usadas e os riscos identificados.

## Como avaliar a saúde de um sistema herdado

Sistema herdado é aquele desenvolvido por outra equipe, que agora precisa de um novo responsável. Antes de assumir a manutenção, uma avaliação inicial costuma responder a estas perguntas:

1. Existe acesso completo ao código, ao repositório, ao servidor, ao banco de dados, ao domínio e às contas de terceiros?
2. O código no repositório é o mesmo que está em produção?
3. Quais versões de linguagem, framework e bibliotecas estão em uso, e quais já perderam suporte?
4. Há vulnerabilidades conhecidas nas dependências?
5. Existem backups recentes, e eles foram restaurados com sucesso alguma vez?
6. Há testes automatizados? Quanto do sistema eles cobrem?
7. Existe documentação de instalação, publicação e regras de negócio?
8. Quais integrações externas o sistema usa, e as versões dessas APIs continuam ativas?
9. Como os dados pessoais estão protegidos? O guia sobre [LGPD em sites e sistemas](/blog/lgpd-em-sites-e-sistemas/) ajuda nessa parte.

O resultado é uma lista de riscos por prioridade e um plano: o que resolver já, o que pode esperar e se faz mais sentido manter, reformar por partes ou reescrever algum módulo.

## Perguntas frequentes

### Site institucional simples também precisa de manutenção?

Sim, em menor escala. Mesmo um site simples depende de hospedagem, certificado, domínio e, muitas vezes, de um gerenciador de conteúdo com plugins que precisam de atualização. O artigo [WordPress ou site sob medida](/blog/wordpress-ou-site-sob-medida/) discute como a escolha da plataforma afeta essa rotina.

### A garantia do projeto substitui a manutenção?

Não. A garantia cobre defeitos do que foi entregue, por um período definido. A manutenção cobre o que muda depois: atualizações, segurança, adaptações e evolução.

### Quanto da manutenção dá para prever?

Monitoramento, backups e atualizações de rotina são previsíveis. Mudanças de APIs de terceiros e correções urgentes de segurança nem sempre. Por isso, vale combinar uma parte fixa e uma reserva para imprevistos.

### Posso trocar o fornecedor de manutenção?

Pode, desde que a empresa tenha os acessos e a documentação. Uma avaliação inicial do sistema, como a descrita acima, é a forma mais segura de fazer a transição.

A PEROVANO desenvolve sites, sistemas e aplicativos, como os que estão em [projetos](/#projetos), e pode ajudar a avaliar a situação do seu. Se o seu sistema está sem acompanhamento ou você quer organizar a manutenção, [fale conosco](/#contato).
