---
title: "Website speed and Core Web Vitals: what to fix first"
description: "How website speed affects sales and SEO, what LCP, INP and CLS measure, how to test your site in PageSpeed Insights and which fixes to prioritize first."
date: 2026-10-30
category: "Websites"
keywords: "website speed, core web vitals, slow website, pagespeed insights"
pt: "velocidade-do-site-core-web-vitals"
---

Website speed affects two things that matter to anyone selling: the experience of the people who arrive and the way Google evaluates the page. A site that takes a while to show its content, freezes when you tap a button or "jumps" while loading loses visitors before they read the offer. And every lost visitor is a lead that never happens.

Google measures this experience with the Core Web Vitals, a set of three metrics: **LCP** (how long the main content takes to appear), **INP** (how long the page takes to respond to an action) and **CLS** (how much the layout moves on its own). They are part of the page experience signals considered in search. They do not replace relevant content, but they can weigh for or against you when competing pages are similar.

The causes of slowness are usually well known: heavy images, too many third-party scripts, weak hosting and bloated themes. You can measure them with free tools and fix them in order, starting with what has the most impact.

## Why speed affects conversion and SEO

A conversion is when the visitor does what the page proposes: request a quote, send a message on WhatsApp, buy. For that to happen, they need to see the offer and be able to act without friction. Think of someone arriving on a phone, with a spotty signal, from a paid ad. If the first screen stays blank for several seconds, some of those people go back to the search results. The company paid for the click and never got the chance to present its service.

In SEO (the set of practices for showing up on Google), speed comes in through the Core Web Vitals as an experience signal. The guide to [SEO for business websites](/en/blog/seo-for-business-websites/) shows how the technical side combines with content and authority.

On [landing pages](/en/blog/what-is-a-landing-page/), pages built for a single action, the effect is often even more visible, because almost all the traffic comes from campaigns and every second of waiting has a direct cost.

## LCP, INP and CLS in plain business language

### LCP: did the main content show up?

LCP stands for *Largest Contentful Paint*. It measures how long it takes for the largest visible element on the first screen to appear, usually the hero image or the main headline. It is the metric that captures the feeling that "the site has opened."

**Good:** 2.5 seconds or less. Above 4 seconds, Google considers it poor.

### INP: did the site respond when I clicked?

INP stands for *Interaction to Next Paint*. It measures the time between a user action, such as tapping a button, opening a menu or typing in a field, and the page's visual response. In 2024, INP replaced FID, an earlier metric that only assessed the first interaction.

**Good:** 200 milliseconds or less. A high INP shows up as that button that seems not to work and makes people tap again.

### CLS: did the page stay still?

CLS stands for *Cumulative Layout Shift*. It measures how much elements move around on their own while the page loads. The classic example: someone is about to tap a link, a banner loads above it and they end up clicking something else.

**Good:** 0.1 or less. It is a unitless score; the lower it is, the more stable the page.

> The three metrics answer simple questions: did the content appear quickly, did the site respond when I tapped, and did the page stay still while I was reading?

## How to measure website speed

### PageSpeed Insights

PageSpeed Insights is a free Google tool. Just paste in the page's address. The report shows two kinds of data, and the difference between them matters:

- **Field data:** comes from real Chrome users who visited the page over the last 28 days. This is what Google uses to assess the Core Web Vitals. Low-traffic sites may not have this data.
- **Lab data:** a simulation run on the spot, under controlled conditions. It is useful for diagnosing problems and testing fixes, but it does not exactly reflect the real experience.

Below the score, the tool lists improvement opportunities, such as images that are too large. Do not chase a lab score of 100; what matters is that the field data falls in the "good" range. Test the mobile version, which is usually more demanding, and several pages, not just the home page.

### Google Search Console

Search Console is Google's free dashboard for tracking how a site appears in search. It has a Core Web Vitals report that groups the site's pages into "good," "needs improvement" and "poor," with mobile and desktop shown separately. It lets you see the problem at scale and follow the effect of your fixes.

## Common causes of slowness

### Heavy images

This is one of the most frequent causes. Photos are uploaded at their original size, much larger than the screen will display. The fixes are well known: resize to the size actually used, use modern formats such as WebP or AVIF, serve different versions for mobile and desktop, and defer loading of images that are below the first screen.

One caveat: the main image, the one that defines the LCP, should not be lazy-loaded. It needs to arrive as soon as possible.

### Third-party scripts

Chat widgets, ad pixels, embedded maps, videos, heatmap tools, review widgets. Each one adds code that the browser has to download and run, and many directly affect INP. It is common to find tools installed for an old campaign that nobody uses anymore.

Take an inventory: what is installed, who uses it and for what. Anything without an owner can go. What stays can be loaded after the main content or only when the user interacts.

### Hosting

If the server takes a long time to start responding, everything else is delayed. Very cheap shared hosting, servers far from the audience and no caching (ready-made copies of pages that can be served faster) are typical causes. A CDN, a network of servers that delivers files from the location closest to the visitor, usually helps.

### Bloated themes and page builders

Ready-made themes and visual page builders come with features to handle any kind of site, and many load all that code on every page. Add to that the plugins accumulated over the years.

In those cases, optimization has limits. Sometimes the most efficient fix is to rebuild the site on a leaner foundation, and that decision belongs in the calculation of [how much a website costs](/en/blog/how-much-does-a-website-cost/).

### Fonts and elements without reserved space

Poorly configured custom fonts delay the display of text. Images, ads and banners without defined dimensions cause layout shifts and worsen CLS. These are small fixes, but they make a difference.

## What to fix first

With the diagnosis in hand, the order below usually brings the best return for the effort:

1. **Start with the pages that bring in business.** The home page, service pages and campaign landing pages come before the blog or the "about us" page.
2. **Optimize images.** It is the cheapest fix and usually the one with the biggest effect on LCP.
3. **Remove unused third-party scripts** and defer the loading of the ones that stay. This mainly helps INP.
4. **Reserve space for images, videos and banners** by setting their dimensions. This solves most CLS problems.
5. **Review hosting, caching and CDN** if the server is slow to respond even when the pages are light.
6. **Assess the site's foundation.** If the previous steps were not enough, the problem may be the theme or the platform.

After each change, check in PageSpeed Insights and follow up in Search Console. Remember that field data covers a 28-day period, so the improvement takes a few weeks to show fully.

Speed is not a one-time adjustment: every new marketing tool or plugin can undo the work. It is worth including a periodic check in the site's maintenance. Our [solutions](/en/#solutions) include building websites on this performance foundation and reviewing existing ones.

## Frequently asked questions

### Does a low PageSpeed Insights score mean the site is slow?

Not necessarily. The 0 to 100 score comes from the lab test, a simulation under specific conditions. What Google uses to assess the experience is field data from real users.

A site can have an average lab score and good Core Web Vitals in the field, and vice versa. Use the score as a diagnostic, not as a target.

### Does improving speed guarantee a higher Google ranking?

No. The Core Web Vitals are one of the signals considered, and content relevance still weighs more. A fast site with weak content is unlikely to beat a page that answers the search better.

The most direct gain is in conversion: more people see the offer and are able to act.

### Will switching hosting fix everything?

Rarely. Hosting affects the server's response time, but heavy images, third-party scripts and bloated themes keep weighing on the visitor's browser. Switching is worth it when the diagnosis shows the server is the bottleneck.

If your site is slow and it is not clear where the problem lies, a technical review helps separate quick fixes from changes that require a new foundation. PEROVANO works remotely and can run the review in English. [Talk to PEROVANO](/en/#contact) and tell us how your site is doing today.
