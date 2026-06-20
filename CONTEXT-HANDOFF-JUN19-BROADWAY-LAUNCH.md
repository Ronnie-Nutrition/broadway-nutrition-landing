# Context Handoff — Broadway Nutrition Launch (June 19, 2026)

## TL;DR
Built and **launched** the Broadway Nutrition website from scratch in one session — neon homepage + 4 local-SEO landing pages — **LIVE at https://broadwaynutrition.com** with HTTPS, its own Meta pixel, schema/FAQ markup, and submitted to Google Search Console (sitemap in, indexing requested). Broadway is Ysela's 2nd location, fully separate from Nutrition Hub. **Next session: build the blog/content cluster for topical authority.**

---

## What was done this session

### Discovery / profile
- Pulled real data from menu images + Ronnie: name **Broadway Nutrition**, **3272 E Broadway St, Ste 145, Pearland TX 77581** (per Google Business Profile — menu's "Suite 23" was wrong), phone **832-827-7133**, IG/FB **@broadwaynutrition.tx**, geo 29.5596947 / -95.2730711, hours **Mon–Fri 7 AM–1 PM** (Sat/Sun closed).
- **Pricing = matches Nutrition Hub** (Ronnie's call): gourmet shakes $9.97, lit teas $9.15/32oz, 20oz smoothies $7.80, protein coffee $4.28, B12 $3. NOT the menu-image prices.
- Built fresh from the Nutrition Hub neon template (did NOT sync the Claude.ai Design mockup — unsyncable + needed work). Reused NH's GitHub-hosted drink photos (same drinks).

### Meta pixel
- No Broadway ads ever ran (checked all 4 reachable ad accounts; "broadway" matches were NH's 8201 Broadway address).
- Couldn't create a new pixel (NH business at its 1-pixel cap; API gated behind Pixel ToS). **Repurposed an idle, never-fired pixel** `26494205896906932` (in the lowercase `nutritionhub101` business, id 479594898170018) → renamed **"Broadway Nutrition Website"**. Wired into all 5 pages.

### Build (generator-driven)
- Homepage: `broadway-neon-home.html` (purple/pink/cyan to match logo).
- 4 landing pages via **`_gen_pages.py`** (edit the script, re-run, NOT the HTML directly):
  - `lit-teas-pearland` (cyan), `weight-loss-smoothies-pearland` (pink), `protein-coffee-pearland` (violet), `protein-shakes-pearland` (orange).
  - Each: FoodEstablishment + FAQPage schema (5 Q&As, visible text matches JSON-LD), text/call `Lead` CTAs, cross-links to siblings + homepage.
  - Chose protein-shakes over a B12 page (Broadway's B12 is a $2.14 enhancer, not a hero shot).
- `sitemap.xml` (5 URLs) + `robots.txt` generated.

### Deploy — LIVE
- DNS: Namecheap A records `@` + `www` → `64.23.156.59` (BasicDNS). Propagated.
- VPS web root `/var/www/broadwaynutrition-home/`, nginx block `broadwaynutrition-home`, Let's Encrypt SSL (auto-renew, expires 2026-09-17). HTTP→HTTPS 301.
- Verified: all 5 pages 200, pixel on every page, **zero NH-pixel leak**, sitemap/robots/logo 200.
- **Nothing on Nutrition Hub was touched** — separate web root + server block.

### Search Console — DONE
- Property `https://broadwaynutrition.com` verified via HTML file `googled00c38b198f8183f.html` (account-level token under azteampossibility@gmail.com; the file lives on the web root — **DO NOT DELETE**).
- Sitemap submitted, indexing requested on homepage + 4 pages.

---

## Infra / deploy cheat-sheet
- **VPS:** `ssh -o IdentitiesOnly=yes -i ~/.ssh/id_ed25519 root@64.23.156.59` (zsh: inline ssh flags, never store in a var)
- **Web root:** `/var/www/broadwaynutrition-home/` (`index.html` + `<slug>/index.html` + `assets/` + sitemap/robots + google verify file)
- **nginx:** `/etc/nginx/sites-available/broadwaynutrition-home` → static, `try_files $uri $uri/ /index.html`, no restart needed after scp
- **Redeploy a page:** edit `_gen_pages.py` → `python3 _gen_pages.py` → `scp <slug>.html root@…:/var/www/broadwaynutrition-home/<slug>/index.html` → verify pixel `26494205896906932` count unchanged
- **Workspace:** `~/GTM-Workspace/broadway-nutrition-landing/` (PROFILE.md = full durable profile)
- **Pixel:** `26494205896906932` ("Broadway Nutrition Website")

---

## Next session — pick up here

### PRIMARY: Blog / content cluster (topical authority, 100% free, in-repo)
Write 2–4 short blog posts per landing page targeting long-tail local questions, each linking UP to its money page. Same schema/canonical/OG discipline + `Article`/`BlogPosting` JSON-LD. Ideas:
- Lit teas: "what's in a lit tea?", "best energy tea for focus", "lit tea vs energy drink"
- Weight-loss smoothies: "are meal replacement smoothies good for weight loss?", "how much protein in a meal replacement shake"
- Protein coffee: "what is protein coffee?", "best high-protein coffee in Pearland"
- Protein shakes: "best post-workout shake", "how much protein after a workout"
Deploy under `/blog/<slug>/`, add to sitemap, link from the relevant landing page, request indexing. (Reuse NH's 6 blog posts in `_templates/`-adjacent backup as structural reference.)

### Optional / follow-ups
- **GBP NAP check** — confirm Google Business Profile reads exactly `3272 E Broadway St, Ste 145`.
- **Ads** — share pixel `26494205896906932` to an ACTIVE ad account (lowercase business's own `act_1662392794332998` is DISABLED). Then run Meta ads with conversion tracking.
- Consider a **B12/enhancers page** if Ronnie wants it (alongside or instead of protein-shakes).
- **GitHub:** Broadway isn't a git repo yet (unlike NH's `Ronnie-Nutrition/Nutritionhub-landing`). If desired, `git init` the workspace + push to a new repo for version history. Live site + local backup are the current source of truth.

See `PROFILE.md` (durable profile) and memory `project_broadway_nutrition_seo.md`.
