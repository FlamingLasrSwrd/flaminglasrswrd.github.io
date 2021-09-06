---
layout: "post"
title: "Nitric Acid"
date: "2018-03-26 11:34"
category: active
phase: experimental
tags: chemistry electronics high-voltage
author: Elijah K. Dunn
zotero-collection: https://www.zotero.org/ekdunn/items/collectionKey/DBGV3U9D
gallery: plasmaNitricAcid
abstract: >
  Atmospheric nitrogen fixation for the amateur using plasma.
graphical-abstract: /assets/img/plasmaNitricAcid/plasmaNitricAcid-nonthermal-plasma-test-2-arc-top.JPG
---

# Prior Art
Almost every amateur chemist youtube channel hosts at least one video on nitric acid synthesis. Most of them follow the nitrate salt + sulfuric acid synthesis. While simple and relatively cheap, production in this manner is time consuming and, at least in my attempts, prone to accidents.

<!--![image](/assets/img/nitric-acid-old/break_0.JPG)-->

Industrially, nitric acid is produced almost exclusively from oxidized ammonia via the Haber-Bosch (HB) and Ostwald processes. The hydrogen is, of course, produced from petroleum. While cheap, this isn't exactly sustainable.

An alternative, less developed method is plasma atmospheric nitrogen fixation. The current shift toward more sustainable sources of fertilizer have garnered new research into old fixation methods. Unfortunately, none of the current plasma methods (even in lab tests) come close to the energy efficiency of HB. That doesn't mean they won't be (cost) efficient for the amateur, though.

The most robust plasma based method today is the Birkeland-Eyed thermal plasma reactor. For a time, BE reactors were used to fix nitrogen in areas with cheap electricity. HB eventually won out, however, and BE reactors are not in use outside of the lab. [Sciencemadness][] has a lengthy discussion on this particular style and the adaptation for amateurs.

## Mechanisms
A BE reactor uses thermal plasma to provide the dissociation energy for nitrogen molecules which then combine with oxygen atoms to produce NO. The reactions here are numerous and ethereal. One important fact to understand is that the desired conversion to NO is reversible and a considerable amount of energy is wasted in this regard. Even from a theoretical standpoint, the production of ammonia via the Haber-Bosch process is about twice as efficient as the BE process, and almost an order of magnitude better than practically achieved.[@cherkasov_review_2015] A non-thermal plasma process could theoretically be 3-4x more efficient than the HB process.

A number of innovations have developed since the relatively brute force BE reactor was invented more than a century ago. The current research seems to point to a non-equilibrium plasma process as fundamental. A mixture of thermal and non-thermal plasmas to get the best of both.

While many small devices have been constructed for lab testing, none so far have been commercially viable. Even at the relatively low power required to produce a few liters of concentrated acid per year, significant heating is an issue. Nitrogen oxides are also quite corrosive to most metals and plastics, increasing the costs of any apparatus. The HB process also has the advantage of creating highly concentrated NOx streams, which greatly reduces the cost of gas handling equipment.

Herein details my work attempting to adapt non-thermal plasma for amateur nitric acid production in a cost efficient and practical manner.

# Construction Considerations
## Electrode Material
Copper [@cormier_degradation_2008], stainless steel, carbon steel, molybdenum, and tungsten [@patil_plasma_2017] have been used as GlidArc electrodes. Due to cost, molybdenum and tungsten are probably out for the amateur chemist. Copper has the benefit of being readily available and easy to machine. Copper pipe could also be water cooled. Stainless might have better chemical resistance, especially to nitric acid if the feed gas contains water vapor. The work function and resistance of a material seem to influence the efficiency somewhat. [@patil_plasma_2017] Mostly because of the arc effects such as rise time and cycle frequency.

## Power Supply
Frequency, pulse width, and voltage all have an effect on the production of NOx in both concentration and efficiency. This seems to arise indirectly as a function of plasma temperature distribution.

### Frequency
Higher frequencies (>5KHz) are more efficient than mains frequencies (50-60Hz). [@yang_nitrogen_2016] This is within the range of a simple 555 timer in astable mode.

### Voltage
Generally speaking, voltage is not a critical factor for sustained plasma. However, the transient nature of non-equilibrium plasmas used in this research necessitate the use of relatively high voltages for arc stability. The original BE reactors could be sustained by only a few hundred volts. For proper functioning, Glidarc reactors require several thousand.

### Pulse Width
Pulse width is an indirect measure of plasma heating and by extension, total current.

## Feed Gas
As previously mentioned, plasma processes suffer from reactant dilution. Only a few percent of nitrogen oxides are typically generated from a plasma process, which means more than 95% of the gas stream is dilutant. At 2% concentration (a high value), the maximum concentration of nitric acid is about 80% before the waste gasses will contain more acid than is produced. [@taylor_vapor_1925]

Of course, nitric acid can be scrubbed using any number of salts to mostly eliminate this waste.

# Yield Calculations
Current Haber-Bosch nitrogen fixation = 0.48 MJ/mol = $0.17 per liter conc. nitric acid.

State of the art Glidarc = 4.8 MJ/mol = 1.3 KWh/mol => $0.11/mol => $1.65 per liter

# Useful Conversions
For my 100mmol sodium carbonate titrant:

$m_{analyte} = \frac{V_{titrant} * 200}{V_{analyte}}$

# Work Log

## 03 Jan 2020
I wonder if the output of the reactor can be used for direct nitrations or Gattermann reactions?

## 30 Dec 2019
Nitrogen dioxide can be [selectively adsorbed onto silica gel](https://www.sciencemadness.org/whisper/viewthread.php?tid=48085&goto=search&pid=397057). Indicator silica is even more useful since the NOx will change the color when saturated. [@farrington_nitric_1951]

## 17 Dec 2019
I came across an alternative electrode configuration that might be worth looking into [@foster_perspectives_2012].

## 20 Oct 2019
So the gas phase reaction of nitrogen dioxide and ozone to form nitrate seems pretty fast [@huie_rate_1974].

I'm still convinced that ozone is the way:

> Intensification of nitric acid production is due to the fact that
much higher rate of nitrous acid oxidation was obtained (ca.
60%) employing ozone rather than only oxygen. [@chacuk_intensification_2007]

The mole ratio of O3:NO should be maintained around 1.5 for efficiency's sake. Complete NO oxidation is obtained at a mole ratio of 2. [@skalska_effectiveness_2011-1]

My last run produced 21mmol NO per hour. According to the research above, this should have been combined with at least 1g per hour of ozone. Considering that an appropriately sized ozone generator looks to be 10x the size of mine, I think my ozone production is insufficient. That explains the absorption issue.

## 18 Aug 2019
Manganese dioxide can be used as a reversible nitrogen dioxide absorbent.

## 10 Aug 2019

![image](/assets/img/plasmaNitricAcid/plasmaNitricAcid-nonthermal-plasma-test-5-setup-knives.JPG)

### Results

- Total Energy = 3.31KWh
- Power Consumption Average = 138W
- Run time = 24 hours
- bubbler solution final pH = 0.91
- first scrubber solution final pH = 1.35
- carbonate scrubber solution initial pH = 11.26
- carbonate scrubber final pH = 9.46
- cooling water final temperature = 26C
- bubbler (400ml) acid concentration (by titration)= 724mM (18.1ml for 5ml)
    - 290mmol
- first scrubber (65.6ml) acid concentration (by titration)= 848mM (21.2ml required for 5ml)
    - 56mmol
- carbonate scrubber acid absorption (see below)= 166mmol
- total nitric acid produced(absorbed): 512mmol; 32.3g
- efficiency = 9.7g/KWh = 0.10KWh/g = 6.5KWh/mol = 23MJ/mol
- production speed = 32g/day
- Estimated cost per day = $0.36
- Electricity Cost to produce 1L of 68% nitric acid = $7.70
- Time to produce 1L "": 21 days

As you can see, the characteristics of this run is the same as before. Even with the additional bubbler and scrubber.

### Scrubber Titration
I started with 87.1 ml of saturated sodium carbonate solution. I used the bubbler acid that I just titrated to calculate the carbonate used:

Titrating the saturated solution:

- saturated sodium carbonate solution: 5ml
- titrated with 18ml 724mmol nitric acid
- total initial carbonate concentration: 1.3M
- total initial carbonate: 114mmol

Titrating the scrubber:

- saturated sodium carbonate solution: 10.3ml
- titrated with 10ml 724mM nitric acid
- scrubber final concentration: 351mM
- scrubber final amount: 30.6 mmol

So a total of 83mmol of sodium carbonated was consumed in the scrubber, which means 166mmol of nitric acid was consumed: Half as much acid as absorbed in the bubbler system. This definitely indicates that my absorption is lacking and a lot of nitrogen oxides are escaping.

## 05 Aug 2019
The arc reactor has been running fairly stably for the last 18 hours or so. I shut it down last night because my chemistry lab is also my bedroom...

I measured the volumetric flow rate of the system today using an inverted 1L graduated cylinder. It took 3 minutes and 42 seconds to fill with gas. That means a total flow rate of unreacted gas of 4.5ml per second. My reactor is 500ml in volume which gives a residence time of 111 seconds. I'm not really sure if that is a good number. The flow rate of Patil's glidarc reactor is tied to arc stability, so I can't really draw any useful comparisons to my work [@patil_plasma_2017].

Shut down the arc reactor at the 24:00hr mark. I'll let everything cool down over night and run the productivity tests tomorrow.

## 02 Aug 2019
So after much deliberation, I came up with a different reactor plan. The arc reactor will consist of two diverging 3/8"OD-5/32"ID 316 stainless steel tubes (what I had on hand). Cooling water can thus be passed through the tubes to reduce wear and capture the heat. The assembly is sandwiched between two pieces of glass. If I had borosilicate or even better quartz, that would be better. All I have is some regular 3mm plate glass. I hope it doesn't break.

![image](/assets/img/plasmaNitricAcid/plasmaNitricAcid-nonthermal-plasma-glidarc-sealed-arc-close.JPG)

Yep. The glass broke. Go figure. I guess I will have to keep looking for materials.

## 02 Aug 2019
Setting up for a longer run of the glidarc reactor... The arc is just too unstable in this rigged configuration. I'm going to try to make a legitimate glidarc reactor.

## 29 Jul 2019

### Third Run Results

![image](/assets/img/plasmaNitricAcid/plasmaNitricAcid-nonthermal-plasma-test-4-setup-vert.JPG)

- Total Energy = 0.51KWh
- Power Consumption Average = W
- Run time = 4 hours
- reactor solution final pH =
- bubbler solution final pH = 1.00
- peroxide solution final pH = 1.74
- distilled solution final pH = 0.86
- reactor acid concentration (by titration)= 10.9M (54.3ml for 1ml)
    - 516mmol
- bubbler acid concentration (by titration)= 712mM (17.8ml for 5ml)
    - 142mmol
- peroxide acid concentration (by titration)= 140mM (7.0ml required for 10ml)
    - 3.5mmol
- distilled acid concentration (by titration)= 21M (268ml required for 2.5ml) **interesting...**
    - 53mmol
- total nitric acid produced(absorbed): -50mmol (a net loss)

I was able to achieve a maximum still head temperature of 90C. 2.5ml was distilled over leaving 47.5ml in the reaction chamber. I couldn't measure these directly because I spilled some. D'oh!

It was interesting that I got a concentration of over 100% acid in the distilled fraction. Perhaps there was a lot of dissolved nitrogen oxides? More likely it is just human error.

In any case, **the direct arc to water process is a bust.** There is just too much decomposition of nitric acid. Dry air it is...

## 28 Jul 2019
Let's run another test. This time starting with 68% nitric acid and an insulated column.

My nitric acid is approximately 68% (15M). Titrating 1ml requires 76.4ml or 15.3M concentration.

Ran for 1 hour and used 0.11KWh. 50ml of 15.3M acid starter was added as a jumpstart (765mmol of nitric acid). Significant instability in the arc was the limiting factor. The rubber seal was charred from repeated arcs. I decided to stop the experiment and rerun it with a ground glass seal.

![image](/assets/img/plasmaNitricAcid/plasmaNitricAcid-nonthermal-plasma-test-4-insulated-arc-close.JPG)

The seal is much better and the arc is more stable now. It still isn't as stable as the original glidarc reactor was, but good enough for now. Power usage is hovering around 128 watts.

I should have done this sooner: I installed a water trap between the ozone line needle valve and the DBD ozone reactor. That way I can visualize the relative flow between the main arc reactor and the ozone system. I definitely didn't have proper ozone flow in prior runs.

The system definitely has some brown nitrogen dioxide being formed. Fortunately, the primary (1L) bubbler seems to be trapping all of the NO2 since there isn't any visible after.

![image](/assets/img/plasmaNitricAcid/plasmaNitricAcid-nonthermal-plasma-test-4-absorption-color.JPG)

The 3-neck RBF has developed a crack from repeated arcing against the wall. :(

![image](/assets/img/plasmaNitricAcid/plasmaNitricAcid-nonthermal-plasma-test-4-cracked-glass.JPG)

Perhaps some sort of inductor/capacitor combo to provide a jump start in case of arc failure?

### Second Run Results
This is actually the 3rd full system test but the second quantitative test.

![image](/assets/img/plasmaNitricAcid/plasmaNitricAcid-nonthermal-plasma-test-3-setup-vert.JPG)

No distillate was collected from the graham condenser. I believe with proper insulation, the acid could start to reflux. Or perhaps a higher concentration of acid would be able to distill over. That would be ideal for purification.

- Total Energy = 0.90KWh
- Power Consumption Average = 150W
- Run time = 6 hours
- reactor solution final pH = 2.53
- bubbler solution final pH = 3.65
- peroxide solution final pH = 3.19
- reactor acid concentration (by titration)= 18mM (2.3ml required)
    - 0.9mmol
- bubbler acid concentration (by titration)= 2mM (0.3ml)
    - 0.4mmol
- peroxide acid concentration (by titration)= 8mM (1ml)
    - 0.2mmol
- total nitric acid produced(absorbed): 1.5mmol = 95mg
- efficiency =  0.11g/KWh = 9.5KWh/g =  600KWh/mol =  2100MJ/mol
- production speed = 16mg/hr
- Estimated cost per day = $0.39
- Electricity Cost to produce 1L of 68% nitric acid = $710
- Time to produce 1L "": 4.9 years

So... ya... abysmal. I guess electrode arc directly to water is a bust. The traveling arc really does look and produce different results. It might be worth attempting the process again with azeotropic nitric acid. The electrical resistance of the water may have been sucking too much energy... A quick arc test with some concentrated acid shows significantly more vigorous arcing. Time for test number... how many is this now?

It is also of note that the peroxide bubbler absorbed some of the nitric acid and thus the ozone did not fully oxidize the nitric oxide. However, I could not directly verify how much ozone was being pushed through the system: It could have been negligible.

The submerged electrode did suffer some degradation:

![image](/assets/img/plasmaNitricAcid/plasmaNitricAcid-nonthermal-plasma-test-3-discoloration.JPG)

## 27 Jul 2019
What would be the feasibility of making a containerized fertilizer plant for organic/low-impact farms? How much fixed N could a few hundred watts provide?

Typical application of fertilizer is 100-200lbs of nitrogen per acre. See the [Iowa State Nitrogen Fertilizer application calculator](http://cnrc.agron.iastate.edu/nRate.aspx) for variances. So to produce 150lbs of N over the course of 250 days at 6 hours per day (solar panel based), you would need a 4KW solar system. That's a little much.

Alternatively, the solar system could just be supplemental. Although this does degrade the "zero-emission/carbon-neutral fertilizer" concept. Running the system continuously from grid power would only require 700W. That is completely reasonable. Currently, the price of nitrogen is about $60 per acre at the 150lb/acre application rate. The price to run such a system would be around $700 without supplemental energy. Obviously this isn't feasible.

Solar panels are $2-3 per watt installed. So a 4KW system would cost around $10,000. It would take up about 25 square meters, which is only 0.6% of an acre.

Started second run of direct-discharge plasma system. This time with secondary and tertiary absorption systems. The same 3-neck RBF filled with 50ml deionized water and vigreux reflux condenser are used. The output of the vigreux column is directed to a graham condenser cooled with ice water. A vacuum take off adapter is used to collect the condensate. The gaseous output of that is led into a 1L bubbler filled with 200ml deionized water and then to 25ml of 3% hydrogen peroxide. Ozone is also piped in separately above the graham condenser. A temperature probe is located above the reflux condenser. A small computer fan is used to cool the electronics. All electrical inputs are run through a Kill-a-Watt energy meter.

The arc seems stable at 150W (less the energy required to run the ancillary electronics). Anything more and it tends to go out every few minutes. I adjusted the air flow rate to a minimum: a few bubbles per second at the last absorber. If this run achieves better efficiency, I will do another, more quantative, run. One for a proper material energy balance. Measure the gas throughput, temperature differentials, etc.

![image](/assets/img/plasmaNitricAcid/plasmaNitricAcid-nonthermal-plasma-test-3-arcing-close.JPG)

The water pump uses less than 5W.

## 26 Jul 2019
I have been contemplating electrodes for a few days now. I like the idea of using two streams of water as electrodes because it provides nearly instant transfer of heat to the water. There also isn't anything to replace like there would be with metallic electrodes. However, this system requires pumps to move the water/nitric acid. Pumps that can withstand concentrated nitric acid are not cheap and tend to wear quickly. I think the better option is with a single electrode arcing to water or a submerged electrode. This also has the benefit of producing small amounts of ammonia [@peng_situ_2018].

The first test of direct arc was a success. A 3-neck RBF is a perfect container for such a reaction. The left neck is input for the ground electrode which is submerged in water. The right neck passes a hollow stainless steel tube for passing input air and high voltage. The center neck holds the reflux condenser. After a few minutes, the temperature at the top of the column reached 70C. Final pH of the 40ml of water was approximately 2.4 after 5 minutes run time.

## 25 Jul 2019
The maximum arc length is at least 8cm. The minimum stable arc striking distance is 8-10mm. If I had the same efficiency as recorded in the literature, my setup could produce 1L of 70% acid every five days. To achieve my 500ml per day mark I would have to increase the power to 300W. Let's call it 500W just to be safe and somewhat even.

To boil 1 kg of water it takes approximately 630Wh or 2250 kJ. 500W should be enough to reflux the necessary acid at least once per hour.

Nitric oxide combines with oxygen below 500C. [@martin_industrial_1915]

## 24 Jul 2019
In-situ combination of water and plasma almost doubles the nitrogen fixation rate [@peng_situ_2018]. UV irradiation also increased fixation but to a lesser extent.

Direct discharge through the water is a possibility and would make construction easier [@janca_investigation_1999].

The total power of the system is less than 200W. Capturing the heat may not even be worth it anyway. Since the temperature of the reactor will always be below 100C, borosilicate glass isn't necessary. Some researchers have used acrylic [@yang_nitrogen_2016].

A completely submerged electrode is also possible. This would allow cooling of the electrode material as well. [@park_reactive_2013]

I would prefer not to have to drill through glass.

[A few amateur Jacob's ladder configurations](http://tesladownunder.com/JacobsLadder.htm).

Honestly, I think a Tesla coil style rotary spark gap is the best option. [A simple construction](http://www.tb3.com/tesla/sparkgaps/index.html).

No matter what I will need some sort of condenser or trap on the exhaust. Nitric acid doesn't have zero vapor pressure at room temperature. Cooling requires more power, however. A hydroxide trap might be more cost effective.

Started a larger scale test on ~200ml 3% hydrogen peroxide (0.88M). I am use a kill-a-watt meter to determine total energy requirements. I can smell NOx on the exhaust, so the results will be low. At an average of 120W and a production rate of approximately 50mg/Wh (estimated from literature), it will take a little under two hours to produce the necessary 11g of nitric acid at a concentration of 0.88M. I'm going to run it for 1 hour just to make sure I don't run out of hydrogen peroxide.

I made a sodium carbonate titration standard: 10.60g dry sodium carbonate in 1L diH2O gives 100.0 +- 0.05mM. I only have 25, 50, and 1000mL volumetric flasks, so that is why I went with 1L. At least I will have enough for a while.

Approximately 110ml of my standard will be needed to neutralize 25ml of 0.88M nitric acid (22mmol). It took only 8.1ml :(

### Results

![image](/assets/img/plasmaNitricAcid/plasmaNitricAcid-nonthermal-plasma-test-2-arc.JPG)

- Total Energy = 0.12KWh
- Power Consumption Average = 120W
- Run time = 1 hour
- solution final pH = 1.86
- solution acid concentration (by titration)= 65mM (8.1ml required)
- total nitric acid produced(absorbed): 13mmol = 820mg
- efficiency = 6.8 g/KWh = 0.15 KWh/g = 9.3 KWh/mol = 33MJ/mol
- production speed: 0.82g/hr = 20g/day
- Estimated cost per day: $0.31
- Electricity Cost to produce 1L of 68% nitric acid = $11
- Time to produce 1L "": 31 days

 So... fairly dismal compared to the literature. Much better than the price of purchasing (~$100 per liter). I'm guessing absorption issues. At least, I hope that's the cause. That's something I plan on fixing.

### Reflections
 Since the production costs could be as low as $0.11 per liter, this could be a profitable commodity for the amateur community. The actual processing of the dilute nitric acid will constitute some loss here. Even if it amounts to ten times the cost of the nitrogen fixation (wildly exaggerated), I could reasonable make $35 per day. What would it take to produce 500mL of concentrated (68%) nitric acid every other day (the 78-day-average rate of acid sold on eBay)?

500mL 70% HNO3 (11.1M) is 350g HNO3. Scaling my current (terribly inefficient) setup would require 2.1KW power input. Not including nitric acid concentration. That's a lot of power, but not impossible. Electrode wear (and arc-stability) will be a problem. Perhaps a dual water jet electrode?

Something like 97-99% of the energy required is wasted as heat, and high-value heat at that.

Other value-added products could be made as well: nitrate salts, nitroparaffins, etc. They all seem to be sold on eBay for much less than the equivalent value of the nitric acid required, however. E.g. potassium nitrate sells for ~$15/lb which requires about 400mL of acid at a net loss of $15 compared to straight acid. Still a profit, though.

## 23 Jul 2019
Several tests over the last couple days. Finally some production: less than 2 minutes of run-time reduced neutral 3% hydrogen peroxide to a pH of 1.72. Reaction with copper metal bubbled and produced a mild blue solution confirming the existence of nitric acid.

![image](/assets/img/plasmaNitricAcid/plasmaNitricAcid-nonthermal-plasma-test-1-copper-in-nitric-acid.JPG)

There are substantial variations in gas production that seem to correlate with power input and plasma shape.

I would like to use the waste heat from the plasma chamber to boil the water for NOx capture. Perhaps adding water directly to the plasma chamber and refluxing above would work?

I also noticed that after the system is turned off, the plasma chamber turns brown in a minute or two. This indicates the presence of nitric oxide.

Plasma stability is not great. I made several electrodes and still it wasn't very stable.

![image](/assets/img/plasmaNitricAcid/plasmaNitricAcid-nonthermal-plasma-test-1-arcing.JPG)

## 19 Jul 2019
Added two 940C20P15K-F caps to the tank capacitance of the ZVS driver to decrease the frequency. Power levels now peak at about 150W and average around 100W.

## 17 Jul 2019
Several tests were done with the ZVS driver. Total input current to the system at 120V is between 0.5-1.5 amps (up to 15A; 12V). I measured this with a clamp-on multimeter. I was originally attempting to get the frequency below 10kHz by increasing the primary inductance and tank capacitance, but I found that between 5-80kHz, NOx production varies quite little [@yang_nitrogen_2016]. Which is a good thing. A 10kHz 100W whine is annoying. So I will rework the system to optimize for current draw and thus power.

It isn't necessary to run the flyback at higher voltages. The high voltage is merely to start and maintain the arc discharge. It is current we are after. Some systems only use the high voltage to create the arc, then use a low voltage, high current supply to actually do the work.

I also reduced the choke inductance to increase the primary current. It does work, but it runs the risk of destroying your power supply.

Definitely need to use refluxing water as an absorption tower [@lee_process_2017].

I definitely want to build a plasma tornado, if only because it looks awesome [@kalra_gliding_2005-1]. I would need an air pump capable of at least 30 liters per minute flow for a similar design.

Propeller arc [@pei_propeller_2018] seems a lot like the rotary spark gap from my early tesla coil days. I like the idea of combining the air pump and plasma by the use of a propeller.

## 06 Jul 2019
Seems that the glidarc reactor was a failure. Even after 8+hrs of running in various configurations, no discernible change to the pH was detected. This could be for a number of reasons. I think the most likely just simply that the total input power to the system was very low.

## 05 Jul 2019
First test of the plasma nitric acid system. Just a 3-neck RBF with air inlet, air outlet, and high-voltage inlet. The output of the flask is fed through a DBD ozone generator pulled from a self-cleaning water cooler. That is fed to a gas washing bottle charged with 5.37g NaOH and ~400ml dH2O. After an hour or so it became apparent that the flyback would overheat, so I set a computer fan to blow across it. That is plenty for now. For the full scale version at 24V, mineral oil submersion will be needed. ZVS driver seems perfectly fine.

Material compatibility might be an issue in the future. Nitrogen dioxide eats just about everything except 300 series stainless, glass, and polymers with fluorine.

I had some trouble with arcing across the black rubber stopper used to feed HV to the reaction chamber (of course). This was solved by sleeving the SS bolts with PE tubing. The two nuts that secured the HV connections were sleeved again with some larger gauge silicone tube. The sleeves also functioned as electrical insulators so the arc spacing could be adjusted by hand. Tubing material choice was determined by availability.

The arc chamber becomes too hot to touch after just a few minutes. Maybe 70-80C. Might be worth looking into using this waste heat for the concentration of dilute nitric acid by distillation.

After the 5.5hr mark of running the reactor and getting no decrease in pH, I decided to try something different. Brown nitrogen dioxide gas is obvious in the arc chamber, so that isn't the issue. It occurred to me that perhaps running the products of the arc reactor through the ozone generator was completely destroying all the NOx. So I rearranged the tubing so the ozone and NOx generators were in parallel, not series. We shall see how it goes...

As a side note: the silicone tubing has already started to show signs of wear. Definitely will not be using it for the final version. Ozone, nitrogen oxides, and nitric acid are a potent combination.

Maybe the ozone is throwing off the pH measurements?!

Still not noticing any change in pH at the 6:50 mark. I disconnected the ozone generator to see what effect that would have. This will skew my results since there is no longer an oxidant.

## 03 Jul 2019
First preliminary test of the glidarc reactor went well. It was just a couple of steel wires bent into the typical jacob's ladder configuration. I had trouble getting the arc to travel appropriately. Perhaps at full power and with a moving air current thing will work better? Brown nitrogen dioxide gas was evident after a minute or two of running at 12V. I would like to run at 24V in the final setup. The flyback might need to be submerged in mineral oil to provide cooling. It didn't get hot or anything, just a bit warm.

## 16 Mar 2019
> Within the range of process parameters investigated in this study, the energy consumption per kg of NOx found to be lowest at 8 kHz and 30 µs, which is 9.1 kWh/kg of NOx for 6870 PPMv of NOx. [@patil_plasma_2016]

## 26 Mar 2018
- Use ammonia, nitrite, nitrate aquarium test strips for efficiency measurements.
- What is the influence of humid air addition to the feed gas? Does it produce ammonia?
- Adding ozone to the resultant gas stream to oxidize NO to NO2 quickly?

# Bibliography

<!--notes-->

<!--links-->
[Sciencemadness]: http://www.sciencemadness.org/talk/viewthread.php?tid=1518
