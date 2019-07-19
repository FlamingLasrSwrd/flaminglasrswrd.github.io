---
layout: "post"
title: "Nitric Acid"
date: "2018-03-26 11:34"
category: active
link-citations: true
tags: chemistry
author: Elijah K. Dunn
zotero-collection: https://www.zotero.org/ekdunn/items/collectionKey/DBGV3U9D
abstract: >
  Atmospheric nitrogen fixation for the amateur using plasma.
---

# Prior Art
Almost every amateur chemist youtube channel hosts at least one video on nitric acid synthesis. Most of them follow the nitrate salt + sulfuric acid synthesis. While easy and cheap, production in this manner is time consuming and, at least in my attempts, prone to accidents. An alternative method is atmospheric nitrogen fixation with plasma. [Sciencemadness][] has a lengthy discussion on a particular style of this known as a Birkeland-Eyde reactor.

A BE reactor uses a thermal plasma to provide the dissociation energy for nitrogen molecules which then combine with oxygen atoms to produce NO. The reactions here are numerous and ethereal. Unfortunately, the desired conversion to NO is reversible and a considerable amount of energy is wasted in this regard. Even from a theoretical standpoint, the production of ammonia via the Haber-Bosch process is about twice as efficient as the BE process, and almost an order of magnitude better than practically achieved.[@cherkasov_review_2015] A non-thermal plasma process could theoretically be 3-4x more efficient than the HB process.

A number of innovations have arisen since the relatively brute force BE reactor was invented. The current research seems to point to a non-equilibrium plasma process. A mixture of thermal and non-thermal to get the best of both.

# Construction Considerations
## Electrode Material
Copper [@cormier_degradation_2008], stainless steel, carbon steel, molybdenum, and tungsten [@patil_plasma_2017] have been used as GlidArc electrodes. Due to cost, molybdenum and tungsten are probably out for the amateur chemist. Copper has the benefit of being readily available and easy to machine. Copper pipe could also be water cooled. Stainless might have better chemical resistance, especially to nitric acid if the feed gas contains water vapor. The work function and resistance of a material seem to influence the efficiency somewhat. [@patil_plasma_2017] Mostly because of the arc effects such as rise time and cycle frequency.

## Power Supply
Frequency, pulse width, and voltage all have an effect on the production of NOx in both concentration and efficiency.

### Frequency
Higher frequencies (>5KHz) are more efficient than mains frequencies. [@yang_nitrogen_2016] This is within the range of a simple 555 timer in astable mode.

### Voltage

### Pulse Width

## Feed Gas


# Yield Calculations
Haber-Bosch nitrogen fixation = 0.48 MJ/mol
Glidarc = 4.8 MJ/mol = 1.3 KWh/mol => $0.11/mol
15 mol nitric acid (68%) => $1.65 per liter in electricity costs

# Log

## 19 Jul 2019
Added two 940C20P15K-F caps to the tank capacitance of the ZVS driver to decrease the frequency. Power levels now peak at about 150W and average around 100W.

## 17 Jul 2019
Several tests were done with the ZVS driver. Total input current to the system at 120V is between 0.5-1.5 amps (up to 15A; 12V). I measured this with a clamp-on multimeter. I was originally attempting to get the frequency below 10kHz by increasing the primary inductance and tank capacitance, but I found that between 5-80kHz, NOx production varies quite little [@yang_nitrogen_2016]. Which is a good thing. A 10kHz 100W whine is annoying. So I will rework the system to optimize for current draw and thus power.

It isn't necessary to run the flyback at higher voltages. The high voltage is merely to start and maintain the arc discharge. It is current we are after. Some systems only use the high voltage to create the arc, then use a low voltage, high current supply to actually do the work.

I also reduced the choke inductance to increase the primary current. It does work, but it runs the risk of destroying your power supply.

Definitely need to use refluxing water as an absorption tower [@lee_process_2017].

I definitely want to build a plasma tornado, if only because it looks awesome [@kalra_gliding_2005-1]. I would need a pump capable of at least 30 liters per minute flow.

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

# References

<!--Annotations-->
[Sciencemadness]: http://www.sciencemadness.org/talk/viewthread.php?tid=1518

<!--Glossary-->
