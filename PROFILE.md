# Broadway Nutrition — Site Profile (Local SEO Buildout)

Ysela's 2nd nutrition-club location. **Separate** from Nutrition Hub — its own NAP,
domain, pixel, prices. Only the method + page templates transfer from Nutrition Hub.

## Confirmed (from menu images + Ronnie, 2026-06-19)
| Field | Value | Source |
|---|---|---|
| Business name (exact) | **Broadway Nutrition** | logo + menu |
| Address | **3272 E Broadway St, Ste 145, Pearland, TX 77581** | **Google Business Profile** (Ronnie 6/19 — authoritative). Menu PNGs said "Suite 23" — superseded by GBP. |
| Phone (live order line) | **832-827-7133** | Ronnie confirmed 6/19 |
| Instagram / Facebook | **@broadwaynutrition.tx** | menu |
| Business type schema | FoodEstablishment | same as Nutrition Hub |
| Tagline | "Let us add a little joy to your day" | logo |
| Ordering model | **Text/call to order + Meta Pixel `Lead` events** on call/text/directions CTAs (ads-ready; no online cart yet) | Ronnie 6/19 |
| Build approach | Build FRESH from Nutrition Hub neon template (not syncing the Claude.ai Design site) | Ronnie 6/19 |
| Host | Same VPS as nutritionhub101.com (root@64.23.156.59) | Ronnie 6/19 |

## ⏳ OPEN — needed before build/deploy
- [x] **Domain** — **broadwaynutrition.com** (registered on Namecheap, Ronnie 6/19). DNS not yet pointed at VPS.
- [x] **Meta Pixel ID** — **`26494205896906932`** ("Broadway Nutrition Website"). Repurposed an idle, never-fired pixel in the lowercase `nutritionhub101` business (id 479594898170018) — renamed 6/19. Separate from NH's main `915336731481586`. Wired into homepage (3 spots). ⚠️ For ads, share this pixel to an ACTIVE ad account — the lowercase business's own ad account `act_1662392794332998` is DISABLED (status 2). Active accounts on Ronnie's login: NH `act_1494337781215320`, EasyAIFlows, Ronald Craig personal.
- [x] **Geo** — 29.5596947, -95.2730711 (OSM geocode). ⚠️ resolved to "3272 **East** Broadway St" — verify E vs W against Google Business Profile.
- [x] **Hours** — Mon–Fri 7:00 AM–1:00 PM; Sat/Sun closed (Ronnie 6/19). In schema + homepage.
- [ ] **Drink photos** — reusing Nutrition Hub product images from `raw.githubusercontent.com/Ronnie-Nutrition/nutritionhub-landing/main/` (same drinks). Ronnie approved 6/19.
- [ ] Confirm prices below are current (3 menu images had conflicting phone #s; prices taken from `menu-prices-1.png`/`-2.png`).

## ⚠️ PRICING = MATCH NUTRITION HUB (Ronnie 6/19) — NOT the menu-image prices
Broadway sells the same drinks at the same prices as Nutrition Hub. Use these on the site:
- **Gourmet smoothies (32oz, 24–30g protein): $9.97**
- **20oz smoothies: $7.80**
- **Lit teas (32oz, NOT 52oz): $9.15**
- **B12 shot: $3** · BCAAs +$3 · Creatine +$2
- **Protein coffee: 15–30g protein** (low sugar)
- Photo→NH-name map: tea_red=Mamacita, shake_salted_caramel=Fried Ice Cream, shake_chocolate=Cocoa Puffs, shake_strawberry_cheesecake=Strawberry Cheesecake.

## Menu / prices from menu images (REFERENCE ONLY — superseded by NH pricing above)
**Drinks**
- Gourmet Smoothies (24–30g protein): **$8.55**
- Smoothies (20oz, 24g protein, 190 cal): **$6.41**
- Lit Tea (52oz, energy/metabolism/focus, low cal): **$7.43**
- Vegetarian Smoothie (24g protein, rice/quinoa pea protein): **$7.43**
- Protein Coffee (15g protein, 2g sugar — House, Mocha): **$4.28**
- Donut Shot Fat Reducer: **$5.34**

**Hot Drinks**
- Chai Latte (15g protein): $5.34
- Khadija Tea (immunity boost): $9.08
- Hot Latte (24g protein): $6.41
- Hangover Tea: $7.43
- Detox Tea: $7.43
- Hot Chocolate (24g protein): $6.41

**Waffles (33g protein):** $10.68 — Banana, Chocolate, Regular, Pineapple Upside; toppings: strawberries, banana, granola, Reddi-Wip, sugar-free syrup

**Enhancers:** Fiber $1.07 · Probiotic $1.60 · Aloe $1.07 · B6/B12 Energy $2.14 · Lift Off 24 $2.67 · Collagen $2.14

**Programs:** 3-Day Eat Clean Challenge $30 · Nutrition Club Owner Opportunity

## Landing-page cluster — BUILT 6/19 (staged, not yet deployed)
Generator: `_gen_pages.py` (re-run to regenerate all 4 + sitemap/robots; edits go in the script, not the HTML).
1. `lit-teas-pearland.html` — cyan — Lit/Energy Teas $9.15/32oz
2. `weight-loss-smoothies-pearland.html` — pink — Meal-replacement gourmet smoothies $9.97 (highest intent)
3. `protein-coffee-pearland.html` — violet — Protein Coffee $4.28 / hot latte $6.41
4. `protein-shakes-pearland.html` — orange — Post-workout protein shakes $7.80/$9.97
Each: FoodEstablishment + FAQPage schema (5 Q&As, visible matches JSON-LD), Broadway pixel, text/call Lead CTAs, cross-linked to siblings + homepage. Homepage "Why" cards link to all 4.
NOTE: chose **protein-shakes** over a B12 page (Broadway's B12 is a $2.14 enhancer, not a hero $3 shot like NH; "protein shakes Pearland" is stronger + has photos). Swap if Ronnie wants B12 instead.

## Deploy — ✅ LIVE as of 2026-06-19
- **https://broadwaynutrition.com** — homepage + 4 landing pages, all 200, SSL (Let's Encrypt, auto-renew, expires 2026-09-17).
- SSH: `ssh -o IdentitiesOnly=yes -i ~/.ssh/id_ed25519 root@64.23.156.59`
- Web root: `/var/www/broadwaynutrition-home/` (index.html + `<slug>/index.html` + assets/ + sitemap.xml + robots.txt)
- nginx: `/etc/nginx/sites-available/broadwaynutrition-home` (HTTP→HTTPS redirect by certbot). Static, `try_files $uri $uri/ /index.html`. Reload after scp, no restart.
- DNS: Namecheap A records @ + www → 64.23.156.59 (BasicDNS). Propagated.
- Redeploy a page: scp local `<slug>.html` → `/var/www/broadwaynutrition-home/<slug>/index.html`. Re-run `_gen_pages.py` first if content changed. Verify pixel `26494205896906932` count unchanged.

## Blog cluster — ✅ BUILT + LIVE 6/20
Generator: `_gen_blog.py` (edit script, re-run — never hand-edit HTML). Writes `blog/index.html` + `blog/<slug>/index.html`. 8 posts, 2 per money page, each with BlogPosting + FAQPage JSON-LD (visible FAQ matches JSON-LD), Broadway pixel, neon styling, internal link UP to its landing page + a related cross-link.
- Lit teas (cyan): `what-is-in-a-lit-tea`, `lit-tea-vs-energy-drink`
- Weight-loss smoothies (pink): `meal-replacement-smoothies-weight-loss`, `how-much-protein-meal-replacement-smoothie`
- Protein coffee (violet): `what-is-protein-coffee`, `protein-coffee-vs-regular-coffee`
- Protein shakes (orange): `best-post-workout-shake`, `how-much-protein-after-workout`
- Blog index at `/blog/`; homepage footer now links to it. All 200, pixel verified, zero NH-pixel leak.
- **Sitemap is now owned jointly**: `_gen_pages.py` globs `blog/*/index.html` and writes the FULL sitemap (14 URLs). **Run order: `_gen_blog.py` first, then `_gen_pages.py`** so the blog URLs land in sitemap.xml.
- Redeploy a post: edit `_gen_blog.py` → `python3 _gen_blog.py` → `python3 _gen_pages.py` (refresh sitemap) → scp `blog/<slug>/index.html` → `/var/www/broadwaynutrition-home/blog/<slug>/index.html`.

## ⏳ Remaining (manual, can't do from code)
- [x] **Google Search Console** — DONE 6/19. Property `https://broadwaynutrition.com` verified via HTML file `googled00c38b198f8183f.html` (account-level token, also on web root — DO NOT DELETE). Sitemap submitted, indexing requested on homepage + 4 pages.
- [ ] **GSC — blog** — sitemap.xml now includes the 8 posts + `/blog/`; Google will discover them on next sitemap fetch. Optional: request indexing per post in GSC to speed it up.
- [ ] **GBP NAP check** — confirm Google Business Profile says exactly `3272 E Broadway St, Ste 145` (matches site).
- [ ] **Ads** — share pixel `26494205896906932` to an active ad account (lowercase business's own account is disabled).
