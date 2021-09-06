---
layout: "post"
title: "Marx Generator"
date: "2019-07-20 17:50"
category: active
phase: research
tags: electronics high-voltage
author: Elijah K. Dunn
zotero-collection: https://www.zotero.org/ekdunn/collections/MHSHVY3M
gallery:
abstract: >
  Building a high voltage pulse circuit known as a marx generator for Halloween.
graphical-abstract:
---

# Prior Art

| source | stages | $C_{stage} (nF)$ | $R_{stage} (k\Omega)$ | $L_{stage} (\mu H)$ | $V_{in} (kV)$ | $V_{out} (kV)$ | arc length (cm) | discharge energy (J) | rate (Hz) |
| ------ | ------ | ---------------- | -------------------- | ------------------- | ------------- | -------------- | --------------- | -------------------- | --------- |
| [Jochen's HV][] | 10 | 8 | 2000 | - | 30 | 210$\dagger$ | 30 | 36 | |
| [PocketMagic][] | 2$\times $11 | 5 | 1000 | - | 10? | ? | 20 | ? | 1.4 |
| [Uzzors2k][] | 2$\times $10 | 1 | 990 | - | 20? | ? | 18 | | 14 |

$\dagger$ Calculated. Actual value not directly measured.

# Calculations

$C = K E_{0} \frac{A}{d}\text{, where }E_{0}= 8.854\times10^{-12}$

$C$ is the capacitance of a parallel plate type capacitor. $K$ is the dielectric constant of the material. $A$ is the overlapping surface area of the plates. $d$ is the distance between the plates. $C$ is the capacitance.

$E = \frac{1}{2} C V^{2}$

$E$ is the energy stored in a capacitor in joules. $C$ is the capacitance in Farads. $V$ is the voltage in volts.

# Work Log

## TODO

- [ ] source a kiln for making Calcium Cupric Titanate
- [ ] purify calcium carbonate, copper oxide, titanium dioxide


## 23 Aug 2019
I'm worried about the inductance of the capacitors made by rolling the plates. I'm also curious why some amateurs get away with cheap ceramic capacitors and others use the way more expensive doorknob style caps. It has to be current capabilities.

Looking at the [Vishay HVCC series capacitor datasheet] I find a few interesting things. First of all, the leakage current is huge: for the 1nF cap it is more than 3mA at 10kV. For a 20 or 30 cap generator that is practically all of the current. The rise time is about 1.2 $\mu S$. These caps sell for about $2.72 each.

**Forget plastics! Lets make our our ceramic caps out of barium titanate!**

I literally have the synthesis materials barium carbonate and titanium dioxide in my storage right now. Sintering seems to be the dominant preparation method. Growing pure crystals can be done using hydrothermal methods which are not outside the reach of the amateur.

$BaCO_{3} + TiO_{2} \Rightarrow BaTiO_{3} + O_{2}$

BaTi is available for $1-2 per gram on ebay. Barium carbonate and titanium dioxide are available for $2-4 per pound at a ceramics store. These are likely impure, but may be serviceable. I could even dope the BaTi with strontium because strontium carbonate is also a cheap ceramic material.

Every other synthesis method uses a water soluble titanium salt, which I don't have and I would prefer not to make: titanium oxalate, citrate [@pechini_barium_1966], alcoholate [@di_method_1961], chloride [@selvaraj_preparation_2015], lactate [@walsh_barium_1961].

Interestingly, titanium dioxide is somewhat soluble in various deep eutectic solvents [@tian_application_2010].

Titanium dioxide alone might suffice for a decent capacitor with a dielectric constant of ~50. TiO2 pucks were made by slip casting in plaster molds using dilute ammonia as a dispersant [@chesley_high_1946].

Barium titanate alone may not have a long lifetime [@coffeen_barium_1957]. More research is needed.

Strontium titanate is used to make artificial diamonds. Could be an interesting crystal to grow for its pure beauty.

Calcium copper titanate has a dielectric constant of **10,000** for bulk material at room temperature. The manufacture of which is relatively simple:

> The method normally uses stoichiometric amounts of the common precursors, i.e., CaCO3, CuO, and TiO2 for being mixed with suitable liquid (acetone or ethanol), using ball mill. To remove volatile impurities, the fine powder is calcined at 930 °C for a designated period of time (12 h). An appropriate amount (1 cc mL−1) of a suitable binder (PVA) is added to the powder and mixed uniformly before being compressed to form a pellet shape. The resulting product is first heated slowly (at a heating rate 5 °C min−1) to a particular temperature (1040 °C) to burn off the binder. The mixture is then maintained at this temperature for 10 h for annealing. The sample is later cooled under a controlled rate of cooling (cooling rate 5 °C min−1). [@ahmadipour_short_2016]

There are also wet chemical, combustion, and sol-gel methods. All of these methods require soluble titanium, which I am trying to avoid.

However, the barium titanate doesn't need to do anything but sit in the gap between the plates. This means I could just glue the titanate powder together. Literally glue [@chiang_polymer_2002].

Even if the density is reduced by 10%, who cares. With a dielectric constant of 1150-1600, a huge amount of capacitance can be packed into a small space. Composite materials also have the advantage of being castable. [@slenes_ceramic-polymer_2014]

[@zhang_development_2011] has a large table of polymer composites and their properties. An epoxy-CCTO dielectric would be awesome for the amateur.

Honestly, metal powder polymer composites sound incredibly easy. Aluminum powder of appropriate size is sold by the pound. 80% 3 micron aluminum in epoxy has a maximum dielectric constant of 30. The only problem is the dielectric strength of such a material...

I wonder what the dielectric constant of JB-Weld is?

### Barium Titanate Synthesis Test
1/20th molar scale in a 50ml beaker:

- 4.00g titanium dioxide + 9.87g barium carbonate are mixed
- 27 ml (slight excess) of concentrated hydrochloric acid are added slowly (with vigorous bubbling)
- solution is neutralized with dilute sodium hydroxide (11g)
- barium titanate should precipitate out

**NOTE: Barium salts are extremely toxic. Do not attempt without the proper PPE.**

It looks like titanium dioxide doesn't actually react with hydrochloric acid. I should have known that. The next test will probably be a solid state reaction at high temperature a la [@arendt_molten_1980].

## 22 Aug 2019
Time to start putting down numbers. I think a ZVS driven flyback is my best starting point. A few tens of kilovolts.

> ...the charging time required by the Marx before firing is approximately equal to $2N^{2}RC$ and the resistors reduce the charging efficiency. [@carey_marx_2002]

Some useful design equations for an inductor based design from that paper:

$L_{stage} = {L_{eq} \over n}\\
C_{stage} = n C_{eq}$

$T_{pulse} = 0.8 \partial \sqrt{L_{eq} C_{eq}}$

$V_{out} = 0.7 n V_{charge}$

$Z = n \sqrt{\frac{L_{stage}}{C_{stage}}}$

So let's pick an arbitrary firing rate of about 1 Hz and an arc length of 30cm. This seems scary enough for a Halloween decoration. The dielectric strength of air is around 3kV/mm for infinite spherical electrodes but much less so for needle points. See [Jochen's spark length](http://www.kronjaeger.com/hv/hv/msr/spk/index.html) page for a convenient table.

So my output voltage should be somewhere in the range of 170kV (needle point) and 600kV (50cm diameter spherical electrode). Let's call it 300kV. Also from that table, 2.5cm diameter components (spark gap electrodes, inductor OD's, etc) are sufficient to prevent corona issues at 30kV.

So my requirements thus far are:

$V_{out} = 300kV$

$V_{charge} \approx 30kV$

Therefore:

$n = 14$

Hmmm... Those [flexible cutting mats](https://www.amazon.com/Flexible-Plastic-Cutting-Colorful-Kitchen/dp/B01HN7ZGUQ/) are suitable priced and appropriately thick polypropylene. 38cm x 30cm X 0.5mm. Using just a single sheet dielectric gives a capacitance of about 3.9nF and a dielectric strength of about 10kV (maybe less for a greater margin of error). They can be rolled to an OD of about 3cm.

Four sheets of dielectric would provide the necessary 30kV (45kV for a 50% margin) voltage rating and give a 1nF capacitor.

With my supposed 1nF caps the energy per discharge is:

$E = 6.3J$

Holy hell [that's](https://www.youtube.com/watch?v=ojcUpDwt6FQ) a big Marx generator.

## 31 Jun 2019
Take a look at this [440KV inductor based unit](https://www.youtube.com/watch?v=Yo618eM7rUc). The comments are enlightening.

## 20 Jun 2019
The traditional, amateur Marx generator is triggered via spark gap and uses charging resistors. What about using something better? There are a couple types of triggered spark gaps shown in this paper [@mayes_spark_1999]. Inductors instead of resistors could be used. They could be wound easily at home for cheap.

\begin{equation}
\beta = N^2 \frac{C'}{C} = \frac{\textrm{Parallel Capacitance of All C's}}{\textrm{Series Capacitance of All Cs}}
\end{equation}

C' is the parasitic capacitance to ground. C is the value of each charging capacitor. This may not be a problem, however, for Marx's that aren't encapsulated in metallic housings. Spark ignition can be started in the middle of the stages to achieve faster rise times. [@buchenauer_optimizing_2010]

An [example](http://users.tm.net/lapointe/Marx_Construction.html) of an amateur design based on inductors instead of resistors.

An [example](https://4hv.org/e107_plugins/forum/forum_viewtopic.php?123977) of one with homemade capacitors.

How to charge? Flyback, MOT, Cockcroft-Walton voltage multiplier?

DIY capacitors? Confirmed: cheap emergency blankets made from aluminized polyester are conductive but only on one side. Mylar (polyester) has a dielectric strength around 7KV/mil. I doubt these cheap blankets are more than half a mil, so they will need some other form of insulation. They may not be able to take the current, though. Mineral oil soaked kraft paper is cheap. Dissipation factor is higher for oil saturated paper versus plastics. Mylar has a relatively high dissipation factor (0.005) for a polymer [source](http://users.tm.net/lapointe/Plastics.htm). HDPE has about ten times lower dissipation but has a dielectric strength of 5kv/mil. Polypropylene is better still with 8kv/mil and 0.0003. Dielectric constants are all between two and four for the commonly available polymers.

I think oil-impregnated polypropylene is the best option. HDPE sheet is more common, though.

Dual polarity charging reduces the number of required spark gaps by half [@heffernan_fast_2005].

Liquid resistors made from copper sulfate are easy to make out of tubing and copper plugs... [@heffernan_fast_2005] A high voltage probe based on copper sulfate would be awesome and cheap. 22 $\Omega$ per centimeter for a saturated $CuSO_{4}$ solution. A [design calculator](http://www.pulsedpower.net/Applets/PulsedPower/CopperSulfateResistor/CopperSulfateResistor.html).

[A discussion on water resistors](https://web.archive.org/web/20191219110824/home.earthlink.net/~jimlux/hv/rwater.htm).

# Bibliography

<!--notes-->

<!--links-->
[Jochen's HV]: http://www.kronjaeger.com/hv/hv/pro/marx/
[PocketMagic]: https://www.pocketmagic.net/marx-generator/
[Uzzors2k]: https://uzzors2k.4hv.org/index.php?page=180marxgen
