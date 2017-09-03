---
layout: post
title:  "Github Pages Local Build"
date:   2017-01-26
category: archive
tags: programming
---
Some environment work on getting this site up and running.
<!--more-->

# Github Pages local build

I'm still not clear on local ownership and permissions when dealing with code development. I've been fiddling with jekyll and github pages for a couple weeks now to no avail. I think the issue is that I tried to install the basic ruby using `sudo apt-get install` which leads to permission trouble later. So I decided to remove everything and install it the right way...

Reinstall ruby.

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get remove ruby
```

I got an error message saying the `/var/lib/gems` folder was not deleted because it wasn't empty, so I deleted it manually.

```
sudo rm -r /var/lib/gems
```

Make sure everything is gone.

```
sudo apt-get autoremove
```

Copy of the procedure from [Write permissions for var/lib/gems/](https://stackoverflow.com/questions/37720892/you-dont-have-write-permissions-for-the-var-lib-gems-2-3-0-directory#37956249) on reinstalling ruby [the right way] using rbenv.

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

```
ruby --version
gem install bundler
rbenv rehash
```

At this point I got another error saying that I didn't have write permission to a folder so I changed ownership.

```
/home/[username]/.bundle/cache/compact_index/rubygems.org.443.29b0360b937aa4d161703e6160654e47/versions`
sudo chown -R $(whoami):$(whoami) ~/.bundler
```

Now I can run `gem install bundler` without issue.
Since I was starting from scratch, I initialized a new git repo.

```
git init web
cd web
```

Created a Gemfile for bundler to use.

```
nano Gemfile
```
```
source 'https://rubygems.org'
gem 'github-pages', group: :jekyll_plugins
```
Then installed the dependencies with bundle.

```
bundle install
```

Now you are set to create a blank jekyll template which can be used for local builds on github pages.

```
jekyll new website
```

**Alternatively**, if you wish to use an existing, empty github repo (as I did):

```
git clone [your_repo_URL]
jekyll new [your_repo_name]
cd [your_repo_name]
```

Preview the build on a local server at the default [127.0.0.1:4000](http://127.0.0.1:4000).

```
bundle exec jekyll serve
```

If any errors crop up, add the requisite gem to your Gemfile as I had to do due to a lack of a Java runtime environment.

```
nano Gemfile
```

Add the lines at the end of the file.

```
gem 'execjs'
gem 'therubyracer'
```

Then install the gems.

```
bundle install
```

Rebuild and serve.

```
bundle exec jekyll serve
```

As long as everything looks good, commit and push everything to your repo.

```
git add -A
git commit -a
git push origin
```

Check your email to make sure everything built as it should -github sends you build error messages. Then check your site at [your_username].github.io.
