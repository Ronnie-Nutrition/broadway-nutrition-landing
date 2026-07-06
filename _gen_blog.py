#!/usr/bin/env python3
"""Generate the Broadway Nutrition blog cluster (topical-authority content).
Same discipline as _gen_pages.py: edit THIS script, re-run, never hand-edit the HTML.
Each post: BlogPosting + FAQPage JSON-LD (visible FAQ matches JSON-LD), canonical, OG,
Broadway pixel, neon styling, and an internal link UP to its money (landing) page.

Output tree (mirrors the deployed web root):
  blog/index.html
  blog/<slug>/index.html   (one per post)

Run order: run _gen_pages.py first, then this. _gen_pages.py rebuilds the FULL
sitemap.xml by globbing blog/ , so the blog URLs are picked up automatically.
"""
import json, os, re

DOMAIN="broadwaynutrition.com"
PIXEL="1026541466453867"
PHONE_DISP="832-827-7133"; PHONE_TEL="+18328277133"
ADDR="3272 E Broadway St, Ste 145"
IG="https://instagram.com/broadwaynutrition.tx"
GH="https://raw.githubusercontent.com/Ronnie-Nutrition/nutritionhub-landing/main"
LOGO=f"https://{DOMAIN}/assets/broadway-nutrition-logo.png"
PUB_DATE="2026-06-20"

# topic palette (matches the 4 money pages)
CY="#23e0ff"; PK="#ff2e88"; VI="#a64dff"; OR="#ff7a18"
GLOW={CY:"rgba(35,224,255,.5)", PK:"rgba(255,46,136,.5)", VI:"rgba(166,77,255,.55)", OR:"rgba(255,122,24,.5)"}

def icard(ic,h,p):
    return f'    <div class="icard"><div class="ic">{ic}</div><h3>{h}</h3><p>{p}</p></div>'

def faq_blocks(faqs):
    jsonld={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a_plain}}
        for (q,a_plain,a_html) in faqs]}
    visible="\n".join(
        f'    <div class="qa">\n      <h3>{q}</h3>\n      <p>{a_html}</p>\n    </div>'
        for (q,a_plain,a_html) in faqs)
    return json.dumps(jsonld,indent=2), visible

def related_html(rel):
    return "\n".join(
        f'    <a class="rcard" href="{url}"><span class="t">{tag}</span><h3>{title}</h3><p>{blurb}</p></a>'
        for (tag,url,title,blurb) in rel)

POSTS=[]

# ============ POST 1: what is in a lit tea (lit teas / cyan) ============
POSTS.append(dict(
 slug="what-is-in-a-lit-tea", acc=CY, kicker="ENERGY TEAS",
 title="What's Actually in a Lit Tea? (Energy Tea Ingredients Explained) | Broadway Nutrition Pearland",
 desc="What's really in a lit tea? The energy tea ingredients explained — clean caffeine, B vitamins, vitamin C, and aloe. A plain-English breakdown from Broadway Nutrition in Pearland, TX.",
 headline="What's Actually in a Lit Tea? (Energy Tea Ingredients Explained)",
 jsonld_desc="A plain-English breakdown of what goes into a loaded energy tea — clean caffeine, B vitamins, vitamin C, and aloe.",
 ogdesc="Clean caffeine, B vitamins, vitamin C and aloe — here's what's really in a 32oz loaded energy tea.",
 ogimg=f"{GH}/tea_dragon_juice.png",
 h1='What\'s Actually in a Lit Tea? <span>(Ingredients Explained)</span>',
 meta_line="The clean energy kick, broken down — no mystery powder",
 body="""  <p>You've seen them all over Pearland — big, brightly colored <strong>lit teas</strong> (a.k.a. loaded teas or energy teas) that everybody's sipping at the gym, in the school pickup line, mid-afternoon at work. They look like candy. So what's actually <em>in</em> one, and where does the energy come from?</p>
  <p>Here's the honest breakdown.</p>
  <h2>The <span>core ingredients</span></h2>
  <div class="ingredients">
""" + "\n".join([
  icard("⚡","Clean caffeine","A smooth caffeine source gives a real lift — enough to wake you up without the jittery crash of a high-stimulant energy drink."),
  icard("🅱️","B vitamins (B6 &amp; B12)","B vitamins support your body's normal energy metabolism — helping you turn food into usable energy."),
  icard("🍊","Vitamin C","An antioxidant boost that rounds out the mix and supports your immune system."),
  icard("🌿","Aloe","Added for a smooth finish — aloe is a common feel-good ingredient in loaded teas."),
 ]) + """
  </div>
  <p>Put it together and you get a <strong>32oz, fruit-flavored iced tea</strong> that's low in calories, loaded with vitamins, and built to give you clean energy that lasts — not a sugar spike that drops you an hour later.</p>
  <h2>Why people pick a lit tea over <span>a soda or energy drink</span></h2>
  <ul>
    <li><strong>Way less sugar</strong> than a soda or a typical canned energy drink.</li>
    <li><strong>Smoother energy</strong> — the B-vitamin + clean-caffeine combo lifts you without the harsh spike-and-crash.</li>
    <li><strong>It actually tastes amazing</strong> — flavors like Dragon Juice, Wonder Woman, and Strawberry Sunrise taste like a treat, not a chore.</li>
    <li><strong>It's huge</strong> — a full 32oz, so it lasts you all afternoon.</li>
  </ul>
  <div class="callout">
    <h3>A note on energy teas</h3>
    <p>Lit teas are a refreshing pick-me-up, not a medical product. Enjoy them for clean energy and great flavor. If you're sensitive to caffeine, just ask us to go lighter — we'll build it to fit you.</p>
  </div>
  <h2>Try one in <span>Pearland</span></h2>
  <p>Curious which flavor is your flavor? See the full lineup on our <a href="/lit-teas-pearland/">lit teas in Pearland</a> page, or text/call <a href="sms:%s" onclick="fbq('track','Lead')">%s</a> to order one ahead and skip the wait. First visit, ask for us when you walk in.</p>""" % (PHONE_TEL, PHONE_DISP),
 faqs=[
  ("What is a lit tea?",
   "A lit tea (also called a loaded or energy tea) is a refreshing, fruit-flavored 32oz iced tea built for energy. It blends a clean caffeine source with B vitamins, vitamin C, and aloe for a smooth lift without the crash. At Broadway Nutrition in Pearland our lit teas come in 20+ flavors like Dragon Juice, Wonder Woman, and Strawberry Sunrise.",
   "A lit tea (also called a loaded or energy tea) is a refreshing, fruit-flavored 32oz iced tea built for energy. It blends a clean caffeine source with B vitamins, vitamin C, and aloe for a smooth lift without the crash. At Broadway Nutrition in Pearland our lit teas come in 20+ flavors like Dragon Juice, Wonder Woman, and Strawberry Sunrise."),
  ("How much caffeine is in an energy tea?",
   "A loaded energy tea typically delivers a moderate caffeine kick — enough for a real energy lift without the jitters of a high-stimulant energy drink. The exact amount depends on the tea base and mix. Ask when you order and we'll tell you what's in yours.",
   "A loaded energy tea typically delivers a moderate caffeine kick — enough for a real energy lift without the jitters of a high-stimulant energy drink. The exact amount depends on the tea base and mix. Ask when you order and we'll tell you what's in yours."),
  ("Are lit teas good for you?",
   "Lit teas are a lighter alternative to sugary sodas and harsh energy drinks — low in calories, with B vitamins, vitamin C, and clean caffeine. They're a popular pick-me-up, not a medical product, so enjoy them as a refreshing energy boost.",
   "Lit teas are a lighter alternative to sugary sodas and harsh energy drinks — low in calories, with B vitamins, vitamin C, and clean caffeine. They're a popular pick-me-up, not a medical product, so enjoy them as a refreshing energy boost."),
 ],
 related=[
  ("ENERGY TEAS","/blog/lit-tea-vs-energy-drink/","Lit Tea vs. Energy Drink: Which Is Better?","Sugar, caffeine, and the crash — an honest side-by-side."),
  ("MENU","/lit-teas-pearland/","Lit Teas in Pearland","32oz loaded teas, 20+ flavors, clean energy, $9.15."),
 ],
 close_h2="Find your <span>flavor.</span>", close_p="Text or call your order ahead and skip the wait — or walk in and ask for us.",
 cta_label="🍵 Text to Order"))

# ============ POST 2: lit tea vs energy drink (lit teas / cyan) ============
POSTS.append(dict(
 slug="lit-tea-vs-energy-drink", acc=CY, kicker="ENERGY TEAS",
 title="Lit Tea vs. Energy Drink: Which Is Better for Clean Energy? | Broadway Nutrition Pearland",
 desc="Lit tea vs. energy drink — which gives better, cleaner energy? An honest side-by-side on caffeine, sugar, calories, and the crash, from Broadway Nutrition in Pearland, TX.",
 headline="Lit Tea vs. Energy Drink: Which Is Better for Clean Energy?",
 jsonld_desc="An honest side-by-side of loaded lit teas and canned energy drinks on caffeine, sugar, calories, and the crash.",
 ogdesc="Caffeine, sugar, calories, and the crash — lit tea vs. canned energy drink, broken down honestly.",
 ogimg=f"{GH}/tea_blue_margarita.png",
 h1='Lit Tea vs. Energy Drink: <span>Which Wins?</span>',
 meta_line="Caffeine, sugar, and the dreaded 3 PM crash",
 body="""  <p>If you need an afternoon lift, you've basically got two popular options in Pearland: grab a canned <strong>energy drink</strong>, or grab a 32oz <strong>lit tea</strong>. They both wake you up — but they're not the same thing. Here's how they really stack up.</p>
  <h2>The <span>side-by-side</span></h2>
  <div class="ingredients">
""" + "\n".join([
  icard("🍬","Sugar","Many canned energy drinks pack a lot of added sugar. Our lit teas are built to be low-calorie and light — no sugar bomb."),
  icard("⚡","Energy curve","Energy drinks can spike you hard and drop you just as fast. A lit tea's clean-caffeine + B-vitamin mix is built for a smoother lift."),
  icard("🥤","Size &amp; sipping","A lit tea is a full 32oz you sip across the afternoon — not a fast 8–16oz hit you slam and regret."),
  icard("🍓","Flavor &amp; freshness","Energy drinks come out of a can. Lit teas are made fresh to order, in 20+ flavors, adjustable to your taste."),
 ]) + """
  </div>
  <h2>So which <span>should you grab?</span></h2>
  <p>If you want a fast, harsh jolt from a can, an energy drink does that. But if you want <strong>clean energy that lasts</strong> — without the sugar crash, in a flavor you actually look forward to — a lit tea wins for most people. It's the same reason our Pearland regulars swapped their afternoon soda or second energy drink for a loaded tea and never looked back.</p>
  <div class="callout">
    <h3>The honest take</h3>
    <p>Both have caffeine, so neither is a free-for-all. If you're caffeine-sensitive, tell us and we'll build your tea lighter. The win for a lit tea is less sugar, a smoother curve, and a drink you'll genuinely enjoy.</p>
  </div>
  <h2>Try one in <span>Pearland</span></h2>
  <p>Pick a flavor on our <a href="/lit-teas-pearland/">lit teas in Pearland</a> page, or text/call <a href="sms:%s" onclick="fbq('track','Lead')">%s</a> to order ahead. First one, ask for us when you walk in.</p>""" % (PHONE_TEL, PHONE_DISP),
 faqs=[
  ("Is a lit tea healthier than an energy drink?",
   "A lit tea is generally a lighter choice — lower in calories and sugar than most canned energy drinks, with B vitamins and vitamin C. Both contain caffeine, so enjoy either in moderation. At Broadway Nutrition we can build your tea lighter if you're caffeine-sensitive.",
   "A lit tea is generally a lighter choice — lower in calories and sugar than most canned energy drinks, with B vitamins and vitamin C. Both contain caffeine, so enjoy either in moderation. At Broadway Nutrition we can build your tea lighter if you're caffeine-sensitive."),
  ("Which gives longer-lasting energy?",
   "Most people get a smoother, longer lift from a lit tea because the clean-caffeine and B-vitamin combo avoids the hard spike-and-crash you often feel from a high-sugar energy drink. A 32oz tea also sips across the whole afternoon.",
   "Most people get a smoother, longer lift from a lit tea because the clean-caffeine and B-vitamin combo avoids the hard spike-and-crash you often feel from a high-sugar energy drink. A 32oz tea also sips across the whole afternoon."),
  ("How much does a lit tea cost in Pearland?",
   "Lit teas at Broadway Nutrition are $9.15 for a 32oz, made fresh to order in 20+ flavors. Text or call 832-827-7133 to order ahead, or walk in at 3272 E Broadway St, Ste 145, Pearland.",
   "Lit teas at Broadway Nutrition are $9.15 for a 32oz, made fresh to order in 20+ flavors. Text or call 832-827-7133 to order ahead, or walk in at 3272 E Broadway St, Ste 145, Pearland."),
 ],
 related=[
  ("ENERGY TEAS","/blog/what-is-in-a-lit-tea/","What's Actually in a Lit Tea?","The B vitamins, vitamin C, aloe, and clean caffeine behind the kick."),
  ("MENU","/lit-teas-pearland/","Lit Teas in Pearland","32oz loaded teas, 20+ flavors, clean energy, $9.15."),
 ],
 close_h2="Ditch the <span>can.</span>", close_p="Text or call your order ahead and skip the wait — or walk in and find your flavor.",
 cta_label="🍵 Text to Order"))

# ============ POST 3: meal replacement smoothies weight loss (pink) ============
POSTS.append(dict(
 slug="meal-replacement-smoothies-weight-loss", acc=PK, kicker="WEIGHT LOSS",
 title="Are Meal Replacement Smoothies Good for Weight Loss? | Broadway Nutrition Pearland",
 desc="Are meal replacement smoothies good for weight loss? How protein-packed smoothies help you stay full on fewer calories — and how to use them right, from Broadway Nutrition in Pearland, TX.",
 headline="Are Meal Replacement Smoothies Good for Weight Loss?",
 jsonld_desc="How protein-packed meal replacement smoothies help you stay full on fewer calories, and how to use them as part of a balanced routine.",
 ogdesc="Stay full on fewer calories — how a protein meal replacement smoothie fits a weight-loss routine.",
 ogimg=f"{GH}/shake_strawberry_cheesecake.png",
 h1='Are Meal Replacement Smoothies <span>Good for Weight Loss?</span>',
 meta_line="The honest answer — and how to actually use them",
 body="""  <p>Short answer: <strong>yes — when you use them right.</strong> A meal replacement smoothie isn't magic, but it's one of the simplest tools for staying full on fewer calories. Here's how it actually works.</p>
  <h2>Why they <span>work</span></h2>
  <div class="ingredients">
""" + "\n".join([
  icard("💪","Protein keeps you full","Our gourmet smoothies pack 24–30g of protein. Protein is the most filling macronutrient, so you stay satisfied longer and snack less."),
  icard("🔥","Fewer calories than fast food","Swapping a 700–1,000 calorie drive-thru meal for a balanced protein smoothie is an easy calorie win — without feeling deprived."),
  icard("⏱️","Convenient = consistent","The #1 reason diets fail is they're a hassle. A grab-and-go smoothie makes the healthy choice the easy choice."),
  icard("🍰","It tastes like dessert","Banana Pudding, Strawberry Cheesecake, Cocoa Puffs — when 'on plan' tastes this good, you stick with it."),
 ]) + """
  </div>
  <h2>How to use one for <span>weight goals</span></h2>
  <ul>
    <li><strong>Swap, don't add.</strong> Replace a meal or a high-calorie snack with the smoothie — don't drink it on top of everything else.</li>
    <li><strong>Lean on the protein.</strong> 24–30g keeps you full into the next meal so you're not raiding the pantry by 3 PM.</li>
    <li><strong>Pair it with your day.</strong> A smoothie is a tool, not the whole plan. Keep the rest of your meals reasonable and stay moving.</li>
    <li><strong>Be consistent.</strong> Results come from doing it most days, not perfectly for three days.</li>
  </ul>
  <div class="callout">
    <h3>The honest take</h3>
    <p>A meal replacement smoothie is a convenient, filling, lower-calorie swap — not a medical weight-loss product. It works because it makes eating fewer calories easier and tastier. Pair it with a balanced routine and you've got a real, sustainable tool.</p>
  </div>
  <h2>Try one in <span>Pearland</span></h2>
  <p>See the gourmet lineup on our <a href="/weight-loss-smoothies-pearland/">meal-replacement smoothies in Pearland</a> page, or text/call <a href="sms:%s" onclick="fbq('track','Lead')">%s</a> to order ahead. Tell us your goal and we'll point you to the right one.</p>""" % (PHONE_TEL, PHONE_DISP),
 faqs=[
  ("Are meal replacement smoothies good for weight loss?",
   "They can be a great tool. A protein-packed meal replacement smoothie helps you stay full on fewer calories than a typical meal or fast food. At Broadway Nutrition in Pearland our gourmet smoothies have 24–30g of protein. Swap one in for a meal or snack and pair it with a balanced routine for best results.",
   "They can be a great tool. A protein-packed meal replacement smoothie helps you stay full on fewer calories than a typical meal or fast food. At Broadway Nutrition in Pearland our gourmet smoothies have 24–30g of protein. Swap one in for a meal or snack and pair it with a balanced routine for best results."),
  ("How often should I drink one for weight loss?",
   "Most people swap one meal or one high-calorie snack a day for a smoothie. The key is using it to replace calories, not add them, and staying consistent. Tell us your goal and we'll help you build a routine that fits.",
   "Most people swap one meal or one high-calorie snack a day for a smoothie. The key is using it to replace calories, not add them, and staying consistent. Tell us your goal and we'll help you build a routine that fits."),
  ("How much do the smoothies cost in Pearland?",
   "Gourmet smoothies are $9.97 and 20oz protein smoothies are $7.80 at Broadway Nutrition. Text or call 832-827-7133 to order ahead, or walk in at 3272 E Broadway St, Ste 145, Pearland.",
   "Gourmet smoothies are $9.97 and 20oz protein smoothies are $7.80 at Broadway Nutrition. Text or call 832-827-7133 to order ahead, or walk in at 3272 E Broadway St, Ste 145, Pearland."),
 ],
 related=[
  ("WEIGHT LOSS","/blog/how-much-protein-meal-replacement-smoothie/","How Much Protein Should a Meal Replacement Smoothie Have?","The number that matters more than calories alone."),
  ("MENU","/weight-loss-smoothies-pearland/","Meal Replacement Smoothies in Pearland","24–30g protein, lower calorie, tastes like dessert. $9.97."),
 ],
 close_h2="Hit your goals <span>without the bland.</span>", close_p="Text or call your order ahead and skip the wait — or walk in and let us build it fresh.",
 cta_label="🥤 Text to Order"))

# ============ POST 4: how much protein meal replacement (pink) ============
POSTS.append(dict(
 slug="how-much-protein-meal-replacement-smoothie", acc=PK, kicker="WEIGHT LOSS",
 title="How Much Protein Should a Meal Replacement Smoothie Have? | Broadway Nutrition Pearland",
 desc="How much protein should a meal replacement smoothie have? The sweet spot for staying full and losing weight — explained simply by Broadway Nutrition in Pearland, TX.",
 headline="How Much Protein Should a Meal Replacement Smoothie Have?",
 jsonld_desc="The protein sweet spot for a meal replacement smoothie that actually keeps you full, explained in plain English.",
 ogdesc="The protein sweet spot for a meal replacement smoothie that actually keeps you full.",
 ogimg=f"{GH}/shake_banana_pudding.png",
 h1='How Much Protein Should a <span>Meal Replacement Smoothie</span> Have?',
 meta_line="The number that matters more than calories alone",
 body="""  <p>If a smoothie is going to stand in for a meal, the protein number is the part that makes or breaks it. Too little and you're hungry in an hour. Here's the sweet spot.</p>
  <h2>The <span>target: 20–30g</span></h2>
  <p>For a meal replacement, aim for roughly <strong>20–30g of protein</strong>. That's enough to trigger real fullness and protect muscle while you're eating fewer calories. Our gourmet smoothies at Broadway Nutrition land right in that range at <strong>24–30g</strong>, and our 20oz protein smoothies hit 24g at around 190 calories.</p>
  <div class="ingredients">
""" + "\n".join([
  icard("💪","Why protein matters most","Protein is the most filling macro and helps preserve muscle in a calorie deficit. It's the number to check first — before calories."),
  icard("🎯","20–30g per serving","Below ~20g and most people get hungry fast. 24–30g keeps you satisfied into the next meal."),
  icard("🔢","Calories matter too","A meal replacement should generally be lower-calorie than the meal it replaces — high protein, controlled calories is the combo."),
  icard("🥤","Real, not chalky","High protein only helps if you actually drink it. Ours taste like dessert, so finishing it is never a chore."),
 ]) + """
  </div>
  <h2>Protein <span>vs. calories</span></h2>
  <p>People obsess over calories, but protein is what makes a lower-calorie day <em>sustainable</em>. A 250-calorie smoothie with 8g of protein leaves you hungry; a 250–300 calorie smoothie with 24–30g of protein keeps you full for hours. Same calories, completely different result. That's why we build ours protein-first.</p>
  <div class="callout">
    <h3>Quick rule of thumb</h3>
    <p>For a meal replacement: <strong>20–30g protein</strong>, and fewer calories than the meal you're swapping out. Hit those two and you've got a smoothie that actually supports your goal.</p>
  </div>
  <h2>Try one in <span>Pearland</span></h2>
  <p>See the protein lineup on our <a href="/weight-loss-smoothies-pearland/">meal-replacement smoothies in Pearland</a> page, or text/call <a href="sms:%s" onclick="fbq('track','Lead')">%s</a> to order ahead.</p>""" % (PHONE_TEL, PHONE_DISP),
 faqs=[
  ("How much protein should a meal replacement smoothie have?",
   "Aim for about 20–30g of protein in a meal replacement smoothie — enough to keep you full and protect muscle while eating fewer calories. Broadway Nutrition's gourmet smoothies have 24–30g, and our 20oz protein smoothies have 24g at around 190 calories.",
   "Aim for about 20–30g of protein in a meal replacement smoothie — enough to keep you full and protect muscle while eating fewer calories. Broadway Nutrition's gourmet smoothies have 24–30g, and our 20oz protein smoothies have 24g at around 190 calories."),
  ("Is more protein always better?",
   "Not necessarily. For a meal replacement, 20–30g hits the fullness sweet spot for most people. Far more than that doesn't add much benefit for a single drink. What matters is hitting that range consistently across your day.",
   "Not necessarily. For a meal replacement, 20–30g hits the fullness sweet spot for most people. Far more than that doesn't add much benefit for a single drink. What matters is hitting that range consistently across your day."),
  ("How many calories are in a Broadway Nutrition smoothie?",
   "Our 20oz protein smoothies run around 190 calories with 24g of protein. Gourmet smoothies are a bit higher with 24–30g of protein. Ask at the counter and we'll match one to your goal.",
   "Our 20oz protein smoothies run around 190 calories with 24g of protein. Gourmet smoothies are a bit higher with 24–30g of protein. Ask at the counter and we'll match one to your goal."),
 ],
 related=[
  ("WEIGHT LOSS","/blog/meal-replacement-smoothies-weight-loss/","Are Meal Replacement Smoothies Good for Weight Loss?","The honest answer — and how to actually use them."),
  ("MENU","/weight-loss-smoothies-pearland/","Meal Replacement Smoothies in Pearland","24–30g protein, lower calorie, tastes like dessert. $9.97."),
 ],
 close_h2="Protein-packed <span>and craveable.</span>", close_p="Text or call your order ahead and skip the wait — or walk in and ask what's fresh.",
 cta_label="🥤 Text to Order"))

# ============ POST 5: what is protein coffee (violet) ============
POSTS.append(dict(
 slug="what-is-protein-coffee", acc=VI, kicker="PROTEIN COFFEE",
 title="What Is Protein Coffee? (And Why It Beats Your Regular Cup) | Broadway Nutrition Pearland",
 desc="What is protein coffee? Real coffee blended with protein and low sugar for a morning lift that keeps you full. Explained by Broadway Nutrition in Pearland, TX.",
 headline="What Is Protein Coffee? (And Why It Beats Your Regular Cup)",
 jsonld_desc="What protein coffee is, how much protein and sugar it has, and why it keeps you fuller than a regular cup.",
 ogdesc="Real coffee + protein + low sugar — the morning cup that keeps you full instead of crashing you.",
 ogimg=f"{GH}/shake_chocolate.png",
 h1='What Is <span>Protein Coffee?</span>',
 meta_line="The morning upgrade that actually keeps you full",
 body="""  <p>You love your coffee. But a regular cup — especially a sweet café drink — gives you caffeine and a sugar spike, then drops you at 10 AM. <strong>Protein coffee</strong> fixes that. Here's what it is and why people are switching.</p>
  <h2>The <span>basics</span></h2>
  <div class="ingredients">
""" + "\n".join([
  icard("☕","Real coffee + protein","It's exactly what it sounds like — real coffee blended with protein. At Broadway Nutrition that's 15–30g of protein per cup, in House or Mocha."),
  icard("🍬","Low sugar","Unlike a sugary café latte, protein coffee keeps the sugar low — so you skip the spike and the crash."),
  icard("🕙","Keeps you full","The protein turns your morning caffeine into actual fuel, so you're not starving (or snacking) an hour later."),
  icard("🔥","Cold or hot","Have it cold, or warm as a 24g-protein hot latte. Same idea, your way."),
 ]) + """
  </div>
  <h2>Why it <span>beats a regular cup</span></h2>
  <ul>
    <li><strong>Caffeine with a job.</strong> You still get the lift — but now it comes with protein to keep you satisfied.</li>
    <li><strong>No sugar bomb.</strong> A sweet café drink can hide a ton of sugar. Protein coffee keeps it low.</li>
    <li><strong>Breakfast in a cup.</strong> Pair it with a protein waffle and you've got a real morning, not just a caffeine hit.</li>
  </ul>
  <div class="callout">
    <h3>The honest take</h3>
    <p>Protein coffee isn't a miracle — it's a smarter version of something you already drink every day. Same caffeine you love, plus protein and less sugar. That's the whole pitch, and it's a good one.</p>
  </div>
  <h2>Try one in <span>Pearland</span></h2>
  <p>See House and Mocha on our <a href="/protein-coffee-pearland/">protein coffee in Pearland</a> page, or text/call <a href="sms:%s" onclick="fbq('track','Lead')">%s</a> to order ahead on your way in.</p>""" % (PHONE_TEL, PHONE_DISP),
 faqs=[
  ("What is protein coffee?",
   "Protein coffee is real coffee blended with protein and low sugar — the upgrade to your morning cup. At Broadway Nutrition in Pearland it comes in House and Mocha with 15–30g of protein, served cold or as a warm hot latte.",
   "Protein coffee is real coffee blended with protein and low sugar — the upgrade to your morning cup. At Broadway Nutrition in Pearland it comes in House and Mocha with 15–30g of protein, served cold or as a warm hot latte."),
  ("How much protein and sugar is in it?",
   "Our protein coffee delivers 15–30g of protein with low sugar, so you get the caffeine lift plus protein to start your day without a sugar spike.",
   "Our protein coffee delivers 15–30g of protein with low sugar, so you get the caffeine lift plus protein to start your day without a sugar spike."),
  ("How much does protein coffee cost in Pearland?",
   "Protein coffee is $4.28 at Broadway Nutrition. Prefer it warm? Our hot lattes with 24g protein are $6.41. Text or call 832-827-7133 to order ahead, or walk in at 3272 E Broadway St, Ste 145, Pearland.",
   "Protein coffee is $4.28 at Broadway Nutrition. Prefer it warm? Our hot lattes with 24g protein are $6.41. Text or call 832-827-7133 to order ahead, or walk in at 3272 E Broadway St, Ste 145, Pearland."),
 ],
 related=[
  ("PROTEIN COFFEE","/blog/protein-coffee-vs-regular-coffee/","Protein Coffee vs. Regular Coffee: Is It Worth It?","An honest look at whether the upgrade is worth it."),
  ("MENU","/protein-coffee-pearland/","Protein Coffee in Pearland","15–30g protein, low sugar, House or Mocha. $4.28."),
 ],
 close_h2="Upgrade <span>your morning cup.</span>", close_p="Text or call your order ahead and skip the wait — or walk in and ask what's brewing.",
 cta_label="☕ Text to Order"))

# ============ POST 6: protein coffee vs regular coffee (violet) ============
POSTS.append(dict(
 slug="protein-coffee-vs-regular-coffee", acc=VI, kicker="PROTEIN COFFEE",
 title="Protein Coffee vs. Regular Coffee: Is It Worth It? | Broadway Nutrition Pearland",
 desc="Protein coffee vs. regular coffee — is the upgrade worth it? Fullness, sugar, and energy compared honestly by Broadway Nutrition in Pearland, TX.",
 headline="Protein Coffee vs. Regular Coffee: Is It Worth It?",
 jsonld_desc="An honest comparison of protein coffee and a regular cup on fullness, sugar, energy, and value.",
 ogdesc="Fullness, sugar, and energy — is protein coffee actually worth it over your regular cup?",
 ogimg=f"{GH}/shake_chocolate.png",
 h1='Protein Coffee vs. <span>Regular Coffee</span>',
 meta_line="Is the upgrade actually worth it?",
 body="""  <p>Plain black coffee is cheap and does the job. So is <strong>protein coffee</strong> actually worth it? It depends what you want out of your morning. Here's the honest comparison.</p>
  <h2>Where they're <span>the same</span></h2>
  <p>Both give you caffeine. If all you want is a quick lift and you eat a solid breakfast anyway, plain coffee is perfectly fine. No one's saying you need to fix what isn't broken.</p>
  <h2>Where protein coffee <span>pulls ahead</span></h2>
  <div class="ingredients">
""" + "\n".join([
  icard("💪","It keeps you full","Plain coffee does nothing for hunger — a lot of people crash or get hungry mid-morning. The 15–30g of protein turns your cup into fuel."),
  icard("🍳","It can replace breakfast","Skipping breakfast or grabbing a pastry? Protein coffee gives you protein in the same cup, so you start the day fueled."),
  icard("🍬","Less sugar than a café drink","If your 'regular coffee' is really a sweet café latte, you're drinking a lot of sugar. Protein coffee keeps it low."),
  icard("😌","Steadier energy","Protein alongside caffeine helps you avoid the sugar spike-and-crash of a sweetened drink."),
 ]) + """
  </div>
  <h2>The <span>verdict</span></h2>
  <p>If you drink black coffee and eat a real breakfast, you don't <em>need</em> protein coffee. But if you skip breakfast, grab something sugary, or crash by mid-morning — protein coffee is absolutely worth it. You're already buying a coffee; for about <strong>$4.28</strong> you get one that actually holds you over. That's an easy upgrade.</p>
  <div class="callout">
    <h3>Bottom line</h3>
    <p>Same caffeine, plus protein and less sugar. If your mornings tend to crash or you skip breakfast, the upgrade pays for itself in how you feel by 10 AM.</p>
  </div>
  <h2>Try one in <span>Pearland</span></h2>
  <p>See House and Mocha on our <a href="/protein-coffee-pearland/">protein coffee in Pearland</a> page, or text/call <a href="sms:%s" onclick="fbq('track','Lead')">%s</a> to order ahead.</p>""" % (PHONE_TEL, PHONE_DISP),
 faqs=[
  ("Is protein coffee better than regular coffee?",
   "It depends on your goal. For caffeine alone, regular coffee is fine. But if you want to stay full, replace a skipped breakfast, or cut the sugar of a café drink, protein coffee is the better choice — it adds 15–30g of protein with low sugar to the same cup.",
   "It depends on your goal. For caffeine alone, regular coffee is fine. But if you want to stay full, replace a skipped breakfast, or cut the sugar of a café drink, protein coffee is the better choice — it adds 15–30g of protein with low sugar to the same cup."),
  ("Does protein coffee taste different from regular coffee?",
   "It's smooth and creamy with the same coffee flavor you expect, plus options like Mocha. Most people find it tastes like a slightly richer latte — not chalky. Try the House or Mocha and see which you like.",
   "It's smooth and creamy with the same coffee flavor you expect, plus options like Mocha. Most people find it tastes like a slightly richer latte — not chalky. Try the House or Mocha and see which you like."),
  ("Is protein coffee worth the price?",
   "At $4.28 it's priced like a regular café coffee but does more — protein to keep you full and low sugar. If your mornings tend to crash or you skip breakfast, most people find it well worth it.",
   "At $4.28 it's priced like a regular café coffee but does more — protein to keep you full and low sugar. If your mornings tend to crash or you skip breakfast, most people find it well worth it."),
 ],
 related=[
  ("PROTEIN COFFEE","/blog/what-is-protein-coffee/","What Is Protein Coffee?","Real coffee + protein + low sugar — the morning upgrade explained."),
  ("MENU","/protein-coffee-pearland/","Protein Coffee in Pearland","15–30g protein, low sugar, House or Mocha. $4.28."),
 ],
 close_h2="Make your coffee <span>do more.</span>", close_p="Text or call your order ahead and skip the wait — or walk in and ask what's brewing.",
 cta_label="☕ Text to Order"))

# ============ POST 7: best post workout shake (orange) ============
POSTS.append(dict(
 slug="best-post-workout-shake", acc=OR, kicker="RECOVERY",
 title="Best Post-Workout Shake for Recovery: What to Look For | Broadway Nutrition Pearland",
 desc="What makes the best post-workout shake? Protein, timing, and the recovery boosters that actually matter — a straight-talk guide from Broadway Nutrition in Pearland, TX.",
 headline="Best Post-Workout Shake for Recovery: What to Look For",
 jsonld_desc="What to look for in a post-workout shake — protein amount, timing, and recovery add-ins that actually matter.",
 ogdesc="Protein, timing, and the recovery boosters that actually matter in a post-workout shake.",
 ogimg=f"{GH}/shake_choc2.png",
 h1='The Best <span>Post-Workout Shake:</span> What to Look For',
 meta_line="Protein, timing, and the boosters that actually matter",
 body="""  <p>You just put in the work. The shake afterward is where recovery starts — but only if it's built right. Here's what actually matters in a post-workout shake, and what's just hype.</p>
  <h2>What to <span>look for</span></h2>
  <div class="ingredients">
""" + "\n".join([
  icard("💪","20–30g of protein","This is the big one. Protein gives your muscles what they need to repair and rebuild. Our shakes deliver 24–30g — right in the recovery sweet spot."),
  icard("⏱️","Timing within a couple hours","You don't need to slam it in 30 seconds, but getting protein in within a couple hours of training supports recovery. A grab-on-your-way-out shake makes that easy."),
  icard("➕","Smart add-ins","Collagen, a B6/B12 energy boost, or aloe can round out your shake. Useful extras — not magic, but a nice edge."),
  icard("🍨","Something you'll actually drink","The best shake is the one you finish. Ours taste like Brownie Batter and Blue Banana — recovery that feels like a treat."),
 ]) + """
  </div>
  <h2>What <span>doesn't</span> matter as much</h2>
  <ul>
    <li><strong>The 'anabolic window' panic.</strong> You don't have to drink it the second you rack the weights. Within a couple hours is fine for most people.</li>
    <li><strong>Mega-doses of protein.</strong> 24–30g per shake covers it. You don't need 60g in one cup.</li>
    <li><strong>Fancy mystery blends.</strong> Solid protein, a flavor you like, and consistency beat a long, confusing ingredient list.</li>
  </ul>
  <div class="callout">
    <h3>The simple formula</h3>
    <p>24–30g of protein, within a couple hours of training, in a flavor you'll actually finish. Add a booster if you want. That's a great post-workout shake — no hype required.</p>
  </div>
  <h2>Try one in <span>Pearland</span></h2>
  <p>See the lineup on our <a href="/protein-shakes-pearland/">protein shakes in Pearland</a> page, or text/call <a href="sms:%s" onclick="fbq('track','Lead')">%s</a> to order ahead and grab it on your way out of the gym.</p>""" % (PHONE_TEL, PHONE_DISP),
 faqs=[
  ("What makes the best post-workout shake?",
   "Look for 20–30g of protein, consumed within a couple hours of training, in a flavor you'll actually finish. Optional boosters like collagen or a B6/B12 add-in can help. Broadway Nutrition's protein shakes deliver 24–30g and taste like dessert.",
   "Look for 20–30g of protein, consumed within a couple hours of training, in a flavor you'll actually finish. Optional boosters like collagen or a B6/B12 add-in can help. Broadway Nutrition's protein shakes deliver 24–30g and taste like dessert."),
  ("How soon after a workout should I drink a protein shake?",
   "Getting protein in within a couple hours of training supports recovery for most people — you don't need to rush it down the second you finish. A grab-and-go shake makes hitting that window easy.",
   "Getting protein in within a couple hours of training supports recovery for most people — you don't need to rush it down the second you finish. A grab-and-go shake makes hitting that window easy."),
  ("How much do protein shakes cost in Pearland?",
   "20oz protein shakes are $7.80 and gourmet shakes are $9.97 at Broadway Nutrition. Add collagen or a B6/B12 energy boost if you want extra. Text or call 832-827-7133 to order ahead, or walk in at 3272 E Broadway St, Ste 145, Pearland.",
   "20oz protein shakes are $7.80 and gourmet shakes are $9.97 at Broadway Nutrition. Add collagen or a B6/B12 energy boost if you want extra. Text or call 832-827-7133 to order ahead, or walk in at 3272 E Broadway St, Ste 145, Pearland."),
 ],
 related=[
  ("RECOVERY","/blog/how-much-protein-after-workout/","How Much Protein Do You Need After a Workout?","The real number — and why more isn't always better."),
  ("MENU","/protein-shakes-pearland/","Protein Shakes in Pearland","24–30g protein, made fresh, tastes like dessert. From $7.80."),
 ],
 close_h2="Refuel <span>the right way.</span>", close_p="Text or call your order ahead and skip the wait — or walk in straight from the gym.",
 cta_label="🥤 Text to Order"))

# ============ POST 8: how much protein after workout (orange) ============
POSTS.append(dict(
 slug="how-much-protein-after-workout", acc=OR, kicker="RECOVERY",
 title="How Much Protein Do You Need After a Workout? | Broadway Nutrition Pearland",
 desc="How much protein do you need after a workout? The real number for recovery — and why more isn't always better. Straight talk from Broadway Nutrition in Pearland, TX.",
 headline="How Much Protein Do You Need After a Workout?",
 jsonld_desc="The real post-workout protein target for recovery, and why drinking far more than that doesn't help.",
 ogdesc="The real post-workout protein number — and why more isn't always better.",
 ogimg=f"{GH}/shake_blue.png",
 h1='How Much Protein <span>After a Workout?</span>',
 meta_line="The real number — and why more isn't always better",
 body="""  <p>It's the most-asked gym question: how much protein should I get after training? The answer is simpler than the supplement aisle makes it look.</p>
  <h2>The <span>target: 20–40g</span></h2>
  <p>For most people, <strong>20–40g of protein</strong> after a workout covers recovery. A common sweet spot is right around <strong>20–30g</strong> — which is exactly what our protein shakes deliver at 24–30g. That's enough to give your muscles what they need to repair and rebuild.</p>
  <div class="ingredients">
""" + "\n".join([
  icard("🎯","20–40g is the range","Most research points to roughly 20–40g post-workout. Going much higher in one sitting doesn't add much more benefit."),
  icard("⚖️","Body size plays a role","Bigger, more muscular athletes sit toward the higher end. If that's you, lean to 30–40g."),
  icard("📅","Daily total matters most","One post-workout shake is great, but your total protein across the whole day is what really drives results."),
  icard("🥤","Easy to hit with a shake","A 24–30g shake hits the target in one cup — no math, no guessing, no chalky aftertaste."),
 ]) + """
  </div>
  <h2>Why <span>more isn't better</span></h2>
  <p>Slamming 60–80g in one shake won't double your gains — your body can only use so much at once, and the rest is just expensive. You're better off hitting <strong>20–30g now</strong> and getting more protein across your other meals than overloading a single drink.</p>
  <div class="callout">
    <h3>Quick rule of thumb</h3>
    <p>Aim for <strong>20–30g after training</strong> (up to 40g if you're bigger), then keep hitting protein at your other meals. Consistency across the day beats one giant shake.</p>
  </div>
  <h2>Try one in <span>Pearland</span></h2>
  <p>Our shakes land right in that range. See the lineup on our <a href="/protein-shakes-pearland/">protein shakes in Pearland</a> page, or text/call <a href="sms:%s" onclick="fbq('track','Lead')">%s</a> to order ahead.</p>""" % (PHONE_TEL, PHONE_DISP),
 faqs=[
  ("How much protein do you need after a workout?",
   "For most people, 20–40g of protein after a workout supports recovery, with 20–30g being a common sweet spot. Broadway Nutrition's protein shakes deliver 24–30g — right in that range. Your total protein across the day matters most of all.",
   "For most people, 20–40g of protein after a workout supports recovery, with 20–30g being a common sweet spot. Broadway Nutrition's protein shakes deliver 24–30g — right in that range. Your total protein across the day matters most of all."),
  ("Is more protein after a workout better?",
   "Not really. Your body can only use so much protein at once, so 20–40g covers it for most people. Megadosing 60–80g in one shake doesn't add much benefit — spreading protein across your meals works better.",
   "Not really. Your body can only use so much protein at once, so 20–40g covers it for most people. Megadosing 60–80g in one shake doesn't add much benefit — spreading protein across your meals works better."),
  ("How much protein is in a Broadway Nutrition shake?",
   "Our 20oz protein shakes have 24g of protein at around 190 calories, and our gourmet shakes pack 24–30g. That puts a single shake right in the recommended post-workout range. Text or call 832-827-7133 to order ahead.",
   "Our 20oz protein shakes have 24g of protein at around 190 calories, and our gourmet shakes pack 24–30g. That puts a single shake right in the recommended post-workout range. Text or call 832-827-7133 to order ahead."),
 ],
 related=[
  ("RECOVERY","/blog/best-post-workout-shake/","Best Post-Workout Shake: What to Look For","Protein, timing, and the boosters that actually matter."),
  ("MENU","/protein-shakes-pearland/","Protein Shakes in Pearland","24–30g protein, made fresh, tastes like dessert. From $7.80."),
 ],
 close_h2="Hit your number <span>the easy way.</span>", close_p="Text or call your order ahead and skip the wait — or walk in straight from the gym.",
 cta_label="🥤 Text to Order"))

# ---------------- shared CSS ----------------
CSS = r""":root{--bg:#0a0610;--card:#16101f;--line:#2a1f36;--acc:__ACC__;--accGlow:__ACCGLOW__;--pink:#ff2e88;--txt:#f1ecf6;--mut:#a99cb8;--font:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;}
  *{margin:0;padding:0;box-sizing:border-box}html{scroll-behavior:smooth}
  body{background:var(--bg);color:var(--txt);font-family:var(--font);overflow-x:hidden;line-height:1.5}
  a{color:inherit;text-decoration:none}.wrap{max-width:1080px;margin:0 auto;padding:0 22px}.narrow{max-width:760px}
  .nav{position:sticky;top:0;z-index:50;background:rgba(10,6,16,.85);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
  .nav .row{display:flex;align-items:center;justify-content:space-between;padding:12px 0}.brand{font-weight:900;letter-spacing:.5px;font-size:18px}.brand span{color:var(--acc)}
  .btn{cursor:pointer;display:inline-block;border:none;font-family:var(--font);font-weight:900;letter-spacing:.5px;border-radius:40px;transition:.18s;font-size:14px}
  .btn-acc{background:var(--acc);color:#0a0610;padding:14px 26px;box-shadow:0 0 24px var(--accGlow)}.btn-acc:hover{transform:translateY(-2px)}
  .nav .btn{padding:9px 18px;font-size:13px}
  .ahead{padding:54px 0 8px;text-align:center;position:relative;overflow:hidden}
  .ahead::before{content:"";position:absolute;inset:0;background:radial-gradient(600px 300px at 20% 0%,var(--accGlow),transparent 62%),radial-gradient(700px 360px at 85% 10%,rgba(255,46,136,.12),transparent 60%)}
  .kicker{position:relative;display:inline-block;color:var(--acc);font-size:12px;font-weight:900;letter-spacing:2px;margin-bottom:16px}
  .ahead h1{position:relative;font-size:clamp(28px,5vw,46px);line-height:1.1;font-weight:900;letter-spacing:-1px;max-width:840px;margin:0 auto}.ahead h1 span{color:var(--acc)}
  .meta{position:relative;color:var(--mut);font-size:13px;margin-top:18px}
  .article{margin:30px auto 0;font-size:17px;line-height:1.8;color:#d6cee0}
  .article h2{color:var(--txt);font-size:clamp(22px,3.6vw,30px);font-weight:900;letter-spacing:-.5px;margin:38px 0 12px}.article h2 span{color:var(--acc)}
  .article p{margin-bottom:18px}.article strong{color:var(--acc)}.article em{color:var(--txt)}.article a{color:var(--pink);text-decoration:underline;text-underline-offset:3px}
  .article ul{margin:0 0 18px 20px}.article li{margin-bottom:10px}
  .ingredients{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin:26px 0}
  .icard{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:20px}
  .icard .ic{font-size:26px;margin-bottom:8px}.icard h3{font-size:16px;font-weight:900;margin-bottom:6px;color:var(--txt)}.icard p{color:var(--mut);font-size:14px;margin-bottom:0}
  .callout{background:var(--card);border:1px solid var(--line);border-left:3px solid var(--acc);border-radius:14px;padding:22px 24px;margin:28px 0}
  .callout h3{font-size:18px;font-weight:900;margin-bottom:8px}.callout p{margin-bottom:0;color:var(--mut);font-size:15px}
  .faq{margin:14px 0 0}
  .qa{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:20px 22px;margin-bottom:14px}
  .qa h3{font-size:16px;font-weight:900;margin-bottom:8px;color:var(--txt)}.qa p{color:var(--mut);font-size:14px;line-height:1.7;margin-bottom:0}.qa a{color:var(--acc);text-decoration:underline}
  .related{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:14px 0 0}
  .rcard{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:20px;transition:.2s}.rcard:hover{transform:translateY(-3px);border-color:var(--acc)}
  .rcard .t{font-size:11px;font-weight:900;letter-spacing:1.4px;color:var(--acc);margin-bottom:8px;display:block}.rcard h3{font-size:17px;font-weight:900}.rcard p{color:var(--mut);font-size:13px;margin-top:6px;margin-bottom:0}
  .close{text-align:center;padding:56px 0 36px;border-top:1px solid var(--line);margin-top:44px}.close h2{font-size:clamp(26px,4.4vw,40px);font-weight:900;letter-spacing:-.5px}.close h2 span{color:var(--acc)}
  .close p{color:var(--mut);max-width:480px;margin:14px auto 26px;font-size:15px}
  .footer{text-align:center;color:#6a5d78;font-size:12px;padding:26px 0;border-top:1px solid var(--line)}.footer a{color:var(--mut)}.crumb{font-size:13px;color:var(--mut);padding-top:18px}.crumb a{color:var(--acc)}
  @media(max-width:780px){.related,.ingredients{grid-template-columns:1fr}}"""

PIXEL_JS = """<script>
!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,
document,'script','https://connect.facebook.net/en_US/fbevents.js');
fbq('init','__PIXEL__');fbq('track','PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=__PIXEL__&ev=PageView&noscript=1"/></noscript>""".replace("__PIXEL__",PIXEL)

NAV = f"""<nav class="nav"><div class="wrap row">
  <a class="brand" href="/">BROADWAY <span>NUTRITION</span></a>
  <a class="btn btn-acc" href="sms:{PHONE_TEL}" onclick="fbq('track','Lead')">Text to Order</a>
</div></nav>"""

FOOTER = f"""<div class="footer"><div class="wrap">
  <div class="crumb"><a href="/blog/">← All posts</a> &nbsp;·&nbsp; <a href="/">Broadway Nutrition home</a></div>
  © 2026 Broadway Nutrition · {ADDR}, Pearland, TX ·
  <a href="{IG}" target="_blank">@broadwaynutrition.tx</a>
</div></div>"""

# ---------------- POST template ----------------
TPL_POST = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__</title>
<meta name="description" content="__DESC__">
<link rel="canonical" href="https://__DOMAIN__/blog/__SLUG__/">
<meta property="og:type" content="article">
<meta property="og:title" content="__OGTITLE__">
<meta property="og:description" content="__OGDESC__">
<meta property="og:url" content="https://__DOMAIN__/blog/__SLUG__/">
<meta property="og:image" content="__OGIMG__">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="__OGTITLE__">
<meta name="twitter:description" content="__OGDESC__">
<script type="application/ld+json">
__POST_JSONLD__
</script>
<script type="application/ld+json">
__FAQ_JSONLD__
</script>
__PIXEL_JS__
<style>
__CSS__
</style>
</head>
<body>
__NAV__
<header class="ahead"><div class="wrap narrow">
  <span class="kicker">__KICKER__ · PEARLAND, TX</span>
  <h1>__H1__</h1>
  <div class="meta">__META_LINE__</div>
</div></header>
<article class="wrap narrow article">
__BODY__
  <h2>Common <span>questions</span></h2>
  <div class="faq">
__FAQ_HTML__
  </div>
  <h2>Keep <span>reading</span></h2>
  <div class="related">
__RELATED__
  </div>
</article>
<div class="close"><div class="wrap">
  <h2>__CLOSE_H2__</h2>
  <p>__CLOSE_P__</p>
  <a class="btn btn-acc" href="sms:__PHONE_TEL__" onclick="fbq('track','Lead')">__CTA_LABEL__</a>
</div></div>
__FOOTER__
</body>
</html>
"""

def post_jsonld(p):
    d={"@context":"https://schema.org","@type":"BlogPosting","headline":p["headline"],
       "description":p["jsonld_desc"],"image":p["ogimg"],"datePublished":PUB_DATE,"dateModified":PUB_DATE,
       "author":{"@type":"Organization","name":"Broadway Nutrition"},
       "publisher":{"@type":"Organization","name":"Broadway Nutrition","logo":{"@type":"ImageObject","url":LOGO}},
       "mainEntityOfPage":{"@type":"WebPage","@id":f"https://{DOMAIN}/blog/{p['slug']}/"}}
    return json.dumps(d,indent=2)

outdir=os.path.dirname(os.path.abspath(__file__))
blogdir=os.path.join(outdir,"blog")
os.makedirs(blogdir,exist_ok=True)

for p in POSTS:
    faq_json, faq_vis = faq_blocks(p["faqs"])
    html=TPL_POST
    rep={
      "__TITLE__":p["title"],"__DESC__":p["desc"],"__DOMAIN__":DOMAIN,"__SLUG__":p["slug"],
      "__OGTITLE__":p["headline"],"__OGDESC__":p["ogdesc"],"__OGIMG__":p["ogimg"],
      "__POST_JSONLD__":post_jsonld(p),"__FAQ_JSONLD__":faq_json,"__PIXEL_JS__":PIXEL_JS,
      "__CSS__":CSS.replace("__ACC__",p["acc"]).replace("__ACCGLOW__",GLOW[p["acc"]]),
      "__NAV__":NAV,"__KICKER__":p["kicker"],"__H1__":p["h1"],"__META_LINE__":p["meta_line"],
      "__BODY__":p["body"],"__FAQ_HTML__":faq_vis,"__RELATED__":related_html(p["related"]),
      "__CLOSE_H2__":p["close_h2"],"__CLOSE_P__":p["close_p"],"__PHONE_TEL__":PHONE_TEL,
      "__CTA_LABEL__":p["cta_label"],"__FOOTER__":FOOTER,
    }
    for k,v in rep.items(): html=html.replace(k,v)
    left=set(re.findall(r"__[A-Z0-9_]+__",html))
    assert not left, f"{p['slug']}: leftover tokens {left}"
    d=os.path.join(blogdir,p["slug"]); os.makedirs(d,exist_ok=True)
    open(os.path.join(d,"index.html"),"w",encoding="utf-8").write(html)
    print("wrote blog/%s/index.html (%d bytes)"%(p["slug"],len(html)))

# ---------------- blog INDEX ----------------
INDEX_INTRO="Straight-talk guides on lit teas, smoothies, protein coffee, and recovery — no fluff, from the counter in Pearland."
blog_jsonld={"@context":"https://schema.org","@type":"Blog","name":"Broadway Nutrition Blog",
  "url":f"https://{DOMAIN}/blog/","description":"Guides on lit teas, meal replacement smoothies, protein coffee, and post-workout recovery from Broadway Nutrition in Pearland, TX.",
  "publisher":{"@type":"Organization","name":"Broadway Nutrition","logo":{"@type":"ImageObject","url":LOGO}},
  "blogPost":[{"@type":"BlogPosting","headline":p["headline"],"url":f"https://{DOMAIN}/blog/{p['slug']}/"} for p in POSTS]}

cards="\n".join(
  f'''  <a class="post" href="/blog/{p["slug"]}/">
    <span class="tag" style="color:{p["acc"]};background:{GLOW[p["acc"]].replace(".5",".15").replace(".55",".15")}">{p["kicker"]}</span>
    <h2>{p["headline"]}</h2>
    <p>{p["meta_line"]}.</p>
    <span class="more" style="color:{p["acc"]}">Read →</span>
  </a>''' for p in POSTS)

INDEX_CSS = r""":root{--bg:#0a0610;--card:#16101f;--line:#2a1f36;--acc:#a64dff;--pink:#ff2e88;--cyan:#23e0ff;--txt:#f1ecf6;--mut:#a99cb8;--font:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;}
  *{margin:0;padding:0;box-sizing:border-box}html{scroll-behavior:smooth}
  body{background:var(--bg);color:var(--txt);font-family:var(--font);overflow-x:hidden;line-height:1.5}
  a{color:inherit;text-decoration:none}.wrap{max-width:1080px;margin:0 auto;padding:0 22px}
  .nav{position:sticky;top:0;z-index:50;background:rgba(10,6,16,.85);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
  .nav .row{display:flex;align-items:center;justify-content:space-between;padding:12px 0}.brand{font-weight:900;letter-spacing:.5px;font-size:18px}.brand span{color:var(--acc)}
  .btn{cursor:pointer;display:inline-block;border:none;font-family:var(--font);font-weight:900;letter-spacing:.5px;border-radius:40px;transition:.18s;font-size:14px}
  .btn-pink{background:var(--pink);color:#fff;padding:14px 26px;box-shadow:0 0 22px rgba(255,46,136,.4)}.btn-pink:hover{transform:translateY(-2px)}
  .nav .btn{padding:9px 18px;font-size:13px}
  .ahead{padding:54px 0 30px;text-align:center;position:relative;overflow:hidden}
  .ahead::before{content:"";position:absolute;inset:0;background:radial-gradient(600px 300px at 20% 0%,rgba(166,77,255,.18),transparent 60%),radial-gradient(700px 360px at 85% 10%,rgba(35,224,255,.12),transparent 60%)}
  .kicker{position:relative;display:inline-block;color:var(--cyan);font-size:12px;font-weight:900;letter-spacing:2px;margin-bottom:16px}
  .ahead h1{position:relative;font-size:clamp(30px,5.4vw,50px);line-height:1.06;font-weight:900;letter-spacing:-1px}.ahead h1 span{color:var(--acc)}
  .ahead p{position:relative;color:var(--mut);max-width:560px;margin:16px auto 0;font-size:16px}
  .grid{display:grid;grid-template-columns:repeat(2,1fr);gap:18px;padding:20px 0 10px}
  .post{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:24px;transition:.2s;display:flex;flex-direction:column}
  .post:hover{transform:translateY(-4px);border-color:var(--acc)}
  .post .tag{font-size:11px;font-weight:900;letter-spacing:1.4px;margin-bottom:10px;display:inline-block;align-self:flex-start;padding:4px 10px;border-radius:30px}
  .post h2{font-size:19px;font-weight:900;letter-spacing:-.3px;line-height:1.25}
  .post p{color:var(--mut);font-size:14px;margin-top:8px;flex:1}
  .post .more{margin-top:14px;font-size:13px;font-weight:900}
  .close{text-align:center;padding:56px 0 36px;border-top:1px solid var(--line);margin-top:30px}
  .close h2{font-size:clamp(26px,4.4vw,40px);font-weight:900;letter-spacing:-.5px}.close h2 span{color:var(--acc)}
  .close p{color:var(--mut);max-width:480px;margin:14px auto 26px;font-size:15px}
  .footer{text-align:center;color:#6a5d78;font-size:12px;padding:26px 0;border-top:1px solid var(--line)}.footer a{color:var(--mut)}.crumb{font-size:13px;color:var(--mut);padding-top:18px}.crumb a{color:var(--acc)}
  @media(max-width:780px){.grid{grid-template-columns:1fr}}"""

index_html=f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Broadway Nutrition Blog — Teas, Smoothies &amp; Energy Tips | Pearland, TX</title>
<meta name="description" content="The Broadway Nutrition blog — straight-talk guides on lit teas, meal replacement smoothies, protein coffee, and post-workout recovery from our Pearland, TX nutrition club.">
<link rel="canonical" href="https://{DOMAIN}/blog/">
<meta property="og:type" content="website">
<meta property="og:title" content="Broadway Nutrition Blog — Teas, Smoothies & Energy Tips">
<meta property="og:description" content="Straight-talk guides on lit teas, smoothies, protein coffee, and recovery from our Pearland nutrition club.">
<meta property="og:url" content="https://{DOMAIN}/blog/">
<meta property="og:image" content="{GH}/shake_strawberry_cheesecake.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Broadway Nutrition Blog — Teas, Smoothies & Energy Tips">
<meta name="twitter:description" content="Straight-talk guides on lit teas, smoothies, protein coffee, and recovery.">
<script type="application/ld+json">
{json.dumps(blog_jsonld,indent=2)}
</script>
{PIXEL_JS}
<style>
{INDEX_CSS}
</style>
</head>
<body>
{NAV.replace('btn-acc','btn-pink')}
<header class="ahead"><div class="wrap">
  <span class="kicker">BROADWAY NUTRITION · PEARLAND, TX</span>
  <h1>The <span>Broadway Nutrition</span> Blog</h1>
  <p>{INDEX_INTRO}</p>
</div></header>
<section class="wrap"><div class="grid">
{cards}
</div></section>
<div class="close"><div class="wrap">
  <h2>Hungry yet? <span>We've got you.</span></h2>
  <p>Text or call your order ahead and skip the wait — or walk in at {ADDR}, Pearland.</p>
  <a class="btn btn-pink" href="sms:{PHONE_TEL}" onclick="fbq('track','Lead')">🥤 Text to Order</a>
</div></div>
<div class="footer"><div class="wrap">
  <div class="crumb"><a href="/">← Back to Broadway Nutrition home</a></div>
  © 2026 Broadway Nutrition · {ADDR}, Pearland, TX ·
  <a href="{IG}" target="_blank">@broadwaynutrition.tx</a>
</div></div>
</body>
</html>
"""
left=set(re.findall(r"__[A-Z0-9_]+__",index_html))
assert not left, f"index leftover tokens {left}"
open(os.path.join(blogdir,"index.html"),"w",encoding="utf-8").write(index_html)
print("wrote blog/index.html (%d bytes)"%len(index_html))
print("\nPOSTS:", ", ".join(p["slug"] for p in POSTS))
