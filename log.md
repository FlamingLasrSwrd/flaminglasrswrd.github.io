---
layout: page
title: "Work Log"
permalink: /log/
abstract: >
  Semi-unfiltered life updates in the moment barely useful to me. Do not take seriously or literally.
---

## 27 Aug 2018
- more work on the server
  - setting up kvms for tor services
  - I might relocated some of the other services mentioned in the server post to kvm for security
  - need to generate some certificates
- messed with some security settings in Tomato
  - turned off pretty much all logging -> will need to reenable them as I do more research into their pen testing usage

## 21 Aug 2018
- Meal Planner

## 20 Aug 2018
School has started again: terrible drivers are a tolerable evil in exchange for the library staying open later than 5pm.

- more remailer website work

## 19 Aug 2018
- ScanTesla finished but didn't output anything -> time completely wasted
- continue work on remailer
  - choosing a theme and relearning css

## 18 Aug 2018
- made another batch of Play Hard
- worked on the remailer website

## 17 Aug 2018
- more meal planner app
  - learning about graph databases [@neo4j_tips_2015]

## 16 Aug 2018
- continued distillation of DMSO
  - had some kind of light brown liquid in the receiving flask, possible suck back from the pump?
    - I'm dumb. I released the vacuum but the system was still warm and as it cooled it sucked the vacuum oil into the flask.
  - going to have to redistill
- I still want to make a meal planner app...

## 15 Aug 2018
- researching urea hydrolysis for ammonia production
  - urease?
    - not available to buy
    - extract from vegetable matter? -> seems like a lot of work
- production of sodium by DES
  - using aluminum? -> energetically favorable by 1250 kj/mol
  - still need anhydrous metal chloride
- Hydrogen peroxide sterilization
  - vacuum chamber
- Started distilling DMSO from 90% cream -> PITA
  - vacuum distillation at around 90C with direct heating

## 10 Aug 2018
- more server: plex

Last night I was a part of a conversation about work. One of my friends was considering a promotion. He would be transitioning from working somewhat independently to managing a dozen people. Essentially the discussion boiled down to how much his happiness was worth to him. Everyone in the room agreed that their current work situation was not ideal. The descriptions ranged from "I don't hate working there" to "I really hate my job". These are highly skilled workers, mind you. I saw how these people, whom I admire, just hated work or at the very least thought of it as a necessary evil.
I never want to be that way.

## 09 Aug 2018
- more server

## 08 Aug 2018
- reinstalled Ubuntu 18.04 LTS on the server (again)
  - gave a write-up of the setup

## 07 Aug 2018
- more site work
  - changed fonts: more simplistic

## 06 Aug 2018
- worked on this site
- TODO: correct image alignment of post graphical abstracts

## 05 Aug 2018
- haven't been feeling the best lately; had my first migraine in something like a year yesterday
- ethanol brewing has successfully yielded more than a gallon of ~80%
  - the distillation column didn't separate as well as I hope- I suspect the small entrance hole (1/8" pipe) was too small
  - I overloaded the column and contaminated the liquor with copper. Doesn't matter since I'm not drinking it and I'll be running it through an all glass system for the final distillation
  - added come charcoal to remove some impurities- mostly worried about methanol

## 27 Jul 2018
- ethanol brewing is slowing; since this is entirely for chemistry, I'll let it ferment to completion
- hopefully I will test my pressure cooker still soon
- I broke my 1m chromatography column yesterday :,(

## 26 Jul 2018
- A lot has happened; I've been too busy to update here :(
- Started a test on ozone sterilization for ethanol production on Monday?
  - I originally wanted to do a side-by-side test of ozone versus placebo, but I messed up the procedure. So I just sparged ozone in both 5 gal carboys to make sure it was feasible in the first place. Plus, I am almost out of abosolute ethanol for the lab. I will have to make a fractionating column to distill it.
- Urea evaporation went poorly. The original solution is perfectly clean, but attempting to boil 2.5 gallons of liquid outside that emits ammonia is difficult to keep clean. Also, I neglected to check whether the latex rubber tubing I used as a gasket was compatible with ammonia. Spoiler... it isn't. So now I am recrystallizing the urea just like I would have done with cheaper fertilizer grade.
- The gym bet failed. Partly because my partner wasn't able to start the bet and partly because it is just too much of a time commitment. Even 30-45 min per day seems excessive. I made it a week without interruption but decided to end it after that. For now, I do a few sprints or quick foot ladder drills in the morning. Just enough to get my heart rate up and that seems to be working.
- The DES one-pot recovery hasn't worked. My guess is that the total solubility of metals in DES is lower than water so I need a greater volume. Something I can easily look up. I started with 1/10 mole choline chloride:1/5 mole ethylene glycol. Roughly 10 mL of solution. A small crystal of iodine was added. I added a sim card for the gold content. The plastic card warped and the iodine color was lost over a day or so, but the gold bits of the card seemed only slightly degraded. I added more iodine but after several days the sim card remained unchanged. I could use more DES or I could electroplate the solution. If all the metal has dissolved in the DES, electroplating will give pure metals. If I recycle the solution by electrolysis and dissolution simultaneously, the metals will plate as impure alloys or even metal sponge.
- The vermiculite furnace failed: the whole thing practically crumbled. The strength of the material wasn't high enough to allow removal of the form. If I had used a metal form, I could have either left it there permanently or calcined the entire thing before removing it. Wood just couldn't handle high enough temperature even just the drying stage. I'll just have to use a metal bucket or similar next time.

## 16 Jul 2018
- TODO: fix graphical abstract size in css

## 13 Jul 2018
- TODO: fix graphical abstract size: too big

## 10 Jul 2018
- currently evaporating urea solution (Blue DEF) to get highly pure urea
- still evaporating the zinc ammonium chloride solution; foaming is a major problem; probably better to buy it next time
- made some iodine ([Doug's Lab Video](https://youtu.be/E5eWKoZ5JzM))
  - for ionometallurgy [@mchem_ionometallurgy_2013]
- The conical flask I was making zinc chloride in cracked! I guess I really will have to buy it...

## 08 Jul 2018
- DES's are even more awesome than I imagined [@liu_recent_2015, @alonso_deep_2016]
- applications to explore:
  - electropolishing of stainless
  - electrodeposition of aluminum
  - biodiesel manufacture
  - electrowinning of gold plating
  - organic synthesis of all kinds :)
- further investigation of [@bagh_ionic_2014] revealed an electrochemical window of only 2.66-3.74 V for DES5 from 100-130C, so it makes sense that I was depositing zinc using 5V
  - make sure temperature is above 130C and voltage is <3.7V
- Testing second batch (1/5 mol scale) of DES5
  - amine smell when attempting to dry >160C... definitely didn't finish drying
  - attempting 3.3V 150C electrolysis using MMO/titanium anode/cathode; actual voltage is 2.66V;
  - saturated with at least 15g sodium chloride

## 07 Jul 2018
- finished construction of the verm box
- initial tests with DES resulted in precipitated spongy grey material onto the cathode
  - Two possibilities: sodium was being produced and reacting with residual water
  - zinc was being reduced from the DES because the voltage was ~5.0V which might be enough to break the Choline chloride: Zinc chloride bond -> will try 3.3V tomorrow
- Started a second 1/5 mole scale using pure HCl this time
  - 16.28g zinc oxide + 15g H2O + 80g HCl 20.2% -> 41.7g ZnCl2*4H2O
  - reduced the resulting liquid to saturated solution; made sure white HCl fumes were gone
  - added 28g choline chloride
  - boiled to get rid of water; >150C
  - total weight of beaker + stir bar + DES = 69.5g
- DES's would make a great high temp heat transfer liquid instead of mineral oil or other flammable solvent
- the first test was with a small piece of platinum wire + copper cathode; not much current flow; will try larger MMO anode + titanium cathode tomorrow
  - in order to make this a good video, I should try more readily available cathodes; carbon for starters
- high index of refraction for DES5 (n = 1.5) [@bagh_ionic_2014] makes images appear larger than expected from a glass of water (n = 1.3)
- TODO: add pic of DES index of refraction demo

## 05 Jul 2018
- filmed starting construction of vermiculite refractory box
  - constructing the box is probably not the best
  - I should just suck it up and use a round metal former
- synthesized zinc chloride 1/10 scale: 8.14g ZnO + 25g HCl 32% soln. + 5mL H2O
  - apparently anhydrous zinc chloride was used in the paper [@bagh_ionic_2014]
  - I added the requisite amount of choline chloride (14g)
  - Tomorrow I will evaporate it down. Hopefully the DES is enough to keep hydrolysis to a minimum
- researched platinum group metals concentration in street dust

## 04 Jul 2018
- filming during daylight
- still working on getting the server back up and running
  - apparently OpenStack is only available for ubuntu16 and I installed 18 :(
  - trying to get it working...
-

## 03 Jul 2018
- set up for filming using Hannah's Nikon
- need more light

## 02 Jul 2018
- filmed parts buy for vermiculite lab furnace video
- did a lot of cleaning of the workspace
-
## 01 Jul 2018
# Deep learning Organic Synthesis
[@coley_prediction_2017]

```bash
git clone git@github.com:connorcoley/ochem_predict_nn.git
git clone git@github.com:connorcoley/rdkit.git
export RDBASE=$(pwd)/rdkit
cd rdkit/
mkdir build
cd build/
cmake ..
make
make install
```

## 30 Jun 2018

### Roofing
- Measure area of foot; add 10% extra for wastage
- Ridge: a single 3-tab single cut into three covers 18 inches of ridge

Items Needed:
- dumpster or large trash can
- gloves
- belts with nail holders?
- knives
- push broom
- magnetic nail pickup

## 29 Jun 2018
- Finished week 1 of workout plan

## 28 Jun 2018
- Made Jafar costume.

![Jafar and Iago]({{ site.url }}/assets/img/20180628_191905.jpg)

## 27 Jun 2018
- Research on AGEs for reddit...

## 26 Jun 2018
- Day 2 of the gym bet successfully completed.
- Still consuming at least 6 'salads' per week. Still haven't had a depressive episode. Longest streak in history for me.
- looking at insulating refractory mixes
  - vermiculite with sulfuric/phosphoric acid chemical binder [@ekedahl_chemically_1959]
- working on site setup

TODO:
- fix website(s)
- plan for upcoming videos
- order chemicals for upcoming videos
- write checklist for flaminglasrswrd work day

## 25 Jun 2018
- Investigating motion capture software for possible inclusion of workout gifs to the food planner project (if I choose to add in workouts later on).
- Investigating better hydrogen torch setup. A separator cell that doesn't explode...
- Started workout program and bet with Matt.

## 15 MAY 2018
I need to get back to work. Spent the weekend at my parents house. Partly for my brother's graduation and partly for Mother's Day. All my sibs were there. I didn't get a headache this time... curious.

## 04 MAY 2018
Been a little off lately. Not quite to the point of depression, but certainly getting there. I'm sure my RescueTime and logkeys data will show how little I've worked the past 3 days. Further evidence for the Kale experiment started a little less than a month ago. I haven't had any symptoms since I started except for now, exactly coinciding with a break from consuming leafy greens.

## 29 APR 2018
So I didn't sleep last night. I "went" to bed at 4am and got up again at 5am without any actual sleep.
Writing academic papers even informally on this blog is painstaking. I wish there was a IDE for journal article writing.

## 17 APR 2018
I tried to use <eatthismuch.com> yesterday. A mildly unpleasant experience. Don't get me wrong, its an admirable site. It just has limitations, which in my opinion, are debilitating. I am now convinced I should write my own.

A few weeks ago I looked into writing my own recipe recommender system. When I located eatthismuch, I decided it wasn't worth it (without even looking at the site in depth). Competition is not my strong suit. But, now, having actually reviewed the site, it doesn't appear all its cracked up to be. They haven't actually captured the semantics of recipes and food prep. The site just seems like a backend collection of if...then statements without any sort of knowledge. For instance, I told the site that I would prefer to eat the food 'whole egg' for breakfast. So when I refreshed the recommendations, the site gave me 1-2 whole *raw* eggs for breakfast. A human, of course, would recognize that input as saying that I would prefer to use eggs as an ingredient in my breakfasts. Of course, I could learn how to use the site properly, but I don't want to do that. I want a recipe/food/meal prep program to have zero learning curve. Like a human whom you ask, "What should I make for dinner tonight." Therefore, I would like to attempt a meal planning service.

## 14 APR 2018
A week of uninterrupted happiness and motivation. I can't remember if that has ever happened to me. Since the last episode on April 5, I have been eating a salad composed principally of leafy green every morning. The hypothesis is that somehow nitric oxide is contributing to my happiness. But whatever the real reason this is working, I'm not going to stop with the breakfast salads.

## 06 APR 2018
Feeling much better today.

I think I'll move any conversations about AI to a separate [page][] from now on.

## 05 APR 2018
Had a depressive episode this morning. Only just arrived at the library (3:30pm). Tested a hypothesis that this episode might be related to nitric oxide system. Consumed 6g of citrulline and 5-6 leaves of kale to test. Oral mouthwash last night and exercise depleted body stores of nitric oxide precursors. That intervention doesn't seem to be working sufficiently. I have a constant need for comfort.

**QOTD:** How does the brain determine what inputs represent features and what are classes? Does it separate the two? Are classes disjoint? Features not so?

## 04 APR 2018
### Why do we have short term memory?
Is it solely to organize actions into a specific order? A telephone number consists of numbers 0-9 but only the specific order is important. Altering the connection weights between any particular number and that sequence isn't very useful. I.e. The fact that a particular sequence has a 9 in it doesn't matter.

If you were to ask Alexa, "What time is it?" You don't want the response to be, "1:26 PM the time it is." Although technically correct (the best kind of correct), it is not the typical response and it doesn't conform to the rules of grammar and syntax. Unless you asked Alexa to change her name to Yoda, of course. An example so simple is certainly understandable for humans because the time scale of the order switching is only a few seconds (within the human short term memory window). A desirable AI system should ideally be able to order an infinite sequence of events, which is obviously impossible.

Hmmm... it seems that visual imagination is competitive in space while auditory imagination is competitive in time. For example, when I think about how a particular object looks and activate its critical feature pattern, that object appears in my mind always in the center of focus. If I attempt to place that object in my periphery, my focus always snaps to it. I cannot simultaneously hold my focus at the center of the visual field and imagine an object in my periphery. I can, of course, imagine lots of different objects of varying complexity, but never two objects of a class. E.g. I can imagine a red circle and a blue circle but not both simultaneously. My mind's eye flits back and forth between them, unable to make permanent changes to the appearance of either. Oddly enough, if the circles touch or overlap, I can imagine them as one shape (like a figure eight). In essence, visual imagination is competitive in space. An object is regarded as one if it is continuous in space, and only one object can be manipulated in imagination at a time.

Likewise, auditory imagination is competitive in time although this one is considerable harder to explain because I cannot express it in alternate dimensionality like I do with visual imagination.

## 03 APR 2018
I dreamed of Prolog last night. Do you know how hard it is to program in your dreams?

### Designing Programs
Syntax, toy problem, blah, syntax, syntax, syntax, toy problem. That's how the vast majority of "tutorials" on programming languages teach and the complete opposite of how one uses a programming language. To use a programming language (and any language for that matter), one starts with an conceptual idea of what one wants to explain or do. From there, a series of decisions are made to accomplish that goal.  Instead of teaching tiny bits of syntax which have no inherent purpose to the brain, wouldn't it be better to show the brain a new item that is actually useful? Teaching syntax is necessary, no doubt, but it shouldn't be the first step in learning a language. E.g. Rosetta Stone and DuoLingo use the practical approach. A lot of online programs use the *learn by example* path, which is somewhat better. But they fail where you have to make actual design decisions later using the particular programming language. E.g. Why would one choose to use a set() over a dict() in python?

I've run into this problem headfirst while learning Prolog. Of the few tutorials on Youtube, none of them cover anything more than syntax. Github is full of *practice problems* from such and such a college course or book.

Fortunately, I've come across a book which might be of use for the particular area of Prolog. [*The Practice of Prolog*](#sterling_practice_1990) teaches how to develop a project in Prolog from start to finish.

## 02 APR 2018
Recently I have been learning about Prolog. I like the idea of pure declarative languages. The beauty of simply defining the problem and having the interpreter/compiler solve the problem is striking. It is quite different from my previous programming adventures in C++ and python. I stumbled upon a realization this morning: Backtracking in Prolog seems to be the exact mechanism that Adaptive Resonance Theory calls "Resonance and Reset".

I've been going about this all wrong. I've been so focused on finding out all the ways the brain solves the problem of knowledge acquisition and use that I have neglected the reason why that problem had to be solved in the first place. The human brain has assuredly a vast number of features that help it solve that problem. A number of them are sure to be superfluous, redundant, and downright incorrect thanks to evolution. Trying to wrap my head around all the various features of the brain is nigh impossible especially since I currently believe there are emergent properties of the brain. A better solution might be to solve the problem of knowledge acquisition from first principles. I'm certainly not the first person to do this. Perhaps all of philosophy (and certainly Ontology) is in this pursuit.

For instance: Why did the brain develop grouping (e.g. a set of pixels on the retina are collectively denoted 'square')? By assigning a group, the brain can modify its internal state only once and have that change propagate to all affected members rather than modifying each affected member separately, thus saving energy.

So the question is: What problems compose knowledge acquisition and use? At first glance, knowledge accuracy and knowledge acquisition speed are a trade off. Knowledge that is applied to a set that is not completely consistent is known as a heuristic.

## 29 Mar 2018
*[stream]*
What would my ideal schedule look like? I have attempted many times in the past to streamline my routine and plan my days (sometimes months) into the future. It never seems to work. Four days is my typical stretch. Then I revert back to my primitive, unscheduled self. Its a tiring routine in and of itself. I keep recalling something I read about Ben Franklin, that he would practice one and only one routine for a month before working up to another one. In the past, I have thought that he just doesn't know how to push himself. But perhaps he really knew what he was doing? My track record of implementing change is practically nil. Perhaps the mind, no matter how excellent or effortful, just can't handle that much change. Inevitably, something breaks down.  
In other news, the fasting has somewhat failed. I think intermittent fasting has its merits. I certainly started out feeling much much healthier and my mood stabilized a bit. My memory mostly returned. The first day I skipped breakfast and lunch. I then only ate 'dinner' after I felt hungry for a couple hours. I made it to 4pm the first day. 5:30pm the second. By day four I didn't even want to eat at 7pm. That is the problem that I am facing now. Last night I stayed up to 4am (a whole problem by itself) and I felt just insane hunger at 3am for some reason. I hadn't eaten much that day because I felt no hunger. I would feel my stomach rumbling, but no desire to consume food. My calorie count is epically low over the last couple days. By my resting metabolic rate I should be consuming circa 3000 kcal per day. Likely I was consuming less than 1500 on some days. Certainly I am in ketosis. I attempted to counteract the low energy a bit by consuming more fat, namely bulletproof coffee. I am still consuming my protein shake thing.[^2] If I wasn't so poor, it would also contain a lot more fat. The only fat I have used in the past in mixes like that is MCT oil. Solid fats would require more prep that I am used to doing. Perhaps I can add some olive oil instead. I tried that with the breast milk project and it doesn't taste good. Today I had, in addition to BP coffee, a breakfast of microwaved broccoli with butter, salt, pepper, and mustard seeds (for the enzymatic conversion to sulforaphane). This was only sort-of breakfast since it was 1pm.  
Let's try an experiment shall we. I'm going to remove/disable social media from my phone. My big crutches are Facebook, Reddit, and Youtube. Combined I spend at least several hours per day on them. I don't need that. The only part I might miss is the event updates on FB. I will still have email, text messaging, and snapchat. The last one because its the only way I seem to be able to communicate with one person in particular. I need to figure something out to minimize that distraction. Note: I've noticed that I can't leave my phone facing up within my visual field... I see phantom LED notifications. Out of the corner of my eye it appears that the indicator LED on my phone is illuminated, but when I look closer nothing has arrived. Serious addiction.  
I don't think I can completely eliminate my cell phone. I did that once. For about 6 months I didn't carry a phone because my old one broke down and I was too poor to buy another. As a consequence, I was freer, but I also lost contact. My mom was especially distraught. She wasn't really on FB at that time and the few calls I did make to her were now nonexistent. Now, of course, she has a phone and is more active on FB. Similarly, I can't forgo the laptop. I am a programmer by skill set. Not impossible, but practically untenable to be a programmer without a computer.  
*[/stream]*

## 26 Mar 2018
- Continuing (4 days now) my experiment on intermittent fasting.[^1]
- Added project pages for [primary alcohol catalysis][] and [nitric acid production][]
- fixed wifi issue!!!

## 21 Mar 2018kugelrohr
Made some updates to this site.
[(Baranes, Oudeyer, and Gottlieb 2015)](#BaranesEyemovementsreveal2015)

## References
{:#sterling_practice_1990}
Sterling, Leon. 1990. The Practice of Prolog. MIT Press. <https://books.google.com/books?id=DaziVk05wk0C>.

{:#BaranesEyemovementsreveal2015}
Baranes, Adrien, Pierre-Yves Oudeyer, and Jacqueline Gottlieb. 2015. “Eye Movements Reveal Epistemic Curiosity in Human Observers.” *Vision Research* 117 (Supplement C): 81–90. <https://doi.org/10.1016/j.visres.2015.10.009>.

## Footnotes
[^1]: 18+ hr fast + fermentable fiber + high protein + vegetables: Testing the effect of fiber consumption on tolerability of intermittent fasting
[^2]: 500ml milk + 30g whey protein + creatine, ALCAR, NAC, TMG, citrulline, beta alanine, taurine, agmatine, ornithine, vit C, Mg, K, Zn, potato starch

[primary alcohol catalysis]: {{ site.baseurl }}{% link _posts/2018-03-26-primary-alcohol-catalysis.md %}
[nitric acid production]: {{ site.baseurl }}{% link _posts/2018-03-26-nitric-acid.md %}
[page]: {{ site.baseurl }}{% link _posts/2017-08-30-AI-research.md %}#journal
