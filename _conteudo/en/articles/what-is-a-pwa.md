---
title: "What is a PWA (progressive web app) and when is it worth it"
description: "What is a PWA? A website you can install like an app that also works offline. See the benefits, the limits on Android and iPhone, and when to choose native."
date: 2026-10-30
category: "Software"
keywords: "what is a PWA, progressive web app, PWA vs native app, PWA advantages and disadvantages"
pt: "o-que-e-pwa"
---

A PWA, short for progressive web app, is a website built to behave like an app. Users open it in the browser and, if they want, install it on the home screen of their phone or computer. From then on, the PWA opens with its own icon, full screen, without the address bar, and it can keep working even without an internet connection.

In practice, it is a single product that works as both a website and an app. Nobody needs to download anything from a store to start using it, and anyone who prefers can install it with one tap. Updates arrive as soon as they are published on the server, without waiting for store approval or for the user to tap "update".

A PWA is usually a good choice for frequently used business software, customer portals, internal tools and products that need to be found on Google. It falls behind a native app when the project depends on advanced device features, heavy processing or a strong presence in the app stores.

## How a PWA works

Three pieces turn an ordinary website into a PWA:

- **HTTPS**: the site must be served over a secure connection, which is already standard in any serious project.
- **Manifest**: a file that tells the device the app's name, icon and colors, and how it should open, for example full screen.
- **Service worker**: a script that runs in the background in the browser, between the app and the internet. It stores screens and data on the device, lets the app open without a connection and receives notifications.

With these pieces in place, the browser recognizes the site as installable. On Android, browsers such as Chrome usually offer installation directly. On the iPhone, the path is the browser's share menu, using the option to add to the home screen.

Offline support is not automatic. The project has to decide what is available without internet: only screens already visited, an entire catalog, or forms that users fill out offline and that are sent once the connection returns. Each level takes more development and testing work.

## Advantages of a PWA

### One codebase for every device

The same PWA runs on Android, iPhone, desktop and tablet. Instead of maintaining an Android app, an iOS app and a separate website, the team maintains a single codebase. That reduces development, testing and maintenance effort over the years.

### Updates without the app store

Fixes and new features go live as soon as they are published. There is no store review queue and no users stuck on old versions. For software whose business rules change often, that makes a difference.

### Lower cost than two native apps

Building two native apps generally means two codebases, two publishing routines and often professionals with different specialties. A PWA tends to cost less because everything lives in one web project. The article on [how much it costs to build an app](/en/blog/how-much-does-it-cost-to-build-an-app/) details the factors that weigh most on the budget.

### It can be found on Google

Because a PWA is a website, its public pages can be indexed by search engines. A native app lives inside the store, and its content does not show up in search the same way. For products that depend on organic traffic, this matters. Good practices for [SEO for business websites](/en/blog/seo-for-business-websites/) and [website speed and Core Web Vitals](/en/blog/website-speed-core-web-vitals/) apply directly.

### No friction to get started

Users can try the product from a link, without downloading anything. Installing becomes a later choice for those who have already seen the value. For new products, this lowers the barrier to entry.

## Limitations you need to factor in

### Access to device features

Modern browsers allow the use of the camera, microphone, geolocation, notifications and sharing. But some features are still restricted or unavailable to web applications, especially outside Android: communication with certain Bluetooth accessories, NFC reading, long-running background tasks and deep integration with the operating system. If your product depends on something like this, confirm compatibility before deciding.

### Differences between Android and iPhone

Android, with Chrome, usually offers broader support for PWA features. On the iPhone, browsers generally use the same engine as Safari, and Apple has historically been more cautious about releasing web features.

Push notifications are one example. iOS started supporting push notifications for PWAs installed on the home screen in version 16.4. In other words, on the iPhone the user has to install the PWA and allow notifications; a site opened only in the browser does not receive them. Details like this change with new system versions, so it is best to test on your audience's real devices before promising a feature.

### App store presence

Many people look for apps directly on Google Play or the App Store. A PWA does not appear there by default. You can package a PWA to publish on Google Play, and there are routes to the App Store, but Apple tends to require the app to offer more than a website inside a frame. If being in the stores is part of your marketing strategy, plan for it from the start.

### Performance in extreme cases

For most business software, such as records management, scheduling, dashboards and orders, a well-built PWA is fast enough. Games with heavy graphics, video editing and intensive on-device processing remain native app territory.

## PWA, native app or cross-platform: how to choose

There are three main paths, and each one fits a different set of needs.

A **PWA** fits when:

- the product needs to work well on both phone and computer
- being found on Google matters
- the rules change often and updates need to be immediate
- the device features required are the common ones, such as camera, location and notifications
- the budget calls for a single codebase

A **native app**, built separately for Android and iOS with each platform's tools, fits when:

- performance is critical, as in games or media processing
- the app depends on specific system features or accessories
- the experience must follow each platform's visual conventions closely

**Cross-platform**, with technologies such as React Native or Flutter, produces store-installable apps for Android and iOS from shared code. It fits when:

- being in the app stores is a must
- the app needs device features the web does not support well on the iPhone
- the budget cannot cover two native apps

> The central question is not which technology is best, but which features the product needs in its first year and where your audience will look for it.

A common strategy is to start with a PWA to validate the product with real users, in the spirit of an [MVP](/en/blog/mvp-how-to-turn-a-software-idea-into-a-product/), and move to an app store app only when there is clear demand. Since the back end (the part of the system that runs on the server, with the rules and the database) can be reused, migrating does not mean starting from scratch. The guide on [how to build an app for your business](/en/blog/how-to-build-an-app-for-your-business/) walks through the project steps for any of these paths.

## What to ask your vendor

- Which features will work offline, and what happens to data entered without a connection?
- Will notifications work on iPhone and Android? Under what conditions?
- On which devices and browsers will the PWA be tested?
- Is there a plan to publish in the app stores, if that becomes necessary later?
- How will the back end be built so it can also serve a future native app?

PEROVANO builds web applications, PWAs and mobile apps, and our [solutions](/en/#solutions) describe each area of work.

## Frequently asked questions

### Is a PWA the same as a responsive website?

No. A responsive website adapts to different screen sizes. A PWA is responsive too, but it goes further: it can be installed, open full screen, work offline and send notifications.

### Does a PWA work on the iPhone?

Yes. Users install it from the browser's share menu. Some features are restricted on iOS, and push notifications only work with the PWA installed on the home screen, starting with iOS 16.4.

### Can I turn my current website into a PWA?

In many cases, yes. Adding a manifest and a service worker is relatively simple. The bigger job is adapting the navigation to feel like an app and deciding what works offline. Very old or slow websites may need a redesign first.

### Can a PWA replace an app store app?

For a lot of business software, yes. For products that depend on app store presence or advanced device features, no. In those cases, the PWA can be the first step, with the store app coming later.

If you are weighing a PWA against a native or cross-platform app, the safest approach is to start from the features your product really needs. PEROVANO works remotely, can run the project in English and can help you assess your case and recommend the best option. [Get in touch](/en/#contact) to talk about your project.
