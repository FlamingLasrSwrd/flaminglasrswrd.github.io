---
layout: "post"
title: "Anti-Theft Bicycle Locator"
date: "2019-03-23 10:13"
category: active
tags: electronics
author: Elijah K. Dunn
zotero-collection:
abstract: >
  My friend has several bicycles that a really expensive. Can I build a cheap and effective GPS tracker for locating a stolen bike?
graphical-abstract:
---

# Prior Art
https://github.com/YuanjieZhao/GPS-Tracker-MSP430
http://www.jordan-maynard.org/2018/03/a-gps-tracker-for-ultra-endurance-cyclists/

# Work Log

## 23 Mar 2019
GPS <-> uC <-SMS-> phone

Ideal scenario: A small device is implanted in the handlebars of your bike. The device can be recharged via usb. When you realize your bike has been stolen, send a SMS to the provided cell number. The system will then awaken and transmit its location every [time period] to the stored cell phone number (yours). You can then take that information to the police to recover your bike.
The device might also be used to GPS track a long bike ride (several days). But this is a secondary goal.

Arduino might have more support but isn't a low power chip. MSP430 is a decent balance between low power and dev support. It might be useful to start with an arduino and work down to the msp430.

- [GSM](https://www.amazon.com/HiLetgo-Smallest-Breakout-Quad-band-3-7~4-2V/dp/B01DLIJM2E) - $9
- [J-F2-B3E8-DR](https://www.digikey.com/product-detail/en/telit/J-F2-B3E8-DR/943-1024-1-ND/4959433) - $15
- [MSP430](https://www.digikey.com/products/en/integrated-circuits-ics/embedded-microcontrollers/685?FV=ffe002ad%2C1f140000&quantity=1&ColumnSort=0&page=2&k=msp430&pageSize=25&pkeyword=msp430) - $1-$5 depending on capabilities
