---
layout: "post"
title: "Chocolate Tempering Machine"
date: "2021-01-07 15:50"
category: active
tags:
author: Elijah K. Dunn
zotero-collection:
gallery:
abstract: >

graphical-abstract:
---

# Prior Art

- [Arduino Temperature Controller | Instructables](https://www.instructables.com/Arduino-Temperature-Controller/)
- [TA4 Temp Controller Datasheet](https://blog.uvm.edu/cwcallah/files/2016/04/Mypin-TA4-manual1.pdf) (my current PID controller for reference)
- [W1209 Temp Controller Datasheet](http://ecx.images-amazon.com/images/I/81dGNBNb9ES.pdf) - cheap on/off relay controller
- [Arduino PID Temp Controller | Nuts and Volts](https://www.nutsvolts.com/magazine/article/arduino-pid-temperature-control) - a veggie canning controller (very similar to my project)

# Work Log

## TODO

- [ ]

## 10 Jan 2020
I think for my purposes, sous-vide is sufficient. However, I would like to have more control that my simple TA4 temp controller can provide.

The ideal chocolate tempering machine should have heating and cooling. Programmable tempering profiles would be awesome. So some sort of control + display is warranted.

Since this is likely going to be a multipurpose machine, named PID profiles would also be nice (e.g. "2L bath"; "5L bath").

On-off and heating/cooling indicator lights could be beneficial. SSR would be better for control, but relays will work.

Commercial PID temperature controllers also have alarm pins for high/low voltages and autotune functions. Thermosensor offset (single value, linear, or lookup table) and type is also necessary.

Hopefully, the design will be general enough to be useful in other processes such as brewing and seed incubation.

Furthermore, the design could be incorporated into future projects like a hydroponics controller.

I know that there are some good controllers already on the market. Inkbird has become a household name for consumer grade control systems. But I want something with heating/cooling profiles so I can just set the chocolate up and let it run.

A TFT screen would be useful to visualize the temperature profile.

I suspect a RTC would be useful.

The age-old question: raspberry pi or arduino? I like the idea of http control.
The ESP8266 wifi module for arduino is cheap. But the cost of the wifi module and arduino uno is about the same as a rasp pi zero W. I think I like python so I'll just use raspberry pi.

## 07 Jan 2020
I've been making a lot of candy and chocolate recently. Maybe that's the cause of some of my weight gain?

Anyway... the subject of chocolate tempering is fascinating to me.

I want a simple machine with minimal hold-up. It should be capable of either temperature or seed crystallization. It should have a dispenser for enrobing or mold filling.

Continuous would be nice, but batch is just fine.

### Dispenser
The low hold-up requirement prevents the design incorporating the Archimedes screw type pump used in cheap chocolate fountains (even though it would be cool looking). That leaves plate and belt type dispensers.

Belt dispensers have more moving parts.

## {{ "2021-01-07 15:50" | date: "%d %b %Y" }}

Project Created!

# Bibliography

<!--notes-->

<!--links-->
