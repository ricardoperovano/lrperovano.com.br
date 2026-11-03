---
title: "How much does it cost to build an app? What drives the price"
description: "How much does it cost to build an app? Learn the factors that shape the price, the recurring costs after launch, and how an MVP keeps the budget in check."
date: 2026-10-30
category: "Software"
keywords: "how much does it cost to build an app, app development cost, cost to develop a mobile app, app development budget"
pt: "quanto-custa-desenvolver-um-aplicativo"
---

There is no single price for building an app. The cost comes from a set of factors: which platforms the app will run on, the technology chosen, the number of screens and business rules, the back end and admin panel, integrations, design, app store publishing and maintenance after launch. Two apps based on the same idea can have very different budgets because of these choices alone.

On top of development, every app has recurring costs: servers, third-party services, developer accounts in the app stores and updates to keep up with new versions of Android and iOS. A quote that shows only the cost of building the app is incomplete.

The safest way to reach a reliable number is to define the scope before asking for proposals and to start with a lean version that covers the essentials.

## The factors that drive the cost of an app

### Platforms: Android, iOS or both

Android and iOS are the two dominant mobile operating systems. Publishing on both widens your reach, but it adds testing, interface adjustments and publishing work, since each store has its own rules and processes.

Starting with a single platform only makes sense when your audience is concentrated there, such as an internal team that uses company-issued phones.

### Native, cross-platform or PWA

This choice carries a lot of weight in the cost:

- **Native app:** built separately for each platform, using each one's official languages and tools. It gives full access to device features, but in practice it means maintaining two codebases.
- **Cross-platform app:** a single codebase produces both the Android and iOS apps, using frameworks such as Flutter or React Native. In most projects it reduces development and maintenance effort, with small platform-specific parts when needed.
- **PWA (progressive web app):** a website that behaves like an app, can be added to the home screen and runs in the browser. It is usually the most economical route, but it has limits on access to device features and on app store presence. The article on [what a PWA is](/en/blog/what-is-a-pwa/) explains when it is enough.

For most business apps, cross-platform strikes a good balance. Native is justified when the app relies heavily on device-specific features or demanding graphics performance.

### Number of screens and business rules

The number of screens is one indicator, but the rules behind them matter more. A simple list screen costs little. A screen that calculates prices, checks inventory, applies discounts by customer type and works offline costs a lot more.

That is why, when you describe the project, it pays to list not only the screens but what each one needs to do and which exceptions exist. A well-written [software project brief](/en/blog/how-to-write-a-software-project-brief/) helps you get proposals you can actually compare.

### Back end and admin panel

The app on the phone is only one part of the system. There is almost always a **back end**, the part that runs on servers, stores the data, applies the rules and talks to other systems. And there is usually an **admin panel**, typically web-based, where your team manages content, tracks orders, supports users and pulls reports.

In many projects, the back end and admin panel account for a large share of the total effort. A quote that does not mention these components should be questioned.

### Login and user roles

Email and password, SMS code, Google or Apple sign-in: each option has its own implementation and rules. Password recovery, email verification and account deletion also add up.

Different user roles increase the scope. An app with a customer, a courier and an administrator, each seeing different screens and permissions, is practically three connected products.

### Integrations and payments

Integrations connect the app to systems you already use: ERP, CRM, e-commerce platform, delivery systems. The cost depends on the quality of the other system's documentation and API (application programming interface). The article on [system integration with APIs](/en/blog/system-integration-with-apis/) explains the types and the risks.

Payments deserve separate attention. Credit cards, Pix (Brazil's instant payment system, run by the Central Bank), subscriptions and refunds all require careful handling of failures and confirmations. See the details in [Pix and payment integration](/en/blog/pix-and-payment-integration/). The app stores also have rules about what can be sold inside an app and through which payment method, and those rules change over time. Confirm the current terms before you settle on a pricing model.

Push notifications, maps, camera, QR code scanning and background location tracking are other items that add effort.

### Design

Using each platform's standard visual components is faster. A custom design, with your brand identity and animations, takes more design and implementation hours. A clickable prototype, built before development starts, prevents expensive rework later.

### App store publishing and developer accounts

To publish on Google Play and the App Store, the company needs its own developer accounts. Broadly speaking, Google charges a registration fee and Apple charges an annual fee. Prices and verification requirements change, so check the current terms directly with each store.

Publishing itself involves descriptions, promotional images, a privacy policy, disclosures about the data collected and each store's review, which may ask for changes before approving the app. This work should be included in the quote.

## Maintenance and operating system updates

An app is never finished for good. Every year, Android and iOS release new versions, and the stores start requiring apps to be updated to recent tooling. The libraries used in the project receive security fixes. Without maintenance, the app starts failing on new devices and may even stop being accepted by the stores.

Add to that bug fixes and new features. The article on [software maintenance](/en/blog/software-maintenance/) explains how to organize this work and what to expect from a contract.

## Recurring costs after launch

Plan the monthly or yearly costs from the start:

- **Servers and database:** hosting for the back end, the admin panel and files uploaded by users. This grows with usage.
- **Third-party services:** email and SMS delivery, push notifications, maps, image storage, error monitoring and authentication. Many have a free tier and start charging as usage grows.
- **Payments:** payment gateways and processors usually charge per-transaction fees.
- **App stores:** Apple's annual account fee and, when the app sells digital content, the commissions set by each store's rules.
- **Maintenance:** hours set aside for updates, fixes and technical support.

Ask your vendor for an estimate of these costs for the number of users you expect in the first year, even a rough one.

## How to reduce the cost without compromising the result

### Start with an MVP

An MVP, or minimum viable product, is the first version with the smallest set of features that solves the main problem end to end. It puts the app in the hands of real users sooner and shows what is worth building next. The guide on [building an MVP](/en/blog/mvp-how-to-turn-a-software-idea-into-a-product/) shows how to define that scope.

### Prioritize with clear criteria

Sort the features into three groups: the app does not work without it; important, but it can wait a few weeks; nice to have. Only the first group goes into the first version. Secondary user roles, advanced reports and non-essential integrations usually come later.

### Use ready-made services where you have no edge

Authentication, email delivery, notifications and payments are already handled by well-established services. Your investment should go into what sets your app apart.

### What not to cut

Testing on real devices, data security, backups and a solid back end should not be sacrificed. Saving money on these usually costs more later, in rework or incidents.

## What to ask your vendor

- Does the quote include the back end, the admin panel and app store publishing?
- Which technology will be used, and why?
- On which devices and operating system versions will the app be tested?
- Who will own the app store accounts, the server and the source code?
- What recurring costs should I expect in the first year?
- How does maintenance work after delivery?

If you want to understand the full process, from goal to launch, see [how to build an app for your business](/en/blog/how-to-build-an-app-for-your-business/). PEROVANO builds apps, custom software and integrations, and you can explore the [solutions](/en/#solutions) we offer.

## Frequently asked questions

### Why can't you know the price of an app without talking first?

Because the cost depends on decisions that only surface once the project is detailed: platforms, user roles, rules, integrations and design. A price given without that information is a guess, and the difference shows up later as change orders.

### Does building only for Android cost half as much?

Not necessarily. The back end, admin panel, design and business rules are shared by both platforms. With cross-platform technology, the difference between publishing on one platform or both tends to be smaller than it seems.

### Once the app is done, are there no more costs?

No. Servers, third-party services, app store accounts and maintenance are ongoing costs. The yearly Android and iOS updates require adjustments so the app keeps working and stays accepted by the stores.

If you have an app in mind and want to understand what drives the cost in your case, the first step is to talk about the problem it needs to solve. PEROVANO works remotely and can run the project in English. [Get in touch](/en/#contact) to review the scope and the best technical path.
