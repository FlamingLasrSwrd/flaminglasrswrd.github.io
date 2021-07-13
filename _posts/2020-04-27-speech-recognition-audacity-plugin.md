---
layout: "post"
title: "Speech Recognition Audacity Plugin"
date: "2020-04-27 19:03"
category: active
phase: experimental
tags: programming
author: Elijah K. Dunn
zotero-collection:
gallery:
abstract: >
  A speech recognition plugin for Audacity for automatic transcription.
graphical-abstract: /assets/img/speech-tagger/speech-tagger-screenshot.jpeg
---

# Installation
I am using Ubuntu Desktop 19.04 with anaconda python environment manager. Python 3.6 will be used throughout.

Start by installing the Google Speech-to-Text pip package.

```(bash)
pip install --upgrade google-cloud-speech
```

A service and access account has to be created on the [Create Service Account Key page](https://console.cloud.google.com/apis/credentials/serviceaccountkey). Download the credentials and note the location.

Set the location of the credentials environmental variable.

```(bash)
export GOOGLE_APPLICATION_CREDENTIALS="[PATH]"
```

Enable API access from your [API Services Console](https://console.developers.google.com/apis/api/speech.googleapis.com/overview).

More instructions are available on the [general Google Cloud Speech-to-Text Docs website](https://cloud.google.com/speech-to-text/docs/libraries) and [Google Cloud Speech Python-specific documentation](https://googleapis.dev/python/speech/latest/index.html).

## Compile Audacity with mod-script-pipe

Audacity does not ship with scripting support for linux. So it must be compiled with Audacity from source. I am following the instructions [here](https://forum.audacityteam.org/viewtopic.php?f=19&t=107852), but look for the most current build instructions [here](https://forum.audacityteam.org/viewforum.php?f=19).

**NOTE**: There are a lot of caveats to this setup. Consult the [linux build wiki](https://wiki.audacityteam.org/wiki/Building_On_Linux) for more info.

If you already have audacity installed via apt-get, remove it first.

```(bash)
sudo apt remove audacity
```

Install wxWidgets and other packages:

```(bash)
sudo apt install cmake build-essential gcc libwxgtk3.0 libavformat-dev libsndfile1 libasound2-dev libgtk2.0-dev gettext libid3tag0-dev libmad0-dev libsoundtouch-dev libogg-dev libvorbis-dev libflac-dev libmp3lame0 -y
```

Get the Audacity source code from [FossHub](https://www.fosshub.com/Audacity.html) and extract it. Then we build:

```(bash)
cd audacity-*
mkdir build
cd build
../configure --with-lib-preference="local system" --with-ffmpeg="system" --disable-dynamic-loading --with-mod-script-pipe
make -j4
```

We also need to build *mod-script-pipe*

```(bash)
cd lib-src/mod-script-pipe
make -j4
```

Let's test it.

```(bash)
cd ../../
mkdir "Portable Settings"
./audacity
```

If everything works, install it.

```(bash)
sudo make install
sudo mkdir /usr/local/share/audacity/modules
sudo cp lib-src/mod-script-pipe/.libs/mod-script-pipe.so /usr/local/share/audacity/modules/mod-script-pipe.so
sudo cp lib-src/mod-script-pipe/.libs/mod-script-pipe.so.0.0.0 /usr/local/share/audacity/modules/mod-script-pipe.so.0.0.0
```

Run Audacity and enable *mod-script-pipe* from the **Edit -> Preferences -> Modules** menu.

![](/assets/img/mod-script-pipe-enable.png)

Make sure to restart Audacity to use the pipe.

Download and run [pipe_test.py](https://github.com/audacity/audacity/blob/master/scripts/piped-work/pipe_test.py) to make sure everything is connected.

```(bash)
wget https://raw.githubusercontent.com/audacity/audacity/master/scripts/piped-work/pipe_test.py
python pip_test.py
```

You should get lots of *OKs*.

Enable the *Extras* menu by clicking **View --> Extra Menus (on/off)** so that scripting will work correctly.

# Work Log

## 27 Apr 2020
I have an idea.

Lately I have been starting some voice-over work for how-to videos. It seems that sound (and perhaps video) editing will be a major consumer of my time. Since I am mainly doing voiceover, i.e., spoken English language, work, perhaps I can use speech recognition to tag sections for easy editing.

The process that I am envisioning consists of two parts: A python API call to Google Speech and an Audacity python script to insert tags.

Well it's 2am and I finally [got the thing to work](https://www.reddit.com/r/audacity/comments/g9hrjo/hooray_i_wrote_a_script_to_automatically/).

# Bibliography

<!--notes-->

<!--links-->
