---
layout: page
title: "Short Term Memory"
permalink: /stm/
---

This is a collection of all the things my short term memory is unable to adequately assimilate.

# TODO

* Migrate the rest of old site and past projects.

# Lead Dioxide Anode

## Lead Nitrate Synthesis

* 255g lead metal
* unknown quantity of dilute HNO_3

# Archived Project Front Matter

---
layout: post
title: ""
date: [YYYY-MM-DD]
categories: [electronics][chemistry][nootropics]
status: [completed][active][in progress]
---

# Star San Replacement
$25 - 32 oz. Star San
  -> 0.945 L -> (1.335 kg/L) -> 1.26 kg -> 0.63 kg H3PO4
 = $39/kg H3PO4

## Original Recipe
* 50% phosphoric acid
* 15% Dodecylbenzene Sulfonic Acid (surfactant)
* 10% isopropyl alcohol
* other - trade secret

## 1st Level Purchase
eBay - phosphoric acid 85% 1 gal $50
 (1.685 kg/l) -> 6.37 kg -> 5.4 kg H3PO4
 = $9.2/kg H3PO4

## Burning Phosphorus
P4 + 5O2 -> P4O10

P4O1O + 6H2O -> 4 H3PO4

For 1kg H3PO4:
-> (98 g/mol) -> 10.2 mol -> 2.6 mol P -> (30 g/mol) -> 77g P
From matchbooks -> 0.03g/box -> 2600 boxes!

# HEPA Flow Hood

* 23.375" x 23.375" x 11.5" MERV 15 Filter
* 2" flow straightener from straws

# Database

## Assumptions

* Time flows forward - only incremental timestamps

## TODO
* Fuzzy error handling
* Decision making
* Instantiation, Inheritance
*

## Function - Process - Macro - Procedure - Operation

### Reversible Process
[state]'object: [state]object


## Classes - Item Types
* Structure
* Methods

# Github Pages local build

I'm still not clear on local ownership and permissions when dealing with code development. I've been fiddling with jekyll and github pages for a couple weeks now to no avail. I think the issue is that I tried to install the basic ruby using `sudo apt-get install` which leads to permission trouble later. So I decided to remove everything and install it the right way...

Reinstall ruby.
`sudo apt-get update`
`sudo apt-get upgrade`
`sudo apt-get remove ruby`
I got an error message saying the `/var/lib/gems` folder was not deleted because it wasn't empty, so I deleted it manually.
`sudo rm -r /var/lib/gems`
Make sure everything is gone.
`sudo apt-get autoremove`
From https://stackoverflow.com/questions/37720892/you-dont-have-write-permissions-for-the-var-lib-gems-2-3-0-directory#37956249.
```
sudo apt-get install git-core curl zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev python-software-properties libffi-dev
git clone https://github.com/rbenv/rbenv.git ~/.rbenv
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(rbenv init -)"' >> ~/.bashrc
exec $SHELL
git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build
echo 'export PATH="$HOME/.rbenv/plugins/ruby-build/bin:$PATH"' >> ~/.bashrc
exec $SHELL
rbenv install 2.3.1
rbenv global 2.3.1
ruby -v
```
Starting with the [Github Pages Local Setup](https://help.github.com/articles/setting-up-your-github-pages-site-locally-with-jekyll/) article.
`ruby --version`
`gem install bundler`
`rbenv rehash`
At this point I got another error saying that I didn't have write permission to `/home/[username]/.bundle/cache/compact_index/rubygems.org.443.29b0360b937aa4d161703e6160654e47/versions`, so I chowned it to my user.
`sudo chown -R $(whoami):$(whoami) ~/.bundler`
Now I can run `gem install bundler` without issue.
Since I was starting from scratch, I initialized a new git repo.
`git init web`
`cd web`
Created a Gemfile for bundler to use.
`nano Gemfile`
```
source 'https://rubygems.org'
gem 'github-pages', group: :jekyll_plugins
```
Then installed the dependencies with bundle.
`bundle install`
Now create a blank jekyll template which will become my github pages folder.
`jekyll new ekdunn.github.io`
