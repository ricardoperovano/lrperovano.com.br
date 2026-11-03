---
title: "WhatsApp Business API integration: how it works"
description: "How WhatsApp Business API integration works: how it differs from the app, what it enables, the requirements, the costs and the risks of unofficial tools."
date: 2026-10-30
category: "Automation"
keywords: "whatsapp business api integration, official whatsapp api, whatsapp business platform, whatsapp crm integration"
pt: "whatsapp-business-api-integracao"
---

A WhatsApp Business API integration connects your company's WhatsApp to its systems: CRM, ERP, online store or customer service platform. With it, several agents use the same number, conversations are recorded in one place and the system sends automatic messages, such as order confirmations and reminders.

The official API is part of the **WhatsApp Business Platform**, maintained by Meta. It is different from the WhatsApp Business app you install on a phone. The app is designed for direct use by small operations. The API is an interface for systems, with no screen of its own, and it needs software to send and receive messages.

Using the API takes some care: a verified business account, a dedicated number, approved message templates to start conversations and attention to Meta's pricing rules. In return, the company gains scale, control and an operation that does not depend on any one phone.

## WhatsApp Business app or official API

The **WhatsApp Business app** is free and works like regular WhatsApp, with extra features: a business profile, a catalog, quick replies, labels and away messages. It works well when one or a few people handle customer service and the volume can be managed by hand.

The **API** is the way to go when the company needs:

- Multiple agents on the same number, with conversations routed between them.
- Conversations integrated with a CRM or an internal system.
- Automatic notifications triggered by the system.
- Chatbots or AI for the first stage of customer service.
- A centralized history and reports.

A simple test: if customer service depends on someone handing the phone to a colleague, copying conversation details into the system by hand or scrolling through old messages to find out what was agreed, the operation has already outgrown what the app offers.

## What the integration enables

### Multiple agents on the same number

With the API, agent access is managed by the customer service platform, which allows several users on the same number. You can create queues by department, transfer conversations between agents and see who replied what.

### Integration with CRM and internal systems

When a message arrives, the system can identify the customer by phone number, show their purchase or ticket history and log the conversation in their record. It also works the other way around: a status change in the system triggers a message to the customer. This kind of connection follows the same principles as any [system integration with APIs](/en/blog/system-integration-with-apis/).

### Automatic notifications

Order confirmations, delivery updates, appointment reminders, a duplicate copy of a boleto (a Brazilian bank payment slip) and due-date reminders are examples of messages the system sends without human intervention. They use approved message templates, explained further below.

### Chatbots and artificial intelligence

A chatbot can collect initial information, answer frequently asked questions and route the customer to the right department. With AI, it is possible to understand freely written messages, summarize the conversation for the agent and suggest replies based on company documents. What it takes for this to work well is covered in the article on [how to use AI in business](/en/blog/how-to-use-ai-in-business/).

### Centralized history

All conversations are stored in the company's system instead of being scattered across employees' phones. If an agent leaves the company, the history remains available. This also makes auditing, service metrics and the management of personal data easier, a point directly tied to [LGPD, Brazil's data protection law, for websites and software](/en/blog/lgpd-brazil-data-protection-for-websites-and-software/). Outside Brazil, check the rules that apply in your country.

One example is VipDesk, a customer service platform built by PEROVANO that brings WhatsApp, Instagram, email and phone together in one place, with a CRM and AI-powered automation. It is among the company's [projects](/en/#projects).

## Requirements for using the official API

The details change over time and should be confirmed at implementation, but the general requirements are these.

### Verified business account

The company needs an account in Meta's business manager and, in general, has to go through business verification, submitting documents that prove the business exists. The display name shown on WhatsApp is also reviewed.

### Dedicated number

The number used with the API is usually dedicated to it. Traditionally, a number active on the API could not be used in the regular app at the same time. Meta has been expanding ways to use it alongside the WhatsApp Business app in some scenarios, with limitations. That is why it is worth deciding at the start of the project which number will be used and what happens to the current conversation history.

### Approved message templates

To start a conversation with a customer, the company must use a **message template**: a standard text with variable fields such as name and order number, submitted in advance for Meta's approval. Templates are grouped into categories, such as marketing, utility (updates about orders and accounts, for example) and authentication (verification codes).

In addition, the customer must have agreed to receive messages from the company on WhatsApp, which is known as *opt-in*. That consent record should be stored in the system.

### Customer service window

When a customer sends a message, a 24-hour **customer service window** opens. Within it, the company can reply with free-form messages, without a template. Outside it, contact can only be started with an approved template. The system needs to track this window to avoid failed sends.

## How the costs work

The costs come in two parts.

The first is the use of Meta's platform. Meta charges for API usage according to the type of message, and the price varies by category and by the recipient's country. The rate card and the pricing model have changed more than once, so the recommendation is to check the current terms when estimating the budget. Replies within the customer service window are treated differently from messages the company initiates.

The second is the software that uses the API: an off-the-shelf customer service platform with a monthly fee, or custom development integrated with the company's systems. The choice follows the same logic as deciding between [custom software and off-the-shelf](/en/blog/custom-software-vs-off-the-shelf/). The factors that weigh most are the number of agents, the message volume, the required integrations and the level of automation.

## Risks of unofficial solutions

Some tools automate WhatsApp without the official API, usually by simulating WhatsApp Web or the app. They look simpler and cheaper at first, but carry serious risks:

- **Number bans.** Unauthorized automation violates WhatsApp's terms and can get the number banned, cutting off contact with your customers.
- **Instability.** A WhatsApp update can break things without warning.
- **No support.** There is no official channel for solving problems.
- **Security and privacy.** Conversations go through a connection that does not follow the official model, which makes it harder to guarantee data protection.

> For an operation that depends on WhatsApp to sell or serve customers, the number is a business asset. Putting it at risk to save on implementation rarely pays off.

## How to plan the integration

1. **Map your current customer service.** How many people handle it, what kinds of conversations come in and what information they look up in other systems.
2. **List the automatic messages.** Which notifications make sense and at what point in the process.
3. **Define the integrations.** CRM, ERP, scheduling, billing system.
4. **Choose the number and prepare the account.** Business verification, profile and message templates.
5. **Start with the essentials.** Multi-agent service and centralized history first, then notifications and automation.

This planning ties in with [how to automate business processes](/en/blog/how-to-automate-business-processes/): organize the workflow first, then automate it.

## Frequently asked questions

### Can I use the WhatsApp API without a system?

Not in practice. The API has no user interface. You need a customer service platform or a purpose-built system to send, receive and organize the messages.

### Can I send bulk messages through the official API?

You can send messages to many customers, as long as they have agreed to be contacted and approved templates are used. There are sending limits that increase based on the number's history and quality. Messages that lead to blocks and reports hurt that quality.

### Will I lose old conversations when migrating to the API?

It depends on how the migration is done and which number is used. This should be assessed before the switch, to decide whether the history needs to be exported and stored.

### Does the chatbot replace human agents?

It handles the repetitive part, such as collecting data and answering common questions. Cases that require analysis or negotiation should be handed over to a person, with the conversation history available.

If your company already serves customers on WhatsApp and wants to integrate that channel with its system or CRM, we can assess the scenario and the most suitable path. PEROVANO works remotely and can run the project in English. [Get in touch](/en/#contact) and tell us how your customer service works today.
