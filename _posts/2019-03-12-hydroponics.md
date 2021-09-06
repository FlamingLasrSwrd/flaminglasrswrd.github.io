---
layout: "post"
title: "Hydroponics"
date: "2019-03-12 11:35"
category: active
phase: design
tags: biology electronics
author: Elijah K. Dunn
zotero-collection: https://www.zotero.org/ekdunn/collections/LHPUXSLC
gallery: hydroponics
abstract: >
  Growing plants in water: an automated approach.
graphical-abstract: /assets/img/plants/plants-tobacco-kratky-seedling.JPG
---

# Prior Art

- [Mycodo](https://github.com/kizniche/Mycodo)
    - An open source environmental regulation system
- [yieldbuddy](https://yieldbuddy.com/)
    - raspberry Pi + arduino stack
- [DRO-Matic](https://github.com/drolsen/DRO-Matic)
    - fully automatic arduino dosing system
- [Atlas Scientific](https://www.atlas-scientific.com/)
    - everything at a price...
- [Aeroponics V4 | Sony Arouje](https://sonyarouje.com/2016/10/06/aeroponic-controller-v4/)
    - manual pH/nutrient adjustment
- [Hydruino | Instructables](https://www.instructables.com/id/Hyduino-Automated-Hydroponics-with-an-Arduino/)
    - pH control, light/humidity/temp sensors, fill/drain control, touchscreen interface
- [TheGreenAutomation](https://thegreenautomation.com/)
    - nothing but a landing page
- [MEG | Kickstarter](https://www.kickstarter.com/projects/yradia/meg-open-source-indoor-greenhouse)
    - funding unsuccessful
- [Bitponics | Kickstarter](https://www.kickstarter.com/projects/1498890810/bitponics-your-shortcut-to-a-green-thumb)
    - funded but seems to have failed with refunds issued
    - [parts list](http://bit.ly/bitponics-parts)
- [Windowfarms | wikipedia](https://en.wikipedia.org/wiki/Windowfarm)
    - funded but failed
    - controversy went so farm as to set up the site: <windowfarmsfraud.com>
- [DIY Hydroponic Controller | YouTube](https://www.youtube.com/watch?v=nGKxxjfAJMk)
    - based on the Atlas Scientific system
- [Basement LED Garden](https://www.youtube.com/watch?v=42wKIU8L4Lw)
    - large system based on commercial automation equipment
- [GrowMau5 DIY pH automation | YouTube](https://youtu.be/OCYezZtpQOI)
    - based on commercial pH controller
- [Build your own Hydroponics System Using Arduino | CityOS Tech Workshops](https://cityos.io/topic/301/Build-Your-Own-Hydroponic-System-using-Arduino)
    - a piecemeal set of basic arduino automation instructions
- [OpenGarden](https://www.cooking-hacks.com/documentation/tutorials/open-garden-hydroponics-irrigation-system-sensors-plant-monitoring/)
    - a self-contained kit for sale
- [Food Computer | MIT](https://www.media.mit.edu/posts/build-a-food-computer/)
    - An extensive MIT project focused on environmental plant studies and standardization and not productivity maximization

# Parts List

|     part     | manufacturer |  cost  |quantity|total|    interface   |    Python Library   |        description        |
| ------------ | ------------ | ------ | ------ | --- | -------------- | ------------------- | ------------------------- |
| [SEN0219‎]    | DFRobot      | $59.74 |  1 | $59.74 | analog (0.4-2V) | [ADC]               | infrared CO2 sensor board |
| [DS18B20‎]    | Maxim Integr |  $3.06 |  5 | $15.30 | 1-wire          | [DS18X20]           |digital temperature sensor |
| [101-70-103] | SainSmart    | $14.99 |  1 | $14.99 | 16xTTL 5V       |[DigitalOutputDevice]| 16 channel relay module; 250V 10A |
| [SEN0137]    | DFRobot      |  $9.79 |  1 |  $9.79 |~~analog (0-3V)~~|[Adafruit_Python_DHT]| DHT22 temp/humidity sensor board |
| [TSW-10]     | Amphenol Adv |  $7.70 |  1 |  $7.70 | analog (0-Vcc)  | [ADC]               | turbidity sensor[^1] |
| [DFR0151]    | DFRobot      |  $4.53 |  1 |  $4.53 | I2C             | N/A[^3]             | RTC module |
| [AD7150BRMZ] | Analog Dev   |  $3.88 |  2 |  $7.76 | I2C             | None                | Capacitance-to-Digital chip |
| [161‎]        | Adafruit     |  $0.95 |  3 |  $2.85 | analog (0-Vcc)  | [LightSensor]       | photocell |
| [TSL2591]    | Adafruit     |  $6.95 |  1 |  $6.95 | I2C             | [Adafruit_TSL2591]  | digital light sensor |
| [BME680]     | Adafruit     | $22.50 |  1 | $22.50 | I2C/SPI         | [Adafruit_BME680]   | Temp/humidity/pressure/gas sensor |
| [BME280]     | Adafruit     | $19.95 |  1 | $19.95 | I2C/SPI         | [Adafruit_BME280]   | Temp/humidity/pressure sensor |
| [MCP3008]    |Microchip Tech|  $2.26 |  2 |  $4.52 | SPI             | [ADC]               | 8 channel ADC |
| [MCP23017]   |Microchip Tech|  $1.24 |  1 |  $1.24 | I2C/SPI         | [Adafruit_MCP230xx] | 16-bit I/O Expander |
| [MCP4725]    | Adafruit     |  $4.95 |  1 |  $4.95 | I2C             | [Adafruit_MCP4725]  | 12-bit DAC |
| [SGP30]      | Adafruit     | $19.95 |  1 | $19.95 | I2C             | [Adafruit_SGP30]    | MOX based VOC meter |
|[4K7 resistor]| Stackpole    |  $0.49 | 10 |  $4.90 |                 |                     | Pull up resistor for I2C connections |

# Required Packages

- [smbus](https://pypi.org/project/smbus-cffi/) - I2C communications
    - or the drop-in [adafruit package](https://github.com/adafruit/Adafruit_Python_PureIO)

# Work Log

## 24 Nov 2020
Kratky hydroponics is not suitable for long term growth. Every time you top up the reservoir, you drown the "air roots" and the plant suffers. Maintaining a consistent liquid level manually is a possibility, but that sucks. I could use float valves.

I think I will use a regular pump recirculating system instead.

## 29 Sep 2020
I'm leaving town for 10 days. I need a way to water my plants.

Ten days isn't long enough for the internal clock to drift far enough that it isn't useful so I won't need a RTC right now.

[Capacitive moisture sensors](https://www.switchdoc.com/2020/06/tutorial-capacitive-moisture-sensor-grove/)

[Soil moisture sensors—How they work. Why some are not research-grade.](https://www.metergroup.com/environment/articles/tdr-fdr-capacitance-compared/)

Soil capacitance measurements are affected by frequency and by temperature.

## 21 Aug 2019

### DIY Rooting Hormone Gel
I started with [this](https://scienceinhydroponics.com/2017/07/making-your-own-diy-plant-rooting-gel.html) formula but used the potassium salt of indole-3-butyric acid instead of IBA. I also wanted a higher concentration of IBA (90mM) because of a paper on cloning walnuts suggested a higher concentration was better [@stevens_origin_2017].

## 20 Aug 2019
Built an ultrasonic cloner today.

![image](/assets/img/hydroponics/hydroponics-ultrasonic-cloner-side-view.JPG)

![image](/assets/img/hydroponics/hydroponics-ultrasonic-cloner-peek-mist.JPG)

I have several hydroponic tests in the works and I want a stable line of plants to compare the results.

## 22 Mar 2019
Looked into growing specialty crops in aquaponic/hydroponic systems. Saffron would yield $1-2 per square foot in 3-4 months. Definitely not worth the labor.

[FarmerTyler Blog](https://farmertyler.com/blog)

Cross-flow filtration for removing solids in aquaponics?

## 21 Mar 2019
[Q&A Aquaponic Pumps | Youtube](https://www.youtube.com/watch?v=x43aplqtMU0) - recommends 400lph pump with a ceramic shaft for each grow bed or siphon. [This](https://www.ebay.com/itm/Simple-Deluxe-UL-Listed-Water-Pump-Submersible-Pond-Fish-Tank-Aquarium-Fountain/152193563685?epid=1582600503&hash=item236f717c25:m:mTc8I7QU6j2K_MYHDSrpiag) pump seems to fit.

[How to mix Masterblend 4-18-38 Hydroponic Solution](http://gardendesigntools.com/how-to-mix-masterblend-4-18-38-hydroponic-nutrient-solution)

Worked on the nutrient analysis spreadsheet.

## 18 Mar 2019
Python web servers? Flask? - nice and simple; plus its templating mechanism uses liquid tags which I have experience with

[Python Flask from Scratch | Youtube](https://www.youtube.com/watch?v=zRwy8gtgJ1A): A very thorough walkthrough.

## 17 Mar 2019
Bell's Siphon for a modified ebb and flow system: Build instructions for a snorkel type siphon for adjustable minimum height [@fox_construction_2010].

PEX or PVC? I'm not worried about leaching, but biofouling in PVC is greater than in PEX. Since my system is designed for indoor use, I'm not worried about UV either. Biofouling in ocean water: LDPE < HDPE < PP [@sudhakar_biofouling_2007].

Place the venturi before the intake of the water pump. That way the bubbles are broken apart by the rotor.

If I have a single grow bed of dimensions 2'x3'x1', a 1/2" drain pipe siphon should be sufficient. If we assume 60% fill density of LECA (just a guess), then the water required to fill the grow bed is about 15 gal. I want that volume to be replaced every 15-20 minutes [@fox_construction_2010]. That means my pump has to move 45-60 gallons per hour (170-230 lph). If we assume a 25% loss of pressure due to the venturi (just a guess) and an extra 50% because restriction is easy, the total flow rate for my pump should be 320-430 lph (115 gph) at a height of about 1 foot. The 1200 gph pump I looked at earlier is way overkill. That seems really small... I think I'm going to go for the 400 gph (~325 gph at 1 foot) version because it is the cheapest from the set of eBay pumps that has screw fittings.

The pump cannot run dry... how to prime it if it is mounted above the sump? Probably manually. That also means that if the power goes out, the siphon will slowly allow the pipe to drain and ruin the pump when the power returns. Perhaps a check valve in the sump? Or I could just run the pump submerged as is recommended. I would prefer to have it accessible and contributing less heat to the system. Or I could just mount it at or below the base of the sump.

I can't find a consistent answer on whether PVC, cPVC, or PEX is better at handling ozone. They all bounce between "B" and "C". This is probably fine for the low concentrations and short contact times I will be using.

**Media**: LECA, river pebbles, lava rock, basalt. Since my system will be synthetic (as opposed to organic) I don't care too much about bacteria growth surface area.

The funnel type bell siphon seems to be more reliable.

This could turn into an entire web site...

## 16 Mar 2019

[Beaglebone or raspberry pi (or arduino)?](https://randomnerdtutorials.com/arduino-vs-raspberry-pi-vs-beaglebone-vs-pcduino/)

Beaglebone uses the [Adafruit BBIO library](https://adafruit-beaglebone-io-python.readthedocs.io/en/latest/index.html) which is less developed than the raspberry pi version. The two might be adapted, however. BB is more powerful, which I like, but it isn't necessary. BB is more expensive (+$20) but has more GPIO pins.

Adafruit has done a lot of the heavy lifting for product and software development. Given the opportunity, I will be purchasing from them even if it costs a bit more.

I think I have decided on Raspberry Pi. It has the most support and has all the capabilities I need. The clock issues are solved by using a RTC module. The lack of pins isn't an issue because a GPIO expander can be used. I/O for a hydroponics controller doesn't need to happen quickly so multiplexing the expander isn't an issue.

Staring work on the Raspberry Pi programming by using an emulator on my Ubuntu machine. [Instructions](https://blog.agchapman.com/using-qemu-to-emulate-a-raspberry-pi/). I didn't need to follow the network bridge part because mine worked out of the box.

## 15 Mar 2019

A nice [PID class in python](https://github.com/ivmech/ivPID) which could be useful for control electronics. Or a [PyPi PID package](https://pypi.org/project/simple-pid/)

Touch screen or buttons?... Or android app...

[I2C extender](https://www.hackster.io/chipmc/extend-the-reach-of-your-i2c-sensor-simply-and-inexpensively-ea6b53) - since I2C is limited to about 1 meter.

I like the idea of using the arduino as a pin-out board with the raspberry pi doing the heavy video and network lifting. Plus I get to use python instead of C++ for all the real work. Although, the Pi does seem to be capable of running the entire system by itself.

A [pin expander](https://learn.adafruit.com/using-mcp23008-mcp23017-with-circuitpython/overview) could be used for additional space if 10 (26 total) digital pins isn't enough. You will need to [get an ADC](https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/overview) for so many sensors. This is only a [few dollars for 8 channels](https://www.digikey.com/product-detail/en/microchip-technology/MCP3008-I-P/MCP3008-I-P-ND/319422).

Also... using RJ-11 connectors for remote sensors is an excellent idea. They are sooo cheap.

[DIY or Buy: Peristaltic Pump | YouTube](https://www.youtube.com/watch?v=AMiXme4bMUk). The "buy" peristaltic pump that the channel GreatScott compares to the "DIY" version is significantly more expensive than the [ones I have found](https://www.ebay.com/itm/DC-12V-24V-Dosing-Pump-Peristaltic-Tube-Head-for-Aquarium-Lab-Chemical-Analysis/202567636530?var=502634245559) and offer 80ml/min. His DIY version is based on [this design on Thingiverse](https://www.thingiverse.com/thing:254956) but with a NEMA 17 stepper. A major downside of that design is the heat generated by the motor tends to overheat PLA.

Looking into using cheaper pH and EC probes for the DRO-Matic.

[Single vs. Double junction pH probe](https://camblab.info/wp/index.php/what-is-the-difference-between-a-single-junction-and-double-junction-ph-electrode/). Double junction probes have an extra compartment to slow ion infiltration that ultimately destroys the probe. Slower infiltration: longer life. Especially when it comes to complex mineral/organic solutions like in hydroponics. Therefore, a double junction probe is recommended for hydroponic use.

A gel filled probe is cheaper, but again, doesn't last as long. A liquid probe can be filled again and again with new solution essentially making the probe last forever.

Since the DRO-Matic system is built to use BNC connectors and has built in calibration, any pH meter can be used. You don't have to buy the really expensive ones. Double junction probes are recommended and can be bought for around $40.

The creator of the DRO-Matic says that he was having trouble with interference between the pH and EC probes. He suggests that buying the Atlas Scientific tentacle and EZO circuits is the only way to solve this problem. I believe the secret is not in some "electrical isolation", but serial rather than parallel measurements. Basically the system only checks each probe once per second in a staggered manner so they don't interfere. One could certainly program that into the arduino, bypassing the issue (and cost) altogether.

[RTC for the Pi](https://pimylifeup.com/raspberry-pi-rtc/)

## 14 Mar 2019

**Hold Everything!!! I found the [answer](https://github.com/drolsen/DRO-Matic).**

[Electrolysis for oxygen generation](https://www.youtube.com/watch?v=3bslWkhZWFs)? I really don't like this presentation because it is a sales pitch. He talks about a lot of things that aren't related. At one point he just says, "It's technical science... It's compelling science.... Microbes." What a joke. Anyway, that doesn't mean there isn't science behind the tech.

Electrolysis is supposedly capable of a 50% boost to oxygen concentrations (12 mg/L vs. 8 mg/L). Would it be worth it? One problem is the production of CO2. Without the significant air flow and mixing provided by a bubbler, excess gasses cannot be removed from the boundary layer just above the reservoir. So it seems that you would need to purchase an electrolysis system in addition to your existing bubbler.

So the question becomes: Does higher DO concentrations compensate for the additional cost of an electrolysis system? [^2] Furthermore, I can't imagine that direct exposure of root systems to a voltage field is entirely nonreactive.

It appears that plant susceptibility to low dissolved oxygen concentrations is plant, growth stage, and end-point specific. Lettuce can tolerate 2mg/L without adverse affects on root growth or sprouting [@goto_effect_1996]. Tomatoes were taller and leaves had higher chlorophyll content in 40mg/L DO water but had negatively impacted weight, leaf area, and stem diameter. [@zheng_upper_2007]

> It is suggested that it was safe to enrich root zone DO to as high as 30 mg L−1, although the growth benefit was minor by increasing DO from ambient air saturated level (∼8.5 mg L−1) to 30 mg L−1. Higher than 30 mg L−1 could cause reduction in tomato plant growth.

Cucumber production was unaffected by elevated oxygen concentrations. Researchers did note that shelf life was increased possibly due to enhanced antioxidant production. Again, oxygen concentrations above typical ambient levels (~8mg/L) is probably not worth the effort. [@ehret_effects_2010]

Ajoene content of garlic was negatively impacted by only oxygenating the nutrient solution 12-hours per day (nighttime oxygenation worse than daytime) compared to 24-hour oxygenation [@naznin_growth_2010]. An interesting side note is that the roots contained ~80% the ajoene content of the bulbs. The maximum DO concentration was ambient (8 mg/L).

Ozone in the hydroponic reservoir doesn't seem to impact plant development (maybe advantageous for antioxidant production) but can significantly reduce pathogenic bacteria. [@graham_aqueous_2011] [@chan_effects_2007] Use of 3.0mg/L ozonated water is recommended for mineral wool based systems [@graham_closing_2012].

Ozonated water is mildly effective at controlling powdery mildew without damage to plants [@fujiwara_effects_2002]

Here's an interesting approach to pH manipulation using electrolysis [@spinu_electrochemical_1998]. Only 5W was needed to control the pH of a 12 sq. meter lettuce raft system. The loss of positive ions is a little disconcerting, however. Perhaps that is why this kind of system was never researched again.

I really hate when a research paper is full of grammatical errors and it still gets accepted for publication. [@saaid_development_2013]

[A 7" capacitive touch screen for a raspberry pi](https://www.amazon.com/7inch-HDMI-LCD-Resolution-Capacitive/dp/B077PLVZCX/) would be an excellent way to display data. I still think arduino is the better choice for direct communication with sensors. [A system like this](http://yieldbuddy.com/). [Here's a project](https://github.com/tpudlik/hydroponics) that runs lights and a pump directly from the raspberry pi GPIO pins. [Another](http://hapihq.com/hapi-series-1-development-schedule/)

## 13 Mar 2019
Looking at automation equipment choices: air/water pumps, venturi, air stones, etc.

Degassing tower: would solve the dissolved CO2/pH issue but add significant humidity to the air. [@pattillo_overview_2017]

What about spectrometers for measuring nutrient concentrations and even plant growth? [@pavlovic_chlorophyll_2014] [@shibghatallah_measuring_2013] Could be viable but would require significant R&D.

PEX tubing has greater chemical resistance and is easier to install. The fittings require a clamp tool (or expensive push-connectors). You can get away with using some wire dikes if you want.

Looking into cable management and [connectors](https://www.youtube.com/watch?v=QKLsTnKVTEY) [2](https://www.youtube.com/watch?v=My-FX1bGikc).

### What size pump?
I need enough flow to work with the venturi. My vacuum aspirator requires a diaphragm pump to reach the high vacuums required. I doubt anything so drastic would be necessary here since the venturi will be mixing in atmospheric air. A simple magnetic drive pump should be sufficient.

[This 4 bucket rDWC system](https://www.amazon.com/Viagrow-VRDWC-4-Recirculating-4-Bucket-Hydroponic/dp/B01LANYQ4G) comes with a 159 GPH magnetic drive pump. [This one](https://www.amazon.com/Hydroponic-Recirculating-Culture-Buckets-Control/dp/B00UQLTNXS) uses a 400 gph pump. Magnetic drive pumps can be restricted without harming the motor, which is nice. Since my system includes a venturi, those values will be low. I would prefer a non-submersible type for cleaning purposes.

[Jims pond blog](https://leisure.prior-it.co.uk/venturi-pond-aeration.shtml) uses a 1600gph pump and a "1 inch venturi" and is surprised by the bubbling.

I think I will just go with [a cheap 1200 gph pump] and be done with it. The output looks like a 3/4 NPT so [this venturi injector] should do. It's rated for "0.65-2.42m³/h  0.7-9.5bar". Now that I look at this my 1200 gph pump might not be sufficient. It lists the pressure head at 13.0ft (5.6psi, 0.39bar). So does that mean I won't have enough pressure? It has been too long since my fluid dynamics class...

## 12 Mar 2019

### Syringe Pump

**Update: Syringe pumps are a lot more expensive than perstaltic pumps.***

This is based on [Open Source Syringe Pump](https://www.appropedia.org/Open-source_syringe_pump) [@wijnen_open-source_2014]. Fortunately, my local library offers free 3D printing. First, installing Lulzbot CURA software on Ubuntu 18.04:

```
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
sudo sed -i '$a deb http://download.alephobjects.com/ao/aodeb buster main' /etc/apt/sources.list
sudo apt-get update
sudo apt-get install cura-lulzbot
```

I got an error following the [installation guide](https://www.lulzbot.com/learn/tutorials/cura-lulzbot-edition-installation-ubuntu) saying that I needed to install a *libssl* package. I found a solution [here](https://forum.lulzbot.com/viewtopic.php?p=44727). Basically it just grabs a debian 10 package (*buster main*) instead of the ubuntu 18 one (*stretch main*).

I also had to install openSCAD to work with the files from the project.

```
sudo add-apt-repository ppa:openscad/releases
sudo apt update
sudo apt install openscad
```

### Capacitive Fluid Level Sensor
This [DIY Fluid Level Sensor | Instructables](https://www.instructables.com/id/Capacitive-Fluid-Level-Sensor/) seems like a good idea, but over constructed for my purposes. The inner, charged electrode can be any insulated wire. Preferably 12AWG solid wire for rigidity. The outer electrode can be any non reactive metal. Preferably stainless steel but copper would work.

The probe should be a centimeter or two in width and about 30cm in depth.

The capacitance-to-digital chip I found measures 0-13pF with 1fF sensitivity. That's extremely low and won't work for a cylindrical capacitance probe. A pair of insulated, parallel copper electrodes would work pretty well.

### EC meter
[$3 EC meter](https://hackaday.io/project/7008-fly-wars-a-hackers-solution-to-world-hunger/log/24646-three-dollar-ec-ppm-meter-arduino)

Let's look at automation. Arduino and raspberry pi are obvious choices for control.

A few arduino garden controllers use peristaltic pumps, but I would rather use syringe pumps. They are more accurate, but slower. Speed isn't an issue for hydroponics. Equilibration of the dose with the reservoir will be an issue.

General hydroponics typical nutrient doses are less than 10ml per gallon. I'll need to order syringes before printing the parts of the open source syringe pump. [NEMA17](https://www.omc-stepperonline.com/nema-17-stepper-motor) looks like a common stepper motor that's relatively cheap.

### Top Picks

|      part      |   manufacturer   |  cost  |quantity| description |
| -------------- | ---------------- | ------ | ------ | ----------- |
| [DS18B20‎]      | Maxim Integrated |  $3.06 |  5 |digital temperature sensor |
| [SEN0219‎]      | DFRobot          | $59.74 |  1 | infrared CO2 sensor board |
| [SEN0137]      | DFRobot          |  $9.79 |  1 | DHT22 temp/humidity sensor board |
| [DFR0151]      | DFRobot          |  $4.53 |  1 | RTC module |
| [161‎]          | Adafruit         |  $0.95 |  3 | photocell |
| [TSW-10]       | Amphenol Advanced|  $7.70 |  1 | turbidity sensor[^1] |
| [DFR0144‎]      | DFRobot          | $14.41 |  1 | 3A x 4 relay board |
| [103030009]    | Seeed Technology | $21.68 |  1 | 10A x 4 relay board |
| [997]          | Adafruit         |  $6.96 |  1 | 12V; 1/2" solenoid valve |
| [ATMEGA328-PU‎] | Microchip Tech   |  $1.96 |  1 | Bare arduino IC |
| [AD7150BRMZ]   | Analog Devices   |  $3.88 |  1 | Capacitance-to-Digital chip|


The photocell will definitely saturate at the light levels I'm expecting (650 lux). If using multiple light sensors, one might be inclined to use an [external DAC] to save pins.

Air pump: rule-of-thumb 1W per gallon. Ideal water temperature for dissolved oxygen content of 8-9 ppm is 68F ([source](http://www.just4growers.com/stream/hydroponic-growing-techniques/airing-out-the-truth-on-dissolved-oxygen-in-hydroponics.aspx)).

# Appendix A

```bash
sudo qemu-system-arm -kernel ./kernel-qemu-4.4.34-jessie -append "root=/dev/sda2 panic=1 rootfstype=ext4 rw" -hda raspbian-stretch-lite.qcow -cpu arm1176 -m 256 -M versatilepb -no-reboot -serial stdio -net nic -net user -net tap,ifname=vnet0,script=no,downscript=no

pi
raspberry

sudo nano /etc/default/keyboard
`XKBLAYOUT="us"`
sudo apt update
sudo apt upgrade -y
sudo shutdown -h now
sudo apt install -y python3-dev git
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py --user
nano ~/.bashrc
`export PATH=$HOME/.local/bin/:$PATH`
pip3 install --user circuitpython-build-tools
pip3 install --user adafruit-circuitpython-lis3dh
sudo raspi-config

- interfacing options
    - P4 SPI
    - P5 I2C
    - P7 1-Wire
- reboot

wget https://github.com/adafruit/circuitpython/releases/download/3.1.2/mpy-cross-3.x-raspbian-stretch

wget https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20190315/adafruit-circuitpython-bundle-3.x-mpy-20190315.zip

git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT/
python3 setup.py install --force-pi --user

pip3 install --user adafruit-circuitpython-DS18X20
```

# Bibliography

<!--notes-->
[^1]: Optional; Used to monitor water quality in the reservoir and as a backup water level sensor.
[^2]: A few stainless steel plates and a cheap power supply would be sufficient, so the cost is minimal.
[^3]: RTCs interface directly with the Pi and replace the fake-hwclock

<!--links-->
[a cheap 1200 gph pump]: https://www.ebay.com/itm/Submersible-90-1450-GPH-Aquarium-Fish-Tank-Water-Pump/253979919126?var=553305096770
[this venturi injector]: https://www.ebay.com/itm/3-4-1-Irrigation-Venturi-Fertilizer-Mixer-Injector-Garden-Water-Device-Tube-OJ/163421319439?hash=item260cab710f:m:mv0zZCb0ysVUw3laKJzMmOw&frcectupt=true
[DS18B20‎]: https://www.digikey.com/product-detail/en/DS18B20%2b/DS18B20%2b-ND/956983/?itemSeq=287062292
[SEN0219‎]: https://www.digikey.com/product-detail/en/SEN0219/1738-1292-ND/7087189/?itemSeq=287062471
[SEN0137]: https://www.digikey.com/product-detail/en/SEN0137/1738-1039-ND/6588461/?itemSeq=287035138
[DFR0151]: https://www.digikey.com/product-detail/en/DFR0151/1738-1054-ND/6588476/?itemSeq=287026205
[161‎]: https://www.digikey.com/product-detail/en/161/1528-2141-ND/7244927/?itemSeq=287035074
[TSW-10]:https://www.digikey.com/product-detail/en/amphenol-advanced-sensors/TSW-10/235-1382-ND/4250485
[DFR0144‎]: https://www.digikey.com/product-detail/en/DFR0144/1738-1099-ND/6588521/?itemSeq=287038585
[103030009]: https://www.digikey.com/product-detail/en/103030009/1597-1146-ND/5774758/?itemSeq=287038576
[external DAC]: https://www.digikey.com/product-detail/en/adafruit-industries-llc/935/1528-1010-ND/4990759
[997]: https://www.digikey.com/product-detail/en/adafruit-industries-llc/997/1528-2003-ND/6827136
[ATMEGA328-PU‎]: https://www.digikey.com/product-detail/en/microchip-technology/ATMEGA328-PU/ATMEGA328-PU-ND/2271026
[AD7150BRMZ]: https://www.digikey.com/product-detail/en/analog-devices-inc/AD7150BRMZ/AD7150BRMZ-ND/1766855
[101-70-103]: https://www.sainsmart.com/products/16-channel-12v-relay-module
[Adafruit_Python_DHT]: https://github.com/adafruit/Adafruit_Python_DHT
[DS18X20]: https://github.com/adafruit/Adafruit_CircuitPython_DS18X20
[ADC]: https://gpiozero.readthedocs.io/en/stable/api_spi.html#analog-to-digital-converters-adc
[LightSensor]: https://gpiozero.readthedocs.io/en/stable/api_input.html#lightsensor-ldr
[DigitalOutputDevice]: https://gpiozero.readthedocs.io/en/stable/api_output.html#digitaloutputdevice
[Adafruit_BME680]: https://github.com/adafruit/Adafruit_CircuitPython_BME680
[BME680]: https://www.adafruit.com/product/3660
[Adafruit_BME280]: https://github.com/adafruit/Adafruit_CircuitPython_BME280
[BME280]: https://www.adafruit.com/product/2652
[MCP2008]: https://www.digikey.com/product-detail/en/microchip-technology/MCP3008-I-P/MCP3008-I-P-ND/319422
[Adafruit_MCP230xx]: https://github.com/adafruit/Adafruit_CircuitPython_MCP230xx
[TSL2591]: https://www.adafruit.com/product/1980
[Adafruit_TSL2591]: https://github.com/adafruit/Adafruit_CircuitPython_TSL2591
[MCP4725]: https://www.adafruit.com/product/935
[Adafruit_MCP4725]: https://github.com/adafruit/Adafruit_CircuitPython_MCP4725
[SGP30]: https://www.adafruit.com/product/3709
[Adafruit_SGP30]: https://github.com/adafruit/Adafruit_CircuitPython_SGP30
[MCP3008]: https://www.digikey.com/product-detail/en/microchip-technology/MCP3008-I-P/MCP3008-I-P-ND/319422
[MCP23017]: https://www.digikey.com/product-detail/en/microchip-technology/MCP23017-E-SP/MCP23017-E-SP-ND/894272
[4K7 resistor]: https://www.digikey.com/product-detail/en/CF18JT4K70/CF18JT4K70CT-ND/2022758/?itemSeq=287482347
