# Broadway Nutrition — First Meta Ad (Playbook for Ysela)
**How to use this:** open Claude on your computer, paste this ENTIRE document in, and say "walk me through this step by step." It has everything Claude needs — no other context required. Work top to bottom; each part ends with what "done" looks like.

---

## CONTEXT (for Claude — read first)
- **Business:** Broadway Nutrition — Ysela's smoothie/nutrition club. 3272 E Broadway St, Ste 145, Pearland TX 77581 · 832-827-7133 · Mon–Fri 7am–1pm · IG/FB: @broadwaynutrition.tx
- **Website (live, ads-ready):** https://broadwaynutrition.com — the ad destination is **https://broadwaynutrition.com/weight-loss-smoothies-pearland/**
- **Meta Pixel already installed on every page:** ID **1026541466453867** ("Broadway Nutrition Website"). It fires `PageView` on load and `Lead` when someone taps the Text-Us / Call buttons. This pixel currently lives in the Business Manager named for "nutritionhub101" (Business ID **479594898170018**) — an older business profile Ysela has login access to. That business's old ad account (**act_1662392794332998**) is disabled.
- **Goal:** one simple local ad — $5/day, 5-mile radius around the club, optimized for the pixel's Lead event (people tapping text/call).
- **Ground rules:** everything runs under Ysela's own login with HER payment card. This is a brand-new campaign for HER business — we are not re-running anything from any restricted account. If Meta asks to verify identity, use her real info.

---

## PART 1 — Five-minute account audit (find out what your login can do)

1. Go to **business.facebook.com** and log in.
2. Top-left business switcher: note **every Business Portfolio** you can see. You're looking for the one containing ID **479594898170018** (Settings → Business info shows the ID).
3. In that portfolio: **Settings (⚙️) → Accounts → Ad accounts** — list what's there and each one's status (Active / Disabled).
4. **Settings → Data sources → Datasets (Pixels)** — confirm you can see pixel **1026541466453867**.
5. **Billing → Payment methods** — is there a valid card? (You'll add yours later if not.)

**Now pick your branch:**

- **Branch A — an ACTIVE ad account exists** (any active one you administer): → go to Part 2.
- **Branch B — only the disabled account exists:** two moves, do both:
  1. **Request review:** Account Quality (facebook.com/accountquality) → select the disabled account → "Request review" → follow the identity steps honestly. Reviews often clear in 24–48h for inherited/stale accounts.
  2. **Try creating a fresh ad account:** Settings → Accounts → Ad accounts → **Add → Create a new ad account** (name: `Broadway Nutrition Ads`, USD, your card). If Meta blocks creation (it sometimes does when a sibling account is disabled), wait for the review in step 1.
  → When you have any active account, go to Part 2.
- **Branch C — you can't see the pixel at all:** stop and text Ronnie. (Fallback exists: his Claude can create a brand-new pixel in your portfolio and re-wire the website to it in ~15 minutes — the site is generated from scripts, so swapping pixel IDs is easy.)

**Done =** you know your active ad account ID (looks like `act_XXXXXXXXX`) and it has your payment card on it.

## PART 2 — Connect the pixel to the ad account (2 min)

Settings → **Data sources → Datasets** → click pixel **1026541466453867** → **Connected assets** (or "Add assets") → add your active ad account.

**Done =** the ad account appears in the pixel's connected-assets list.

## PART 3 — Confirm the pixel is alive (2 min)

**Events Manager** (business.facebook.com/events_manager2) → select pixel 1026541466453867 → Overview should show recent `PageView` (and maybe `Lead`) activity. To force a test: open **Test events** tab, then visit https://broadwaynutrition.com in another tab and tap a Text-Us button — both events should appear within ~30 seconds.

**Done =** you've seen PageView + Lead arrive.

## PART 4 — Build the campaign (Ads Manager, ~15 min)

Open **Ads Manager** on the active account → **+ Create**.

**Campaign**
- Objective: **Leads**
- Name: `Broadway WLS Smoothies — Leads v1`
- Advantage campaign budget: ON → **$5.00/day**

**Ad set** (`Pearland 5mi — Lead`)
- Conversion location: **Website** · Pixel: **1026541466453867** · Event: **Lead**
- Location: drop a pin at **3272 E Broadway St, Pearland TX** → radius **+5 miles**
- Age **21–65**, all genders. No interest targeting — leave broad (5-mile local + broad beats narrow interests at this budget).
- Placements: **Advantage+** (automatic).

**Ad** (`WLS v1`)
- Identity: **Broadway Nutrition** Facebook page + **@broadwaynutrition.tx** Instagram. (If the page doesn't appear, your login lacks page access — text Ronnie before continuing.)
- Format: single image. Creative: a bright, real photo of the actual shakes on YOUR counter (phone photo is perfect — real beats stock every time; square 1080×1080).
- Website URL: `https://broadwaynutrition.com/weight-loss-smoothies-pearland/`
- Call to action button: **Learn more**
- Copy — use variant 1; keep 2 and 3 for the ad's "Add text variation" slots:

**Variant 1**
> Primary: Meal-replacement smoothies, made fresh on Broadway in Pearland. 24g of protein, around 200–300 calories, and it tastes like a milkshake — not a chore. Open Mon–Fri 7am–1pm. Text or call ahead and yours is ready when you walk in. 🥤
> Headline: Fresh Meal-Replacement Smoothies · Pearland

**Variant 2**
> Primary: Breakfast that works as hard as you do. Our meal-replacement smoothies pack 24g of protein into ~250 calories — grab one on Broadway before work, Mon–Fri from 7am. First time in? Tell us — we'll take care of you. 💪
> Headline: Your New Breakfast Stop on Broadway

**Variant 3**
> Primary: New to Broadway Nutrition? We're the smoothie club at Broadway & 35 in Pearland. Real meal-replacement shakes, protein coffee, and energy teas — made to order, weekday mornings 7am–1pm. Come see what the neighbors keep talking about. 👋
> Headline: Pearland's Neighborhood Nutrition Club

**⚠️ Compliance guardrails (Meta is strict on the weight-loss category — the copy above is written to pass; keep these rules if you edit):**
- Never address the reader's body or weight ("struggling with your weight?" = instant rejection). Talk about the PRODUCT, not their body.
- No before/after photos, no "lose X pounds," no timeframe promises.
- Keep age targeting 21+ as set above.

**Publish.** It'll go into review — usually approved within a few hours.

## PART 5 — After launch
1. Text Ronnie: the ad account ID you used, and "live."
2. Don't touch it for 7 days — $5/day needs a full week to learn. No edits, no panic at day-2 numbers.
3. Ronnie's Claude will pull the readout (spend, CPL, Lead events) via the pixel/API at day 7 and recommend next steps.

## If anything blocks you
Screenshot the exact screen + error and text it to Ronnie. The usual suspects: page access missing (Part 4 identity step), payment method rejected (use a different card of yours), or ad rejected (usually copy — re-check the guardrails, or use Variant 3 which has zero weight-loss language).
