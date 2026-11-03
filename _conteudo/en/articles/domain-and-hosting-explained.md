---
title: "Domain and hosting explained: what they are, how to choose"
description: "The difference between a domain and web hosting, how to register a domain in your company's name, what DNS does and what to require from your website vendor."
date: 2026-10-30
category: "Websites"
keywords: "domain and hosting explained, difference between domain and hosting, how to register a domain for a business, types of web hosting"
pt: "dominio-e-hospedagem"
---

A domain is your website's address, such as `yourcompany.com`. Hosting is the server where the site's files live and from which they are delivered to visitors. One is the name on the sign; the other is the building. They are purchased separately, can sit with different providers and each has its own renewal.

The main rule for choosing well is simple: the domain should be registered in your company's name, with access controlled by someone inside the company. Hosting should match the type of site and include HTTPS, backups and support. Price matters, but only after those points.

The most common problems are not technical: a domain registered to a former employee or an old agency, a forgotten renewal, passwords nobody can find.

## The difference between a domain and hosting

A **domain** is a name registered for a set period, which the company must renew to keep using it. It stores no files. On its own, it only points somewhere.

**Hosting** is the service that keeps the site running: a computer that is always on and connected to the internet, answering whenever someone types the address. It can also hold a database, form submissions and, on some plans, email.

The two are connected through DNS, explained below. That is why you can change hosting providers without changing your domain, and the address your customers know stays the same.

## How to register a domain

Domains are registered through registrars, companies accredited to sell names under a given extension. Generic extensions such as `.com` are sold by many registrars, each with its own terms. Country-code extensions often have their own registry and eligibility rules. In Brazil, for example, `.br` domains such as `.com.br` are managed by Registro.br, the organization responsible for Brazil's country-code domain. You can register directly with it or through companies that offer the service, and the holder must provide a CPF (Brazil's individual taxpayer number) or a CNPJ (the national company registration number). Check the current conditions for the extension you want before you buy.

Whatever the extension, a few precautions apply:

- **Register it to the company.** The domain is a business asset. In Brazil, that means using the company's CNPJ; elsewhere, it means listing the company as the registrant. If the domain sits in the name of a partner, an employee or the vendor, transferring it depends on that person's goodwill.
- **Use a contact email the company controls.** Expiration notices and confirmation requests go to that address. If it belongs to someone who has left, the notices get lost.
- **Keep the login safe.** The username, password and two-factor authentication, when available, should stay with the company. Your vendor can be given technical permission to configure things without being the owner.

## Renewals and the risk of losing your domain

A domain is registered for a period and has to be renewed. When renewal doesn't happen, the website and email stop working. If the situation isn't fixed within the window set by the registry's rules, the domain can become available again and be registered by someone else.

Getting back a domain that a third party has already registered can be hard, slow or impossible. So:

- turn on auto-renewal when the registrar offers it;
- register for more than one year, if the budget allows;
- put the expiration date on a responsible person's calendar;
- once a year, check that the registrant and contact details are correct.

## DNS in plain language

DNS (the Domain Name System) is the internet's contact list. It translates a name like `yourcompany.com` into the numeric address of the server where the site lives. That information is stored in records, and the most common ones are:

- **A:** points the domain to the address of the website's server.
- **CNAME:** points one name to another, such as `www` pointing to the main domain.
- **MX:** tells the world which service receives the domain's email.
- **TXT:** holds verification text and email security settings.

Whoever manages DNS can change where the website and email point. One wrong change takes both down. That is why DNS access deserves the same care as access to the domain itself. After a change, it can take from minutes to a few hours to apply everywhere, because servers keep cached answers for a while.

## Types of hosting

### Shared hosting

Many sites share the same server. It is the simplest option to buy and usually comes with a ready-made control panel. It works well for small sites with little traffic. The downside is that other sites on the same server can affect performance, and the settings you can change are limited.

### VPS

A VPS (virtual private server) is a slice of a server with resources reserved for your site. You get more control and more predictable performance. In return, someone has to set up and maintain the operating system, security updates and monitoring. If nobody does that, a VPS ends up worse than well-managed shared hosting.

### Cloud

With cloud hosting, resources can scale up or down with demand, and there are managed services for databases, storage and queues. It is the common choice for web applications, online stores with variable traffic and systems that need high availability. It takes technical knowledge to configure and to keep costs under control.

### Static site hosting

A static site is one whose pages are generated ahead of time and delivered ready-made, with no database query on each visit. For this kind of site, there are specialized services that distribute the files across servers in several regions. The result is usually a fast site with little maintenance and fewer points of attack. Business websites and blogs fit this model well. Speed also helps with Google, as the article on [Core Web Vitals](/en/blog/website-speed-core-web-vitals/) shows.

Which model fits depends on how the site is built. A WordPress site needs a server with PHP and a database; a static site doesn't. The comparison [WordPress vs. custom website](/en/blog/wordpress-vs-custom-website/) helps with this part.

## Email on your domain

An address like `contact@yourcompany.com` builds more trust than a free email account, and it stays with the company when an employee leaves. It can live with your hosting provider or with a separate email service, which the MX record points to.

Keeping email and website separate is usually good practice. Changing hosting providers or a problem on the website's server won't affect email. It is also worth setting up the email authentication records (SPF, DKIM and DMARC), which help keep your messages out of spam folders and make it harder for scammers to use your domain.

## HTTPS and certificates

HTTPS is the secure version of the web protocol. It protects data between the visitor's browser and the server, and the browser shows a padlock in the address bar. For that, the site needs a valid digital certificate.

Today, HTTPS is effectively mandatory for any website. Browsers warn visitors when it's missing, and unprotected forms expose personal data, which is also a data protection issue, as covered in our article on [LGPD, Brazil's data protection law, for websites and software](/en/blog/lgpd-brazil-data-protection-for-websites-and-software/). Many hosting providers offer free certificates with automatic renewal. Confirm that renewal actually works, because an expired certificate triggers a security warning for every visitor.

## Backups

A backup is a copy of the site and its data stored somewhere else, so you can restore everything after a failure, an attack or human error. Ask:

- How often are backups made?
- How long are copies kept?
- Are they stored separately from the main server?
- Who handles a restore, and how long does it take?
- Has a test restore ever been done?

A backup that has never been tested is an assumption.

## What to require from your vendor

When you hire someone to build your website, ask for these in writing:

1. The domain registered in the company's name, with owner access under your control.
2. The hosting account in the company's name, or guaranteed administrator access.
3. A list of every service purchased, with renewal dates and who is responsible.
4. HTTPS configured with automatic renewal.
5. A backup policy covering frequency, retention and test restores.
6. Documentation of the DNS and email settings.
7. A plan for maintenance and security updates after delivery.

These items belong in the proposal comparison as much as the design does. The article on [how much a website costs](/en/blog/how-much-does-a-website-cost/) explains the recurring costs, and the guide to [what a business website needs](/en/blog/what-a-business-website-needs/) covers the rest of the list.

> If your vendor disappeared tomorrow, could the company keep its website and email running? If the answer is no, something needs fixing.

## Frequently asked questions

### Can I have my domain with one company and my hosting with another?

Yes, and it's common. You just configure DNS to point the domain to the hosting. Keeping them separate even makes it easier to switch hosting later.

### My domain is in my old agency's name. What should I do?

Ask for the registrant to be transferred to the company (in Brazil, to the company's CNPJ). The process depends on the registrar and usually requires authorization from the current holder. The sooner you deal with it the better, because it gets harder if you lose contact with the vendor.

### Is cheap hosting good enough for my business?

It depends on the site. A simple business website can run well on an entry-level plan or on static site hosting. Web applications, online stores and high-traffic sites need more resources and technical support that responds quickly.

If your company wants to get its domain, hosting and email in order, or is planning a new website, it pays to do it from the start with everything in your name. PEROVANO builds [websites and software](/en/#solutions), delivers the setup fully documented and works remotely with clients in English. [Get in touch](/en/#contact) to talk about your situation.
