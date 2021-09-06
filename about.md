---
layout: page
title: About
permalink: /about/
abstract: >
  The following descriptions are good approximations of my character, but always
  with caveats and made as grandiose as possible.
---

# Site Title
*Newton's flaming laser sword* is a term coined in 2004 by Mike Alder. In an article in __Philosophy Now__, Alder draws a parallel between the well known *Occam's Razor* and this new cleaving tool. With Occam's razor, the search space of possible solutions to a problem or question only the most parsimonious survives. While this is extremely helpful, Newton's flaming laser sword is "much sharper and more dangerous". Put simply, it says that only propositions that can be tested with science should be considered or even discussed.  [@alder_newtons_2004]

Thus the scope of this site is defined: Anything that can be tested with science. More narrowly I tend to stick to the fields of chemistry, physics, philosophy, electronics, and computer science.

# Descriptive Titles
In no particular order:

- Pragmatist
- Secular Humanist
- Atheist
- Existentialist
- Egotistical Altruist
- Skeptic
- Hopeful Marxist
- Human
- Animal
- Resident of Earth

# Philosophical Inspiration
- Seneca
- Sagan
- Marx
- Freud
- Feynman
- Hobbes
- Nietzsche

# Other Influences
- Too much science fiction
   - Heinlein
   - Dick
   - Bradbury
   - Asimov

# Current Life Goal
To maximize my contribution to the human race.

- maximize the total AUC of contribution vs time
- contribution: open to subjective interpretation; anything from reproduction to global welfare; Eudaimonia

# Research Process
My current research process proceeds through several utility programs:

- [Zotero][]
- [Foxit PDF reader][]
- [Zotfile][]
- [Better Bibtex][]
- [Atom][]
- [Pandoc][]
- [Jekyll][]
- [Github][]

## Building This Website

This site is first written in pandoc markdown format using Atom. The markdown-writer plugin (and [personalized config file](/assets/src/_mdwriter.cson)) is particularly useful.

Then a series of hacks and poorly coded {{liquid}} tags are fed into Jekyll. The ruby gem jekyll-pandoc uses a bibliography exported by Better-Bibtex from Zotero to generate the appropriate citations using a custom .csl style I made for markdown. The complete set of html and associated files are backed up to github and transferred via a [rsync script](/assets/src/push_fls_site.sh) to my web host NearlyFreeSpeech.net.

## Progress Phase Tags
Each project page will have a *progress* liquid tag that describes how far along each project is.

### Exploratory
The first phase. This is the initial research phase where the project general parameters are expanded or narrowed. Prior art is located and skimmed.

It is at this phase that a project is determined to be feasible. Primary reasons for project abandon are: expense, lack of tooling, or sufficient documentation elsewhere.

A project in the exploratory phase may or may not have a dedicated project page. They usually start as an aside on the [Work Log]({{ site.url }}/log/) page.

### Research
Primary research is more of an extension of the exploratory phase than a distinct phase. The major difference is more thorough documentation of prior art and research. This is where Zotero comes into play.

Projects in the research phase are given posts.

### Experimental
Some projects require intermediate experimentation to determine direction and/or gain experience. These experiments will probably not be documented extensively except to point out failures and ultimate success.

### Design
Once experimentation and/or research has revealed a path forward, the design phase begins. Small details are worked out.

### Results
Primary results are reported. This may or may not come before the design phase.

### Write-Up
The final and ideal end-point of a project is a write-up. Of course there will be notes along the way, but a complete how-to or more formal *Methods* description is easier to repeat.

## Priority Tags
Sometimes projects have fallen out of interest. *low* - *high* priority tags reflect that.

# Stats

- [ENTP][][^1]
- Typicall score high on Need for Cognition, Openness to Experience, and Epistemic Curiosity

![Big Five personality results.]({{ site.url }}/assets/img/big5.png) [^2]

# Contact

Email me: flaminglasrswrd at protonmail dot com

<button class="btn" type="button" data-toggle="collapse" data-target="#pgp" aria-expanded="false" aria-controls="pgp">PGP Public Key</button>
<div class="collapse" id="pgp"><div class="card card-body">
    {{site.pgp}}
</div></div>

# Bibliography

<!--notes-->
[^1]: This used to be INTP, but I've come out of my shell a bit. Also, Myers-Briggs isn't a very good test anyway.
[^2]: I disagree with the results on agreeableness. I am usually quite trustful, straightforward, altruistic, and modest. I would not consider myself tender-minded. This particular test from [OpenPsychometrics][] had some unusual questions.

<!--links-->
[ENTP]: https://www.16personalities.com/entp-personality
[OpenPsychometrics]: https://openpsychometrics.org
[Zotero]: https://www.zotero.org/
[Foxit PDF reader]: https://www.foxitsoftware.com/pdf-reader/
[Zotfile]: https://zotfile.com/
[Atom]: https://atom.io/
[Better Bibtex]: https://retorque.re/zotero-better-bibtex/
[Jekyll]: https://jekyllrb.com/
[Github]: https://github.com
[Pandoc]: https://pandoc.org
