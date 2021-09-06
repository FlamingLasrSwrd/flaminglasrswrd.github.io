---
layout: "post"
title: "Thermoacoustic Refrigerator"
date: "2021-02-17 23:14"
category: active
tags: chemistry
phase: exploratory
author: Elijah K. Dunn
zotero-collection: https://www.zotero.org/ekdunn/collections/6AG25HBX
gallery:
abstract: >
  Maybe a 3D printable acoustic cold trap?
graphical-abstract:
---

# Intro

So I need a cold trap to protect my vacuum pump.

# Design Considerations

For the initial design we will stick to 1 atm air as a working fluid, a loudspeaker driver, and PLA construction.

# Work Log

## TODO

- [ ]

## 20 Mar 2021
Watch [Acoustic Cooling & How To Manipulate Heat With Sound (Thermoacoustics Part 2)](https://www.youtube.com/watch?v=kkBBkQ8jFRY)

## 17 Feb 2021
Los Alamos lab has [a thermoacoustic design program](https://www.lanl.gov/org/ddste/aldps/materials-physics-applications/condensed-matter-magnet-science/thermoacoustics/computer-codes.php). It doesn't seem to work out of the box with wine on Ubuntu, so I'll have to check it out later.

Also, I discovered OpenFOAM: an OS CFD software. It only takes up a gig of hard drive space!

PLA would make a great stack material. It has lower thermal conductivity and higher heat capacity than mylar (0.13 W/m K, 1800 J/kg K) which is a good thing. [@raut_design_2017]

Ooooo phase change thermoacoustic refrigerator. [@yang_environmentally-sound_2021]

So I'm thinking that I should just model a 3D printable thermoacoustic device and see how well it performs. Run a few numbers in the optimization equations to get basic parameters and see what happens. [@alamir_thermoacoustic_2020]

## {{ "2021-02-17 23:14" | date: "%d %b %Y" }}

Project Created!

# Bibliography

<!--notes-->

<!--links-->
