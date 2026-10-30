---
title: "Como integrar Pix e pagamentos ao seu sistema"
description: "Como integrar Pix, boleto e cartão ao seu sistema: gateway ou banco, QR Code dinâmico com webhook, Pix Automático, conciliação, estornos e segurança."
date: 2026-10-30
category: "Automação"
keywords: "integração com Pix, integrar pagamentos ao sistema, API Pix, gateway de pagamento"
---

Integrar Pix e pagamentos a um sistema significa fazer o próprio sistema gerar a cobrança, receber a confirmação do pagamento e dar baixa sozinho, sem ninguém conferir extrato. O cliente vê o QR Code ou o formulário de cartão na tela, paga, e o pedido, a mensalidade ou a ordem de serviço mudam de status automaticamente.

Há dois caminhos principais. O primeiro é usar um gateway ou intermediador de pagamento, uma empresa que oferece Pix, boleto e cartão em uma única API (interface que permite que sistemas conversem entre si). O segundo é integrar diretamente com o banco ou a instituição de pagamento onde a empresa tem conta, usando a API Pix que essas instituições disponibilizam.

O gateway costuma ser mais rápido de implantar e reúne vários meios de pagamento. A integração direta tende a dar mais controle sobre o Pix e pode ter outra estrutura de custos. A escolha depende dos meios de pagamento necessários, do volume e de quanto a empresa quer depender de um intermediário.

## Gateway ou integração direta com o banco

### Gateway ou intermediador de pagamento

O gateway fica entre o sistema da empresa e as instituições financeiras. Uma integração só dá acesso a Pix, boleto, cartão de crédito e, em muitos casos, assinaturas recorrentes. Ele também cuida de boa parte da segurança do cartão e oferece painel para consultar transações.

Pontos de atenção:

- As taxas e prazos de repasse variam bastante entre fornecedores e por meio de pagamento. Compare as condições atuais diretamente com cada um.
- Em alguns modelos, o dinheiro passa por uma conta do intermediador antes de chegar à conta da empresa.
- Trocar de gateway depois exige refazer parte da integração, então vale isolar esse código no sistema.

### Integração direta com o banco ou instituição de pagamento

O Pix foi criado pelo Banco Central do Brasil, que também definiu um padrão de API para as instituições participantes. Por isso, a integração direta segue uma estrutura parecida de banco para banco, embora cada um tenha detalhes próprios de credenciamento e autenticação.

Em geral, ela exige conta jurídica na instituição, habilitação da API e um certificado digital para autenticar as chamadas. Faz sentido quando o Pix é o principal meio de recebimento e a empresa quer o dinheiro direto na própria conta. Para cartão, a integração direta com adquirentes é mais complexa e raramente compensa para empresas pequenas e médias.

## Pix com QR Code dinâmico e confirmação automática

Existem dois tipos de QR Code Pix. O **estático** é fixo, pode ser reutilizado e normalmente não identifica qual cobrança está sendo paga. Serve para doações ou balcão, mas obriga alguém a conferir o extrato.

O **dinâmico** é gerado pelo sistema para cada cobrança, com valor, identificador único e, se necessário, data de validade. É ele que permite a automação completa:

1. O sistema cria a cobrança na API do banco ou do gateway e recebe o QR Code e o código "copia e cola".
2. O cliente paga pelo aplicativo do banco.
3. A instituição envia um webhook, um aviso automático para um endereço do sistema, informando que aquela cobrança foi paga.
4. O sistema confere os dados, dá baixa e dispara o próximo passo: liberar o acesso, emitir o recibo, avisar a equipe.

O webhook pode falhar ou chegar mais de uma vez. Um sistema bem feito trata isso: registra cada aviso, ignora duplicados e consulta periodicamente as cobranças pendentes para não depender só do aviso. O artigo sobre [integração de sistemas via API](/blog/integracao-de-sistemas-api/) explica webhooks e reprocessamento com mais detalhe.

Um exemplo é o Portal da Igreja, desenvolvido pela PEROVANO, em que o dízimo é pago por Pix com QR Code dentro de uma plataforma de gestão com membros e financeiro. Ele está entre os [projetos](/#projetos) da empresa.

## Pix Automático para cobranças recorrentes

O Pix Automático foi lançado pelo Banco Central em 2025 para cobranças que se repetem, como mensalidades, assinaturas e contas de consumo. Em termos gerais, o cliente autoriza uma única vez, no aplicativo do próprio banco, que aquela empresa faça cobranças periódicas. A partir daí, os pagamentos acontecem conforme as regras autorizadas, e o cliente pode consultar ou cancelar a autorização pelo banco.

Para a empresa, é uma alternativa ao boleto mensal e ao cartão de crédito recorrente. A disponibilidade, os requisitos de adesão e as condições variam entre instituições, então vale confirmar com o banco ou o gateway como o recurso funciona hoje e o que o sistema precisa implementar.

## Boleto e cartão

### Boleto

O boleto ainda é exigido por muitos clientes empresariais. O sistema registra o boleto pela API, envia o documento ao cliente e recebe a notificação de pagamento. A diferença em relação ao Pix é o prazo: a confirmação não é instantânea, o que precisa estar refletido nas regras de liberação de pedidos.

### Cartão de crédito e tokenização

No cartão, o principal cuidado é não deixar os dados do cartão passarem pelo servidor da empresa. Os gateways oferecem formulários ou componentes próprios que enviam os dados diretamente para eles e devolvem um token, um código que representa aquele cartão sem revelar o número.

O sistema guarda apenas o token. Com ele, é possível cobrar de novo, por exemplo em uma **assinatura recorrente**, sem pedir o cartão ao cliente a cada mês. Muitos gateways oferecem a gestão de assinaturas pronta, com novas tentativas automáticas quando a cobrança é recusada.

## Conciliação automática

Conciliação é conferir se o que foi cobrado bate com o que entrou na conta. Feita à mão, consome horas e gera erros. Com a integração, o sistema faz isso sozinho:

- Cada cobrança tem um identificador único, ligado ao pedido ou cliente.
- O pagamento confirmado dá baixa no registro certo, sem digitação.
- Relatórios cruzam cobranças, pagamentos, taxas e repasses.
- Diferenças, como pagamento a menor ou em duplicidade, viram alertas para a equipe.

A conciliação é uma das automações com retorno mais claro. O guia sobre [como automatizar processos na empresa](/blog/como-automatizar-processos-na-empresa/) mostra como priorizar esse tipo de tarefa. Em produtos por assinatura, ela é parte essencial do faturamento, como discutido em [como criar um SaaS](/blog/como-criar-um-saas/).

## Estornos e falhas

Pagamento nunca é só o caminho feliz. O sistema precisa prever:

- **Devoluções de Pix**: total ou parcial, iniciadas pela empresa por meio da API.
- **Estornos e contestações de cartão**: quando o portador contesta a compra junto ao banco emissor, o gateway informa e o sistema precisa atualizar o pedido.
- **Cobranças expiradas**: QR Codes e boletos vencidos devem mudar de status e, se for o caso, gerar nova cobrança.
- **Instabilidade do fornecedor**: se a API não responder, o sistema deve tentar de novo sem criar cobranças duplicadas.
- **Avisos ao cliente**: confirmação, lembrete e falha de pagamento. Mensagens pelo WhatsApp podem ajudar, como mostra o artigo sobre [integração com a API do WhatsApp Business](/blog/whatsapp-business-api-integracao/).

## Segurança

Os dados de cartão são protegidos por um padrão internacional de segurança, o PCI DSS. Armazenar número, validade ou código de segurança exige certificação adequada e um nível de controle que raramente faz sentido para quem não é do setor de pagamentos. A regra prática é nunca armazenar dados de cartão no próprio sistema e usar a tokenização do gateway.

Outros cuidados:

- Credenciais da API, chaves e certificados ficam em local seguro no servidor, nunca no código-fonte nem no aplicativo instalado no celular.
- O endereço que recebe webhooks deve validar a origem do aviso antes de dar baixa.
- Acesso ao painel do gateway e do banco com autenticação em dois fatores e usuários individuais.
- Dados pessoais de pagadores seguem a LGPD, como explicado em [LGPD em sites e sistemas](/blog/lgpd-em-sites-e-sistemas/).

> Uma integração de pagamento só está pronta quando trata bem as falhas, não apenas quando o primeiro pagamento funciona.

## O que perguntar ao fornecedor

- Quais meios de pagamento estão disponíveis e quais são as taxas e prazos de repasse atuais?
- A API oferece webhooks? Como validar que o aviso é legítimo?
- Existe ambiente de testes para simular pagamentos, estornos e falhas?
- Como funcionam assinaturas, Pix Automático e novas tentativas de cobrança?
- Há relatórios ou API de extrato para conciliação?

## Perguntas frequentes

### Preciso de gateway para receber Pix no sistema?

Não necessariamente. É possível integrar direto com a API Pix do banco ou instituição de pagamento. O gateway faz mais sentido quando também são necessários cartão, boleto ou assinaturas em um só lugar.

### Qual a diferença entre QR Code estático e dinâmico?

O estático é fixo e reutilizável, sem identificar a cobrança. O dinâmico é gerado para cada cobrança, com valor e identificador, o que permite a confirmação automática pelo sistema.

### Posso guardar o cartão do cliente para cobranças futuras?

Pode guardar o token gerado pelo gateway, não os dados do cartão. O token permite cobranças recorrentes sem que o número do cartão passe pelo seu sistema.

### Quanto custa integrar pagamentos?

Depende de quantos meios de pagamento entram, do tratamento de falhas, da conciliação e das regras de negócio envolvidas. As taxas por transação são definidas por cada fornecedor e devem ser comparadas à parte.

Um sistema que gera a cobrança e dá baixa sozinho libera a equipe para o que importa e reduz erros no caixa. A PEROVANO desenvolve sistemas e integrações de pagamento e pode ajudar a escolher o caminho mais adequado ao seu volume e aos seus meios de recebimento. [Fale conosco](/#contato) para conversar sobre o projeto.
