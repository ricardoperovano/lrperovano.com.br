---
title: "Fixed-price vs. hourly software development: how to choose"
description: "Fixed price or hourly? How each software development pricing model works, the risks of each, how to handle scope changes and what to put in the contract."
date: 2026-10-30
category: "Project management"
keywords: "fixed price vs time and materials, fixed-price software development, hourly software development, software development pricing models"
pt: "escopo-fechado-ou-por-hora"
---

A fixed price works best when what will be built can be described precisely before work starts: a business website, a well-defined integration, a small system with known rules. Price and timeline are agreed in advance, and the risk of the estimate being wrong sits with the vendor.

Hourly billing, also called time and materials, works best when there is uncertainty: a new product, a system whose shape will become clear as people use it, an operation that changes often. The client pays for the time actually worked and gains the freedom to change priorities, but takes on the risk that the total will vary.

Between the two extremes there are hybrid models, which tend to be the most balanced choice for medium and large projects: paid discovery to define the scope, followed by phases at a fixed price or with an hours budget per phase.

## How each model works

### Fixed price with a defined scope

The vendor estimates the effort, adds a risk margin and proposes a price and a timeline to deliver a scope described in detail. Changes to that scope are handled separately, with a new quote.

This model depends on a well-written scope. The vaguer the description, the larger the risk margin built into the price and the greater the chance of disputes about what was or was not included. A [well-written brief](/en/blog/how-to-write-a-software-project-brief/) is the starting point.

### Time and materials (hourly)

The client pays for the hours worked at an agreed rate, plus direct costs such as infrastructure and third-party services, when there are any. There is usually an initial estimate, which serves as a reference, not a commitment.

The work is typically organized in short cycles of one or two weeks, with a prioritized list of tasks called the backlog. At the end of each cycle, the client reviews what was delivered and decides what comes next.

### Dedicated team

The vendor assigns professionals to the client's project for a period, billed monthly per person or per team. The client is more involved in day-to-day management and sets the priorities. This is common for products in continuous development, when the company does not have an in-house team yet or wants to supplement it.

### Hybrid models

The most common ones:

- **Paid discovery followed by phases.** An initial stage at a fixed price produces the detailed scope, the risks, the architecture and an estimate per phase. With that material, the client decides whether to proceed, with the same vendor or another one.
- **Fixed first phase, hourly afterward.** The initial version, such as an [MVP](/en/blog/mvp-how-to-turn-a-software-idea-into-a-product/), ships with a defined scope and price. After launch, development continues hourly or with a dedicated team, guided by real usage.
- **Hourly with a cap.** The client pays for the hours worked up to an agreed limit per phase. When the limit gets close, both sides review the scope before continuing.

## Advantages and risks of each model

### Fixed price

For the client, the advantage is predictability: the budget is approved and comparing proposals is simpler. The risk is rigidity. Every new idea becomes a change order, and it is common to discover mid-project that something important was not planned for. There is also the risk margin built into the price, which the client pays even if the surprises never happen.

For the vendor, the advantage is being able to gain efficiency on projects it knows well. The risk is underestimating the effort. When that happens, schedule pressure can lead to cuts in testing, documentation or code quality, which surface later for the client.

### Hourly

For the client, the advantage is flexibility: changing priorities without renegotiating the contract and paying only for what was done. The risk is the total cost ending up higher than expected, especially without close oversight. The model requires someone on the client side to take part in decisions frequently.

For the vendor, the advantage is not carrying the estimation risk. The risk is the relationship wearing down if the client feels there is no control over the hours. Clear reports and frequent deliveries are how to avoid that.

### Dedicated team

For the client, the advantage is having a team that builds up knowledge about the product. The risk is paying for capacity even in periods of low demand. For the vendor, the model provides predictable revenue, with the risk of the team becoming dependent on a single client.

## How to handle scope changes

Changes will happen in any model. What needs to be agreed is the process:

1. The change is recorded in writing, with a description of what is wanted.
2. The vendor assesses the impact on timeline, cost and the work already done.
3. The client approves it, rejects it, or swaps it for another item of the same size that leaves the scope.
4. The decision is recorded, along with the new timeline, if there is one.

With a fixed price, this usually produces a change order. In the hourly model, it is a reprioritization of the task list, but the budget impact should be communicated just the same.

## Phased delivery and acceptance milestones

Splitting the project into phases reduces risk in both models. Each phase ends with a usable delivery and an acceptance milestone: the moment the client checks the delivery and formally approves it.

An acceptance criterion is an objective description of what must work for a delivery to be approved. "Customer records working" is vague. "Create, edit and search customers by name or company tax ID (the CNPJ, in Brazil), with ID validation and export of the list to a spreadsheet" is verifiable.

It is also worth agreeing on how long the client has to test and respond, and what happens if there is no response within that time. Tying payments to acceptance milestones aligns the interests of both sides.

## What the proposal and contract should include

This content is not legal advice. To draft or review a contract, consult a lawyer. From a project standpoint, these are the items that are most often missed when they are not in writing:

- **Deliverables.** What will be delivered in each phase: features, screens, integrations, documentation, deployment.
- **Out of scope.** What is explicitly not included.
- **Acceptance criteria** and the period for validation.
- **Pricing model**, the hourly rate when there is one, payment terms and milestones.
- **The scope change process.**
- **Code ownership** and the transfer of the repository, domain and third-party accounts. The article on [how to choose a software development company](/en/blog/how-to-choose-a-software-development-company/) covers this in detail.
- **Defect warranty**, with the period and what it covers.
- **Support and maintenance** after the warranty. See what to consider in [software maintenance](/en/blog/software-maintenance/).
- **Client responsibilities**, such as providing content, access and approvals on time.
- **Personal data protection**, when the system handles that kind of information. The guide on [LGPD, Brazil's data protection law, for websites and software](/en/blog/lgpd-brazil-data-protection-for-websites-and-software/) helps define what to ask for. In other countries, check the rules that apply locally.
- **Termination**, covering what is handed over and how the transition works if the contract ends early.

## Which to choose in each situation

- **Business website or landing page with defined content:** fixed price. The article on [how much a website costs](/en/blog/how-much-does-a-website-cost/) shows what usually goes into the price.
- **Integration between two systems with documented APIs:** fixed price, ideally with an initial technical check of the APIs.
- **Custom software with rules still being defined:** paid discovery and phases.
- **New product, such as an app or a [SaaS](/en/blog/how-to-build-a-saas/):** an MVP at a fixed price, then hourly or a dedicated team.
- **Product in continuous development:** a dedicated team or a monthly block of hours.
- **Fixes and small adjustments to an existing system:** hourly or a maintenance contract.

A rule of thumb: the greater the uncertainty, the less sense it makes to fix price and scope all at once. Instead of forcing a fixed estimate onto something nobody understands well yet, it is better to fix the price of the stage that reduces the uncertainty.

## Frequently asked questions

### Is a fixed price cheaper?

Not necessarily. A fixed price includes a risk margin, and changes produce change orders. With hourly billing, the cost can be lower if the project goes well, or higher if the scope grows unchecked.

### How do I keep hours under control in the hourly model?

Ask for periodic reports with hours per task, frequent deliveries you can test, an estimate per phase and, if it makes sense, a cap that triggers a review before it is exceeded.

### Is paid discovery worth it?

On projects with uncertainty, it usually is. Discovery turns ideas into a verifiable scope, which lets you compare proposals and reduce surprises. Agree in advance on which documents will be delivered and whether they can be used with another vendor.

### Can I switch models mid-project?

Yes, as long as the change is recorded. A common switch is moving from a fixed price to hourly after launch, when development starts being guided by usage.

PEROVANO builds [websites, custom software and integrations](/en/#solutions) and can help define the scope and the pricing model that fit your project's level of uncertainty. We work remotely and can run projects in English. If you are weighing how to contract the work, [talk to us](/en/#contact) about the best path.
