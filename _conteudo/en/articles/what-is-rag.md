---
title: "What is RAG (retrieval-augmented generation)?"
description: "What RAG is: how AI searches your company documents to answer with sources, how it works step by step, use cases, pitfalls and how it differs from fine-tuning."
date: 2026-10-30
category: "Artificial intelligence"
keywords: "what is RAG, retrieval-augmented generation, RAG vs fine-tuning, AI with company documents"
pt: "o-que-e-rag"
---

RAG, short for *retrieval-augmented generation*, is a technique in which an AI system, before answering, searches your company's documents for the most relevant passages and uses them as the basis for its answer. Instead of answering only from what it learned in training, the model answers from what is written in your manuals, policies and contracts.

This solves an important limitation of language models: they don't know your company's internal information and, when they don't know, they may make things up. With RAG, the answer rests on text that can be verified, and the system can show which document the information came from.

It is the most widely used technique for building internal assistants, searchable knowledge bases and customer service chatbots that answer according to the company's own rules.

## Why RAG reduces made-up answers

A language model is trained on large volumes of public text up to a certain date. It writes well and knows a lot about general topics, but it doesn't know your store's return window, which documents your HR team requires or how your refund process works.

When it gets a question about these things without context, the model tends to produce a plausible answer based on what is common at other companies. This behavior is called **hallucination**: an answer that looks correct but has no real basis.

With RAG, the model receives, along with the question, the passages from the documents that cover the topic and the instruction to answer only from them. That brings three advantages:

- **Grounded answers.** The model stops guessing and starts summarizing what is written.
- **Citable sources.** The system knows which passages it used and can show the document and section, so the person can check.
- **Simple updates.** If the policy changes, you update the document. Nothing needs to be retrained.

RAG reduces hallucinations, but it doesn't eliminate them. The model can still misread a passage or combine information incorrectly. That's why showing the source and letting the assistant say "I couldn't find that information" are important parts of the project.

## How RAG works under the hood

Our article on [how to use AI in business](/en/blog/how-to-use-ai-in-business/) summarizes the flow in four steps. Here is each stage in more detail, in plain language.

### 1. Prepare the documents

Documents come in many formats: PDF, Word, intranet pages, spreadsheets, help center articles. The first step is to extract the text and clean up what gets in the way, such as repeated headers, footers and page numbers. Scanned PDFs need text recognition (OCR) first.

This stage also records each document's **metadata**: title, date, owning department, version and who can access it. This is used later to filter results and control permissions.

### 2. Split into chunks

A hundred-page manual doesn't fit into every question, and it shouldn't. The text is split into smaller passages of a few paragraphs each, called *chunks*. Ideally, each chunk covers one topic and makes sense on its own.

How you split has a big influence on quality. Chunks that are too small lose context. Chunks that are too large mix topics and bring in irrelevant information. Following the document's structure, such as headings and sections, usually gives better results than cutting by character count.

### 3. Generate embeddings

Each chunk is converted into an **embedding**: a list of numbers that represents the meaning of the text. Chunks with similar meanings produce similar lists of numbers, even when they use different words. "Return deadline" and "how many days do I have to exchange this" end up close together, even though they share almost no words.

These embeddings are stored in a database built for this kind of search, called a vector database, or in an extension to a database you already use.

### 4. Retrieve the relevant chunks

When someone asks a question, it is also converted into an embedding. The system looks for the chunks whose embeddings are closest to the question's. This is **semantic search**: searching by meaning rather than by exact words.

In many projects, semantic search is combined with traditional keyword search, which works better for product codes, proper names and clause numbers. It's also common to apply metadata filters, such as department or date, and a reranking step that puts the most useful chunks at the top.

### 5. Compose the answer

The retrieved chunks are sent to the model along with the question and instructions such as: answer only from the passages below, cite the source and, if the information isn't there, say you don't know. The model writes the answer, and the system displays links to the documents it used.

## RAG use cases in business

- **Internal knowledge base.** Employees ask about processes, systems and procedures and get the answer with a link to the document. It cuts down interruptions for the people who always know where things are.
- **Customer service.** An [AI chatbot for customer service](/en/blog/ai-chatbot-for-customer-service/) answers based on the delivery, return and payment rules the company has documented, not on assumptions.
- **Technical manuals.** Field and support teams search long equipment or system manuals with natural-language questions.
- **Policies and standards.** HR, compliance and legal teams make internal policies available through an assistant that answers and points to the relevant clause.
- **Support for agents.** [AI agents](/en/blog/ai-agents-for-business/) that carry out tasks use RAG to check the rules before acting, such as the discount policy when putting together a proposal.

## What to watch out for in a RAG project

### Document quality and freshness

The assistant answers with what is in the knowledge base. Outdated, duplicated or contradictory documents produce outdated or contradictory answers. Before you start, it's worth cleaning up: remove old versions, decide which document is the official one for each topic and assign someone to maintain it. You also need to define how updates get into the system, automatically or on a schedule.

### Per-user access permissions

If the knowledge base brings together documents from several departments, not everyone can see everything. An intern shouldn't receive passages from the payroll spreadsheet in an answer. The search needs to filter chunks according to the permissions of the person asking, ideally following the same access rules as the source systems. This control should happen in the search step, before the chunks reach the model.

### Evaluating answers

Build a list of real questions with their correct answers and run the system against it whenever something changes: how documents are split, the model or the instructions. Check whether the system found the right chunks and whether the answer is faithful to them. In production, collect user feedback and review a sample of conversations.

### Sensitive data

Documents containing personal data about customers or employees call for care under data protection law. In Brazil, that is the LGPD (Lei Geral de Proteção de Dados), Brazil's data protection law, similar in spirit to Europe's GDPR. Companies in other countries should check the data protection rules that apply to them. In any case, you need to know what is indexed, who can access it, where the data is processed and how long it is kept. Often the best decision is not to index these documents at all, or to remove the personal data first. Our article on [the LGPD for websites and software](/en/blog/lgpd-brazil-data-protection-for-websites-and-software/) goes deeper into the topic.

## RAG or training the model (fine-tuning)

**Fine-tuning** means continuing to train a model on your own examples to change how it behaves. It is a different technique from RAG, with different goals.

RAG gives the model **knowledge**: facts, rules, content that changes. Fine-tuning adjusts **behavior**: a very specific answer format, a writing style, a classification task repeated at high volume.

To answer from company documents, RAG is usually the right choice because:

- Information is updated just by replacing the document, with no retraining.
- The answer can cite its source, something a fine-tuned model doesn't do reliably.
- Permissions can be controlled per user, since the information doesn't live "inside" the model.
- Upfront investment and maintenance tend to be lower.

The two can be combined, but in most business projects, RAG with good instructions does the job without fine-tuning.

## Frequently asked questions

### Does RAG work with any kind of document?

It works with any document you can extract text from. Scanned PDFs need text recognition first. Complex tables, images and diagrams require specific handling and may need to be described in text.

### Are the company's documents used to train the AI?

With RAG, the documents are not used to train the model: the chunks are sent at the time of each question. What happens to that data at the vendor depends on the service and the plan you have contracted, and should be checked in the vendor's terms.

### How much does a RAG project cost?

It depends on the volume and variety of documents, the preparation work, the integrations with source systems, the permission rules and the volume of questions. There is the development cost, concentrated at the start, and the recurring cost of model usage and infrastructure. A pilot with a small set of documents helps estimate both.

If your company has manuals, policies or a knowledge base that the team looks up often, a RAG assistant can be a good first AI project. PEROVANO works remotely and can run the project in English. Explore our [solutions](/en/#solutions) or [get in touch](/en/#contact) to talk about your documents and how you expect to use them.
