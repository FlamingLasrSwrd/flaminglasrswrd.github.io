---
layout: "post"
title: "Syringe Pump"
date: "2020-06-23 16:41"
category: active
phase: design
tags: chemistry
author: Elijah K. Dunn
zotero-collection: https://www.zotero.org/ekdunn/collections/AC3I2IJV
gallery: syringe-pump
abstract: >
  Tweaking the open source designs of syringe pumps for some microreactor tests.
graphical-abstract: /assets/img/syringe-pump/syringe-pump-poseidon-replication-build.JPG
---

# Parts Selection

The **linear bushings** are the cylindrical type with a 15mm OD. Any of the LM8- series of linear bearings will work. These are are small (17mm), regular (24mm), and large (45mm) versions: LM8SUU, LM8UU, LM8LUU, respectively. The original design fits the small overall length version LM8SUU. I'm going with the lm8uu because it was cheaper.

**688zz bearings** are common type. The cheapest will do since it isn't going fast or experiencing too much radial load.

The **limit switches** are SPST-NO, OFF-MOM, chassis mount, levered (preferably roller) switches ([digikey search string](https://www.digikey.com/short/z9j8dj)). They are also available on eBay by searching for "lever switch" typically under the ["Limit Switches" category](https://www.ebay.com/b/Limit-Switches-/111606).

# Work Log

## TODO

## 11 Dec 2020

I set the current limiting V_ref to 0.180.

YEL - RED - BLU - ORA

## 07 Jul 2020
Some work was done on another project page.

Manually disconnecting the push block from the lead screw to load a syringe would be nice.

## 29 Jun 2020
[Metafluidics | Open Repository for Fluidic Systems](https://metafluidics.org/)

[Poseidon: Open source bioinstrumentation](https://github.com/pachterlab/poseidon)[@booeshaghi_design_2019]

## 28 Jun 2020
There's a question of precision that has to be made here.

If you want precision and a long life, use a lead screw not a threaded rod. [Ditch the threaded rod in your RepRap 3D printer | 3Ders](https://www.3ders.org/articles/20151127-ditch-the-threaded-rod-in-your-reprap-3d-printer-and-upgrade-to-a-lead-screw-z-axis.html)

[This](https://www.youtube.com/watch?v=dz2N6qxstk4) design (video) uses slide in adapters to hold the syringes which can be changed out quickly for different sizes. [Video playlist](https://www.youtube.com/watch?v=sx5VR6oJWaY&list=PLX53bZT1uB5lPl_5kWw40hWeIYNU5rnih&index=1) and [website](https://chem.uncg.edu/croatt/flow-chemistry/).

That site also has a page discussing [tubing for flow reactors](https://chem.uncg.edu/croatt/flow-chemistry/designing-and-connecting-the-tubing/) which is really helpful.

They recommend PFA tubing for flow reactors. I initially decided on stainless because of its heat conductance (~14 W/mK). PFA, PEEK, PTFE, PP, PE tubing all hover around 0.2-0.4. PFA seems to resist just about about everything whereas SS responds terribly to chlorine containing chemicals especially acids.

[**Open-Source Syringe Pump | Mass Spectrometry Laboratory; Moscow State University**](https://www.mass-spec.ru/projects/diy/syringe_pump/eng/) [@samokhin_syringe_2020]

This looks to be exactly what I need.

The large online 3D print services are expensive! The lowest quote I got was $174 for a single pump's worth of parts excluding the case! Or... I could order from TREATSTOCK instead and pay $60 for all three including the cases.

## 27 Jun 2020
After having looked more closely, I think the 500g force sensor will be more useful for my applications. It more closely matches the PendoTech PRESS-S-000 pressure sensor used in the feedback syringe pump model.[@lake_low-cost_2017]

So a 500g load sensor with 0.5% error will need and ADC capable of at least 200 bits.

## 24 Jun 2020

Minimum and maximum flow rates using different syringe sizes based on pump mechanics is given in Table 3.[@garcia_low-cost_2018]

Using 1-50ml syringes gives a minimum flow rate of 0.1 uL/s and a maximum of 2.8ml/s. But that doesn't take into account the maximum force of ~1N that we can measure using the 100g sensor.

The output area of a syringe is standard at 1.3$mm^{2}$. In reality, it is the taper that is standard, but this is just an estimate.

From Bernoulli's equation:

\begin{equation}
\frac{\rho}{2} ( {q_{1}^{2} - q_{2}^{2} \over A^{2}} ) = \Delta P
\end{equation}

This only sort of applies since we are using two different systems and not the same system in two different states.

There has to be a way to calculate the work done by 1N over the plunger travel length and find the flow rate that way... Gah! I see why everyone just uses CFD.

Moving on...

### Control System

That system is a little more elaborate--using a touchscreen control. I like that idea.[@garcia_low-cost_2018] Which brings me on to the concept of control.

A touch screen adds an additional $50-$80 to the project. Some resistive touch screens are in the $30-$40 range. Perhaps web-server control? That would ease the transition to automation via API as well.

Small TFT screens with tactile switches would work and be much cheaper. But they are clunky and not amenable to upgrades. TFT screens come in at $10-$20 depending on the resolution and size. They still might be appropriate for displaying operating data in tandem with a web server backend for major control. LED segment displays might work for the bare minimum of information at around $5.

I think we are splitting hairs here on price.

I wonder if you could use some sort of spring based damper to reduce the variation in force between steps. Since we know the forces involved (<1N), we can easily pick and appropriate spring.

Although an elastomer based solution might be better. A simple butyl rubber cutout placed somewhere in the line of force would probably be sufficient. I bet a plastic plunger (both the seal and piston arm) provides some smoothing. Less so for glass syringes.

Useful Data:

- flow rate
- flow direction
- time elapsed
- time remaining
- status
- total volume delivered
- mode: infusion, continuous
- syringe style/type
- force/pressure
- target volume
- total elapsed infusion time
- time started, ended, current time
- manual control: forward/reverse
- calibration menu

Trying to find a control system or open source protocol to adapt to this system. A completely open source lab, from the software to the hardware would be awesome. Even more so if the data produced was added to a blockchain so that it couldn't be altered later. The data could be encrypted/decrypted for privacy, but it couldn't be altered. Developers could get a reward whenever their control software is used.

Looks like [Standard in Lab Automation | SiLA](https://en.wikipedia.org/wiki/Standardization_in_Lab_Automation) is the only actively developing protocol standard.

[Laboratory Information Management systems | LIMS](https://en.wikipedia.org/wiki/Laboratory_information_management_system) is more of a database than a control protocol. Might be useful to look into any reporting standards here.

### Design

[Syringe Pump Overview | Cole-Parmer](https://www.youtube.com/watch?v=kkQ3RC0657s).

#### Clamps
Some of the open source designs seem to limit themselves on a particular syringe style or size. For instance, the touchscreen version can only accommodate a single syringe size without swapping out different 3D printed parts.[@garcia_low-cost_2018] I think researchers get excited about bespoke 3D parts when generic is often more suitable.

Commercial versions have a rounded or angled well in which the syringe sits with clamping pressure applied with a screw-tightened cross bar (e.g. [kdScientific 100 series](https://www.kdscientific.com/media/catalog/product/cache/1/image/1800x/040ec09b1e35df139433887a97daa66f/k/d/kds-780100-kds100-syringe-pump.jpg)).

The [kdScientific 210](https://www.sisweb.com/art/lc/kds210.jpg) features an adjustable clamp to secure the syringe body flange. This would help relieve tension on the syringe body (and reduce deformation) for both forward and reverse action (infusion and withdraw). A similar clamp is also located on the plunger arm.

[Another example](https://www.chemyx.com/wp-content/uploads/2016/09/DSC_2613.png) from Chemyx.

#### Carriage
There are several variations. Every commercial version I see is horizontal. Although the Cole-parmer versions can be flipped.

Limit switches are commonly used to prevent the carriage from extending beyond the work area boundaries in case of an error. Considering that the overall length of syringes varies considerably with syringe volume, some sort of mechanism for limiting the draw length needs to be in place. This could be implemented in software but a hardware option is better.

## {{ "2020-06-23 16:41" | date: "%d %b %Y" }}
Project Created!

A few open-source syringe pumps have been published.[@wijnen_open-source_2014] [@cubberley_inexpensive_2017] [@garcia_low-cost_2018]

I like the idea of PID pressure feedback for smoother flow.[@lake_low-cost_2017]

My microfluidics work might encompass some corrosive chemicals in the future, so the standard pressure transducers won't work. I tried to find some [compatible sensors on digikey](https://www.digikey.com/short/zhv1w7), but none of them seemed to work. I had to manually look through each datasheet to find the suitable working conditions, btw.

I thought about using some sort of manometer for indirect, non-contact pressure measurement via fluid height. While that might still work, I have a better idea... The pressure can be determined by the force on the syringe (duh!).

Some calibration would be necessary. Syringe (head) size is an obvious factor.

Ultimately we are trying to determine flow rate and use that measurement to keep the flow rate stable over time. Since liquids are (relatively) incompressible, their flow is proportional to pressure.

A thermal liquid flow meter might be useful here and a DIY project worth looking into. Or you could buy a [FS2012 MEMS mass flow sensor from Renesas](https://www.idt.com/us/en/document/dst/fs1012-datasheet) for $44. That measures relatively high flow rates of 1 lpm and is nonlinear at <50ml/min.

The advantages of force measurement compared to pressure are of reusability and non-contact. A single force gauge is required per syringe and the load cell never comes in contact with the working fluid.

### Force Sensor Requirements
Wijnen et. al measured the force produced by their designs, but did not use it as an active feedback mechanism.[@wijnen_open-source_2014] From their data we can determine that our motor-screw combo will output up to 200N. That's ~50psi for a 50ml syringe (1 square inch head size). Lake et. al measured pressures for a simple two-input mixed microreactor from 0-3 psig.[@lake_low-cost_2017]

So I think 0-10 psig is probably common. For a 50 ml syringe, that's about 0-40N (4000g). I'm using a 50ml syringe because I think it is the largest that anyone would use for microreactor work. Using a smaller syringe would reduce the force needed for a given pressure, so consider these values to be a maximum.

If one were to use a 1ml syringe with a head diameter of 0.15 inches and a maximum pressure of 10psig gives 0.8 newtons or 80g of force. That's pretty small. A single load cell for multiple syringe sizes probably isn't going to work if you want any decent level of accuracy.

So we are looking for a load cell (force sensor) capable of measuring 0-4kg for the 50ml design. Fortunately for use, this is a really common size and already used in arduino projects ([SparkFun SEN-14729 | $10.95](https://www.sparkfun.com/products/14729])).

Sparkfun also has a 500g variety ([SEN-14728 | $9.95](https://www.sparkfun.com/products/14728)) and a 100g variety ([SEN-14727 | $8.95](https://www.sparkfun.com/products/14727)).

The 500g variety would allow for measurement of up to 5N. That's up to 1 psi on the 500ml syringe and up to 60psi on the 1ml syringe. I suppose you will have to decide on your process design parameters to pick the best option.

*Note* These calculations are actually in pound-force, but I am too lazy to fix it. You live on the same planet as I do, so they should be similar to pound-mass.

Here's a table to give you a rough idea of the choices. These measurements are based on the random glass syringes I have laying around: YMMV.

| **syringe capacity** | **head diameter** | **100g max** | **100g error** | **500g max** | **500g error** | **5kg max** | **5kg error** |
| ---------------- | ------------- | -------- | ---------- | -------- | ---------- | ------- | --------- |
|      *ml*      |      *mm*       |   *psi*    |     *psi*    |    *psi*   |     *psi*    |   *psi*   |    *psi    |
|  1 |  3.9 | 12    | 0.06   | 60   | 0.3   | 600 | 3    |
|  5 | 11   |  1.5  | 0.007  |  7.5 | 0.04  |  75 | 0.4  |
| 10 | 14   |  0.92 | 0.005  |  4.6 | 0.02  |  46 | 0.2  |
| 50 | 25   |  0.29 | 0.0014 |  1.4 | 0.007 |  14 | 0.07 |

The equation used to calculate these values (using the stated units):

\begin{equation}
P_{max} = \frac{F_{max}}{ 454 \pi (\frac{D}{2*25.4})^2 }
\end{equation}

In other words, a pump with interchangeable syringes 1-50ml with a 100g load cell will allow you to measure from 0-12 psi with a minimum accuracy of 0.06psi. I think this is suitable.

I know that there is a way to calculate the fluid velocity based on these values, but I don't want to get into that right now. We can just assume for now that the flow rate will be the same for a given load cell since the force applied to the plunger is the same. At least, I think that makes sense.

...Or maybe I'm completely wrong and the flow velocity is proportional to the square root of the pressure. Idk. It has been a long time since my fluid dynamics class.

Looks like I have more reading to do. [Microreactors in Organic Chemistry and Catalysts, Second Edition (2013)](https://schoolbag.info/chemistry/microreactors)


# Bibliography

<!--notes-->

<!--links-->
