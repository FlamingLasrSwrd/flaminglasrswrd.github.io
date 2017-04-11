---
layout: post
title: "mnemosyne"
date: "2017-04-03 13:16:19 -0500"
category: archive
tags: programming
---
[Mnemosyne](http://mnemosyne-proj.org/) is a flash card spaced repetition software created to further human memory research. Installation on Ubuntu is somewhat straightforward.
<!--more-->

# Ubuntu 16.04
Installation on a fresh copy of Ubuntu 16.04.

* [Download](http://mnemosyne-proj.org/download-mnemosyne.php) the latest version of Mnemosyne (2.4.1 at the time of this writing).
* Extract the tarball.
```
cd Mnemosyne-2.4.1/
sudo apt-get install python3-pip
sudo pip3 install PyQt5 pillow matplotlib webob cheroot
sudo python3 setup.py install

```
Optional support for LaTeX in mnemosyne:

```
sudo apt-get install texlive
```
