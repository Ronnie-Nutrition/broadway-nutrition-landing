# Context Handoff — Broadway Nutrition Blog Cluster (June 20, 2026)

## TL;DR
Built and **launched the Broadway Nutrition blog/content cluster** — the PRIMARY task from the Jun 19 handoff. **8 long-tail posts (2 per money page) + a blog index, all LIVE under https://broadwaynutrition.com/blog/** with BlogPosting + FAQPage schema, the Broadway pixel, internal links up to each landing page, and added to the sitemap (now 14 URLs). Homepage footer now links to the blog. Verified end-to-end: all 200, pixel on every page, **zero NH-pixel leak**.

---

## What was done this session

### Blog generator — `_gen_blog.py` (NEW)
Same discipline as `_gen_pages.py`: **edit the script, re-run — never hand-edit the HTML.** Writes `blog/index.html` + `blog/<slug>/index.html`. Each post:
- **BlogPosting + FAQPage JSON-LD**, with a **visible FAQ section that matches the JSON-LD** (stronger than NH's blog, which only had JSON-LD FAQ) — validated 3/3 on every post.
- Broadway pixel `26494205896906932`, neon styling tinted to its money page's color.
- An internal link **UP to its landing (money) page** + a "Keep reading" related cross-link to its sibling post.
- Text/call `Lead` CTA (not "Order Online" — Broadway has no cart).

### The 8 posts (2 per money page)
| Money page | Posts |
|---|---|
| Lit teas (cyan) | `what-is-in-a-lit-tea`, `lit-tea-vs-energy-drink` |
| Weight-loss smoothies (pink) | `meal-replacement-smoothies-weight-loss`, `how-much-protein-meal-replacement-smoothie` |
| Protein coffee (violet) | `what-is-protein-coffee`, `protein-coffee-vs-regular-coffee` |
| Protein shakes (orange) | `best-post-workout-shake`, `how-much-protein-after-workout` |

Plus `/blog/` index (purple theme, Blog JSON-LD listing all 8).

### Sitemap — now jointly owned
Edited `_gen_pages.py` to **glob `blog/*/index.html`** and write the full sitemap (now 14 URLs: home + 4 landing + /blog/ + 8 posts). Decoupled — it picks up whatever blog posts exist.
⚠️ **RUN ORDER: `python3 _gen_blog.py` first, then `python3 _gen_pages.py`** (so the blog files exist when the sitemap globs).

### Homepage
Added a footer link `Read the Broadway Nutrition Blog →` (cyan) so the homepage links into the cluster for crawl + users. Re-deployed `index.html`.

### Deploy — LIVE + verified
- scp'd blog tree + sitemap.xml + updated homepage to `/var/www/broadwaynutrition-home/`.
- Live checks: all 11 URLs (home, /blog/, 8 posts, sitemap) **200**; Broadway pixel present on every page (BW=2: init + noscript); **NH pixel `915336731481586` leak = 0 everywhere**; schema present; homepage blog link live; sitemap = 14 `<loc>`.

---

## Infra / deploy cheat-sheet (unchanged)
- **VPS:** `ssh -o IdentitiesOnly=yes -i ~/.ssh/id_ed25519 root@64.23.156.59`
- **Web root:** `/var/www/broadwaynutrition-home/` — blog lives at `blog/index.html` + `blog/<slug>/index.html`
- **Pixel:** `26494205896906932` ("Broadway Nutrition Website")
- **Redeploy a post:** edit `_gen_blog.py` → `python3 _gen_blog.py` → `python3 _gen_pages.py` (refresh sitemap) → `scp blog/<slug>/index.html root@…:/var/www/broadwaynutrition-home/blog/<slug>/index.html` → verify pixel count unchanged. nginx `try_files` serves it, no restart.

---

## Next session — pick up here

### Manual (can't do from code)
- **GSC:** sitemap already includes the 8 posts; Google discovers them on next fetch. Optionally open Search Console and **request indexing per post** to speed it up.
- **GBP NAP check** — confirm Google Business Profile reads exactly `3272 E Broadway St, Ste 145`.
- **Ads** — share pixel `26494205896906932` to an ACTIVE ad account (lowercase business's `act_1662392794332998` is DISABLED).

### Optional content / SEO follow-ups
- **Deepen the cluster:** go from 2 → 3–4 posts per money page for more topical authority (e.g. "lit tea flavors ranked", "best meal replacement for busy moms", "is protein coffee good for weight loss", "pre- vs post-workout shake").
- **More landing pages** — e.g. a B12/enhancers page, or "smoothies near me" variants.
- **GitHub:** Broadway still isn't a git repo (unlike NH's `Ronnie-Nutrition/Nutritionhub-landing`). If desired, `git init` the workspace + push for version history. Live site + workspace are the current source of truth.

See `PROFILE.md` (durable profile) and memory `project_broadway_nutrition_seo.md`.
