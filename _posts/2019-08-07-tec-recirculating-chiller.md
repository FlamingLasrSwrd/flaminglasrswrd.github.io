---
layout: post
title: TEC Recirculating Chiller
date: '2019-08-07 19:18'
category: archive
phase: results
tags: chemistry electronics
author: Elijah K. Dunn
zotero-collection: https://www.zotero.org/ekdunn/items/collectionKey/HAQTRVE5
gallery: tec
abstract: |
  Building a general purpose recirculating cooler for the lab.
graphical-abstract: /assets/img/tec/191105-170706-tec-chiller-single-test-final-temp.JPG
---

# Introduction

Thermoelectric (peltier) devices offer a compact and reliable, albeit somewhat inefficient, source of cooling/heating for the lab.

# Work Log

## 16 Nov 2020
I got around to adding a larger reservoir to the TEC chiller project. Prior to this, every time I wanted to change condensers I had to perform a complicated procedure of draining and filling because the reservoir wasn't large enough to accommodate the excess fluid.

![](/assets/img/tec/tec-chiller-v2-overview.JPG)

While the system was apart I decided to add some more insulation. I also had to repair one of the pump connectors that broke.

I replaced the water with a 1:1 mix of water and -50F RV antifreeze. I choose the propylene glycol based antifreeze because it is designed to sit for long periods of time. Unlike the antifreeze intended for cars, it is not routinely sterilized. I am hoping that that will discourage growth in the tubing which I had problems with in the past.

I still cannot get below 5-7C. That could be either the limit of the radiator or the TECs. I'm leaning toward the radiator.

## 15 Jun 2020
I rebuilt the system using just a single layer of TECs and it works much better. I also insulated the cold reservoir with foam.

![](/assets/img/tec/tec-chiller-overview-with-insulation.JPG)

I'm happy with the results, so I am archiving this project.

Sometime in the future I want to install a larger reservoir. Currently, every time I want to exchange condensers, I have to manually add water to fill it. A larger reservoir capable of holding at least one condenser's worth of coolant would be nice.

## 24 Jan 2020
Bought some better thermal paste. The package claims a heat conductance of >3.17 W/(m K) and a thermal resistance of <0.067 C in2/w. I just searched for the cheapest non-drying, silver based paste on eBay. I ended up buying a 5g set of Protronix Series 7 for about $6.

![](/assets/img/tec/tec-chiller-thermal-paste.JPG)

## 09 Nov 2019
First full-scale test is working well. I accidentally hooked the hot side pump in backwards and the TECs upside down, but other than that...

![](/assets/img/tec/191109-104510-tec-chiller-triple-full-scale-test-setup.JPG)

Condensation on the cold line is going to be an issue. Sealing the box and wood completely will help. The cold side should be independently insulated since the box will be warmer than normal. Of course, everything will need to be secured in place. It's all just kind of sitting there.

The hot side reservoir is too small for the flow rate. Air bubbles are swept into circulation.

The cooling fans may be inadequate. Hot side temps hover around 38C. I'm going to put a second pair of fans on the opposite side of the radiator in push-pull mode.

...Definitely better in push-pull mode. The radiator temp is now 34C. It is 24.5C in my room. The cold side hovers between eight and ten Celsius. Kinda disappointing. This is probably the limit of the radiator more than anything. I will buy another one when I get the chance.

The entire system consumes 290W. The pumps and fans consume 13W according to their labels. The power supply is about 90% efficient. So I estimate the TECs are consuming about 250W.

The best part of all is that the whole system is quiet. Very quiet.

The temperature differential at the water blocks is 32.5C (39.4-6.9).

## 06 Nov 2019
The TECs are not an even thickness, having an average variation of +-0.003 inches. This isn't much of a differential for a single unit, but I don't want to stack three thick ones together and get a +9mil difference. I measured each TEC with calipers and grouped them accordingly. It still isn't perfect, but better.

![](/assets/img/tec/191106-101954-tec-chiller-sandwich-nom-nom.JPG)

The top water block was later flipped to better fit the setup.

Except for the project specific items (TECs, heatsinks, etc.), this unit is constructed from materials I have on hand. I use 1/2 inch HDPE sheet for the TEC supports because that's what I have.

![](/assets/img/tec/191106-092714-tec-chiller-triple-support-alignment.JPG)

*hint*: Whenever you are at a second-hand store, look for plastic cutting boards and stainless baking sheets. They are cheaper than buying these materials new.

I'm worried about bacteria growth in the closed loop (hot) side. I'm looking at using ethylene glycol and methanol. [A good resource](https://www.overclockers.com/pc-water-coolant-chemistry-part-ii/).

The water blocks and radiator are made from aluminum. The pump is ceramic. ABS, Nylon, PVC, and tygon are used as well.

ABS does not tolerate methanol at all. I think I will take a trip to the automotive store and look at the various additives. A pool algaecide containing "alkyl dimethyl benzyl ammonium chloride" (benzalkonium chloride) or similar might be work looking into.

I'm going to leave the system open for now. After some use, I want to see if a temp controller can be used for setting hot/cold working fluid temps.

The TEC stack is currently set so that the two cold side units are in series and in parallel with the hot side unit. So the two cold units receive 6V each and the hot unit, 12V.

## 05 Nov 2019
I finally got around to working on this project again. Turns out that I needed to spend more on nylon hose barbs than the TECs.

Picked up some 1.5" PVC end caps and 1/4" nylon hose barbs. The initial test run will just be with a single TEC just to see what kind of chilling I can achieve.

Phew! Leveling these cheap water blocks is a serious work out. First with 120 grit then 800. A belt sander would be so much easier. The leveling is more for equalizing the pressure on the TECs than efficient heat transfer.

![](/assets/img/tec/191006-140024-tec-chiller-single-sanded-water-blocks.JPG)

Test run with a single TEC was excellent. The hot loop only requires about 100ml of working fluid.

![](/assets/img/tec/191105-170706-tec-chiller-single-test-final-temp.JPG)

## 24 Aug 2019
I'm picking out some fans. Let's calculate the minimum air flow needed to move that heat away from the radiator.

$q = \frac{h_{s}}{c_{p} \rho \Delta T}$

For an explanation see [Engineering Toolbox](https://www.engineeringtoolbox.com/cooling-heating-equations-d_747.html).

In order to capture 400W at a temperature differential of 5C, 140cfm would be required. 15C requires only 70cfm. That's entirely within the range of 120mm fans (typically 40-150cfm each). So I believe the limiting factor here is really the heat transfer from the radiator to the air.

$1 m^{3} = 35 ft^{3}$

Forced air heat transfer from a radiator to metal is really complicated.

The maximum flow necessary to minimize the temperature gradient between water and radiator occurs at 100-150 liters per hour [@thoren_development_2011]. Exactly on par with my pump selection. At that flow rate the temperature delta is around 1C.

Fans in a push-pull configuration result in a one degree performance gain when compared to a single fan at the same noise level: Hardly worth the extra cost. Pressure drop across a tiny radiator is negligible (0.2mm H2O). Pull-intake single fan configuration is the best. [@thoren_development_2011]

## 13 Aug 2019
Car heater cores are so much cheaper. The only difference I see is that computer radiators are designed for maximum inlet-outlet temperature differential while car heater cores are designed to transfer the maximum amount of heat. This is called double and single pass radiators. Also, computer radiators have convenient screw holes for fans.

My fume hood stands almost 2 meters tall. So that is the maximum pump height I need. Realistically, only 1.5 is necessary. I also do not need much flow at this height. A maximum of one or two liters per minute (16gph) should be sufficient. Diaphragm pumps can easily pump to this height, but lack flow, stealth, and longevity. Centrifugal pumps do not easily pump to this height.

With a tec system, the pumps will not be submerged. It is difficult to find a small enough centrifugal pump that isn't designed to be submerged...

I finally settled on [this pump](https://www.ebay.com/itm/DC-12V-Large-Flow-Micro-RS-365-Circulating-Water-Pump-Small-Impeller-Water-Pump/323819336110) after looking through hundred of listings. I bought 3 just in case one is faulty. They are only $4 each. Unfortunately, they won't arrive for weeks: The price we pay for cheap Chinese electronics.

## 10 Aug 2019
[120W TEC chillers](https://www.ebay.com/itm/Thermoelectric-Peltier-Refrigeration-Water-Chiller-Cooling-System-Cooler-120W-MF/282658506038) are available for about $40. I imagine that they pump significantly less than 120W, however.

I ordered 9 TEC1-12170s, two 120mm liquid cooler blocks, and one 240mm radiatior. I should have bought two radiators, but the eBay seller only had one available.

[Formulas](https://thermal.ferrotec.com/technology/thermoelectric-reference-guide/thermalref12/) for calculating pumping characteristics of cascaded TECs.

## 08 Aug 2019
It would take approximately 750W to boil 1L of water per hour.

MAX1978 is a single chip driver for peltier units. If precise temperature control is needed, this is where to start. For my purposes, $24 to power 30W is just too expensive. [A lot of good info from Maxim Integrated](https://www.maximintegrated.com/en/app-notes/index.mvp/id/3318).

A full H-bridge with PWM control seems like an efficient option.

## 07 Aug 2019
Today my old chiller decided to quit. This is the second time it has done so. I was distilling some acetone at the time. I quickly rigged up a ice water bath chiller and disconnected the hoses from the old one. Several hours of smooth distillation went by without a problem. I went outside to walk the dog. During that unattended ten minutes or so, the old chiller decided to start up again (I had forgotten to unplug it) and spill all of its cooling fluid over my bench and floor.

So.... ya. I'm going to build a better, more reliable system. I'm starting with TECs because of the compact size.

From [here](https://www.thermoelectric.com/liquid-chillers/bench-top/) it looks like 200-400 watts is common for bench top models.

[Cooling capacity of radiators](https://www.youtube.com/watch?v=gohE6cytlFU) is about ~100W per 120mm section. [These radiators](https://www.ebay.com/itm/240mm-Computer-Water-Cooling-System-Liquid-Heat-Exchanger-Row-Radiator/133034582945) are extremely cheap. Two should be sufficient (400W capacity).

A standard server power supply with PWM can be used to set the perfect voltage for each TEC. Alternatively, you can take a small hit on performance and just go with straight 12v each.

For the __TEC1-12107__:

$T_{hot} = 25^{\circ}C, V = 12.0v; T_{cold} = 0^{\circ}C$

$\Rightarrow Q_{i} = 96W$
$\Rightarrow Q_{c} = 50W$
$\Rightarrow COP = 0.52$

$T_{hot} = 25^{\circ}C, V = 6.0v; T_{cold} = 0^{\circ}C$

$\Rightarrow Q_{i} = 24W$
$\Rightarrow Q_{c} = 15W$
$\Rightarrow COP = 0.63$

# Bibliography

<!--notes-->

<!--links-->
