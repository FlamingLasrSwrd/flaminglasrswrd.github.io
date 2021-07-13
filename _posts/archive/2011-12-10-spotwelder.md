---
layout: post
title:  "Spot Welder"
date:   2011-12-10
tags: electronics
category: archive
phase: write-up
gallery: spot-welder
abstract: >
  Spot welders are used to affix two materials by melting and fusing under pressure without the addition of filler material. A simple spot welder can be constructed at home using a microwave over transformer.
graphical-abstract: /assets/img/spot-welder/full.JPG
---

# Background

I first became interested in this project because I needed to spot weld titanium cathodes and anodes for a chlorate cell project. I also use it to make frames for other projects such as the $1.49 hot plate. A quick Google search brought a tutorial from Hack A Day's page: [Spot Welder][]. I started out with a close copy of their spot welder but found it to be unsatisfactory. Probably because I used pre-1982 pennies for the contacts instead of MIG welder tips like they suggested. The wires I used were way too small for the current produced. So I built a second one using steel bolts as the contacts and beefier wiring. It is somewhat better but not the best.
Spot welders join two thin pieces of metal together by resistive heating. The metal is sandwiched between two contacts and a large current (>400 amps) is applied. The contact point between the two metal pieces has a high resistance and heats up to the melting point. The metal flows together and becomes one piece. The current is removed and the is metal allowed to cool. Now you have a spot of welded metal. Spot welders are used industrially to make just about every metal frame on the market from cars to toasters. They give short and precise welding without heating up the whole piece. They are limited to thin metal about nine gauge or smaller and usually aluminum or steel only. Spot welders are usually capacitor bank units instead of the constant source welders made by amateurs.

# The Making of...

The image at the top of the page is the finished welder. I have made lots of good welds with this machine. Overall it took about an hour to make. Most of that time I was fighting with the MOT secondary. It was more of an epic two day battle really.

## Step 1: Transformer

![](/assets/img/spot-welder/transformer.JPG)

The first thing to do is locate a suitable transformer. Microwave Oven Transformers (MOT) are the best. They are designed for high power applications (>1 KW) and the MOTs are easy to rewind. Not to mention that people throw them out all the time. Often they just have a blown fuse and rarely, if ever, the transformers are blown. If you don't have a microwave to rip apart post an add in your local freecycle or free craigslist. You will undoubtedly get a few hits. Try to find the heaviest transformer you can. Heavier generally means more power when it comes to transformers.

Now that you have a transformer you will have to strip the secondary coil (the fine wire set) in order to rewind it. This takes a combination of strength and skill with a lot of will power. I used a chisel and hammer to shave off the wires on the four points of contact with the laminated core. Alternatively you can just use a cutoff wheel with a dremel. Make sure you wear gloves, a facemask, and goggles when you cut into the secondary. I'm not sure if the epoxy used is toxic but it certainly can't be good for your lungs or eyes.

To rewind the transformer you will need some beefy wires. I used an old set of jumper cables. The smaller the wire you use the faster it will heat up. Certainly don't use anything less than 3 or 4 AWG. Here is a good table for [AWG current handling][]. If you don't have anything that large you can gang smaller wires together. That's what I did for my first spot welder. The wires would get extremely hot after only a few seconds of use and then I would have to wait for them to cool. Not exactly a fast process. Sorry I don't have pictures of that one. The jumper cables barely heat up even after several welds. Aim to have about three or four turns in your secondary rewinding. This really depends on your wire choice and how big your transformer is. Three to five volts is typically what a spot welder runs at. The cool thing about such a low voltage is that there is very low risk of electrocution. Pretty much the only way to get electrocuted by the arms is if it started raining salt water and then you grabbed both arms. Now that you have a secondary it is time to create the arms and supports.

## Step 2: Supports and Arms

![](/assets/img/spot-welder/supports.JPG)

Somehow you have to get the power to the metal being welded. You have to be able to maneuver your metal into place and clamp down on it. You also have to carry large currents without heating significantly. Then the arms have to have supports that allow pivot. How do you accomplish all this you ask? I used 3/8" soft copper tubing and sheet metal. It helps to have long, skinny arms like the ones shown. They allow you to make welds in tight places and small spaces. You could use the same wire as the secondary windings for the arms. It would have to be supported somehow. The bottom arm is screwed into the wooden base and electrically insulated from the sheet metal support. The wires from the transformer are just squeezed into the tubing and crimped into place. I used some electrical tape to reduce movement between the two. The support uses a single bolt and two washers as the pivot point.

## Step 3: Electrical Control

![](/assets/img/spot-welder/switches.JPG)

A good spot weld is largely a function of time. Too little time and the metals don't heat enough, too much time and the electrodes degrade and the metal oxidizes producing a poor weld. A regular light switch can be used for timing. Put it in series with the primary winding. They are only designed for about ten amps so you can't put it on the secondary side. I chose to include a second switch as a safety precaution. To operate you must have both switches on.

**Do not forget to core ground your MOT.** If you don't the core will kill you if you touch it. All you have to do is connect a grounding wire (usually green) to one of the transformer mounting screws. Doing something so easy to avoid death: probably a good idea.

## Step 4: Contacts

![](/assets/img/spot-welder/contacts.JPG)

If you have some tungsten laying around that would be great. Unfortunately I did not. I used two 1 1/2 inches bolts with a diameter of about 0.25 inch. Definitely not the best choice but it worked. The copper was flattened at the end and a hole drilled through. Two nuts can secure the bolts to the arms. Make sure to sand all the contact points to ensure a good connection. Pretty simple huh?

# Results

And now you have a spot welder. Grab some metal and start welding. This page will give you an idea of the spot welding time, cycles, electrode diameter, etc. I typically use three or four cycles at 5 seconds for welding 1.5 mm titanium cathodes. You can do a test weld and then break it. A good weld will rip off a "nugget" of the metal.

<div><iframe width="560" height="315" src="https://www.youtube.com/embed/hr-SQwcQj7E?rel=0" frameborder="0" allowfullscreen></iframe></div>

<!--urls-->
[AWG current handling]: https://www.powerstream.com/Wire_Size.htm
[This]: https://www.robot-welding.com/Welding_parameters.htm
[Spot Welder]: https://hackaday.com/2009/06/23/how-to-build-your-own-spot-welder/
