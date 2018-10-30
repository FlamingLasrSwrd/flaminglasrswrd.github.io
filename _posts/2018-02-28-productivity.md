---
layout: "post"
title: "Productivity"
date: "2018-02-28 17:34"
category: active
tags: computers
abstract: >
  Keylogging and mouse tracking data can be used as a primary endpoint for evaluating the effect of any *quantified self* data that one seeks to track. RescueTime is also available to monitor mouse movement and time.
---

# Summary
I am slightly obsessed with productivity. In the past, I have used 'how I felt' about my productivity as the primary endpoint instead of actually measuring it. In the last month, I have committed to finding at least some measure of my productivity that is objective. Since I do almost all my work nowadays on the computer, monitors that track my activity there are a good start. So I choose to activate RescueTime and logkeys. I am also participating in a [Harvard doctoral study][] that sends me thrice daily surveys on my happiness and some factors that might be related.
Hopefully these data will lead to some interesting correlations that I can later test. Supplementation is probably a big player here and I have yet to devise a passive way to measure that. Still working on untracked productivity such as any project in the real world...

# Logkeys
Install Logkeys using the [.deb file here](http://launchpadlibrarian.net/165012984/logkeys_0.1.1a+git5ef6b0dcb9e3-2_amd64.deb). 
I couldn't figure out how to get logkeys to start on boot. The service kept giving errors about the existence of a keyboard device even though I checked it many times. It turns out that logkeys doesn't follow links. Rather than use ```DEVICE=/dev/by-id/platform-i8042-serio-0-event-kbd``` in ```/etc/default/logkeys```, I should have been using where that linked to: ```DEVICE=/dev/input/event4```. Now it starts up great. A note: since logkeys starts before the home directory is decrypted, you must put your keymap in a system folder. Now my keymap is in ```/etc/default/keymap``` with the logkeys default set to ```KEYMAP=/etc/default/keymap```. I also had to change the DAEMON_OPTS line in ```/etc/init.d/logkeys``` to ```DAEMON_OPTS="-s -d $DEVICE -o $LOGFILE -m $KEYMAP $DAEMON_OPTS"```.

[My Keymap][]

# Log

# References

<!--Annotations-->
[Logkeys manpage](http://manpages.ubuntu.com/manpages/trusty/man8/logkeys.8.html)

[Harvard doctoral study]: https://www.trackyourhappiness.org/
[My Keymap]: {{ site.baseurl }}assets/src/my_keymap

<!--Glossary-->
