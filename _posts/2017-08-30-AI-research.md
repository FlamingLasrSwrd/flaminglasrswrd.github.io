---
layout: post
title:  "AI Research"
date:   2017-08-30
tags: school
category: active
---
Artificial intelligence has held my interest longer than any other topic I have researched. What follows is a collection of researchers and their contribution to the field of AI as well as its implication for my research.
<!--more-->

# Research Interests
Of the dozens of projects I have undertaken, none have held my interest quite like Artificial Intelligence. On many occasions I have lamented the time it takes to analyze a new subject and use that knowledge to solve some problem. E.g. learning a new coding language. These sorts of problems are abhorrent to me because of their redundancy. In the case of coding, how many people across the word have learned to code in a particular language? Wouldn't it be great if we only had to discover/invent something once and then everyone could use that new knowledge? That is where I believe AI will take us, but maybe not in my lifetime.

## Biologically Inspired AI
Many researchers view biological data as convoluted and unnecessary or perhaps even *dirty* when it comes to AI development. Evolution spanning millions of years has made a very complex intelligence machine and not necessarily the best one possible. I still believe, however, that an analysis of the (human) brain is the fastest and surest way to a general AI.

## Evolution Vs Big Data
*Given sufficient time and the right optimization function, big data driven AI research will derive what evolution created over eons with biological intelligence.*

If one could surmise the goal of the evolutionary development of a central nervous system, what would it be?[^1] It would be to generate a processing and storage medium that can use past information to manipulate the world in a way that benefits the organism.

Many of the problems of AI research are shared by evolution.
* How is information stored?
* How is information used to manipulate the world?
* How is resource use minimized?

# Researchers
*A list of researchers or groups which I reference heavily.*

## Stephen Grossberg
Adaptive Resonance Theory (ART)[^grossberg_adaptive_2013] is a top-level architecture derived from biological data. It is quite hard to adequately describe ART is just a few sentences. Grossberg's research encompases more than 40 years of development with information spanning all areas of AI research. Here is one sentence of the various explanations given by Grossberg:

> ART provides functional and mechanistic explanations of such diverse topics as laminar cortical circuitry; invariant object and scenic gist learning and recognition; prototype, surface, and boundary attention; gamma and beta oscillations; learning of entorhinal grid cells and hippocampal place cells; computation of homologous spatial and temporal mechanisms in the entorhinal–hippocampal system; vigilance breakdowns during autism and medial temporal amnesia; cognitive–emotional interactions that focus attention on valued objects in an adaptively timed way; item–order–rank working memories and learned list chunks for the planning and control of sequences of linguistic, spatial, and motor information; conscious speech percepts that are influenced by future context; auditory streaming in noise during source segregation; and speaker normalization.

I have been working my way through Grossberg's work for the better part of a year and I still feel ignorant. From what I have gathered so far, ART will be an integral part of my research in the future.

### Summary
Adaptive Resonance Theory defines several entities in the brain which control the flow of information processing throughout the bulk of the memory storage/computational medium. ART does not explain the fine grain details of cortex organization and information processing as [#Numenta][] does. Rather, ART focuses on what information those repeating units are exposed to and assumes those units will process and learn that information interchangeably. Two particularly interesting concepts of ART and its successors (e.g. ARTSCAN) are the "ART search cycle" and "invariant category learning". The former details how a brain might go about combining old, stable memories with novel information without compromising the integrity of the first. The latter combines this with an internal learning switch that inhibits the search cycle while more information is gathered.

## Numenta
Jeff Hawkins and his research group has developed a more localized theory of the brain: Hierarchical Temporal Memory (HTM). Their research attempts to model a single column of neurons in the neocortex. Unlike Deep Learning and similiar algorithms, HTM uses temporal information integrally.
> We demonstrate that HTM networks learn complex high-order sequences from data streams, rapidly adapt to changing statistics in the data, naturally handle multiple predictions and branching sequences, and exhibit high tolerance to system faults. [^cui_continuous_2016]

# Current Working Theory


# Bibliography
[^grossberg_adaptive_2013]: Grossberg, Stephen. 2013. “Adaptive Resonance Theory: How a Brain Learns to Consciously Attend, Learn, and Recognize a Changing World.” Neural Networks 37: 1–47. doi:10.1016/j.neunet.2012.09.017.
[^cui_continuous_2016]: Cui, Yuwei, Subutai Ahmad, and Jeff Hawkins. 2016. “Continuous Online Sequence Learning with an Unsupervised Neural Network Model.” Neural Computation 28 (11): 2474–2504. doi:10.1162/NECO_a_00893.


[^1]: Yes, I know that isn't how evolution works.
