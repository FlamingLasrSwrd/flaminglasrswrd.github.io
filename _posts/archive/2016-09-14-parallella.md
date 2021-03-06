---
layout: post
title:  "Parallella"
date:   2016-09-14
tags: programming
category: archive
phase: research
abstract: >
  I supported a kickstarter a while back to develop a 16-core FPGA based microcomputer capable of running a standard(ish) linux distro. And thus... Parallella was born. Currently, my parallella board is collecting dust because I don't have the knowledge to take advantage of multi-threading.
---

# Specifications
* Parallella board - kickstarter version with Zynq 7020
* 16-core Epiphany processor
* ssh parallella@192.168.1.3

# Initial Setup

`sudo apt update`  
`sudo apt upgrade`

## Static IP Configuration

`sudo vi /etc/network/interfaces.d/eth0`  
Changed "dhcp" to static and added the relevant information.
```
auto eth0
iface eth0 inet static
        address 192.168.1.3
        netmask 255.255.255.0
        gateway 192.168.1.1
```
Modified the DNS server configuration.  
`sudo vi /etc/resolv.conf`  
Modified to include one original DNS server from my ISP (75.76.84.70), one google server, and my gateway.
```
domain knology.net
search knology.net
nameserver 75.76.84.70
nameserver 8.8.8.8
nameserver 192.168.1.1
```

# Node.js
[Node.js Source Code](https://nodejs.org/dist/v4.5.0/node-v4.5.0.tar.gz)  
`wget https://nodejs.org/dist/v4.5.0/node-v4.5.0.tar.gz`  
`tar -xvf node-v4.5.0.tar.gz`  
`cd node-v4.5.0'`  
`'sudo ./configure'`  
`'sudo make -j16'`  

# Numenta
`sudo apt-get install python-pip`  
`sudo apt-get install python-numpy`  
`sudo pip install nupic`  


# Apendix A: Installed Apps

*  acl
*  adduser
*  apt
*  apt-utils
*  at
*  at-spi2-core
*  avahi-daemon
*  base-files
*  base-passwd
*  bash
*  bc
*  bind9-host
*  binutils
*  bison
*  bsdmainutils
*  bsdutils
*  build-essential
*  busybox-initramfs
*  bwm-ng
*  bzip2
*  ca-certificates
*  clinfo
*  colord
*  colord-data
*  console-setup
*  console-setup-linux
*  coreutils
*  cpio
*  cpp
*  cpp-4.9
*  cron
*  curl
*  dash
*  dbus
*  dconf-gsettings-backend:armhf
*  dconf-service
*  dctrl-tools
*  debconf
*  debianutils
*  device-tree-compiler
*  devscripts
*  dh-python
*  diffstat
*  diffutils
*  distro-info-data
*  dmsetup
*  docbook-xml
*  dpkg
*  dpkg-dev
*  dput
*  e2fslibs:armhf
*  e2fsprogs
*  emacs-nox
*  emacs24-bin-common
*  emacs24-common
*  emacs24-common-non-dfsg
*  emacs24-nox
*  emacsen-common
*  ethtool
*  fake-hwclock
*  fakeroot
*  file
*  findutils
*  flex
*  fontconfig
*  fontconfig-config
*  fonts-dejavu-core
*  ftp
*  g++
*  g++-4.9
*  gawk
*  gcc
*  gcc-4.9
*  gcc-4.9-base:armhf
*  gcc-5-base:armhf
*  gdb
*  gdbserver
*  geoip-database
*  gettext
*  gettext-base
*  git
*  git-man
*  glib-networking:armhf
*  glib-networking-common
*  glib-networking-services
*  gnupg
*  gpgv
*  grep
*  groff-base
*  gsettings-desktop-schemas
*  gzip
*  hardening-includes
*  hicolor-icon-theme
*  hostname
*  htop
*  i2c-tools
*  ifplugd
*  ifupdown
*  info
*  init
*  init-system-helpers
*  initramfs-tools
*  initramfs-tools-bin
*  initscripts
*  insserv
*  install-info
*  intltool-debian
*  iperf
*  iproute
*  iproute2
*  iputils-ping
*  isc-dhcp-client
*  isc-dhcp-common
*  iso-codes
*  kbd
*  keyboard-configuration
*  klibc-utils
*  kmod
*  krb5-locales
*  language-pack-en
*  language-pack-en-base
*  less
*  libacl1:armhf
libalgorithm-c3-perl
libalgorithm-diff-perl
libalgorithm-diff-xs-perl
libalgorithm-merge-perl
liballegro4.4:armhf
libapparmor1:armhf
libapt-inst1.5:armhf
libapt-pkg-perl
libapt-pkg4.12:armhf
libarchive-extract-perl
libarchive-zip-perl
libasan1:armhf
libasn1-8-heimdal:armhf
libasound2:armhf
libasound2-data
libasprintf-dev:armhf
libasprintf0c2:armhf
libasyncns0:armhf
libatk-bridge2.0-0:armhf
libatk1.0-0:armhf
libatk1.0-data
libatm1:armhf
libatomic1:armhf
libatspi2.0-0:armhf
libattr1:armhf
libaudit-common
libaudit1:armhf
libauthen-sasl-perl
libavahi-client3:armhf
libavahi-common-data:armhf
libavahi-common3:armhf
libavahi-core7:armhf
libbabeltrace-ctf1:armhf
libbabeltrace1:armhf
libbind9-90
libbison-dev:armhf
libblkid1:armhf
libboost-filesystem1.55.0:armhf
libboost-system1.55.0:armhf
libbsd0:armhf
libbz2-1.0:armhf
libc-bin
libc-dev-bin
libc6:armhf
libc6-dbg:armhf
libc6-dev:armhf
libcaca0:armhf
libcairo-gobject2:armhf
libcairo-perl
libcairo2:armhf
libcap-ng0:armhf
libcap2:armhf
libcap2-bin
libcgi-fast-perl
libcgi-pm-perl
libcgmanager0:armhf
libck-connector0:armhf
libclass-accessor-perl
libclass-c3-perl
libclass-c3-xs-perl
libclc-dev
libclone-perl
libcloog-isl4:armhf
libcolord2:armhf
libcolorhug2:armhf
libcomerr2:armhf
libcommon-sense-perl
libconfig++-dev:armhf
libconfig++9:armhf
libconfig-dev:armhf
libconfig-doc
libconfig9:armhf
libcpan-meta-perl
libcroco3:armhf
libcryptsetup4
libcups2:armhf
libcurl3:armhf
libcurl3-gnutls:armhf
libdaemon0:armhf
libdata-optlist-perl
libdata-section-perl
libdatrie1:armhf
libdb5.3:armhf
libdbus-1-3:armhf
libdconf1:armhf
libdebconfclient0:armhf
libdevil-dev
libdevil1c2
libdevmapper1.02.1:armhf
libdigest-hmac-perl
libdistro-info-perl
libdns-export100
libdns100
libdpkg-perl
libdrm-dev:armhf
libdrm-exynos1:armhf
libdrm-freedreno1:armhf
libdrm-nouveau2:armhf
libdrm-omap1:armhf
libdrm-radeon1:armhf
libdrm2:armhf
libedit2:armhf
libelf1:armhf
libelfg0:armhf
libelfg0-dev
libemail-valid-perl
libencode-locale-perl
libept1.4.12:armhf
liberror-perl
libestr0
libevent-2.0-5:armhf
libevent-core-2.0-5:armhf
libevent-dev
libevent-extra-2.0-5:armhf
libevent-openssl-2.0-5:armhf
libevent-pthreads-2.0-5:armhf
libexif12:armhf
libexpat1:armhf
libexporter-lite-perl
libfakeroot:armhf
libfcgi-perl
libffi6:armhf
libfftw3-3:armhf
libfftw3-bin
libfftw3-dev:armhf
libfftw3-double3:armhf
libfftw3-single3:armhf
libfile-basedir-perl
libfile-fcntllock-perl
libfile-listing-perl
libfl-dev:armhf
libflac8:armhf
libfont-afm-perl
libfontconfig1:armhf
libfreetype6:armhf
libfribidi0:armhf
libgcc-4.9-dev:armhf
libgcc1:armhf
libgcrypt20:armhf
libgd3:armhf
libgdbm3:armhf
libgdk-pixbuf2.0-0:armhf
libgdk-pixbuf2.0-common
libgeoip1:armhf
libgettextpo-dev:armhf
libgettextpo0:armhf
libgl1-mesa-dev:armhf
libgl1-mesa-dri:armhf
libgl1-mesa-glx:armhf
libglapi-mesa:armhf
libglib-perl
libglib2.0-0:armhf
libglib2.0-data
libglu1-mesa:armhf
libgmp-dev:armhf
libgmp10:armhf
libgmp3-dev
libgmpxx4ldbl:armhf
libgnutls-deb0-28:armhf
libgnutls-openssl27:armhf
libgomp1:armhf
libgpg-error0:armhf
libgphoto2-6:armhf
libgphoto2-l10n
libgphoto2-port10:armhf
libgpm2:armhf
libgraphite2-3:armhf
libgssapi-krb5-2:armhf
libgssapi3-heimdal:armhf
libgtk-3-0:armhf
libgtk-3-bin
libgtk-3-common
libgtk2-perl
libgtk2.0-0:armhf
libgtk2.0-bin
libgtk2.0-common
libgudev-1.0-0:armhf
libgusb2:armhf
libharfbuzz0b:armhf
libhcrypto4-heimdal:armhf
libheimbase1-heimdal:armhf
libheimntlm0-heimdal:armhf
libhogweed2:armhf
libhtml-form-perl
libhtml-format-perl
libhtml-parser-perl
libhtml-tagset-perl
libhtml-tree-perl
libhttp-cookies-perl
libhttp-daemon-perl
libhttp-date-perl
libhttp-message-perl
libhttp-negotiate-perl
libhx509-5-heimdal:armhf
libicu52:armhf
libidn11:armhf
libieee1284-3:armhf
libintl-perl
libio-html-perl
libio-pty-perl
libio-socket-inet6-perl
libio-socket-ssl-perl
libio-string-perl
libio-stringy-perl
libipc-run-perl
libirs-export91
libisc-export95
libisc95
libisccc90
libisccfg-export90
libisccfg90
libisl13:armhf
libjasper1:armhf
libjbig-dev:armhf
libjbig0:armhf
libjpeg-dev:armhf
libjpeg-turbo8:armhf
libjpeg-turbo8-dev:armhf
libjpeg8:armhf
libjpeg8-dev:armhf
libjs-jquery
libjson-c2:armhf
libjson-glib-1.0-0:armhf
libjson-glib-1.0-common
libjson-perl
libjson-xs-perl
libjson0:armhf
libk5crypto3:armhf
libkeyutils1:armhf
libklibc
libkmod2:armhf
libkrb5-26-heimdal:armhf
libkrb5-3:armhf
libkrb5support0:armhf
liblcms2-2:armhf
liblcms2-dev:armhf
libldap-2.4-2:armhf
liblist-moreutils-perl
libllvm3.6:armhf
liblocale-gettext-perl
liblockfile-bin
liblockfile1:armhf
liblog-message-perl
liblog-message-simple-perl
libltdl7:armhf
liblua5.2-0:armhf
liblwp-mediatypes-perl
liblwp-protocol-https-perl
liblwres90
liblzma-dev:armhf
liblzma5:armhf
libmagic1:armhf
libmailtools-perl
libmirclient8:armhf
libmircommon3:armhf
libmirprotobuf0:armhf
libmng2:armhf
libmodule-build-perl
libmodule-pluggable-perl
libmodule-signature-perl
libmount1:armhf
libmpc-dev:armhf
libmpc3:armhf
libmpdec2:armhf
libmpfr-dev:armhf
libmpfr4:armhf
libmro-compat-perl
libncurses5:armhf
libncursesw5:armhf
libnet-dns-perl
libnet-domain-tld-perl
libnet-http-perl
libnet-ip-perl
libnet-smtp-ssl-perl
libnet-ssleay-perl
libnettle4:armhf
libnewt0.52:armhf
libnih-dbus1:armhf
libnih1:armhf
libnss-mdns:armhf
libogg0:armhf
libopts25:armhf
libp11-kit0:armhf
libpackage-constants-perl
libpam-modules:armhf
libpam-modules-bin
libpam-runtime
libpam-systemd:armhf
libpam0g:armhf
libpango-1.0-0:armhf
libpango-perl
libpangocairo-1.0-0:armhf
libpangoft2-1.0-0:armhf
libparams-util-perl
libparse-debcontrol-perl
libparse-debianchangelog-perl
libpcre3:armhf
libperl5.20
libperlio-gzip-perl
libpipeline1:armhf
libpixman-1-0:armhf
libplymouth4:armhf
libpng12-0:armhf
libpod-latex-perl
libpod-readme-perl
libpolkit-agent-1-0:armhf
libpolkit-backend-1-0:armhf
libpolkit-gobject-1-0:armhf
libpopt0:armhf
libprocps3:armhf
libprotobuf9:armhf
libproxy1:armhf
libpthread-stubs0-dev:armhf
libpulse0:armhf
libpython-stdlib:armhf
libpython2.7:armhf
libpython2.7-minimal:armhf
libpython2.7-stdlib:armhf
libpython3-stdlib:armhf
libpython3.4:armhf
libpython3.4-minimal:armhf
libpython3.4-stdlib:armhf
librarian0
libreadline6:armhf
libregexp-common-perl
librest-0.7-0:armhf
libroken18-heimdal:armhf
librtmp1:armhf
libruby2.1:armhf
libsane:armhf
libsane-common
libsasl2-2:armhf
libsasl2-modules:armhf
libsasl2-modules-db:armhf
libsdl1.2debian:armhf
libselinux1:armhf
libsemanage-common
libsemanage1:armhf
libsensors4:armhf
libsepol1:armhf
libsigsegv2:armhf
libslang2:armhf
libsmartcols1:armhf
libsndfile1:armhf
libsocket6-perl
libsoftware-license-perl
libsoup-gnome2.4-1:armhf
libsoup2.4-1:armhf
libsqlite3-0:armhf
libss2:armhf
libssl1.0.0:armhf
libstatgrab9
libstdc++-4.9-dev:armhf
libstdc++6:armhf
libsub-exporter-perl
libsub-install-perl
libsub-name-perl
libsystemd0:armhf
libtasn1-6:armhf
libtcl8.6:armhf
libterm-ui-perl
libtext-levenshtein-perl
libtext-soundex-perl
libtext-template-perl
libtext-unidecode-perl
libthai-data
libthai0:armhf
libtie-ixhash-perl
libtiff5:armhf
libtiff5-dev:armhf
libtiffxx5:armhf
libtimedate-perl
libtinfo5:armhf
libtxc-dxtn-s2tc0:armhf
libubsan0:armhf
libudev1:armhf
libunistring0:armhf
liburi-perl
libusb-0.1-4:armhf
libusb-1.0-0:armhf
libustr-1.0-1:armhf
libuuid1:armhf
libv4l-0:armhf
libv4lconvert0:armhf
libvorbis0a:armhf
libvorbisenc2:armhf
libvpx1:armhf
libvte-2.90-9
libvte-2.90-common
libwayland-client0:armhf
libwayland-cursor0:armhf
libwind0-heimdal:armhf
libwrap0:armhf
libwww-perl
libwww-robotrules-perl
libx11-6:armhf
libx11-data
libx11-dev:armhf
libx11-doc
libx11-xcb-dev:armhf
libx11-xcb1:armhf
libxapian22
libxau-dev:armhf
libxau6:armhf
libxcb-dri2-0:armhf
libxcb-dri2-0-dev:armhf
libxcb-dri3-0:armhf
libxcb-dri3-dev:armhf
libxcb-glx0:armhf
libxcb-glx0-dev:armhf
libxcb-present-dev:armhf
libxcb-present0:armhf
libxcb-randr0:armhf
libxcb-randr0-dev:armhf
libxcb-render0:armhf
libxcb-render0-dev:armhf
libxcb-shape0:armhf
libxcb-shape0-dev:armhf
libxcb-shm0:armhf
libxcb-sync-dev:armhf
libxcb-sync1:armhf
libxcb-xfixes0:armhf
libxcb-xfixes0-dev:armhf
libxcb1:armhf
libxcb1-dev:armhf
libxcomposite1:armhf
libxcursor1:armhf
libxdamage-dev:armhf
libxdamage1:armhf
libxdmcp-dev:armhf
libxdmcp6:armhf
libxext-dev:armhf
libxext6:armhf
libxfixes-dev:armhf
libxfixes3:armhf
libxi6:armhf
libxinerama1:armhf
libxkbcommon0:armhf
libxml-libxml-perl
libxml-namespacesupport-perl
libxml-parser-perl
libxml-sax-base-perl
libxml-sax-expat-perl
libxml-sax-perl
libxml2:armhf
libxmuu1:armhf
libxpm4:armhf
libxrandr2:armhf
libxrender1:armhf
libxshmfence-dev:armhf
libxshmfence1:armhf
libxtables10
libxtst6:armhf
libxxf86dga1:armhf
libxxf86vm-dev:armhf
libxxf86vm1:armhf
libyaml-0-2:armhf
linaro-nano
linaro-overlay-minimal
lintian
linux-firmware
linux-libc-dev:armhf
lm-sensors
locales
lockfile-progs
login
logrotate
lsb-base
lsb-release
m4
make
makedev
man-db
manpages
manpages-dev
mawk
mesa-common-dev:armhf
mime-support
mir-client-platform-mesa2:armhf
module-init-tools
mount
mountall
multiarch-support
nano
ncurses-base
ncurses-bin
ncurses-term
net-tools
netbase
netcat-openbsd
ntp
ntpdate
ocl-icd-dev
ocl-icd-libopencl1:armhf
ocl-icd-opencl-dev:armhf
opencl-headers
openssh-client
openssh-server
openssh-sftp-server
openssl
passwd
patch
patchutils
perl
perl-base
perl-modules
pkg-config
plymouth
plymouth-theme-ubuntu-text
policykit-1
procps
python
python-apt-common
python-minimal
python2.7
python2.7-minimal
python3
python3-apt
python3-chardet
python3-debian
python3-magic
python3-minimal
python3-pkg-resources
python3-requests
python3-six
python3-urllib3
python3.4
python3.4-minimal
rarian-compat
read-edid
readline-common
rename
rsync
rsyslog
ruby
ruby2.1
rubygems-integration
screen
sed
sensible-utils
sgml-base
sgml-data
shared-mime-info
ssh
ssh-import-id
strace
sudo
synaptic
systemd
systemd-sysv
sysv-rc
sysvinit-utils
t1utils
tar
tcpd
tcsh
texinfo
tmux
tzdata
ubuntu-keyring
ucf
udev
unzip
upstart
usbutils
util-linux
vim-common
vim-nox
vim-runtime
wdiff
wget
whiptail
x11-common
x11proto-core-dev
x11proto-damage-dev
x11proto-dri2-dev
x11proto-fixes-dev
x11proto-gl-dev
x11proto-input-dev
x11proto-kb-dev
x11proto-xext-dev
x11proto-xf86vidmode-dev
xauth
xdg-user-dirs
xkb-data
xml-core
xorg-sgml-doctools
xtrans-dev
xz-utils
zlib1g:armhf
zlib1g-dev:armhf
