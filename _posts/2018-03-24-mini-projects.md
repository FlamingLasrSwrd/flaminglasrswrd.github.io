---
layout: "post"
title: "Mini Projects"
date: "2018-03-24 15:41"
category: archive
---
A list of shorter projects.<!--more-->

# Intermittent Wifi
**Update2:**
I may have it figured. I think that my wifi issue was hard to diagnose because it had to do with encryption. Basically, every time my wifi card wanted to get a better signal (change AP's) or experienced too much interference on a particular channel, it used a random MAC address to attempt a reconnect. Unfortuantely, something about the PEAP-MSCHAPv2 verification algorithm at my University was rejecting the new MAC addresses and anything that caused my card to cycle would end up loosing connectivity. So bluetooth and locking my computer would cause cycling and end the connection (without actually ending it). Anyway, now I have a seemingly stable connection after stabilizing the driver and network manager.

## Driver Fix
To test:
```bash
sudo modprobe -r rtl8821ae
sudo modprobe rtl8821ae msi=1 ant_sel=2
```
To make permanent:
```bash
echo "options rtl8821ae msi=1 ant_sel=2" | sudo tee /etc/modprobe.d/rtl8821ae.conf
```
- I am still using the rtl8821ae from lwfinger driver found below.

## Network Manager Fix
```bash
echo -e "[device-mac-randomization]\nwifi.scan-rand-mac-address=0" | sudo tee -a /etc/NetworkManager/NetworkManager.conf
```
There's probably a better place for that than in the NetworkManager.conf file.

## Archive

**Update:**
I'm still having trouble with the wifi, so don't follow this procedure. Leaving it here for archival purposes.

I've always had trouble with this laptop hardware. Sometimes the wifi would cut in and out. Sometimes the audio would have lots of artifacts. F.Lux didn't work at all. Just weird stuff. I believe most of it is related to kernel and drivers. Recently, the wifi has been extremely slow, but only intermittently. Also, I've been getting ubuntu error reporting pop-ups dealing with systemd-journald SIGABRT messages on every boot. After a few hours of fiddling, I finally realized the two were related. Apparently, there's a bug somewhere in bluetooth causing the error on boot. I don't use bluetooth at all so I tried to disable the service. That didn't work either. Eventually I figured out that I also had to blacklist the driver.
My grub is not standard either. I had to do some fiddling to get it to boot properly with GNOME and an encrypted drive.
I'm not sure if this is related, but I was having trouble with ```sudo``` commands. Any sudo command in terminal would take several seconds to ask for my password. I used [this solution][]. Basically, just add your hostname to ```/etc/hosts``` at the end of a couple lines.
I've also had trouble with ```/etc/resolv.conf``` and I don't know why...

The whole procedure went something like this:
```
sudo nano /etc/default/grub
# Changed:
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash acpi=force intel_idle.max_cstate=1 pci=nomsi pcie_aspm=off"
# save; exit
sudo update-grub
sudo service bluetooth stop
sudo systemctl disable bluetooth.service
sudo nano /etc/modprobe.d/blacklist.conf
# Added to end of file:
blacklist bluetooth
# save; exit
hostname
> x550vx
sudo nano /etc/hosts
# Changed:
127.0.0.1       localhost
127.0.1.1       X550VX
::1     ip6-localhost ip6-loopback
# To:
127.0.0.1       localhost x550vx
127.0.1.1       x550vx
::1     ip6-localhost ip6-loopback x550vx
# save; exit
```
For the record, I am using the rtl8821ae driver from [lwfinger/rtlwifi_new][] on a [asus x550VX laptop][] running Ubuntu 16.04 with kernel 4.15.4. I don't know if that driver is necessary anymore, but my wifi works so I'm not going to mess with it. The non-standard kernel also fixed some sound and f.lux issues. Plus I want to keep as updated as possible in response to the Meltdown and Spectre exploits.  
**Update:**  
Apparently, that bluetooth driver is unnecessary. ```sudo service bluetooth start``` works just fine. Perhaps the conflict was that rtlwifi_new shipped with appropriate bluetooth drivers? Anyway, you can reenable the service ```sudo systemctl enable bluetooth.service```.

# Penny Charms
A friend of mine is making a necklace and needs a few charms made from pennies.  
![image](/assets/img/penny.jpg)  
They are all 2013 pennies. Holes were drilled and countersunk to prevent wear. The rings are made from 14 AWG copper wire and soldered with lead-free (silver) solder. I attempted to solder the ring directly to the penny at a 90 degree angle, but couldn't get the solder to flow well enough to make it attractive.



[this solution]: https://serverfault.com/questions/38114/why-does-sudo-command-take-long-to-execute
[lwfinger/rtlwifi_new]: https://github.com/lwfinger/rtlwifi_new/
[asus x550VX laptop]: https://www.asus.com/us/Laptops/X550VX/overview/
