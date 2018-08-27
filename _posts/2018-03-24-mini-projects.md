---
layout: "post"
title: "Mini Projects"
date: "2018-03-24 15:41"
category: archive
abstract: >
  A list of shorter projects.
---
# Jafar Costume
![][assets/img/jafarstaff.jpg]

# References in Markdown Regex
```
[@]+\b([a-zA-Z_0-9-]*)+\b
[^$1]
```

# Initramfs Trouble

Today I woke up to a system that wouldn't boot. The system just dropped to the busybox terminal after 30 seconds giving an error that said ```/dev/mapper/ubuntu--vg-root``` couldn't be located. ```cat /dev/mapper``` only gave *control* or something like that. Obviously it would never find the drive: I had full disk encryption and was never asked for a password. Booting to a different kernel work once, but I foolishly executed ```update-initramfs -u -k all``` and killed all my other kernels at once. I couldn't just decrypt the drive because ```cat /proc/modules``` didn't show *cryptsetup* at all.

So I went on an adventure for six hours this morning attempting to fix it. The [best explanation][] I could find was that something went wrong with LVM making the system not recognize the encrypted drive on boot. I believe my issue sprang from removing ```libreadline5``` because of some dependency issues with ```swi-prolog```. I ended up just building SWIP-pl from source, but somehow I managed to screw up *libreadline*. The short version is:

- boot using ubuntu live flash drive with persistence enabled
- mount the drive including the encrypted portion
- chroot into the drive
- reinstall lvm2
  - I had to download packages separately using the live disk system then install them in the chrooted system
- comment out a line in the initramfs script to stop sync [a bug][]
- update-initramfs

## Persistent Flash drive
Persistence may not be necessary in all cases, but it makes things much simpler. On another ubuntu system with a spare flash drive mounted at ```/dev/sdd``` and fresh copy of ubuntu 12.04 downloaded at ```~/Downloads/ubuntu-16.04.4-desktop-amd64.iso``` [ref][]:

```bash
sudo add-apt-repository ppa:mkusb/ppa
sudo apt update
sudo apt install mkusb
# The p is persistence; mkusb was replaced by dus but this still works
sudo -H mkusb ~/Downloads/ubuntu-16.04.4-desktop-amd64.iso p
```

I could only get the *classic* version to run as gui. Just follow the on screen instructions and go with the defaults if unsure. I alloted 100% for the persistence volume. It takes several minutes for mkusb to finish. After, you should be able to unplug the device and boot up the broken system.

## Boot and Fix
So now you have a bootable ubuntu live flash drive with persistence plugged into your broken system. If you haven't already, enable booting from the flash drive in your BIOS (hold down Shift or F2 or F8 or some other F-key). Start up your system and select "Try Ubuntu with persistence." It should be the default option.

If everything goes to plan you now have a copy of ubuntu running and an encrypted drive at ```/dev/sda```. Launch a terminal (```Ctrl-Alt-T```):

```bash
sudo cryptsetup luksOpen /dev/sda3 sda3_crypt
# Enter your password to decrypt
sudo vgchange -ay
sudo mount /dev/mapper/ubuntu--vg-root /mnt
sudo mount /dev/sda2 /mnt/boot
sudo mount -t proc proc /mnt/proc
sudo mount -o bind /dev /mnt/dev
sudo chroot /mnt
```

For some reason I couldn't resolve any hosts (```sudo apt update``` returned unresolved hosts). Probably because of all the weird stuff with my wifi card shown below. Either way, in a separate terminal running as the ubuntu live user:

```bash
sudo apt update
cd /mnt/tmp
sudo apt-get download lvm2
# if you messed up with libreadline like I did:
sudo apt-get download libreadline5
exit
```

So now we have the *.deb* packages downloaded in ```/mnt/tmp``` which is running under the chroot terminal from earlier. Go back to that terminal:

```bash
dpkg -i libreadline5_5.2+dfsg-3build1_amd64.deb
dpkg -i lvm2_2.02.133-1ubuntu10_amd64.deb
# or whatever versions of libreadline5 and lvm2 you downloaded
# I attempted to run:
dpkg --configure -a
# But it just hung and never completed update-initramfs
# If you run:
update-initramfs -u -v
# It hangs on the line: Building cpio /boot/initrd.img-4.4.0-116-generic.new initramfs
```

So I also located [a bug][] in ubuntu which causes *sync* to hang. To fix you need to comment out (insert *#*) the line that says ```sync``` (line 176) under the ```generate_initramfs``` function in the file ```/dev/usr/sbin/update-initramfs```. Make sure you are editing the */dev/* version not the live flash drive version.

Now that sync has been stopped, you can continue with dpkg:

```bash
dpkg --configure -a
# I also updated initramfs manually just to be sure:
update-initramfs -v -u
# Or a specific kernel version:
update-initramfs -v -d -k 4.4.0-116-generic && update-initramfs -v -c -k 4.4.0-116-generic
```

So that's it! Hopefully. You should be able to shutdown the live system, reboot to the original drive, and enter your password. If all that works you can reinstall any experimental kernels you may have and ```update-initramfs``` will be called automatically. One last thing, make sure you uncomment that sync line from ```/usr/sbin/update-initramfs```. You can run ```sudo update-initramfs -u -v -k all``` afterwards to make sure everything is square.

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
![image](assets/img/penny.jpg)  
They are all 2013 pennies. Holes were drilled and countersunk to prevent wear. The rings are made from 14 AWG copper wire and soldered with lead-free (silver) solder. I attempted to solder the ring directly to the penny at a 90 degree angle, but couldn't get the solder to flow well enough to make it attractive.

# Log

# References

<!--Annotations-->
[this solution]: https://serverfault.com/questions/38114/why-does-sudo-command-take-long-to-execute
[lwfinger/rtlwifi_new]: https://github.com/lwfinger/rtlwifi_new/
[asus x550VX laptop]: https://www.asus.com/us/Laptops/X550VX/overview/
[a bug]: https://bugs.launchpad.net/ubuntu/+source/initramfs-tools/+bug/1667512
[ref]: https://askubuntu.com/a/753163
[best explanation]: https://feeding.cloud.geek.nz/posts/recovering-from-unbootable-ubuntu-encrypted-lvm-root-partition/

<!--Glossary-->
