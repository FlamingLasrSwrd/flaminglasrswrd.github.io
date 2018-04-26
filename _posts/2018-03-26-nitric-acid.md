---
layout: "post"
title: "Nitric Acid"
date: "2018-03-26 11:34"
category: active
tags: chemistry
---
Producing nitric acid from the air using electricity.<!--more-->

# Prior Art
Almost every amateur chemist youtube channel hosts at least one video on nitric acid synthesis. Most of them follow the nitrate salt + sulfuric acid synthesis. While easy and cheap, production in this manner is time consuming and, at least in my attempts, prone to accidents. An alternative method is atmospheric nitrogen fixation with plasma. [Sciencemadness][] has a lengthy discussion on a particular style of this known as a Birkeland-Eyde reactor.

A BE reactor uses a thermal plasma to provide the dissociation energy for nitrogen molecules which then combine with oxygen atoms to produce NO. The reactions here are numerous and ethereal. Unfortunately, the desired conversion to NO is reversible and a considerable amount of energy is wasted in this regard. Even from a theoretical standpoint, the production of ammonia via the Haber-Bosch process is about twice as efficient as the BE process, and almost an order of magnitude better than practically achieved.[^1] A non-thermal plasma process could theoretically be 3-4x more efficient than the HB process.

A number of innovations have arisen since the relatively brute force BE reactor was invented. The current research seems to point to a non-equilibrium plasma process. A mixture of thermal and non-thermal to get the best of both.

# Construction Considerations
## Electrode Material
Copper[^2], stainless steel, carbon steel, molybdenum, and tungsten[^3] have been used as GlidArc electrodes. Due to cost, molybdenum and tungsten are probably out for the amateur chemist. Copper has the benefit of being readily available and easy to machine. Copper pipe could also be water cooled. Stainless might have better chemical resistance, especially to nitric acid if the feed gas contains water vapor. The work function and resistance of a material seem to influence the efficiency somewhat.[^3] Mostly because of the arc effects such as rise time and cycle frequency.

## Power Supply
Frequency, pulse width, and voltage all have an effect on the production of NOx in both concentration and efficiency.

### Frequency
Higher frequencies (>5KHz) are more efficient than mains frequencies.[^4] This is within the range of a simple 555 timer in astable mode.

### Voltage

### Pulse Width

## Feed Gas


# Yield Calculations
Haber-Bosch nitrogen fixation = 0.48 MJ/mol
Glidarc = 4.8 MJ/mol = 1.3 KWh/mol => $0.11/mol
15 mol nitric acid (68%) => $1.65 per liter in electricity costs


# Notes
- Use ammonia, nitrite, nitrate aquarium test strips for efficiency measurements.
- What is the influence of humid air addition to the feed gas? Does it produce ammonia?
- Adding ozone to the resultant gas stream to oxidize NO to NO2 quickly?

[Sciencemadness]: http://www.sciencemadness.org/talk/viewthread.php?tid=1518

# Bibliography
[^1]: Cherkasov, N., A. O. Ibhadon, and P. Fitzpatrick. 2015. “A Review of the Existing and Alternative Methods for Greener Nitrogen Fixation.” Chemical Engineering and Processing: Process Intensification 90 (April): 24–33. https://doi.org/10.1016/j.cep.2015.02.004.
[^2]: Cormier, Jean Marie, Olivier Aubry, and Ahmed Khacef. 2008. “Degradation of Organic Compounds and Production of Activated Species in Dielectric Barrier Discharges and Glidarc Reactors.” ArXiv:0810.5433 [Physics], October. http://arxiv.org/abs/0810.5433.
[^3]: Patil, Bhaskar. 2017. “Plasma (Catalyst) Assisted Nitrogen Fixation: Reactor Development for Nitric Oxide and Ammonia Production.”
[^4]: Yang, Jin, Tianyue Li, Chongshan Zhong, Xinxing Guan, and Can Hu. 2016. “Nitrogen Fixation in Water Using Air Phase Gliding Arc Plasma.” Journal of The Electrochemical Society 163 (10): E288–92. https://doi.org/10.1149/2.0221610jes.
