---
title: "How to build a SaaS: from business model to architecture"
description: "How to build a SaaS: what changes from internal software, multi-tenancy, data isolation, recurring billing, data protection, validation and the key metrics."
date: 2026-10-30
category: "Software"
keywords: "how to build a saas, software as a service development, multi-tenant architecture, saas recurring billing"
pt: "como-criar-um-saas"
---

Building a SaaS means building software that many customers use at the same time, over the internet, paying a subscription. That is why it requires decisions an internal system does not: how to keep each customer's data separate, how to bill every month and deal with those who do not pay, and how to let someone sign up and start using the product without talking to anyone.

The safest path has four parts. Validate that there is a problem people will pay to solve. Build a lean first version, but with the right technical foundation, especially data isolation between customers. Automate recurring billing. And track retention metrics from the very first customer.

## What SaaS is

SaaS stands for *software as a service*. Instead of buying a license and installing the program, the customer accesses the system through a browser or an app and pays a subscription for as long as they use it. The provider takes care of servers, updates, backups and security.

Tools for financial management, customer support, scheduling and electronic signatures often follow this model. If you are on the other side, deciding whether to subscribe to an existing product or build your own, the article on [custom software vs. off-the-shelf](/en/blog/custom-software-vs-off-the-shelf/) helps with that decision.

## What changes compared to an internal system

### Many customers in the same system

An internal system serves one company. A SaaS serves many, on the same installation. Each customer company is called a **tenant**, and an architecture that serves many of them is called **multi-tenant**. One customer's data must never be visible to another.

### Sign-up and free trial

In a SaaS, customers usually sign up on their own, set up the account and try the product before paying. That requires a very well-designed onboarding flow: account creation, email confirmation, initial setup and some kind of getting-started guide. If customers get lost in the first few minutes, they rarely come back.

### Plan tiers

Different plans mean different limits: number of users, records or storage, or access to certain modules. The system needs to know these limits, enforce them and let customers switch plans without manual intervention.

### Recurring billing

Revenue comes from automated monthly or yearly payments. That involves integrating with payment methods, issuing invoices and handling failures, a topic covered in its own section below.

### Support

With many customers, support has to scale. A help center, in-app messages and internal tools that let your team look up a customer's account, with a log of who accessed what, are all part of the product.

## Essential technical decisions

### Data isolation between customers

This is the most important decision and the most expensive one to change later. The most common approaches are:

- **A separate database per customer:** strong isolation, but operations get more demanding as the number of customers grows.
- **A separate schema per customer:** one database with separate areas for each tenant. It sits in the middle.
- **Shared tables with a customer identifier:** all the data lives together, and each record carries the tenant it belongs to. This is the simplest option to operate and scale, but it demands strict discipline.

With the third approach, the customer filter cannot depend on every developer remembering to apply it in every query. It must be enforced in a central layer of the system or by the database itself. Some databases, such as PostgreSQL, offer row-level security, a feature that applies this rule automatically. Automated tests that try to access another tenant's data also help.

### Security

Beyond isolation, a SaaS needs robust authentication with an option for two-factor verification, role-based permissions within each customer account, encrypted communication, tested backups and a log of important actions. Integration credentials must be kept out of the code.

### Realistic scalability

Scalability is the ability to serve more customers without losing performance. Designing for millions of users from day one is usually wasteful. What matters is not creating obvious bottlenecks: queries with proper indexes, slow tasks run in the background and an architecture that lets you add capacity when the numbers call for it.

### Observability

Observability is the ability to know what is happening in the system in production: event logs, error monitoring, response times and alerts. In a SaaS, a problem affects many customers at once. Finding a failure through monitoring, rather than through a customer complaint, makes a difference to trust in the product.

## Recurring billing and failed payments

Recurring billing usually relies on credit cards with automatic charges and, in Brazil, also on boleto (a bank payment slip widely used in the country) or Pix (Brazil's instant payment system, run by the Central Bank). The available methods vary by country. Payment gateways offer subscription features that handle part of the work, but the system still has to react to every event: payment approved, declined, refunded, subscription canceled. The article on [Pix and payment integration](/en/blog/pix-and-payment-integration/) explains how these confirmations work.

Failed payments are part of the model. Cards expire, limits are reached, payment slips are forgotten. A clear policy prevents both lost revenue and losing customers over a one-off problem:

- Automatic retries on different days.
- Notices by email and inside the product, with a link to update the payment method.
- A grace period before restricting access.
- Gradual restriction, for example switching to read-only before blocking.
- Clear rules on how long data is kept after cancellation.

Check the current terms, the recurring payment methods available and the fees with the gateway you choose.

## Data protection in a SaaS

In Brazil, a SaaS company usually plays two roles under the LGPD (Lei Geral de Proteção de Dados), Brazil's data protection law, similar in spirit to Europe's GDPR. For its own customers' data, such as account and billing details, it decides how the data is processed. For the data customers put into the system, such as information about their own clients, it generally processes that data on their behalf, following their instructions. Other countries have their own rules, so check the ones that apply to you and to your customers.

In practice, this calls for a contract and terms of use that make these roles clear, access control, a log of who views the data, an incident response plan and ways to export and delete data on request. The article on [LGPD for websites and software](/en/blog/lgpd-brazil-data-protection-for-websites-and-software/) goes deeper into each of these points.

## How to validate before building everything

The biggest risk for a SaaS is not technical. It is building something nobody pays to use. Before investing in the full product:

- Talk to potential customers about the problem, not the solution. Ask how they handle it today and what it costs them in time or money.
- Offer a presale or a waiting list with a set price. Interest that does not turn into commitment is a weak signal.
- Serve the first customers partly by hand, if possible, to understand the process before automating it.
- Launch an [MVP](/en/blog/mvp-how-to-turn-a-software-idea-into-a-product/) with the main flow working end to end.

Even when lean, a SaaS MVP should not give up data isolation and security. Features can wait; the foundation cannot. No-code tools can help test interest, and the article on [no-code, low-code or custom development](/en/blog/no-code-low-code-or-custom-development/) helps you see how far they go.

## Metrics that matter

A few metrics show whether a SaaS is healthy:

- **Recurring revenue:** how much comes in every month from active subscriptions. It shows the predictable base of the business.
- **Churn:** the share of customers or revenue lost in a period. High churn cancels out sales efforts, because customers leave as fast as they arrive.
- **Retention:** how many customers keep using and paying over time. Tracking it by cohorts of customers who joined in the same month shows whether the product is improving.
- **Trial-to-paid conversion:** how many of those who try the product become subscribers. It indicates whether the product delivers value quickly enough.
- **Active usage:** how many customers actually use the core features. Customers who pay but do not use the product tend to cancel.

There is no universal ideal number. Values vary with the market, the price and the type of customer. What matters is measuring from the start and following the trend.

> In a SaaS, keeping a customer is often as important as winning a new one.

## Frequently asked questions

### Can I turn an internal system into a SaaS?

It is possible, but it is rarely just a matter of opening it up to other customers. Data isolation, sign-up, plans, billing and support have to be added, and rules built for a single company need to become settings. A technical assessment of the current system shows whether it is worth adapting or rebuilding parts of it.

### Does a SaaS need a mobile app?

No. Many SaaS products work only in the browser. PaceOn, Estudatta and Portal da Igreja are examples of web products built by PEROVANO; see our [projects](/en/#projects). An app makes sense when mobile use is central for the customer.

### What is the biggest technical mistake when building a SaaS?

Leaving data isolation between customers for later. Fixing it with the system in production is expensive and risky, because it means touching every query and migrating every customer's data.

### How long does it take for a SaaS to pay off?

It depends on the market, the price and the ability to retain customers. Because it is subscription-based, the return usually builds up over time rather than arriving at the moment of sale.

If you have a SaaS idea and want to assess the technical foundation and the scope of the first version, a good place to start is a conversation about the problem and the audience. PEROVANO works remotely and can run the project in English. [Talk to PEROVANO](/en/#contact) to discuss your project.
