---
title: "LGPD: Brazil's data protection law for websites and software"
description: "What Brazil's LGPD requires of websites and software: who it applies to, legal bases, minimal data, privacy policy, cookies, rights, security and vendors."
date: 2026-10-30
category: "Software"
keywords: "lgpd brazil, lgpd compliance, brazil data protection law, lgpd for websites, lgpd software development"
pt: "lgpd-em-sites-e-sistemas"
---

The LGPD (Lei Geral de Proteção de Dados Pessoais, Law No. 13,709/2018) is Brazil's general data protection law, similar in spirit to Europe's GDPR. It applies to company websites and software that collect or use data about individuals, such as a name, email, phone number, CPF (Brazil's individual taxpayer number), address or purchase history. In practice, a company must know what data it collects, why, on what legal basis, for how long, who it shares it with and how it protects it.

For a website, that means forms that ask only for what's needed, a clear privacy policy, a cookie banner that actually works and a channel for people to exercise their rights. For software, it also means access control, a record of who accesses what, an incident response plan and contracts with vendors that process data on the company's behalf.

This article is informational and technical. It is not legal advice and does not replace guidance from a legal professional, who should assess your company's specific situation.

## Who the LGPD applies to

The LGPD covers personal data processing by companies, organizations and public bodies, online or offline, and is not limited to companies based in Brazil. In general terms, it can apply when the processing takes place in Brazil, when the purpose is to offer goods or services to people located in Brazil or to process their data, or when the data was collected in Brazil. A foreign company with customers or users in Brazil may therefore need to comply. There are exceptions, such as purely personal, non-commercial use. If you operate in other countries, their own data protection rules may apply as well, so check the rules where you do business.

## Key concepts

A few terms come up constantly:

- **Personal data:** any information that identifies a person or makes it possible to identify them.
- **Sensitive personal data:** data about health, racial or ethnic origin, religion, political opinion, union membership, sex life, and genetic or biometric data. It calls for extra care.
- **Data subject:** the person the data refers to.
- **Processing:** any operation involving data, such as collecting, storing, viewing, sharing or deleting it.
- **Controller:** whoever makes decisions about the processing. Usually, the company that owns the website or software.
- **Processor:** whoever processes data on the controller's behalf, such as the hosting company, the email marketing platform or the software vendor.

## Legal bases: every use of data needs a justification

The LGPD lists the circumstances that authorize processing data, called **legal bases**. They include the data subject's consent, performance of a contract, compliance with a legal or regulatory obligation and the controller's legitimate interest, among others set out in the law.

In practice, each purpose must be tied to an appropriate legal basis. A delivery address for an order is justified by performance of the contract. Issuing a nota fiscal (the Brazilian electronic invoice) is justified by a legal obligation. Sending a newsletter usually depends on consent. Choosing the right legal basis for each case is a decision that should involve legal advice.

A common mistake is treating consent as the answer to everything. It is one of the bases, and not always the most appropriate.

## Collect only what you need

The necessity principle calls for collecting the minimum data required for the purpose. On a website, that means reviewing every form:

- Does a contact form need a CPF? Almost never.
- Is the date of birth used for anything? If not, remove it from the form.
- Is the phone number required or optional?

Less data collected means less risk if there's a breach. This review is easiest during planning, so include it in the [project brief](/en/blog/how-to-write-a-software-project-brief/).

## A clear privacy policy

The privacy policy explains to data subjects, in understandable language, how their data is handled. At a minimum, it should state:

- what data is collected and how;
- for what purposes;
- who it is shared with, such as vendors and partners;
- how long it is kept;
- what the data subject's rights are and how to exercise them;
- who the controller is and how to contact the data protection officer.

Copying another site's policy is a problem: it has to describe what your site actually does, including traffic analytics tools and advertising pixels.

## Consent and the cookie banner

When consent is the applicable legal basis, it must be free, informed and unambiguous, for a specific purpose. Pre-checked boxes and vague text like "I accept everything" don't meet that standard. People must also be able to withdraw consent easily.

Cookies are small files a website stores in the browser. Some are necessary for the site to work, such as keeping a user logged in. Others are used for audience analytics or advertising and generally depend on consent.

A cookie banner that actually works:

- groups cookies by category (necessary, analytics, marketing);
- loads optional scripts only after the visitor accepts;
- makes declining as easy as accepting;
- lets the visitor change their choice later.

The most frequent mistake is the decorative banner, which appears after the tracking scripts have already loaded. Controlling those scripts also helps your [website speed](/en/blog/website-speed-core-web-vitals/).

## Data subject rights

The law grants data subjects a set of rights, including: confirming whether the company processes their data, accessing that data, correcting inaccurate information, requesting deletion of data processed on the basis of consent, requesting portability, knowing who the data has been shared with and withdrawing consent.

Your software must be able to locate all of a person's data, export it, correct it and delete or anonymize it when appropriate. With data scattered across spreadsheets and disconnected systems, a simple request turns into slow manual work. Good [system integration with APIs](/en/blog/system-integration-with-apis/) helps keep data organized and traceable.

## Security and access control

The LGPD requires technical and administrative measures to protect data. In software, that includes, among other things:

- **Role-based access control:** each person sees only what they need for their job. A support agent doesn't need to see financial data, for example.
- **Strong authentication:** passwords stored as hashes using algorithms designed for that purpose (never in plain text) and, for administrative access, two-factor verification.
- **Encryption in transit:** HTTPS across the whole site and on every integration.
- **Protected and tested backups.**
- **Security updates** for the server, the framework and the libraries.

### Recording who accesses what

Keeping **access logs**, meaning records of who viewed or changed a given piece of data and when, helps investigate incidents, spot improper access and demonstrate good practices. Those logs need protection too.

## Security incidents

An incident is any event that compromises the confidentiality, integrity or availability of data, such as a leak, unauthorized access or the loss of a database.

When an incident may cause significant risk or harm to data subjects, the law requires notifying the ANPD (Autoridade Nacional de Proteção de Dados, Brazil's national data protection authority) and the affected data subjects. That's why the plan has to exist beforehand: who gets called, how to contain the problem, how to assess the impact and how to document what happened.

## The role of the data protection officer (DPO)

The **encarregado**, the LGPD's term for what is commonly called the DPO (data protection officer), is the person or company appointed by the controller as the point of contact with data subjects and with the ANPD. They receive requests and complaints and guide the team on good practices.

The DPO's identity and contact details must be clearly available, usually in the privacy policy. There are specific, simplified rules for small businesses, which should be checked with legal counsel.

## Processors and vendors

Almost every website and system depends on third parties: hosting, email, payment gateway, CRM, AI services. Each one that processes data on the company's behalf is a processor.

In practice, you need to:

- map which vendors receive personal data;
- check where that data is stored and whether it is transferred to other countries;
- have contract clauses covering data protection;
- confirm the vendor's security measures.

The same applies to whoever develops your software. When deciding between [custom software and an off-the-shelf product](/en/blog/custom-software-vs-off-the-shelf/), ask who has access to the production environment and how backups work. Projects involving [artificial intelligence](/en/blog/how-to-use-ai-in-business/) call for the same care.

## Privacy by design

Retrofitting an existing system is usually more work than building it with privacy in mind from the start. Defining access roles, retention periods and logs during the design phase avoids rework. See the [solutions](/en/#solutions) we build for websites and software.

> LGPD compliance is not a document posted in the website footer. It is the sum of technical and process decisions that have to hold up day to day.

## Frequently asked questions

### Does a simple business website need to comply with the LGPD?

Yes, if it collects any personal data from people covered by the law, even just a name and email in a contact form, or if it uses analytics or advertising cookies. The effort is smaller than for a full system, but a privacy policy, data minimization and a cookie banner are still necessary.

### Is publishing a privacy policy enough?

No. The policy describes what happens, but the website and the software have to work the way it says. If the policy says marketing cookies depend on consent, they can't load before the visitor accepts.

### Who is responsible if the software vendor leaks the data?

The law divides responsibilities between controller and processor according to each one's role. That's why clear contracts and vendors with good practices matter. Any specific case should be assessed with legal advice.

### Do I have to delete all the data when a customer asks?

Not always. Some data must be kept because of legal obligations, such as tax records. The system should delete or anonymize what can be removed and keep, securely, what the law requires.

If you're planning a website or software product and want data protection built into the design from the beginning, let's talk about the project. PEROVANO works remotely and can run projects in English. [Get in touch](/en/#contact) and tell us what you need built.
