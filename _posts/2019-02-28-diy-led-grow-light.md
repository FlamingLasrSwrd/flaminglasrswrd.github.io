---
layout: "post"
title: "DIY LED Grow Light"
date: "2019-02-28 15:14"
category: active
phase: results
tags: biology electronics
author: Elijah K. Dunn
zotero-collection:
gallery: ledGrowLight
abstract: >
  Designing a low-cost, high-performance LED grow light for plants.
graphical-abstract: /assets/img/ledGrowLight/ledGrowLight-quick-test.JPG
---

# Intro
Now that I have built a small hydroponic herb garden, I need a better light source. Single CFLs in shop light fixtures just don't cut it anymore. LEDs seem like a viable option.

# Current Plan
[cart](https://www.digikey.com/short/pqrn10)

- 2 x *BXRE-40E6500-D-73*
- 7 x *BXRE-27G6500-D-73*
- 3 x *ELG-150-C1400A*[^5]

Total: 52,251 lumens @ 460 watts

# Work Log

## 18 Apr 2021
Just uploading my [strip light cost comparison](/assets/doc/striplights-digikey.ods).

## 24 Nov 2020
I am building a new grow light for a small succulent garden.

I would like this grow light to be self-standing and be somewhat visually appealing. With my new 3D printer, I have the capability to make the electronics enclosure from the ground up with relative ease.

I bought a SL-B8T4N90LAWW strip and IDLC-45-1050 supply. The succulent box that this light is intended for is meant to sit astride a 4x4 post. So there is a 3 5/8" cavity that the electronics can occupy. [It looks like this](https://www.homedepot.com/p/Bloem-Deck-Rail-Planter-24-in-Terra-Cotta-Plastic-Deck-Rail-Planter-477241-1001/301861704).

The plan is to have all of the electronics in a box that sits on the table and slides into the post cavity. The box will contain the power supply and a digital timer. The weight of the box will keep the lamp arm from tipping over (hopefully).

![image](/assets/img/ledGrowLight/ledGrowLight-succulent-light-electronics-box-dims.JPG)

I bought a [cheap plug in digital timer](https://www.menards.com/main/electrical/light-switches-dimmers-outlets/outlet-timers/smart-electrician-reg-digital-timer/81339/p-3149259783272843-c-6471.htm) and gutted it.

![image](/assets/img/ledGrowLight/ledGrowLight-succulent-light-timer-disassembled.JPG)

Initially I thought that the front panel was too complicated to reproduce, so I sketched the layout reusing the faceplate as a whole.

![image](/assets/img/ledGrowLight/ledGrowLight-succulent-light-electronics-box-draft.JPG)

But ultimately I decided that I should just do the work and model the faceplate. This will be a good opportunity to learn more CAD. After attempting a couple times to trace over a picture, I decided that I needed more accurate measurements if I wanted it to work. So I ordered some calipers.

And now I await Amazon.

## 22 Oct 2020
I made a small succulent garden for a friend a few months ago. Now that it is fall, the plants need some supplemental lighting.

I selected a Samsung ‎SL-B8T4N90LAWW‎ strip light and a Mean Well IDLC-45-1050‎ to power it.

## 17 Nov 2019
I gave the prototype panel to a friend for his basement aquaponics setup. He is so happy with the lighting intensity, he asked if I could build another one.

### Cost Breakdown

| Item | Cost per Item | Units | Total |
| ---- | ------------- | ----- | ----- |
| BXRE-27G6500-D-73 | $10.85 | 2 | $21.70 |
| BXRE-40E6500-D-73 | $10.85 | 1 | $10.85 |
| ELG-150-C1400A    | $47.52 | 1 | $47.52 |
|Arctic Alpine 64 GT cooler| $8.52 | 3 | $25.56 |
| AC110-12V 10W PS  |  $6.19 | 1 |  $6.19 |
| Cellular PVC ceiling tile 4 sq ft | $13.45 | 0.5 | $6.73 |
| SPST 250V 10A rocker switch |  $0.60 | 1 | $0.60 |

So a total of $119.48. Plus a few connectors, wire, hooks, shipping, etc. Call it **$130 per panel in materials**

Each panel only takes 2-3 hours to assemble. Probably a lot less if some sort of standardized manufacturing was involved.

## 21 Aug 2019
Ran some thermal tests today on the mostly finished panel. With an ambient temperature of 25C, the temperature of the heat sink edge stayed around 34C. Just next to the COB the temperature leveled off around 42C: 98% relative luminous flux according to the [the datasheet][]. The temperature can approach 57C if the panel is laid flat on a table. Even then the relative luminous flux is around 95%. The heat sinks return to 30C after only a minute when COB power is removed. I am happy with these thermal tests.

![image](/assets/img/ledGrowLight/ledGrowLight-thermal-testing.JPG)

It is impossible to work on this panel without sunglasses.

## 20 Aug 2019
Bought some IP65 12V power supplies for the fans instead of attempting to rig one of my own from an old wall wort. They were $6 each for 10W. That's enough for a set of three fans.

## 19 Aug 2019
This page is apparently one of my most popular, despite its lack of practical information.

I ran a quick test of one of the COBs, blinding myself in the process. Damn these things are bright. I think I will go with a flat plate support instead of the aluminum bracketing I originally planned.

![image](/assets/img/ledGrowLight/ledGrowLight-quick-test.JPG)

I picked up a 2'x2' stucco ceiling panel. It isn't actually stucco, it is PVC foam. It just has a stucco pattern for looks. I cut it in half to make two panels that can be adjusted as needed. Three COBs per panel is a little luminous (~9Klumens per square foot), but the driver can be adjusted.

![image](/assets/img/ledGrowLight/ledGrowLight-cut-panel.JPG)

![image](/assets/img/ledGrowLight/ledGrowLight-heatsink-hole-trace.JPG)

![image](/assets/img/ledGrowLight/ledGrowLight-heatsink-hole-cut.JPG)

![image](/assets/img/ledGrowLight/ledGrowLight-heatsink-clips.JPG)

![image](/assets/img/ledGrowLight/ledGrowLight-heatsink-holes.JPG)

The panel is currently utilizing two BXRE-27G6500-D-73 and one BXRE-40E6500-D-73 driven with a single ELG-150-C1400A. When they arrive, a separate 12V power supply will run the fans.

## 12 Mar 2019
What about the cost of increasing to 10,000 lux/sq.ft.? The price per square foot will change, but the choice of COBs will not. Two drivers can provide power enough to illuminate 3.4 sq.ft.. I think I would like at least 5 sq.ft. of grow room so buying 3 drivers is probably better (52,251 lumens: 5.2 sq.ft. at 10,000 or 7.5 at 7,000). That's 421 watts consumed and $23-$25 per month in electricity. Plus a little for loss from the drivers.

**1 lumen per square foot is 0.0929 lux**

## 11 Mar 2019
Heat sink? I would prefer active cooling. [ARCTIC Alpine 64 GT](https://www.amazon.com/gp/product/B001A5V1K2) looks pretty good. I will tap some blind holes for mounting bolts. It features an 80mm fan and dissipates 65W all for the low price of $7.87.

## 03 Mar 2019
I looked into LED strip lights AKA Quantum Boards. From what I have looked at they are generally the same as COBs. [LED strips | digikey]. The [SI-B8T341B2CUS](https://www.digikey.com/product-detail/en/samsung-semiconductor-inc/SI-B8T341B2CUS/1510-2215-ND/6623999) strip is slightly higher cost but has similar efficiency and light output. The only categorical advantage I can see is the distribution of the light over a wider area.

## 02 Mar 2019
What about driving the diodes in series instead of using a single supply for each diode? So glad my physics degree is helping me with this project.

[Wiring LEDs in Series and Parallel](http://ledgardener.com/wiring-led-cobs/)

So now the 50V COBs seem like a good option. Two in series would be close to line voltage so a constant current supply would have pretty good efficiency even with linear voltage regulators. CMT2890, CMT2870, CXM-32 (Luminus Devices) all seem like viable candidates. None of them are clear winners and none are stocked at mouser.

- [CMT2890-0000-000P0B0A40E] & [ELG-240-C1400B]
  - one power supply for a series of two diodes
  - total cost per square foot is $8.80 [^3] (needs additional red diodes)

Basically none of the best COBs are stocked on mouser. The whole CMT series is exactly what I need, but minimum lead times start at 7 weeks. By the time you are reading this, the stocking may have changed.

Or you could wire three CMA1840s in series... 1.1A at 104V. 5000-7000 lumens (1-2 COB per square foot) and only ~$10 each. Still suffers from the stocking issue. The CXB series suffers from terrible efficiency (roughly half the lm/W of the CMA and CMT series).

I just found out that Bridgelux isn't listed on mouser at all. So off to digikey... Bridgelux is so much cheaper!!

It seems that Bridgelux spectrum characteristics are similar to Cree, so my conclusions about color temperature still hold. Probably because they use the same doping materials for the LED manufacture.

Check out [my spreadsheet](/assets/doc/COBs_digikey.ods) for a better price analysis. Some selections:

|     Part Number   |  Cost  |  CCT  |Lumens|Current|Voltage|lm/W|CRI|#/sq.ft.|$/sq.ft. initial|$/sq.ft 1yr|$/sq.ft. 5yr|
| ----------------- | ------ | ----- | ----- | --- | ---- | --- |----| ---- | ------ | ------ | ------- |
| BXRE-40E6500-D-73 | $10.85 | 4000K |  6956 | 1.4 | 33.4 | 149 | 80 | 1.01 | $18.47 | $39.05 | $141.98 |
| BXRC-40E10K0-B-73 |	$24.29 | 4000K | 13585 | 1.8 | 50.7 | 149 | 80 | 0.52 | $20.25 | $40.83 | $143.76 |
| BXRC-27G10K0-B-73	| $24.29 | 2700K | 11611 | 1.8 | 52.0 | 124 | 90 | 0.60 | $23.69 | $48.65 | $173.48 |
| BXRE-27G6500-D-73	| $10.85 | 2700K |  5477 | 1.4 | 33.4 | 117 | 90 | 1.28 | $23.45 | $49.73 | $181.13 |
| BXRE-27E6500-D-73	| $10.85 | 2700K |  6635 | 1.4 | 33.4 | 142 | 80 | 1.32 | $24.20 | $51.36 | $187.14 |

I gave an extra 25% boost to the CRI90s (versus the CRI70s/80s) for 2700K or less bulbs. That pushed the *27Gs* to the top of the list. In reality, it should be a 50% or most boost based on the spectrum graphs.

Essentially we have two options: 50V and 34V. Since you can only buy whole numbers of power supplies, the choice between the two depends on the area of your intended use. We want to maintain a 4:1 ratio of red:blue (citation needed). *BXRE-40E6500-D-73* and *BXRE-27G6500-D-73* can be driven together. For a single driver, the ratio is about 1.6:1 at 2.6 sq.ft.. Two drivers is 3.9:1 at 4.9 sq.ft.. Three drivers is 6.3:1 at 7.3 sq.ft. or 3.1:1 at 8.2 sq.ft. for 2x4000K. I think two drivers and a total of 6 COBs sounds like a plan. Another benefit is that when it comes time to switch to a more red light to induce fruiting in some species, the 4000K COB can be simply switched out for another 2700K. Similarly if plants become elongated because of a lack of blue, an extra 4000K COB can be switched in.

Now to locate a suitable driver... The ELG-150-C1400A looks great. 107V max at 1.4A out with line AC in. Max of 150W and the *C1400A* is adjustable via potentiometer. You can save $3 and buy the non-adjustable *C1400* if you prefer. 91% efficiency isn't too bad. So for about 5 sq.ft. we have 300W (actual) and 34,341 lumens for $155 plus shipping. Check out the [cart](https://www.digikey.com/short/pqrn10) on digikey. I added and extra 2700K COB for switching over later, but it isn't necessary.

Factoring in power for the first year, efficiency of the supplies, etc, the total cost comes to about $280-$340 depending on your cooling solution. An equivalent store bought LED implementation would cost $250 [^4] with no guarantee on the PAR efficiency of the bulbs. Those LED bulbs use about 7% more power in this example and have a slightly shorter lifespan. Personally I think the COBs are worth the extra $50. That would take about 5 years for the COBs to pay for themselves directly based on energy savings. Furthermore, COBS have a 120 degree viewing angle that is aimed directly at the plants. Store-bought bulbs are designed to illuminate all 360 degrees of a room. Even with a great reflector, you would be loosing a significant amount of radiation.

An equivalent CFL implementation would be ~$336 for the first year ($114 purchase price for 22 bulbs and fixtures + $222 for power). Plus the bulbs have a lifespan one-third of LEDs at best. No contest there.

Both COBs have a typical power of 46.8W. Based on [this article](http://ledgardener.com/find-heat-sink-cob/):

- P_th = 46.8 * 0.75 = 35.1 W
- T_a = 20 C
- T_c_max = 105 C
- R_tim = 0.07
- =>R_c_a = (105 - 20)/35.1 = 2.42 C/W
- =>R_h_a = 2.42 - 0.07 = 2.35 C/W

I'm just going to go with actively cooled cheap heat sinks. Trying to find ones specifically for the Gen 7 V22s is ridiculous. The dies are 28mm squared with mounting holes 22.8mm center-to-center. I can always tap my own mounting holes. During initial testing I will run a series of COBs and measure the temperature to make sure everything is within tolerances.

**Mental Note: Remember to solder the connections before mounting the COBs to the heatsink!**

## 28 Feb 2019
Continuing the search for the best LEDs.

Looking at the relative spectral strength graphs from Cree I don't think that it matters for the cool white bulbs if they are CRI 70 or 90. The peaks around 450nm is just about the same. The difference is really apparent for >680nm between different CRIs. CRI 90 is about 50% better at 680nm than CRI 80. One could go with the cheaper CRI 70 for the blue bulbs and get 80 or 90 CRI for the red bulbs. 4000K at 70/80CRI gives the same 450nm performance as 5000K, 5700K, and 6500K the with significant 680nm+ performance. 5000K+ bulbs suffer a lot at 530nm+ for all CRIs. It appears that the 90CRI graph is missing the 4000K line...

In summary, for CREE COBs:

- **2200K/2700K at 80/90 CRI (90 better) for red**
- **4000K at 70 CRI for blue**

Blue light is mostly needed for inhibiting the formation of auxins which causes elongation of the plant. Blue isn't an efficient light source for photosynthesis. So we need just enough blue to keep the plant from growing out of control. 3-4 red for every blue? IDK...

The CMT2850-36V seem the ideal series for LED grow lights. Unfortunately, CRI90s aren't stocked on mouser and they aren't even available on digikey.

[driver search](https://www.mouser.com/Optoelectronics/LED-Lighting/LED-Lighting-Electronics/LED-Drivers-Power-Supplies/_/N-b1aslZ1yzvvqx?Ns=Pricing%7c0&No=50&FS=True&P=1yzot00Z1z0wbceZ1z0ixqeZ1yzneynZ1yzvclyZ1yzt3mqZ1yzvclrZ1yx6g1cZ1yzj353Z1ya6wfoZ1yzrx4u&Rl=b1aslZgjdhnxZ1yxt7boZ1yxt75eSGTb1aslZgjdhnwZ1y92d5bZ1yxt6yqS1y92d3vZ1y92d3uZ1yxt5hjZ1yxt5taZ1yxt5hgZ1yxt5qyZ1y92d5zZ1y92d09Z1yxt62mZ1y92d4uZ1yvvbycZ1yxt69qZ1y92d4vZ1y92d69Z1ywudc1Z1yxa5xuZ1yxa5y0Z1y92d4tZ1y92d6aZ1y92d4wZ1yxa5xkZ1y92d66Z1yxa5xqZ1yxa5xsZ1y92da8Z1y92d1aZ1y92d12Z1y92d8lZ1y92d4sZ1y92d3cZ1yxt5gxZ1y92d8hZ1y92d5cZ1y92d38Z1y92d67Z1y92d4mZ1y92d43Z1y92d20Z1y92d6lZ1y92d8bZ1y92d31Z1y92d0yZ1y92d76Z1y92d18Z1y92d17Z1y92d9qZ1y92d44Z1y92d24Z1y92da5Z1y92d54Z1y92d68Z1y92d4nZ1y92d45GT)
[driver search](https://www.mouser.com/Optoelectronics/LED-Lighting/LED-Lighting-Electronics/LED-Drivers-Power-Supplies/_/N-b1aslZ1yzvvqx?P=1yzot00&Rl=b1aslZgjdhnwZ1yxt5gxZ1y98oauS1yxt69sZ1yxt69qZ1yxt69rZ1yxt69pZ1y92d4bZ1yxt6niZ1y92d51Z1y92d6jZ1y92d4aZ1y92d5oZ1y92d23Z1y92da8Z1y92d4sGTb1aslZer85Z1yzs35aZ1yzrx4uSGTb1aslZgjdhnxZ1yxt7boZ1yxt79sSGT&FS=True&Ns=Pricing|0)

## 27 Feb 2019

Unfortunately, any time you search "plant light lumens" almost every result is marijuana based. Now the government is going to think I'm growing weed in my house. I barely have enough room for me and Murphy, let alone a huge plant. Plus I like the look of my young avocado tree more.

[Here](https://www.cropsreview.com/light-intensity.html) is a good review. I'm aiming for something between overcast weather (1000 ft-cd) and direct sunlight (10,000 ft-cd). 7000 ft-cd seems like a good compromise for direct light plants

I searched for [white, high power LEDs on mouser] subject to the filters:

- 500 lm or more (I don't want to solder more than 10 per sq.ft.)
- 120 degree or more viewing angle (to increase color mixing)
  	- may not be necessary; most LEDs are 115 degree
- COB, Star, and MCPCB - Star package styles
- 2500K-3000K + 5000K-6500K
- In stock

**Choices:**

|         Part Number        | Cost  |Lumens| Wattage| Temp  |lm/W[^2]|
| -------------------------- | ----- | ---- | ------ | ----- | --- |
| [CXA1507-0000-000N0UD427H] | $1.84 |  550 | 14.8 W | 2700K |  77 |
| [CXA1507-0000-000N0HF450F] | $1.78 |  730 | 14.8 W | 5000K | 102 |
| [CXA1512-0000-000F00M40E3] | $2.48 | 1485 | 19.0 W | 5000K | 122 |
| [CXA1512-0000-000F00M40E1] | $2.48 | 1485 | 19.0 W | 6500K | 122 |
| [CMT1407-0000-000N0U0A30U] | $2.80 |  833 |   ?    | 3000K | 122 |
| [CXA1512-0000-000N00M230G] | $2.94 | 1380 |   ?    | 3000K | 114 |
| [CXA1816-0000-000N00P457F] | $3.02 | 1965 | 16.7 W | 5700K | 122 |
| [CXA1512-0000-000N00N20E1] | $3.08 | 1590 | 19.0 W | 6500K | 127 |
| [CXA1816-0000-000N00P230G] | $3.10 | 1830 |   ?    | 3000K | 117 |
| [CXA1512-0000-000F00M230H] | $3.32 | 1380 | 19.0 W | 3000K | 114 |
| [CXA1816-0000-000N00Q20E3] | $3.80 | 2100 | 16.7 W | 5000K | 131 |
| [CXA1820-0000-000N00Q450F] | $3.84 | 2260 | 40 W[^1]|5000K | 115 |
| [CXA1512-0000-000F00M430F] | $4.56 | 1485 | 19.0 W | 3000K | 122 |
| [CMA1516-0000-000N0B0A65E] | $4.80 | 2480 |   ?    | 6500K | 157 |
| [CMA1516-0000-000N0B0A50E] | $4.80 | 2457 |   ?    | 5000K | 156 |
| [CXA2530-0000-000N00T230H] | $5.12 | 3200 |   ?    | 3000K | 112 |
| [CMT1420-0000-000N0U0A50G] | $5.40 | 2441 |   ?    | 5000K | 129 |
| [CXA1830-0000-000N0HT450F] | $5.80 | 3440 | 57.0 W | 5000K | 120 |
| [CXB1820-0000-000N0BS465E] | $5.92 | 2990 |   ?    | 6500K | 156 |
| [CMA1516-0000-00PN0U0A30G] | $6.00 | 2043 |   ?    | 3000K | 130 |
| [L2C5-27901204E0900]       | $6.30 | 2320 |   ?    | 2700K |  90 |
| [CXA2530-0000-000N00U465F] | $6.56 | 3955 | 61.0 W | 6500K | 138 |
| [CMT1922-0000-000N0U0A50G] | $6.60 | 2741 |   ?    | 5000K | 134 |
| [CMA1825-0000-000N0H0A30G] | $6.90 | 3370 |   ?    | 3000K | 139 |
| [CMA1825-0000-000N0U0A57G] | $7.04 | 3152 |   ?    | 5700K | 130 |
| [CMT1925-0000-000N0B0A57E] | $7.20 | 3979 |   ?    | 5700K | 166 |
| [CMT1922-0000-000N0H0A30G] | $7.26 | 2930 |   ?    | 3000K | 142 |
| [CMT1925-0000-000N0H0A30G] | $7.92 | 3380 |   ?    | 3000K | 141 |
| [CXA2540-0000-000N00W40E3] | $8.06 | 5225 | 86.0 W | 5000K | 133 |
| [CMT1930-0000-000N0H0A30G] | $8.80 | 3920 |   ?    | 3000K | 142 |
| [CMA1840-0000-000N0U0A50G] | $9.00 | 4957 |   ?    | 5000K | 130 |
| [CMA1840-0000-000N0H0A30G] | $9.46 | 5300 |   ?    | 3000K | 139 |
| [CMA1840-0000-000N0B0A65E] | $9.46 | 6114 |   ?    | 6500K | 160 |
| [CMA1840-0000-000N0B0A57E] | $9.46 | 6238 |   ?    | 5700K | 163 |
| [L2C5-30801208F1500]       | $9.69 | 4717 |   ?    | 3000K | 151 |
| [CMT1945-0000-000N0H0A30G] |$10.56 | 5710 |   ?    | 3000K | 137 |
| [L2C5-30801211F1900]       |$13.95 | 6305 |   ?    | 3000K | 151 |
| [CMA2550-0000-000N0H0A30G] |$15.00 | 6850 |   ?    | 3000K | 144 |
| [CMT2850-0000-000N0B0A50E] |$17.60 | 8058 |   ?    | 5000K | 170 |
| [CMT2850-0000-000N0H0A30G] |$17.60 | 7050 |   ?    | 3000K | 148 |
| [CMT2870-0000-000P0B0A50E] |$24.20 |10801 |   ?    | 5000K | 163 |
| [CMT2870-0000-000P0H0A30G] |$24.20 | 9450 |   ?    | 3000K | 143 |
| [CMT2890-0000-000P0B0A65E] |$30.00 |13473 |   ?    | 6500K | 164 |
| [CMA3090-0000-000Q0H0A30G] |$30.00 |11720 |   ?    | 3000K | 145 |
| [CMT2890-0000-000P0B0A50E] |$33.00 |13350 |   ?    | 5000K | 162 |
| [CXM-32-65-80-54-AC00-F2-5]|$37.08 |17805 |140.0 W | 6500K | 135 |
| [CXM-32-50-80-54-AC00-F2-5]|$37.08 |17880 |140.0 W | 5000K | 136 |
| [CVM-32-56-95-54-AC00-F2-3]|$67.28 |24800 |   ?    | 5600K | 107 |

**?**: not listed

[LED price analysis (spreadsheet)]

**Selected:**

|        Part Number       |  Cost |  Temp |1yr Cost|  Volt  |Current | Power  |
| ------------------------ | ----- | ----- | ------ | ------ | ------ | ------ |
| CMA1840-0000-000N0B0A65E | $9.46 | 6500K | $29.99 | 34.7 V | 1.10 A | 38.2 W |
| CMA1840-0000-000N0B0A57E | $9.46 | 5000K | $29.43 | 34.7 V | 1.10 A | 38.2 W |
| CMT1945-0000-000N0H0A30G |$10.56 | 3000K | $35.33 | 34.7 V | 1.20 A | 41.6 W |
| L2C5-30801208F1500       | $9.69 | 3000K | $34.68 | 34.8 V | 0.90 A | 31.3 W |

Each lamp should occupy around 1 square foot (~7000 lumens). Each lamp requires [a constant current supply]. The Lumileds 3000K product has a slightly lower cost, but the power supply is more expensive. Overall it is best to stick with the three Cree products listed.

[ALD-E100] -> 1050mA @ 45VDC; input: 50VDC; $13.26 each

The driver relies on a buck converter so the efficiency is ~95%. You can spend an extra dollar and get the [version with lead wires], but I like the terminal type. I will have to provide 50VDC input to the converters. Several amps worth... *totally infeasible*

[LPC-60-1050] - 1050mA @ 48VDC; input: 90-264VAC; $16.02 each

Much better. Efficiency took a hit (87%), but that's just the cost of reducing the voltage from line.

So the total cost is a little more than $25 per square foot. A comparable CFL implementation is perhaps half that cost but probably use twice the power.

**I did all this work and didn't take into account the CRI!!!**

The spectral diagram for the 90 CRI bulbs is much close to ideal for chlorophyll. Looks like 3500K, 3000K, and 2700K are all basically identical for 600nm+. 5000K, and 5700K are identical below 500nm.

[A better search]


# Bibliography

[^1]: Uses almost the same forward current and voltage as the 16.7W version. Probably a misprint.
[^2]: Extracted from digikey, which used average lumens instead of minimum lumens.
[^3]: Assume 12 total square feet; two 4000k bulbs and four 2700K bulbs; 2200 ft-cd
[^4]: 23x100W-equivalent bulbs at 1500 lumens per bulb costing $2.39 each with $6 per bulb per year electrical cost + $2.36 mounting fixture for each
[^5]: [ELG-150-C1400B] has more dimming capabilities; I would order this one for an additional $2 next time.

<!--links-->

[ELG-150-C1400B]: https://www.digikey.com/products/en?keywords=ELG-150-C1400B

[LED strips | digikey]: https://www.digikey.com/short/pqfh4m

[CMT2890-0000-000P0B0A40E]: https://www.mouser.com/ProductDetail/Cree-Inc/CMT2890-0000-000P0B0A40E?qs=sGAEpiMZZMu4Prknbu83y%252BlrQIM%2FH7mNu789bQ27ReqfnTvG008j2w%3D%3D
[ELG-240-C1400B]: https://www.mouser.com/ProductDetail/MEAN-WELL/ELG-240-C1400B?qs=sGAEpiMZZMvV8Y9YugmIgk59%2FApAE%2FIVB3MmBjWTkYEX60FVWGQkJg%3D%3D

[LED price analysis (spreadsheet)]: /assets/doc/LED_price_analysis.ods

[A better search]: https://www.mouser.com/Optoelectronics/LED-Lighting/LED-Emitters/High-Power-LEDs-White/_/N-8usfjZ1yzvvqx?P=1yooko6Z1yonoecZ1yci252Z1yxpyhjZ1yxq3mwZ1yxptx8Z1yxpu8sZ1yvhvgeZ1yzt855Z1yzrumgZ1yzt876Z1yzt85wZ1yzt83qZ1yzt84hZ1yzt86sZ1yzt87eZ1yzt879Z1yzt851Z1yzt850Z1yzt86z&Rl=8usfjZgjdhgkZ1y8tpzvZ1y9gvpdSGT&Ns=Pricing|0

[LPC-60-1050]: https://www.mouser.com/ProductDetail/MEAN-WELL/LPC-60-1050?qs=sGAEpiMZZMvV8Y9YugmIgv34XFuep%2F6U%252B4%252B4n69ZSZA%3D

[version with lead wires]: https://www.mouser.com/ProductDetail/Cincon/ALD-E100-LW?qs=sGAEpiMZZMvV8Y9YugmIggXPjVR9iwOZ%252BfAiagcLvnGiEA7R4KLRgg%3D%3D

[ALD-E100]: https://www.mouser.com/ProductDetail/Cincon/ALD-E100?qs=sGAEpiMZZMvV8Y9YugmIggXPjVR9iwOZ65yiH4kerU6FpV7Xpe3NuA%3D%3D

[a constant current supply]: https://www.mouser.com/Optoelectronics/LED-Lighting/LED-Lighting-Electronics/LED-Drivers-Power-Supplies/_/N-b1aslZ1yzvvqx?P=1yzot00&Rl=b1aslZgjdhnxZ1yxt71pZ1yxt66zSGTb1aslZgjdhnwZ1y92d3sZ1yxt61iZ1y92d4nZ1yxt6kxZ1y92d32Z1y92d2cS1yxt78tZ1y92d2rZ1y92d8sZ1y8t2h6Z1y92d4mZ1y9kk49Z1y92d43Z1yxt5rjZ1y9179lZ1yxt5v2Z1y9kk5kZ1y92d20Z1y92d8mZ1y92d6lZ1y9kk4xZ1y92d8bZ1y92d0yZ1y92d76Z1y92d31Z1yxt76mZ1y92d18Z1y92d19Z1y92d9qZ1y92czyZ1y92d16Z1y92d44Z1y92d17Z1y9kk4qZ1y8t2gyZ1y92d24Z1y92d5nZ1yxt6yjZ1y8t2h2Z1y92da5Z1y92d54Z1y9kk4gZ1y92d45Z1y9kk4tZ1y92d5bZ1y92d21Z1y92d29Z1yxt78uZ1y92d30Z1y92d0zZ1yxt6ngZ1y92d8rZ1y92d55Z1y9kk5fZ1y92d58Z1yxt5h2Z1yxt5guZ1y92d25Z1yxt5plZ1y92d2aZ1y9179xZ1y8t2haZ1y92d6oZ1y917aqZ1y92d1sZ1yxt6yqZ1y8t2gxZ1y92d8eZ1y92d8xZ1y92czxZ1y92d1tZ1y92d1zZ1y92d5dZ1y8t2grZ1y92d1xZ1y92d78Z1y92d33Z1y92d46Z1y92d2sZ1y92d2bZ1y9kk4cZ1y9kk3sZ1y9kk4bZ1y92d8wZ1y92d8dZ1y92d1uZ1y92d26Z1y92d5gZ1y98oauZ1y8t7t2Z1y92d2zZ1y92d2lZ1y92d8yZ1yxt5peZ1y92d2vZ1y92d2iZ1y8t7t6Z1y92d2oZ1y92d2jZ1y92d2yGT&FS=True&Ns=Pricing|0

[CVM-32-56-95-54-AC00-F2-3]: https://www.mouser.com/ProductDetail/Luminus-Devices/CVM-32-56-95-54-AC00-F2-3?qs=sGAEpiMZZMu4Prknbu83y1K8cRC5EIEFvY3el1FUptFs%252BteuEHu9Uw%3D%3D

[CXM-32-50-80-54-AC00-F2-5]: https://www.mouser.com/ProductDetail/Luminus-Devices/CXM-32-50-80-54-AC00-F2-5?qs=sGAEpiMZZMu4Prknbu83y8X8A8GeNfW3XrqXS%2FWu7e4dJTWFKYjQBg%3D%3D

[CXM-32-65-80-54-AC00-F2-5]: https://www.mouser.com/ProductDetail/Luminus-Devices/CXM-32-65-80-54-AC00-F2-5?qs=sGAEpiMZZMu4Prknbu83y8X8A8GeNfW39lMZyXx3jggDBGSRd0pQzA%3D%3D

[CMT2890-0000-000P0B0A50E]: https://www.mouser.com/ProductDetail/Cree-Inc/CMT2890-0000-000P0B0A50E?qs=sGAEpiMZZMu4Prknbu83y%252BlrQIM%2FH7mNRbbVdejwrZaURO7fJ%252BTsPw%3D%3D

[CMA3090-0000-000Q0H0A30G]: https://www.mouser.com/ProductDetail/Cree-Inc/CMA3090-0000-000Q0H0A30G?qs=sGAEpiMZZMu4Prknbu83y%252BlrQIM%2FH7mNbH4PJiWU0W%2FcPqHONNE41Q%3D%3D

[CMT2890-0000-000P0B0A65E]: https://www.mouser.com/ProductDetail/Cree-Inc/CMT2890-0000-000P0B0A65E?qs=sGAEpiMZZMu4Prknbu83y%252BlrQIM%2FH7mN9d%2FF7WhtqFutytZM7UDtUA%3D%3D

[CMT2870-0000-000P0H0A30G]: https://www.mouser.com/ProductDetail/Cree-Inc/CMT2870-0000-000P0H0A30G?qs=sGAEpiMZZMu4Prknbu83y%252BlrQIM%2FH7mNUQgijIEw3JKDIRk9wSzdKw%3D%3D

[CMT2870-0000-000P0B0A50E]: https://www.mouser.com/ProductDetail/Cree-Inc/CMT2870-0000-000P0B0A50E?qs=sGAEpiMZZMu4Prknbu83y%252BlrQIM%2FH7mNevciZ8sa1f%2F1P1bvwzRq2Q%3D%3D

[CMT2850-0000-000N0H0A30G]: https://www.mouser.com/ProductDetail/Cree-Inc/CMT2850-0000-000N0H0A30G?qs=sGAEpiMZZMu4Prknbu83y%252BlrQIM%2FH7mNyqoEO86G2AEVZmGlXRTl%252Bg%3D%3D

[CMT2850-0000-000N0B0A50E]: https://www.mouser.com/ProductDetail/Cree-Inc/CMT2850-0000-000N0B0A50E?qs=sGAEpiMZZMu4Prknbu83y%252BlrQIM%2FH7mNkWZt%252B99wlYRSiMYFXDLK%2FA%3D%3D

[CMA2550-0000-000N0H0A30G]: https://www.mouser.com/ProductDetail/Cree-Inc/CMA2550-0000-000N0H0A30G?qs=sGAEpiMZZMu4Prknbu83y%252BlrQIM%2FH7mNUmhtF1XK4RDIV4akWs8wWg%3D%3D

[L2C5-30801211F1900]: https://www.mouser.com/ProductDetail/Lumileds/L2C5-30801211F1900?qs=sGAEpiMZZMu4Prknbu83y%252BlrQIM%2FH7mNvBga5IkufV5RC4jsf8RrVA%3D%3D

[CMT1945-0000-000N0H0A30G]: https://www.mouser.com/ProductDetail/Cree-Inc/CMT1945-0000-000N0H0A30G?qs=sGAEpiMZZMu4Prknbu83y%252BlrQIM%2FH7mNk1WKtD5K3NDXaoz7stG7pg%3D%3D

[L2C5-30801208F1500]: https://www.mouser.com/ProductDetail/Lumileds/L2C5-30801208F1500?qs=sGAEpiMZZMu4Prknbu83y%252BlrQIM%2FH7mNkzGkKSmaOPqHxrQA6BlJbw%3D%3D

[CMA1840-0000-000N0B0A57E]: https://www.mouser.com/ProductDetail/Cree-Inc/CMA1840-0000-000N0B0A57E?qs=sGAEpiMZZMu4Prknbu83y%252BlrQIM%2FH7mNN7w78e5IFouvSMZGA1%2FCqw%3D%3D

[CMA1840-0000-000N0B0A65E]: https://www.mouser.com/ProductDetail/Cree-Inc/CMA1840-0000-000N0B0A65E?qs=sGAEpiMZZMu4Prknbu83y%252BlrQIM%2FH7mNd2N8rNnXSNDgsyH7f2mwYQ%3D%3D

[CMA1840-0000-000N0H0A30G]: https://www.mouser.com/ProductDetail/Cree-Inc/CMA1840-0000-000N0H0A30G?qs=sGAEpiMZZMu4Prknbu83y%252BlrQIM%2FH7mNL8ReUlYv%252BEb5bYPXzgUNcg%3D%3D

[CMA1840-0000-000N0U0A50G]: https://www.mouser.com/ProductDetail/Cree-Inc/CMA1840-0000-000N0U0A50G?qs=sGAEpiMZZMu4Prknbu83y%252BlrQIM%2FH7mNfKslDMyGrBQWiRqT%2FJgHZA%3D%3D

[CMT1930-0000-000N0H0A30G]: https://www.mouser.com/ProductDetail/Cree-Inc/CMT1930-0000-000N0H0A30G?qs=sGAEpiMZZMu4Prknbu83y%252BlrQIM%2FH7mNwGnVpD6OEVoxBK4ywQp1zg%3D%3D

[CXA2540-0000-000N00W40E3]: https://www.mouser.com/ProductDetail/Cree-Inc/CXA2540-0000-000N00W40E3?qs=sGAEpiMZZMu4Prknbu83y6noNGF7VgVo2kRvablqBIA%3D

[CMT1925-0000-000N0H0A30G]: https://www.mouser.com/ProductDetail/Cree-Inc/CMT1925-0000-000N0H0A30G?qs=sGAEpiMZZMu4Prknbu83y%252BlrQIM%2FH7mN4qjrybkgRYOug5nh5GQbvw%3D%3D

[CMT1922-0000-000N0H0A30G]: https://www.mouser.com/ProductDetail/Cree-Inc/CMT1922-0000-000N0H0A30G?qs=sGAEpiMZZMu4Prknbu83y%252BlrQIM%2FH7mNI1ZZselRJsFxaOhgG0P3Bw%3D%3D

[CMT1925-0000-000N0B0A57E]: https://www.mouser.com/ProductDetail/Cree-Inc/CMT1925-0000-000N0B0A57E?qs=sGAEpiMZZMu4Prknbu83y%252BlrQIM%2FH7mNax4Sa5w%2FOapo1DUH5hBnTQ%3D%3D

[CMA1825-0000-000N0U0A57G]: https://www.mouser.com/ProductDetail/Cree-Inc/CMA1825-0000-000N0U0A57G?qs=sGAEpiMZZMu4Prknbu83y%252BlrQIM%2FH7mNrY26LJR6DIkS0D2SK%2FRnbw%3D%3D

[CMA1825-0000-000N0H0A30G]: https://www.mouser.com/ProductDetail/Cree-Inc/CMA1825-0000-000N0H0A30G?qs=sGAEpiMZZMu4Prknbu83y%252BlrQIM%2FH7mNdvoY0L5x2cvnjYgyzV5Elw%3D%3D

[CMT1922-0000-000N0U0A50G]: https://www.mouser.com/ProductDetail/Cree-Inc/CMT1922-0000-000N0U0A50G?qs=sGAEpiMZZMu4Prknbu83y%252BlrQIM%2FH7mNfgjKLZrPlPe3OMUGybOFLw%3D%3D

[CXA2530-0000-000N00U465F]: https://www.mouser.com/ProductDetail/Cree-Inc/CXA2530-0000-000N00U465F?qs=sGAEpiMZZMu4Prknbu83yx7PpVbn5Yo%2F2NixKgNR3SQUmFj%2FbCLpCQ%3D%3D

[L2C5-27901204E0900]: https://www.mouser.com/ProductDetail/Lumileds/L2C5-27901204E0900?qs=sGAEpiMZZMu4Prknbu83y%252BlrQIM%2FH7mNPby6Zwi9MIWGrxWvIocZyA%3D%3D

[CMA1516-0000-00PN0U0A30G]: https://www.mouser.com/ProductDetail/Cree-Inc/CMA1516-0000-00PN0U0A30G?qs=sGAEpiMZZMu4Prknbu83y%252BlrQIM%2FH7mNLmGsmqCAItOREJ9OEWyudA%3D%3D

[CXB1820-0000-000N0BS465E]: https://www.mouser.com/ProductDetail/Cree-Inc/CXB1820-0000-000N0BS465E?qs=sGAEpiMZZMu4Prknbu83y%2FXSy%2FGad3PU3uVBf8FJj4yr%2FXEAC6kHIQ%3D%3D

[CXA1830-0000-000N0HT450F]: https://www.mouser.com/ProductDetail/Cree-Inc/CXA1830-0000-000N0HT450F?qs=sGAEpiMZZMu4Prknbu83y9VUK3Vb4TG%252BgIu8QD06WkO6deyJ2L1JgQ%3D%3D


[CMT1420-0000-000N0U0A50G]: https://www.mouser.com/ProductDetail/Cree-Inc/CMT1420-0000-000N0U0A50G?qs=sGAEpiMZZMu4Prknbu83y%252BlrQIM%2FH7mN1Pf8KEtt3SDgksdEnwRSqA%3D%3D

[CXA2530-0000-000N00T230H]: https://www.mouser.com/ProductDetail/Cree-Inc/CXA2530-0000-000N00T230H?qs=sGAEpiMZZMu4Prknbu83yzLAly4%252BfzjBA4cl2aN16tg%3D

[CMA1516-0000-000N0B0A50E]: https://www.mouser.com/ProductDetail/Cree-Inc/CMA1516-0000-000N0B0A50E?qs=sGAEpiMZZMu4Prknbu83y%252BlrQIM%2FH7mNc0HpWWkEqCfS3omoFELZlQ%3D%3D

[CMA1516-0000-000N0B0A65E]: https://www.mouser.com/ProductDetail/Cree-Inc/CMA1516-0000-000N0B0A65E?qs=sGAEpiMZZMu4Prknbu83y%252BlrQIM%2FH7mNRzeOM4xDe9uyLqki8hbN3Q%3D%3D

[CXA1512-0000-000F00M430F]: https://www.mouser.com/ProductDetail/Cree-Inc/CXA1512-0000-000F00M430F?qs=sGAEpiMZZMu4Prknbu83yx7PpVbn5Yo%2FZ6gQA1p%2F5Q6%252BC5XFczB7dQ%3D%3D

[CXA1820-0000-000N00Q450F]: https://www.mouser.com/ProductDetail/Cree-Inc/CXA1820-0000-000N00Q450F?qs=sGAEpiMZZMu4Prknbu83y0bObCPMgyC%2F6eQrRQzNkhSkJhYnhKewoQ%3D%3D

[CXA1816-0000-000N00Q20E3]: https://www.mouser.com/ProductDetail/Cree-Inc/CXA1816-0000-000N00Q20E3?qs=sGAEpiMZZMu4Prknbu83y6h2xOogBff7jzDTL4ZhH1U%3D

[CXA1512-0000-000F00M230H]: https://www.mouser.com/ProductDetail/Cree-Inc/CXA1512-0000-000F00M230H?qs=sGAEpiMZZMu4Prknbu83y2v%252BSc%2F9JbOgYniy2Jv1gKPBQ7l3rRdnrA%3D%3D

[CXA1816-0000-000N00P230G]: https://www.mouser.com/ProductDetail/Cree-Inc/CXA1816-0000-000N00P230G?qs=sGAEpiMZZMu4Prknbu83y%2FXSy%2FGad3PU3CHVC0WPKtU4ix24cUDGFw%3D%3D

[CXA1512-0000-000N00N20E1]: https://www.mouser.com/ProductDetail/Cree-Inc/CXA1512-0000-000N00N20E1?qs=sGAEpiMZZMu4Prknbu83y9VUK3Vb4TG%252BrrbbPqJKBxI6ejaaDGnPSg%3D%3D

[CXA1816-0000-000N00P457F]: https://www.mouser.com/ProductDetail/Cree-Inc/CXA1816-0000-000N00P457F?qs=sGAEpiMZZMu4Prknbu83y9VUK3Vb4TG%252BohSX5s56yPX4WPzglv2a%252BA%3D%3D

[CMT1407-0000-000N0U0A30U]: https://www.mouser.com/ProductDetail/Cree-Inc/CMT1407-0000-000N0U0A30U?qs=sGAEpiMZZMu4Prknbu83y%252BlrQIM%2FH7mNbJS7OONKC4l5Ca4IoCLLIw%3D%3D

[CXA1512-0000-000N00M230G]: https://www.mouser.com/ProductDetail/Cree-Inc/CXA1512-0000-000N00M230G?qs=%2Fha2pyFadui2tF2f%252BrCuvTbl14KSpr8r%252Bm%252BIIgMjCeYn8Vrjb1pxHV5dmE3SIPXj

[CXA1512-0000-000F00M40E1]: https://www.mouser.com/ProductDetail/Cree-Inc/CXA1512-0000-000F00M40E1?qs=sGAEpiMZZMu4Prknbu83y2v%252BSc%2F9JbOg3SkQEVjlXWroGuudCTL3JQ%3D%3D

[CXA1512-0000-000F00M40E3]: https://www.mouser.com/ProductDetail/Cree-Inc/CXA1512-0000-000F00M40E3?qs=sGAEpiMZZMu4Prknbu83y2v%252BSc%2F9JbOg3k4cF4PoeCPJIEBylxeI%252BQ%3D%3D

[CXA1507-0000-000N0HF450F]: https://www.mouser.com/ProductDetail/Cree-Inc/CXA1507-0000-000N0HF450F?qs=sGAEpiMZZMu4Prknbu83y8%252BOyfcV9kMegqBXZmtFdF0%3D

[CXA1507-0000-000N0UD427H]: https://www.mouser.com/ProductDetail/Cree-Inc/CXA1507-0000-000N0UD427H?qs=sGAEpiMZZMu4Prknbu83y8%252BOyfcV9kMeVgOzvhAxJpU%3D

[white, high power LEDs on mouser]: https://www.mouser.com/Optoelectronics/LED-Lighting/LED-Emitters/High-Power-LEDs-White/_/N-8usfjZ1yzvvqx?Ns=Pricing%7c0&No=100&P=1yooko6Z1yonoecZ1yci252Z1yvhvgeZ1yzt855Z1yzt876Z1yzt87eZ1yzt879Z1yzt851Z1yzt850Z1yzt86z&Rl=8usfjZgjdhgkZ1yzri0aZ1yxt7pySGT

[the datasheet]: https://www.bridgelux.com/sites/default/files/resource_media/Bridgelux%20DS103%20V22%20Gen%207%20Array%20Datasheet%2020181105%20Rev%20N.pdf)
