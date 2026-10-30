---
title: "O que é RAG (geração aumentada por recuperação)"
description: "O que é RAG: como a IA busca trechos nos documentos da empresa para responder com fonte, como funciona, casos de uso, cuidados e a diferença para fine-tuning."
date: 2026-10-30
category: "Inteligência artificial"
keywords: "o que é RAG, geração aumentada por recuperação, retrieval-augmented generation, IA com documentos da empresa"
---

RAG, sigla de *retrieval-augmented generation* (geração aumentada por recuperação), é uma técnica em que a IA, antes de responder, busca os trechos mais relevantes nos documentos da empresa e usa esses trechos como base para a resposta. Em vez de responder só com o que aprendeu no treinamento, o modelo responde com o que está escrito nos seus manuais, políticas e contratos.

Isso resolve um limite importante dos modelos de linguagem: eles não conhecem as informações internas da sua empresa e, quando não sabem, podem inventar. Com RAG, a resposta se apoia em um texto verificável, e o sistema pode mostrar de qual documento a informação veio.

É a técnica mais usada para criar assistentes internos, bases de conhecimento consultáveis e chatbots de atendimento que respondem com as regras da própria empresa.

## Por que o RAG reduz respostas inventadas

Um modelo de linguagem é treinado com grandes volumes de texto público até uma certa data. Ele sabe escrever bem e conhece muitos assuntos gerais, mas não sabe qual é o prazo de troca da sua loja, quais documentos o seu RH exige ou como funciona o seu processo de reembolso.

Quando recebe uma pergunta sobre isso sem contexto, o modelo tende a gerar uma resposta plausível, baseada no que é comum em outras empresas. Esse comportamento se chama **alucinação**: uma resposta com aparência de correta, mas sem base real.

Com RAG, o modelo recebe junto com a pergunta os trechos dos documentos que tratam do assunto e a instrução de responder apenas com base neles. Isso traz três vantagens:

- **Respostas fundamentadas.** O modelo deixa de "chutar" e passa a resumir o que está escrito.
- **Fonte citável.** O sistema sabe quais trechos usou e pode mostrar o documento e a seção, para que a pessoa confira.
- **Atualização simples.** Mudou a política, atualiza-se o documento. Não é preciso treinar nada de novo.

O RAG reduz as alucinações, mas não as elimina. O modelo ainda pode interpretar mal um trecho ou juntar informações de forma errada. Por isso, mostrar a fonte e permitir que o assistente diga "não encontrei essa informação" são partes importantes do projeto.

## Como o RAG funciona por dentro

O artigo sobre [inteligência artificial nas empresas](/blog/inteligencia-artificial-nas-empresas/) resume o fluxo em quatro passos. Aqui, cada etapa em mais detalhe, em linguagem acessível.

### 1. Preparar os documentos

Os documentos chegam em formatos variados: PDF, Word, páginas internas, planilhas, artigos de uma central de ajuda. O primeiro passo é extrair o texto e limpar o que atrapalha, como cabeçalhos repetidos, rodapés e numeração de página. PDFs escaneados precisam de reconhecimento de texto antes.

Nesta etapa também se registram os **metadados** de cada documento: título, data, área responsável, versão e quem pode acessá-lo. Eles serão usados depois para filtrar resultados e controlar permissões.

### 2. Dividir em trechos

Um manual de cem páginas não cabe inteiro em cada pergunta, e nem deveria. O texto é dividido em trechos menores, de alguns parágrafos cada, chamados em inglês de *chunks*. O ideal é que cada trecho trate de um assunto e faça sentido sozinho.

A forma de dividir influencia muito a qualidade. Trechos pequenos demais perdem contexto. Grandes demais misturam assuntos e trazem informação irrelevante. Respeitar a estrutura do documento, como títulos e seções, costuma dar melhores resultados do que cortar por número de caracteres.

### 3. Gerar embeddings

Cada trecho é convertido em um **embedding**: uma lista de números que representa o significado do texto. Trechos com significados parecidos geram listas de números parecidas, mesmo quando usam palavras diferentes. "Prazo para devolução" e "quantos dias tenho para trocar" ficam próximos, embora quase não tenham palavras em comum.

Esses embeddings são guardados em um banco de dados preparado para esse tipo de busca, chamado banco vetorial, ou em uma extensão de um banco de dados já existente.

### 4. Buscar os trechos relevantes

Quando alguém faz uma pergunta, ela também é convertida em embedding. O sistema procura os trechos cujos embeddings estão mais próximos do da pergunta. Isso é a **busca semântica**: uma busca pelo significado, e não pela palavra exata.

Em muitos projetos, a busca semântica é combinada com a busca tradicional por palavras-chave, que funciona melhor para códigos de produto, nomes próprios e números de cláusulas. Também é comum aplicar filtros pelos metadados, como área ou data, e uma etapa de reordenação para colocar os trechos mais úteis no topo.

### 5. Montar a resposta

Os trechos encontrados são enviados ao modelo junto com a pergunta e com instruções como: responda apenas com base nos trechos abaixo, indique a fonte e, se a informação não estiver neles, diga que não sabe. O modelo redige a resposta, e o sistema exibe os links para os documentos usados.

## Casos de uso de RAG na empresa

- **Base de conhecimento interna.** Colaboradores perguntam sobre processos, sistemas e procedimentos e recebem a resposta com o link para o documento. Reduz as interrupções para quem sempre sabe onde as coisas estão.
- **Atendimento ao cliente.** Um [chatbot com IA para atendimento](/blog/chatbot-com-ia-para-atendimento/) responde com base nas regras de entrega, troca e pagamento cadastradas, e não em suposições.
- **Manuais técnicos.** Equipes de campo e suporte consultam manuais extensos de equipamentos ou sistemas com perguntas em linguagem natural.
- **Políticas e normas.** RH, compliance e jurídico disponibilizam políticas internas em um assistente que responde e aponta a cláusula.
- **Apoio a agentes.** [Agentes de IA](/blog/agentes-de-ia-para-empresas/) que executam tarefas usam RAG para consultar regras antes de agir, como a política de descontos ao montar uma proposta.

## Cuidados em um projeto de RAG

### Qualidade e atualização dos documentos

O assistente responde com o que está na base. Documentos desatualizados, duplicados ou contraditórios geram respostas desatualizadas ou contraditórias. Antes de começar, vale fazer uma limpeza: remover versões antigas, definir qual é o documento oficial de cada assunto e nomear um responsável por mantê-lo. Também é preciso definir como as atualizações entram no sistema, de forma automática ou periódica.

### Permissões de acesso por usuário

Se a base reúne documentos de várias áreas, nem todo mundo pode ver tudo. Um estagiário não deve receber, em uma resposta, trechos da planilha de salários. A busca precisa filtrar os trechos conforme as permissões de quem pergunta, de preferência respeitando as mesmas regras de acesso dos sistemas de origem. Esse controle deve ser feito na busca, antes de os trechos chegarem ao modelo.

### Avaliação das respostas

Monte uma lista de perguntas reais com as respostas corretas e rode o sistema contra ela sempre que mudar algo: a forma de dividir os documentos, o modelo ou as instruções. Avalie se o sistema encontrou os trechos certos e se a resposta é fiel a eles. Em produção, colete a avaliação dos usuários e revise uma amostra das conversas.

### Dados sensíveis

Documentos com dados pessoais de clientes ou colaboradores exigem cuidado com a LGPD: saber o que está indexado, quem pode acessar, onde os dados são processados e por quanto tempo ficam guardados. Muitas vezes, a melhor decisão é não indexar esses documentos ou remover os dados pessoais antes. O artigo sobre [LGPD em sites e sistemas](/blog/lgpd-em-sites-e-sistemas/) aprofunda o tema.

## RAG ou treinar o modelo (fine-tuning)

**Fine-tuning**, ou ajuste fino, é continuar o treinamento de um modelo com exemplos próprios para mudar o comportamento dele. É uma técnica diferente do RAG, com objetivos diferentes.

O RAG serve para dar **conhecimento** ao modelo: fatos, regras, conteúdos que mudam. O fine-tuning serve para ajustar **comportamento**: um formato de resposta muito específico, um estilo de escrita, uma tarefa de classificação repetida em grande volume.

Para responder com base em documentos da empresa, o RAG costuma ser a escolha certa porque:

- A informação é atualizada só trocando o documento, sem novo treinamento.
- A resposta pode citar a fonte, algo que um modelo ajustado não faz de forma confiável.
- As permissões podem ser controladas por usuário, já que a informação não fica "dentro" do modelo.
- O investimento inicial e a manutenção costumam ser menores.

Os dois podem ser combinados, mas na maioria dos projetos empresariais o RAG com boas instruções resolve sem fine-tuning.

## Perguntas frequentes

### O RAG funciona com qualquer tipo de documento?

Funciona com qualquer documento do qual seja possível extrair o texto. PDFs escaneados precisam de reconhecimento de texto antes. Tabelas complexas, imagens e diagramas exigem um tratamento específico e podem precisar ser descritos em texto.

### Os documentos da empresa são usados para treinar a IA?

No RAG, os documentos não são usados para treinar o modelo: os trechos são enviados no momento de cada pergunta. O que acontece com esses dados no fornecedor depende do serviço e do plano contratado, e deve ser conferido nos termos do fornecedor.

### Quanto custa um projeto de RAG?

Depende do volume e da variedade dos documentos, do trabalho de preparação, das integrações com os sistemas de origem, das regras de permissão e do volume de perguntas. Há o custo de desenvolvimento, concentrado no início, e o custo recorrente de uso do modelo e de infraestrutura. Um piloto com um conjunto pequeno de documentos ajuda a estimar os dois.

Se a sua empresa tem manuais, políticas ou uma base de conhecimento que a equipe consulta com frequência, um assistente com RAG pode ser um bom primeiro projeto de IA. Conheça nossas [soluções](/#solucoes) ou [entre em contato](/#contato) para conversar sobre os documentos e o uso esperado.
