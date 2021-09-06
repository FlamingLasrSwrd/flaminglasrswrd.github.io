---
layout: "post"
title: "Powered Rower"
date: "2021-03-03 17:51"
category: active
phase: exploratory
tags: health
author: Elijah K. Dunn
zotero-collection: https://www.zotero.org/ekdunn/collections/F9G4N4F5
gallery:
abstract: >
  A homemade motor-driven exercise rowing machine.
graphical-abstract:
---


# Work Log

## TODO

- [ ]

## 03 Mar 2021
This example rowing machine uses the charging of ultracapacitors as lightweight regenerative braking but relies on a freewheeling clutch for the return stroke (not eccentric). It is controlled by a [four-quadrant power converter](https://www.analog.com/en/analog-dialogue/raqs/raq-issue-183.html) with adjustable ratio (forward braking and reverse motoring). Simple and effective. [@richter_impedance_2015]

Position is measured using an optical encoder placed on the motor system. A load cell on the handle measures the force.

Ultracapacitors on the order of several hundred farads are expensive even for this scaled-down version.

The behavior of this system is very close to natural rowing conditions.

[Four Quadrant Operation of DC Motor](https://circuitglobe.com/four-quadrant-operation-of-dc-motor.html)

A very detailed four-qudrant power converter used at CERN. See section 5.3 Four-quadrant linear stage. [@thurel_switched_2015]

Simple torque controlled motors would directly discharge the excess power into the power electronics. They would likely overheat at the several hundred watt level. [Brushless Motors Torque Control using ARDUINO and SOLO (ESC - BLDC - PMSM) in Closed-loop Mode](https://www.youtube.com/watch?v=sTjh5KbStGE)

[Arduino based 4 Quadrant DC Motor Control](https://www.edgefxkits.com/blog/arduino-based-4-quadrant-dc-motor-control/)

The thesis work of Zolezzi uses a 1Kw 2500 RPM 3N-m AC servo. [@zolezzi_design_2017] Something [like this costs about $120](https://www.ebay.com/itm/Servo-Motor-1KW-4NM-AC-Servo-CNC-2500PRM-Pure-Copper-Processing-Steel-Sheet/372788345885) although the lack of competition at that price leads me to think there is something wrong.

> The operation of the control system can be summarized as follows: there are two discrete states: coupled (pull phase) and decoupled (return phase). An impedance regulator is used during the pull phase to provide the force-velocity characteristic corresponding to a flywheel, a nonlinear damper and a small spring action. The force along the pull chain is monitored in this mode. Near the end of the pull stroke, when the force crosses a lower threshold, a transition to the decoupled mode is triggered. The target impedance of the regulator is switched to provide a very low inertia and damping, along with the spring action. At the same time, a real-time simulation of the flywheel is started, mimicking a decelerating flywheel in a conventional machine. The user reverses motion and returns to the starting position and initiates a new pull phase. When the velocity of the chain rises above the velocity of the virtual flywheel, the coupled mode is re-engaged, and the entire cycle repeated.

Position, force, and velocity measurements are needed. Optical encoders on the sprocket and flywheel are used to measure the angular speed. The control system is entirely implemented using a [DSpace MicroLabBox](https://www.dspace.com/en/inc/home/products/hw/microlabbox.cfm).

Servos are used instead of steppers because the torque vs. speed graph is relatively linear in the former. Steppers lose significant torque above a certain speed.

## {{ "2021-03-03 17:51" | date: "%d %b %Y" }}

Project Created!

# Bibliography

<!--notes-->

<!--links-->
