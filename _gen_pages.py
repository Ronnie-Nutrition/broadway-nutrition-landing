#!/usr/bin/env python3
"""Generate Broadway Nutrition local-SEO landing pages from a shared template.
Keeps NAP / pixel / schema / FAQ identical across pages; visible FAQ is generated
from the same data as the JSON-LD so they always match."""
import json, os

DOMAIN="broadwaynutrition.com"
PIXEL="1026541466453867"
ADDR_STREET="3272 E Broadway St, Ste 145"
ADDR_LOC="Pearland"; ADDR_REG="TX"; ADDR_ZIP="77581"
LAT=29.5596947; LNG=-95.2730711
PHONE_DISP="832-827-7133"; PHONE_TEL="+18328277133"
IG="https://instagram.com/broadwaynutrition.tx"
FB="https://facebook.com/broadwaynutrition.tx"
GH="https://raw.githubusercontent.com/Ronnie-Nutrition/nutritionhub-landing/main"
MAPS="https://www.google.com/maps/dir/?api=1&destination=3272+E+Broadway+St+Ste+145+Pearland+TX+77581"

HOURS_ROWS = """<div class="hrow"><span class="d">Mon – Fri</span><span class="t">7:00 AM – 1:00 PM</span></div>
      <div class="hrow"><span class="d">Saturday</span><span class="t">Closed</span></div>
      <div class="hrow"><span class="d">Sunday</span><span class="t">Closed</span></div>"""
HOURS_SCHEMA = '{ "@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "07:00", "closes": "13:00" }'

def card(img, tag, name, desc, price):
    if img:
        media = f'<img src="{img}" alt="{name} in Pearland" loading="lazy">'
    else:
        media = '<div class="emoji">🥤</div>'
    pr = f'<span class="price">{price}</span>' if price else ''
    return f"""    <div class="drink">
      {media}
      <span class="tag">{tag}</span>
      <h3>{name}</h3>
      <p>{desc}</p>
      {pr}
    </div>"""

def faq_blocks(faqs):
    jsonld = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a_plain}}
        for (q,a_plain,a_html) in faqs]}
    visible = "\n".join(
        f'    <div class="qa">\n      <h3>{q}</h3>\n      <p>{a_html}</p>\n    </div>'
        for (q,a_plain,a_html) in faqs)
    return json.dumps(jsonld, indent=2), visible

PAGES = []

# ---------- shared CTA snippets ----------
def ctas(label):
    return (f'<a class="btn btn-acc" href="sms:{PHONE_TEL}" onclick="fbq(\'track\',\'Lead\')">{label}</a>\n'
            f'    <a class="btn btn-pink" href="tel:{PHONE_TEL}" onclick="fbq(\'track\',\'Lead\')">📞 Call {PHONE_DISP}</a>')

# ================= PAGE 1: LIT TEAS =================
lit_grid = "\n".join([
 card(f"{GH}/tea_dragon_juice.png","LIT TEA","Dragon Juice","32oz · energy, focus &amp; metabolism boost","$9.15"),
 card(f"{GH}/tea_blue_margarita.png","LIT TEA","Wonder Woman","32oz · low-cal clean energy","$9.15"),
 card(None,"20+ FLAVORS","Ask what's fresh","Cherry Bomb, Jolly Rancher, Jungle Juice, Green Apple, Pretty in Pink, Purple Rain, Strawberry Sunrise &amp; more","$9.15"),
])
lit_faq=[
 ("What is a lit tea (energy tea)?",
  "A lit tea — also called an energy tea — is a refreshing 32oz fruit-flavored iced tea loaded for clean energy, mental focus, and a metabolism boost. At Broadway Nutrition in Pearland, every tea is made fresh, comes in 20+ bold flavors, is low calorie, and includes aloe for digestive support.",
  "A lit tea — also called an energy tea — is a refreshing 32oz fruit-flavored iced tea loaded for clean energy, mental focus, and a metabolism boost. At Broadway Nutrition in Pearland, every tea is made fresh, comes in 20+ bold flavors, is low calorie, and includes aloe for digestive support."),
 ("Will a lit tea make me jittery?",
  "Most people get a smooth, clean lift with no jitters and no afternoon crash. If you want it lighter or stronger, just tell us when you order and we'll adjust it.",
  "Most people get a smooth, clean lift with no jitters and no afternoon crash. If you want it lighter or stronger, just tell us when you order and we'll adjust it."),
 ("How much do lit teas cost in Pearland?",
  "Lit teas at Broadway Nutrition are $9.15 each for a 32oz, made fresh to order. Text or call 832-827-7133 to order ahead, or walk in at 3272 E Broadway St, Ste 145.",
  "Lit teas at Broadway Nutrition are $9.15 each for a 32oz, made fresh to order. Text or call 832-827-7133 to order ahead, or walk in at 3272 E Broadway St, Ste 145."),
 ("Are lit teas low in calories?",
  "Yes — our 32oz loaded teas are designed to be light and refreshing, a popular lower-calorie alternative to soda and sugary energy drinks, with aloe for digestive support.",
  "Yes — our 32oz loaded teas are designed to be light and refreshing, a popular lower-calorie alternative to soda and sugary energy drinks, with aloe for digestive support."),
 ("Where can I get lit teas near me in Pearland, TX?",
  "Broadway Nutrition is at 3272 E Broadway St, Ste 145, Pearland, TX 77581, open Mon–Fri 7 AM–1 PM. Text or call 832-827-7133 to order ahead. First visit, ask for us when you walk in.",
  "Broadway Nutrition is at 3272 E Broadway St, Ste 145, Pearland, TX 77581, open Mon–Fri 7 AM–1 PM. Text or call 832-827-7133 to order ahead. First visit, ask for us when you walk in."),
]
PAGES.append(dict(
 slug="lit-teas-pearland", acc="#23e0ff", acc2="#ff2e88", accglow="rgba(35,224,255,.5)",
 title="Lit Teas & Energy Teas in Pearland, TX | Broadway Nutrition",
 desc="32oz lit teas & energy teas in Pearland, TX — clean energy, focus & a metabolism boost, low calorie with aloe. $9.15. Text or call to order at 3272 E Broadway St, Ste 145.",
 ogimg=f"{GH}/tea_dragon_juice.png",
 schema_desc="32oz lit teas and energy teas in Pearland, TX — clean energy, focus, and a metabolism boost, low calorie with aloe.",
 serves=["Energy Teas","Lit Teas","Smoothies"],
 h1='Lit Teas &amp; <span class="a">Energy Teas</span><br>in <span class="b">Pearland, TX</span>',
 hero_sub="32oz loaded teas made fresh — clean energy, mental focus, and a metabolism boost. Low calorie, with aloe for digestive support. No crash.",
 intro_h2='Pearland\'s home for <span>clean lit teas</span>',
 intro="""<p>Searching for <strong>lit teas in Pearland</strong>? You're in the right spot. At Broadway Nutrition on E Broadway, our 32oz loaded teas — a lot of folks call them <strong>energy teas</strong> — are made fresh in 20+ bold flavors for clean energy, mental focus, and a metabolism boost. Low calorie, with aloe for digestive support.</p>
    <p>It's the upgrade to your afternoon soda or that second coffee: refreshing, light, and built to actually keep you going. Grab one before work, before the gym, or as your midday pick-me-up.</p>
    <p>Want protein too? See our <a href="/weight-loss-smoothies-pearland/">meal-replacement smoothies</a>, <a href="/protein-coffee-pearland/">protein coffee</a>, or head <a href="/">back to the full menu</a>.</p>""",
 grid_h2='Fan-favorite <span>tea flavors</span>',
 grid_lead="A taste of what's on the board — flavors rotate, so ask what's fresh today.",
 grid=lit_grid,
 why_h2='Why our <span>lit teas</span> hit different',
 why=[("⚡","Smooth <span>energy</span>","Loaded for clean energy, mental focus, and a metabolism boost — no jitters, no 3 PM crash."),
      ("🍓","20+ <span>flavors</span>","Fruity, refreshing, made fresh to order. Want it lighter or stronger? Just say the word."),
      ("🌿","Light &amp; <span>clean</span>","Low calorie with aloe for digestive support — a smart swap for soda and energy drinks.")],
 faqs=lit_faq, cta_label="🍵 Text to Order",
 close_h2='Your new <span>favorite tea</span> is waiting.',
 close_p="Text or call your order ahead and skip the wait — or walk in and let us make it fresh.",
))

# ================= PAGE 2: WEIGHT LOSS / MEAL REPLACEMENT SMOOTHIES =================
wl_grid = "\n".join([
 card(f"{GH}/shake_banana_pudding.png","GOURMET SMOOTHIE","Banana Pudding","24–30g protein · tastes like dessert","$9.97"),
 card(f"{GH}/shake_strawberry_cheesecake.png","GOURMET SMOOTHIE","Strawberry Cheesecake","24–30g protein · creamy &amp; filling","$9.97"),
 card(f"{GH}/shake_chocolate.png","GOURMET SMOOTHIE","Cocoa Puffs","24–30g protein · cereal-milk shake","$9.97"),
])
wl_faq=[
 ("What is a meal replacement smoothie?",
  "A meal replacement smoothie is a protein-packed drink built to stand in for a meal — filling, balanced, and lower in calories than most fast food. At Broadway Nutrition in Pearland, our gourmet smoothies have 24–30g of protein and taste like dessert.",
  "A meal replacement smoothie is a protein-packed drink built to stand in for a meal — filling, balanced, and lower in calories than most fast food. At Broadway Nutrition in Pearland, our gourmet smoothies have 24–30g of protein and taste like dessert."),
 ("Can meal replacement smoothies help with weight goals?",
  "A lot of our Pearland regulars swap a high-calorie meal or snack for one of our protein smoothies to stay full on fewer calories. They're a tasty, convenient tool that fits into a balanced routine — pair them with the rest of your day for best results.",
  "A lot of our Pearland regulars swap a high-calorie meal or snack for one of our protein smoothies to stay full on fewer calories. They're a tasty, convenient tool that fits into a balanced routine — pair them with the rest of your day for best results."),
 ("How much protein is in a Broadway Nutrition smoothie?",
  "Our gourmet smoothies pack 24–30g of protein. We also make 20oz protein smoothies with 24g of protein at around 190 calories.",
  "Our gourmet smoothies pack 24–30g of protein. We also make 20oz protein smoothies with 24g of protein at around 190 calories."),
 ("How much do the smoothies cost in Pearland?",
  "Gourmet smoothies are $9.97 and 20oz protein smoothies are $7.80. Text or call 832-827-7133 to order ahead, or walk in at 3272 E Broadway St, Ste 145.",
  "Gourmet smoothies are $9.97 and 20oz protein smoothies are $7.80. Text or call 832-827-7133 to order ahead, or walk in at 3272 E Broadway St, Ste 145."),
 ("Where can I get meal replacement smoothies near me in Pearland?",
  "Broadway Nutrition is at 3272 E Broadway St, Ste 145, Pearland, TX 77581, open Mon–Fri 7 AM–1 PM. Text or call 832-827-7133 to order ahead.",
  "Broadway Nutrition is at 3272 E Broadway St, Ste 145, Pearland, TX 77581, open Mon–Fri 7 AM–1 PM. Text or call 832-827-7133 to order ahead."),
]
PAGES.append(dict(
 slug="weight-loss-smoothies-pearland", acc="#ff2e88", acc2="#a64dff", accglow="rgba(255,46,136,.5)",
 title="Weight Loss & Meal Replacement Smoothies in Pearland, TX | Broadway Nutrition",
 desc="Gourmet meal-replacement protein smoothies in Pearland, TX — 24–30g protein, lower calorie, tastes like dessert. $9.97. Text or call 832-827-7133.",
 ogimg=f"{GH}/shake_strawberry_cheesecake.png",
 schema_desc="Gourmet meal-replacement protein smoothies in Pearland, TX — 24–30g protein, lower calorie, made fresh.",
 serves=["Protein Smoothies","Meal Replacement Shakes","Smoothies"],
 h1='Weight Loss &amp; <span class="a">Meal Replacement</span><br>Smoothies in <span class="b">Pearland, TX</span>',
 hero_sub="Gourmet protein smoothies with 24–30g protein that taste like dessert — a filling, lower-calorie swap for a meal. Made fresh to order.",
 intro_h2='Meal replacement smoothies in <span>Pearland</span>',
 intro="""<p>Looking for <strong>meal replacement or weight-loss smoothies in Pearland</strong>? At Broadway Nutrition on E Broadway, our gourmet protein smoothies pack <strong>24–30g of protein</strong> and taste like dessert — a filling, convenient swap for a high-calorie meal or snack.</p>
    <p>Whether you're chasing a goal or just want something that keeps you full without the crash, our regulars grab one for breakfast, lunch on the go, or an afternoon reset. Want a smaller option? Our 20oz protein smoothies run about 190 calories with 24g protein.</p>
    <p>Pair it with a <a href="/lit-teas-pearland/">lit tea for clean energy</a>, add a <a href="/protein-coffee-pearland/">protein coffee</a>, or see the <a href="/">full Broadway menu</a>.</p>""",
 grid_h2='Fan-favorite <span>smoothies</span>',
 grid_lead="A taste of the gourmet board — all 24–30g protein, made fresh to order.",
 grid=wl_grid,
 why_h2='Why our <span>smoothies</span> work',
 why=[("💪","24–30g <span>protein</span>","Real protein that actually keeps you full — the key to swapping a meal without feeling hungry."),
      ("🍰","Dessert <span>flavors</span>","Banana Pudding, Strawberry Cheesecake, Cocoa Puffs and more — craveable, not chalky."),
      ("🔥","Lower <span>calorie</span>","A filling stand-in for fast food that fits your goals — popular with our Pearland regulars.")],
 faqs=wl_faq, cta_label="🥤 Text to Order",
 close_h2='Hit your goals <span>without the bland.</span>',
 close_p="Text or call your order ahead and skip the wait — or walk in and let us build it fresh.",
))

# ================= PAGE 3: PROTEIN COFFEE =================
pc_grid = "\n".join([
 card(f"{GH}/shake_chocolate.png","PROTEIN COFFEE","Mocha","15–30g protein · low sugar","$4.28"),
 card(None,"PROTEIN COFFEE","House","15–30g protein · smooth &amp; clean","$4.28"),
 card(None,"HOT LATTE","Hot Latte","24g protein · warm &amp; cozy","$6.41"),
])
pc_faq=[
 ("What is protein coffee?",
  "Protein coffee is real coffee blended with protein and low sugar — the upgrade to your morning cup. At Broadway Nutrition in Pearland, it comes in House and Mocha with 15–30g of protein.",
  "Protein coffee is real coffee blended with protein and low sugar — the upgrade to your morning cup. At Broadway Nutrition in Pearland, it comes in House and Mocha with 15–30g of protein."),
 ("How much protein and sugar is in it?",
  "Our protein coffee delivers 15–30g of protein with low sugar, so you get the caffeine lift plus protein to start your day without a sugar spike.",
  "Our protein coffee delivers 15–30g of protein with low sugar, so you get the caffeine lift plus protein to start your day without a sugar spike."),
 ("How much does protein coffee cost in Pearland?",
  "Protein coffee is $4.28 at Broadway Nutrition. Prefer it warm? Our hot lattes with 24g protein are $6.41. Text or call 832-827-7133 to order ahead.",
  "Protein coffee is $4.28 at Broadway Nutrition. Prefer it warm? Our hot lattes with 24g protein are $6.41. Text or call 832-827-7133 to order ahead."),
 ("Do you have hot drinks too?",
  "Yes — beyond protein coffee we make hot lattes, hot chocolate, and specialty teas. Ask what's available when you order.",
  "Yes — beyond protein coffee we make hot lattes, hot chocolate, and specialty teas. Ask what's available when you order."),
 ("Where can I get protein coffee near me in Pearland?",
  "Broadway Nutrition is at 3272 E Broadway St, Ste 145, Pearland, TX 77581, open Mon–Fri 7 AM–1 PM. Text or call 832-827-7133 to order ahead.",
  "Broadway Nutrition is at 3272 E Broadway St, Ste 145, Pearland, TX 77581, open Mon–Fri 7 AM–1 PM. Text or call 832-827-7133 to order ahead."),
]
PAGES.append(dict(
 slug="protein-coffee-pearland", acc="#a64dff", acc2="#23e0ff", accglow="rgba(166,77,255,.55)",
 title="Protein Coffee in Pearland, TX | Broadway Nutrition",
 desc="Protein coffee in Pearland, TX — 15–30g protein, low sugar. House & Mocha, $4.28. Plus hot lattes. Text or call 832-827-7133. 3272 E Broadway St, Ste 145.",
 ogimg=f"{GH}/shake_chocolate.png",
 schema_desc="Protein coffee in Pearland, TX — 15–30g protein, low sugar, in House and Mocha, plus hot lattes.",
 serves=["Coffee","Protein Coffee","Protein Smoothies"],
 h1='<span class="a">Protein Coffee</span><br>in <span class="b">Pearland, TX</span>',
 hero_sub="Real coffee with 15–30g protein and low sugar — House or Mocha. The upgrade to your morning cup. Hot lattes too.",
 intro_h2='Protein coffee in <span>Pearland</span>',
 intro="""<p>If you want your caffeine to actually do something, try <strong>protein coffee in Pearland</strong>. At Broadway Nutrition on E Broadway, we blend real coffee with <strong>15–30g of protein</strong> and keep the sugar low — so your morning cup keeps you full instead of crashing you at 10 AM.</p>
    <p>Choose House or Mocha, served cold or as a warm hot latte. It's the perfect grab on your way in, and pairs great with a protein waffle.</p>
    <p>Not a coffee morning? Grab a <a href="/lit-teas-pearland/">lit tea for clean energy</a>, a <a href="/weight-loss-smoothies-pearland/">meal-replacement smoothie</a>, or see the <a href="/">full Broadway menu</a>.</p>""",
 grid_h2='Ways to <span>get your protein coffee</span>',
 grid_lead="House or Mocha, cold or hot — all made fresh to order.",
 grid=pc_grid,
 why_h2='Why <span>protein coffee</span>',
 why=[("☕","Coffee <span>+ protein</span>","15–30g of protein in your cup — caffeine that comes with fuel, not just a buzz."),
      ("🍬","Low <span>sugar</span>","All the flavor without the sugar spike and crash of a sweetened latte."),
      ("🧇","Pairs <span>perfectly</span>","Add a 33g-protein waffle or a B6/B12 energy boost and you've got a full morning.")],
 faqs=pc_faq, cta_label="☕ Text to Order",
 close_h2='Upgrade <span>your morning cup.</span>',
 close_p="Text or call your order ahead and skip the wait — or walk in and ask what's brewing.",
))

# ================= PAGE 4: PROTEIN SHAKES (POST-WORKOUT) =================
ps_grid = "\n".join([
 card(f"{GH}/shake_choc2.png","PROTEIN SHAKE","Brownie Batter","24g protein · rich &amp; thick","$7.80"),
 card(f"{GH}/shake_blue.png","PROTEIN SHAKE","Blue Banana","24g protein · creamy refuel","$7.80"),
 card(f"{GH}/shake_banana_pudding.png","GOURMET SHAKE","Banana Pudding","24–30g protein · dessert flavor","$9.97"),
])
ps_faq=[
 ("Are your protein shakes good post-workout?",
  "Yes — our protein shakes deliver 24–30g of protein to help you refuel and recover after training. They're thick, creamy, and taste like dessert, so the post-gym shake is the part you look forward to.",
  "Yes — our protein shakes deliver 24–30g of protein to help you refuel and recover after training. They're thick, creamy, and taste like dessert, so the post-gym shake is the part you look forward to."),
 ("How much protein is in a Broadway Nutrition shake?",
  "Our 20oz protein shakes have 24g of protein at around 190 calories, and our gourmet shakes pack 24–30g. Tell us your goal and we'll point you to the right one.",
  "Our 20oz protein shakes have 24g of protein at around 190 calories, and our gourmet shakes pack 24–30g. Tell us your goal and we'll point you to the right one."),
 ("How much do protein shakes cost in Pearland?",
  "20oz protein shakes are $7.80 and gourmet shakes are $9.97. Want an extra boost? Add a collagen or B6/B12 energy enhancer. Text or call 832-827-7133 to order ahead.",
  "20oz protein shakes are $7.80 and gourmet shakes are $9.97. Want an extra boost? Add a collagen or B6/B12 energy enhancer. Text or call 832-827-7133 to order ahead."),
 ("Can I add extras to my shake?",
  "Absolutely — boost any shake with collagen, fiber, probiotic, aloe, or a B6/B12 energy add-in. Just ask when you order.",
  "Absolutely — boost any shake with collagen, fiber, probiotic, aloe, or a B6/B12 energy add-in. Just ask when you order."),
 ("Where can I get protein shakes near me in Pearland?",
  "Broadway Nutrition is at 3272 E Broadway St, Ste 145, Pearland, TX 77581, open Mon–Fri 7 AM–1 PM. Text or call 832-827-7133 to order ahead.",
  "Broadway Nutrition is at 3272 E Broadway St, Ste 145, Pearland, TX 77581, open Mon–Fri 7 AM–1 PM. Text or call 832-827-7133 to order ahead."),
]
PAGES.append(dict(
 slug="protein-shakes-pearland", acc="#ff7a18", acc2="#ff2e88", accglow="rgba(255,122,24,.5)",
 title="Protein Shakes in Pearland, TX | Broadway Nutrition",
 desc="Post-workout protein shakes in Pearland, TX — 24–30g protein, made fresh, tastes like dessert. From $7.80. Text or call 832-827-7133. 3272 E Broadway St, Ste 145.",
 ogimg=f"{GH}/shake_choc2.png",
 schema_desc="Post-workout protein shakes in Pearland, TX — 24–30g protein, made fresh to order.",
 serves=["Protein Shakes","Protein Smoothies","Smoothies"],
 h1='<span class="a">Protein Shakes</span><br>in <span class="b">Pearland, TX</span>',
 hero_sub="Thick, creamy protein shakes with 24–30g protein — the post-workout refuel that tastes like dessert. Made fresh to order.",
 intro_h2='Post-workout protein shakes in <span>Pearland</span>',
 intro="""<p>Just finished training? Grab a <strong>protein shake in Pearland</strong> at Broadway Nutrition on E Broadway. Every shake is made fresh with <strong>24–30g of protein</strong> to help you refuel and recover — thick, creamy, and tasting like dessert.</p>
    <p>Our 20oz protein shakes run about 190 calories with 24g protein, and the gourmet shakes go up to 30g. Add a collagen or B6/B12 energy boost if you want extra. It's the post-gym treat you'll actually look forward to.</p>
    <p>Chasing a goal instead? See our <a href="/weight-loss-smoothies-pearland/">meal-replacement smoothies</a>, grab a <a href="/lit-teas-pearland/">lit tea</a>, or view the <a href="/">full Broadway menu</a>.</p>""",
 grid_h2='Fan-favorite <span>protein shakes</span>',
 grid_lead="A taste of the board — all made fresh with 24g+ protein.",
 grid=ps_grid,
 why_h2='Why refuel <span>with us</span>',
 why=[("💪","24–30g <span>protein</span>","Real protein to help your muscles recover after a hard session — no chalky aftertaste."),
      ("🍨","Dessert <span>flavors</span>","Brownie Batter, Blue Banana, Banana Pudding and more — the treat that fits your macros."),
      ("➕","Add a <span>boost</span>","Top any shake with collagen, fiber, or a B6/B12 energy add-in for extra support.")],
 faqs=ps_faq, cta_label="🥤 Text to Order",
 close_h2='Refuel <span>the right way.</span>',
 close_p="Text or call your order ahead and skip the wait — or walk in straight from the gym.",
))

# ---------------- TEMPLATE ----------------
TPL = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__</title>
<meta name="description" content="__DESC__">
<link rel="canonical" href="https://__DOMAIN__/__SLUG__/">

<meta property="og:type" content="website">
<meta property="og:title" content="__TITLE__">
<meta property="og:description" content="__DESC__">
<meta property="og:url" content="https://__DOMAIN__/__SLUG__/">
<meta property="og:image" content="__OGIMG__">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="__TITLE__">
<meta name="twitter:description" content="__DESC__">

<!-- LocalBusiness structured data -->
<script type="application/ld+json">
__BIZ_JSONLD__
</script>

<!-- FAQ structured data (eligible for FAQ rich results) -->
<script type="application/ld+json">
__FAQ_JSONLD__
</script>

<!-- Meta Pixel -->
<script>
!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,
document,'script','https://connect.facebook.net/en_US/fbevents.js');
fbq('init','__PIXEL__');fbq('track','PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=__PIXEL__&ev=PageView&noscript=1"/></noscript>
<style>
  :root{
    --bg:#0a0610; --card:#16101f; --line:#2a1f36;
    --acc:__ACC__; --acc2:__ACC2__; --accGlow:__ACCGLOW__; --pink:#ff2e88;
    --txt:#f1ecf6; --mut:#a99cb8;
    --font:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  }
  *{margin:0;padding:0;box-sizing:border-box}
  html{scroll-behavior:smooth}
  body{background:var(--bg);color:var(--txt);font-family:var(--font);overflow-x:hidden;line-height:1.5}
  a{color:inherit;text-decoration:none}
  .wrap{max-width:1080px;margin:0 auto;padding:0 22px}
  .nav{position:sticky;top:0;z-index:50;background:rgba(10,6,16,.85);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
  .nav .row{display:flex;align-items:center;justify-content:space-between;padding:12px 0}
  .brand{font-weight:900;letter-spacing:.5px;font-size:18px}
  .brand span{color:var(--acc)}
  .nav .btn{padding:9px 18px;font-size:13px}
  .hero{position:relative;padding:64px 0 46px;text-align:center;overflow:hidden}
  .hero::before{content:"";position:absolute;inset:0;background:
    radial-gradient(600px 300px at 18% 0%,var(--accGlow),transparent 62%),
    radial-gradient(700px 360px at 85% 18%,rgba(255,46,136,.12),transparent 60%)}
  .pill{position:relative;display:inline-flex;align-items:center;gap:8px;background:var(--card);border:1px solid var(--line);color:var(--mut);font-size:12px;font-weight:800;letter-spacing:1.2px;padding:7px 16px;border-radius:40px;margin-bottom:22px}
  .hero h1{position:relative;font-size:clamp(32px,6vw,58px);line-height:1.05;font-weight:900;letter-spacing:-1px}
  .hero h1 .a{color:var(--acc);text-shadow:0 0 18px var(--accGlow)} .hero h1 .b{color:var(--pink)}
  .hero p{position:relative;max-width:600px;margin:18px auto 0;color:var(--mut);font-size:17px}
  .cta{position:relative;display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin-top:30px}
  .btn{cursor:pointer;display:inline-block;border:none;font-family:var(--font);font-weight:900;letter-spacing:.5px;border-radius:40px;transition:.18s;font-size:14px}
  .btn-acc{background:var(--acc);color:#0a0610;padding:14px 26px;box-shadow:0 0 24px var(--accGlow)}
  .btn-acc:hover{transform:translateY(-2px)}
  .btn-pink{background:var(--pink);color:#fff;padding:14px 26px;box-shadow:0 0 22px rgba(255,46,136,.4)}
  .btn-pink:hover{transform:translateY(-2px)}
  .btn-ghost{background:transparent;border:1px solid var(--line);color:var(--txt);padding:13px 24px}
  .btn-ghost:hover{border-color:var(--acc);color:var(--acc)}
  .sec{padding:48px 0;border-top:1px solid var(--line)}
  .sec h2{font-size:clamp(26px,4.4vw,38px);font-weight:900;letter-spacing:-.5px;text-align:center}
  .sec h2 span{color:var(--acc)}
  .sec .lead{color:var(--mut);text-align:center;max-width:620px;margin:12px auto 0;font-size:15px}
  .prose{max-width:760px;margin:28px auto 0;color:var(--txt);font-size:16px;line-height:1.75}
  .prose p{margin-bottom:18px;color:#d6cee0}
  .prose strong{color:var(--acc)}
  .prose a{color:var(--pink);text-decoration:underline;text-underline-offset:3px}
  .grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:34px}
  .drink{background:var(--card);border:1px solid var(--line);border-radius:20px;padding:18px;text-align:center;position:relative;overflow:hidden;transition:.2s;display:flex;flex-direction:column}
  .drink::after{content:"";position:absolute;left:0;top:0;height:3px;width:100%;background:linear-gradient(90deg,var(--acc),var(--acc2))}
  .drink:hover{transform:translateY(-4px);border-color:var(--acc)}
  .drink img{width:100%;height:200px;object-fit:contain;margin-bottom:12px}
  .drink .emoji{font-size:52px;margin:18px 0 22px}
  .drink .tag{font-size:11px;font-weight:900;letter-spacing:1.5px;padding:4px 10px;border-radius:30px;display:inline-block;margin-bottom:8px;background:var(--card);border:1px solid var(--line);color:var(--acc)}
  .drink h3{font-size:17px;font-weight:900;letter-spacing:-.3px}
  .drink p{color:var(--mut);font-size:13px;margin-top:4px;flex:1}
  .drink .price{display:block;margin-top:8px;font-weight:900;color:var(--txt);font-size:15px}
  .feats{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:34px}
  .fcard{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:24px}
  .fcard .ic{font-size:28px;margin-bottom:10px}
  .fcard h3{font-size:18px;font-weight:900;margin-bottom:6px}
  .fcard h3 span{color:var(--acc)}
  .fcard p{color:var(--mut);font-size:14px}
  .faq{max-width:760px;margin:30px auto 0}
  .qa{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:20px 22px;margin-bottom:14px}
  .qa h3{font-size:16px;font-weight:900;margin-bottom:8px;color:var(--txt)}
  .qa p{color:var(--mut);font-size:14px;line-height:1.7}
  .qa a{color:var(--acc);text-decoration:underline}
  .info{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:34px}
  .infocard{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:24px}
  .infocard h3{font-size:16px;font-weight:900;letter-spacing:1px;color:var(--pink);margin-bottom:14px}
  .hrow{display:flex;justify-content:space-between;padding:9px 0;border-bottom:1px solid var(--line);font-size:14px}
  .hrow:last-child{border-bottom:none}
  .hrow .d{color:var(--mut)} .hrow .t{font-weight:700}
  .infocard .addr{font-size:15px;line-height:1.7}
  .infocard .addr b{color:var(--acc)}
  .close{text-align:center;padding:60px 0 36px;border-top:1px solid var(--line)}
  .close h2{font-size:clamp(28px,4.6vw,44px);font-weight:900;letter-spacing:-.5px}
  .close h2 span{color:var(--acc)}
  .close p{color:var(--mut);max-width:480px;margin:14px auto 26px;font-size:15px}
  .footer{text-align:center;color:#6a5d78;font-size:12px;padding:26px 0;border-top:1px solid var(--line)}
  .footer a{color:var(--mut)}
  .crumb{font-size:13px;color:var(--mut);padding-top:18px}
  .crumb a{color:var(--acc)}
  @media(max-width:780px){.grid{grid-template-columns:1fr 1fr;gap:12px}.feats{grid-template-columns:1fr}.info{grid-template-columns:1fr}.drink img{height:160px}}
  @media(max-width:480px){.grid{grid-template-columns:1fr}}
</style>
</head>
<body>

<nav class="nav"><div class="wrap row">
  <a class="brand" href="/">BROADWAY <span>NUTRITION</span></a>
  <a class="btn btn-pink" href="sms:__PHONE_TEL__" onclick="fbq('track','Lead')">Text to Order</a>
</div></nav>

<header class="hero"><div class="wrap">
  <span class="pill">📍 __ADDR_STREET__ · PEARLAND, TX</span>
  <h1>__H1__</h1>
  <p>__HERO_SUB__</p>
  <div class="cta">
    __CTAS__
    <a class="btn btn-ghost" href="#more">See More</a>
  </div>
</div></header>

<section class="sec"><div class="wrap">
  <h2>__INTRO_H2__</h2>
  <div class="prose">
    __INTRO__
  </div>
</div></section>

<section class="sec" id="more"><div class="wrap">
  <h2>__GRID_H2__</h2>
  <p class="lead">__GRID_LEAD__</p>
  <div class="grid">
__GRID__
  </div>
  <div class="cta" style="margin-top:34px">
    <a class="btn btn-acc" href="sms:__PHONE_TEL__" onclick="fbq('track','Lead')">__CTA_LABEL__ →</a>
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <h2>__WHY_H2__</h2>
  <div class="feats">
__WHY__
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <h2>__FAQ_H2__ — <span>FAQ</span></h2>
  <div class="faq">
__FAQ_HTML__
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <h2>Come <span>see us</span></h2>
  <div class="info">
    <div class="infocard">
      <h3>HOURS</h3>
      __HOURS_ROWS__
    </div>
    <div class="infocard">
      <h3>LOCATION</h3>
      <p class="addr">
        <b>Broadway Nutrition</b><br>
        __ADDR_STREET__<br>
        Pearland, TX 77581
      </p>
      <div class="cta" style="justify-content:flex-start;margin-top:18px">
        <a class="btn btn-ghost" href="__MAPS__" target="_blank">Get Directions</a>
        <a class="btn btn-ghost" href="__IG__" target="_blank">Message Us on IG</a>
      </div>
    </div>
  </div>
</div></section>

<div class="close"><div class="wrap">
  <h2>__CLOSE_H2__</h2>
  <p>__CLOSE_P__</p>
  <a class="btn btn-acc" href="sms:__PHONE_TEL__" onclick="fbq('track','Lead')">__CTA_LABEL__</a>
</div></div>

<div class="footer"><div class="wrap">
  <div class="crumb"><a href="/">← Back to Broadway Nutrition home</a></div>
  © 2026 Broadway Nutrition · __ADDR_STREET__, Pearland, TX ·
  <a href="__IG__" target="_blank">@broadwaynutrition.tx</a>
</div></div>

</body>
</html>
"""

def biz_jsonld(p):
    d={"@context":"https://schema.org","@type":"FoodEstablishment","name":"Broadway Nutrition",
       "description":p["schema_desc"],"url":f"https://{DOMAIN}/{p['slug']}/","image":p["ogimg"],
       "servesCuisine":p["serves"],"priceRange":"$","telephone":"+1-832-827-7133",
       "address":{"@type":"PostalAddress","streetAddress":ADDR_STREET,"addressLocality":ADDR_LOC,
                  "addressRegion":ADDR_REG,"postalCode":ADDR_ZIP,"addressCountry":"US"},
       "geo":{"@type":"GeoCoordinates","latitude":LAT,"longitude":LNG},
       "acceptsReservations":"False","sameAs":[IG,FB]}
    s=json.dumps(d,indent=2)
    # inject opening hours as raw (already valid json fragment)
    s=s[:-2]+',\n  "openingHoursSpecification": [\n    '+HOURS_SCHEMA+'\n  ]\n}'
    return s

def why_html(why):
    return "\n".join(
        f'    <div class="fcard">\n      <div class="ic">{ic}</div>\n      <h3>{h}</h3>\n      <p>{p}</p>\n    </div>'
        for (ic,h,p) in why)

outdir=os.path.dirname(os.path.abspath(__file__))
for p in PAGES:
    faq_json, faq_vis = faq_blocks(p["faqs"])
    html=TPL
    rep={
      "__TITLE__":p["title"],"__DESC__":p["desc"],"__DOMAIN__":DOMAIN,"__SLUG__":p["slug"],
      "__OGIMG__":p["ogimg"],"__PIXEL__":PIXEL,"__ACC__":p["acc"],"__ACC2__":p["acc2"],
      "__ACCGLOW__":p["accglow"],"__BIZ_JSONLD__":biz_jsonld(p),"__FAQ_JSONLD__":faq_json,
      "__ADDR_STREET__":ADDR_STREET,"__H1__":p["h1"],"__HERO_SUB__":p["hero_sub"],
      "__CTAS__":ctas(p["cta_label"]),"__INTRO_H2__":p["intro_h2"],"__INTRO__":p["intro"],
      "__GRID_H2__":p["grid_h2"],"__GRID_LEAD__":p["grid_lead"],"__GRID__":p["grid"],
      "__WHY_H2__":p["why_h2"],"__WHY__":why_html(p["why"]),
      "__FAQ_H2__":p["title"].split(" in ")[0]+" in Pearland","__FAQ_HTML__":faq_vis,
      "__HOURS_ROWS__":HOURS_ROWS,"__MAPS__":MAPS,"__IG__":IG,"__PHONE_TEL__":PHONE_TEL,
      "__CTA_LABEL__":p["cta_label"],"__CLOSE_H2__":p["close_h2"],"__CLOSE_P__":p["close_p"],
    }
    for k,v in rep.items(): html=html.replace(k,v)
    # safety: no leftover tokens
    import re
    left=set(re.findall(r"__[A-Z0-9_]+__",html))
    assert not left, f"{p['slug']}: leftover tokens {left}"
    path=os.path.join(outdir,f"{p['slug']}.html")
    open(path,"w",encoding="utf-8").write(html)
    print("wrote",path,f"({len(html)} bytes)")

# sitemap + robots
sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemap-1.0.org/schemas/sitemap/0.9">\n'.replace("sitemap-1.0.org/schemas/sitemap","www.sitemaps.org/schemas/sitemap")
urls=[f"https://{DOMAIN}/"]+[f"https://{DOMAIN}/{p['slug']}/" for p in PAGES]
import glob
# blog cluster (generated by _gen_blog.py). Glob so this stays decoupled —
# the sitemap picks up whatever blog/ pages exist. Run _gen_blog.py first.
if os.path.isfile(os.path.join(outdir,"blog","index.html")):
    urls.append(f"https://{DOMAIN}/blog/")
for ix in sorted(glob.glob(os.path.join(outdir,"blog","*","index.html"))):
    slug=os.path.basename(os.path.dirname(ix))
    urls.append(f"https://{DOMAIN}/blog/{slug}/")
sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for u in urls:
    sm+=f"  <url><loc>{u}</loc><changefreq>weekly</changefreq></url>\n"
sm+="</urlset>\n"
open(os.path.join(outdir,"sitemap.xml"),"w",encoding="utf-8").write(sm)
open(os.path.join(outdir,"robots.txt"),"w",encoding="utf-8").write(
    f"User-agent: *\nAllow: /\nSitemap: https://{DOMAIN}/sitemap.xml\n")
print("wrote sitemap.xml + robots.txt")
print("\nPAGES:", ", ".join(p["slug"] for p in PAGES))
