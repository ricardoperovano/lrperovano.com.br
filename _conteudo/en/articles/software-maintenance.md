---
title: "Software maintenance: what it includes and why you need it"
description: "Software maintenance explained: corrective, adaptive, perfective and preventive work, monitoring, backups, contract models and what to define in the agreement."
date: 2026-10-30
category: "Project management"
keywords: "software maintenance, software maintenance contract, types of software maintenance, application support and maintenance, website maintenance"
pt: "manutencao-de-software"
---

Software maintenance is the ongoing work that keeps a website, system or app running, secure and useful after it goes live. It includes fixing defects, updating libraries and components, adapting the system to changes in browsers, operating systems and third-party services, applying security patches, monitoring how it runs and making sure there are backups.

It is necessary because software does not live in isolation. It depends on dozens of components that change all the time, and the business itself changes. A system nobody updates does not stand still: it ages, piles up known security flaws and, sooner or later, stops working somewhere.

For whoever is paying, the practical question is not whether there will be maintenance, but how it will be organized: who does it, what is included, how quickly problems are handled and how it is billed.

## The four types of maintenance

### Corrective

This is fixing defects: a button that does not respond, a wrong calculation, a report that freezes with large amounts of data. Some appear right after delivery, others only when usage grows or a combination of data nobody anticipated shows up. Defects found during the warranty period are usually fixed at no cost, according to the project contract.

### Adaptive

This is maintenance that adjusts the system to external changes, even when nothing has changed in the business. Common examples:

- **Libraries and frameworks.** Almost all software uses ready-made components, called dependencies. They get new versions with fixes, and old versions stop being maintained.
- **Browsers.** Chrome, Safari, Firefox and Edge are updated frequently. Features change behavior or disappear.
- **Operating systems.** New versions of Android and iOS bring different permission and privacy rules. The app stores also update their requirements for publishing and keeping apps from time to time.
- **Third-party APIs.** An API is the interface through which one system talks to another. Payment gateways, messaging platforms, map services and social networks release new versions and retire old ones. When that happens, the integration needs to be adjusted. The article on [system integration with APIs](/en/blog/system-integration-with-apis/) explains how this works.
- **Legal and tax rules.** Changes in obligations, such as how documents must be issued or how personal data must be handled, may require adjustments.

### Perfective (evolutionary)

This is adding new features or changing existing ones to keep up with the business: a new report, an extra step in an approval workflow, an integration with another system. It is the part of maintenance that creates new value, and it is usually handled as small projects, with an estimate and prior approval.

### Preventive and security

This is work done before a problem appears: applying security patches, reviewing access permissions, improving fragile parts of the code, optimizing slow database queries, renewing certificates. Users barely see it, but it is what prevents incidents.

## Monitoring and backups

Monitoring means watching the system in production so you learn about a problem before a customer complains. The basics include:

- Uptime checks that alert you when the website or API goes down.
- Error logging, with alerts when errors increase.
- Tracking of server, database and storage usage.
- Expiration alerts for the domain and for the security certificate, which is behind the padlock shown in the browser.

A backup is a copy of the data and, when applicable, of the files users upload. A good backup plan defines how often copies are made, how long they are kept, where they are stored (preferably somewhere separate from the main server) and, above all, when restoring them is tested. A backup that has never been restored is an assumption, not a guarantee.

## What happens to a system without maintenance

- **Known vulnerabilities.** Security flaws in popular libraries are published and fixed. If you do not update, you stay exposed to exactly the flaws that are public knowledge, which are the easiest to exploit.
- **Incompatibilities.** A browser or phone operating system update breaks a screen. A payment API retires the version in use and billing stops working.
- **Unsupported dependencies.** Old versions of languages and frameworks stop receiving fixes. Over time, updating requires big jumps, which cost far more than small, regular updates.
- **Slowness and rising costs.** Data volume grows, queries slow down and the server needs more resources.
- **Lost knowledge.** With nobody looking after the system, the people who knew the details move on. When a problem appears, someone has to relearn everything in a hurry.

On websites, the effect also shows up in Google: slow pages or pages with errors perform worse, as the article on [website speed and Core Web Vitals](/en/blog/website-speed-core-web-vitals/) explains.

> Postponed maintenance does not go away: it piles up and comes back more expensive, usually at a worse moment.

## Common contract models

Models vary between vendors, but three come up often:

- **Block of hours.** The company buys a number of hours per month or per period, used for fixes, adjustments and small improvements. It is important to define what happens to unused hours and to anything beyond the block.
- **Monthly fee with a defined scope.** A fixed amount covers agreed activities, such as monitoring, backups, security updates and a volume of fixes. New features are usually quoted separately.
- **On demand.** Each need is quoted and approved separately. This works for simple, stable systems, but offers no guaranteed response time and no preventive care.

Many contracts combine these models: a monthly fee for the basics and hours or quotes for new features. The billing logic resembles the one used to contract the project itself, discussed in [fixed-price vs. hourly development](/en/blog/fixed-price-vs-hourly-software-development/).

## What to define in the agreement

- **What is included and what is not.** Monitoring, backups, dependency updates, fixes, small adjustments, new features, user support.
- **Priorities.** A simple classification, for example: critical (system down or billing stopped), high (an important function failing with no workaround), normal and low.
- **Response time and resolution time by priority.** Response time is how long it takes to start working on a ticket. Resolution time is how long it takes to solve it. They are different things and should be stated separately.
- **Support hours.** Business days, business hours, or on-call coverage for critical cases.
- **The channel for opening tickets** and how the history is recorded.
- **The client company's responsibilities**, such as keeping third-party accounts active and reporting changes in the business.
- **Access and ownership.** Who has access to the server, the repository and the backups, and how that is handed back if the contract ends.
- **A periodic report** with what was done, the hours used and the risks identified.

## How to assess the health of an inherited system

An inherited system is one built by another team that now needs a new owner. Before taking over maintenance, an initial assessment usually answers these questions:

1. Is there full access to the code, repository, server, database, domain and third-party accounts?
2. Is the code in the repository the same as what is running in production?
3. Which versions of the language, framework and libraries are in use, and which have already lost support?
4. Are there known vulnerabilities in the dependencies?
5. Are there recent backups, and have they ever been restored successfully?
6. Are there automated tests? How much of the system do they cover?
7. Is there documentation for installation, deployment and business rules?
8. Which external integrations does the system use, and are those API versions still active?
9. How is personal data protected? The guide on [LGPD, Brazil's data protection law, for websites and software](/en/blog/lgpd-brazil-data-protection-for-websites-and-software/) helps with this part. Outside Brazil, check the rules that apply in your country.

The result is a prioritized list of risks and a plan: what to fix now, what can wait, and whether it makes more sense to maintain the system, refactor it piece by piece or rewrite a module.

## Frequently asked questions

### Does a simple business website need maintenance too?

Yes, on a smaller scale. Even a simple website depends on hosting, a certificate, a domain and, often, a content management system with plugins that need updating. The article on [WordPress vs. a custom website](/en/blog/wordpress-vs-custom-website/) discusses how the choice of platform affects that routine.

### Does the project warranty replace maintenance?

No. The warranty covers defects in what was delivered, for a defined period. Maintenance covers what changes afterward: updates, security, adaptations and new features.

### How much of maintenance can be predicted?

Monitoring, backups and routine updates are predictable. Changes in third-party APIs and urgent security fixes are not always. That is why it is worth combining a fixed part with a reserve for the unexpected.

### Can I switch maintenance vendors?

Yes, as long as your company has the access and the documentation. An initial assessment of the system, like the one described above, is the safest way to make the transition.

PEROVANO builds websites, custom software and apps, like the ones in our [projects](/en/#projects), and can help assess the state of yours. If nobody is looking after your system or you want to organize its maintenance, [talk to us](/en/#contact). We work remotely and can run the work in English.
