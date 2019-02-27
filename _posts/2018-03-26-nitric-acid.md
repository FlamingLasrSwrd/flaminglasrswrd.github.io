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


# Notes

# Log

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
