---
layout: "post"
title: "Marx Generator"
date: "2019-07-20 17:50"
category: active
tags: electronics high-voltage
author: Elijah K. Dunn
zotero-collection: https://www.zotero.org/ekdunn/items/collectionKey/MHSHVY3M
gallery: marx
abstract: >
  Building a high voltage pulse circuit known as a marx generator for Halloween.
graphical-abstract:
---


# Work Log

## 20 Jun 2019
The traditional, amateur Marx generator is triggered via spark gap and uses charging resistors. What about using something better? There are a couple types of triggered spark gaps shown in this paper [@mayes_spark_1999]. Using inductors instead of resistors could be used. They could be wound easily at home for cheap.

\begin{equation}
\beta = N^2 \frac{C'}{C} = \frac{Parallel Capacitance of All C's}{Series Capacitance of All Cs}
\end{equation}

C' is the parasitic capacitance to ground. C is the value of each charging capacitor. This may not be a problem, however, for Marx's that aren't encapsulated in metallic housings. Spark ignition can be started in the middle of the stages to achieve faster rise times. [@buchenauer_optimizing_2010]

An [example](http://users.tm.net/lapointe/Marx_Construction.html) of an amateur design based on inductors instead of resistors.

An [example](https://4hv.org/e107_plugins/forum/forum_viewtopic.php?123977) of one with homemade capacitors.

How to charge? Flyback, MOT, Cockcroft-Walton voltage multiplier?

DIY capacitors? Confirmed: cheap emergency blankets made from aluminized polyester are conductive but only on one side. Mylar (polyester) has a dielectric strength around 7Kv/mil. I doubt these cheap blankets are more than half a mil, so they will need some other form of insulation. They may not be able to take the current, though. Mineral oil soaked kraft paper is cheap. Dissipation factor is higher for oil saturated paper versus plastics. Mylar has a relatively high dissipation factor (0.005) for a polymer [source](http://users.tm.net/lapointe/Plastics.htm). HDPE has about ten times lower dissipation but has a dielectric strength of 5kv/mil. Polypropylene is better still with 8kv/mil and 0.0003. Dielectric constants are all between two and four for the commonly available polymers.

I think oil-impregnated polypropylene is the best option. HDPE sheet is more common, though.

Dual polarity charging reduces the number of required spark gaps by half [@heffernan_fast_2005].

Liquid resistors made from copper sulfate are easy to make out of tubing and copper plugs... [@heffernan_fast_2005] A high voltage probe based on copper sulfate would be awesome and cheap. 22 ohms per centimeter for a saturated CuSO4 solution. A [design calculator](http://www.pulsedpower.net/Applets/PulsedPower/CopperSulfateResistor/CopperSulfateResistor.html).


# Bibliography

<!--notes-->

<!--links-->
