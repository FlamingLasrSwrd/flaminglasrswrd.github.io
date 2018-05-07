---
layout: post
title: AI Research
date: 2017-08-30T00:00:00.000Z
tags: school
category: active
abstract: >
  Artificial intelligence has held my interest longer than any other topic I have researched. Here are my notes on AI. They are not really for the benefit of reading, just the writing. I rarely even read it.
---

# Research Interests

Of the dozens of projects I have undertaken, none have held my interest quite like Artificial Intelligence. On many occasions I have lamented the time it takes to analyze a new subject and use that knowledge to solve some problem. E.g. learning a new coding language. These sorts of problems are abhorrent to me because of their redundancy. In the case of coding, how many people across the word have learned to code in a particular language? Wouldn't it be great if we only had to discover/invent something once and then everyone could use that new knowledge? That is where I believe AI will take us, but maybe not in my lifetime.

## Biologically Inspired AI

Many researchers view biological data as convoluted and unnecessary or perhaps even _dirty_ when it comes to AI development. Evolution spanning millions of years has made a very complex intelligence machine and not necessarily the best one possible. I still believe, however, that an analysis of the (human) brain is the fastest and surest way to a general AI.

## Evolution Vs Big Data

_Given sufficient time and the right optimization function, big data driven AI research will derive what evolution created over eons with biological intelligence._

If one could surmise the maximization function of central nervous system natural selection, what would it be? It would be to generate a processing and storage medium that can use past information to manipulate the world in a way that benefits the organism.

Many of the problems of AI research are shared by evolution.

- How is information stored?
- How is information used to manipulate the world?
- How is resource use minimized?

# Researchers

_A list of researchers or groups which I reference heavily._

## Stephen Grossberg

Adaptive Resonance Theory (ART)[^GrossbergAdaptiveResonanceTheory2013] is a top-level architecture derived from biological data. It is quite hard to adequately describe ART is just a few sentences. Grossberg's research encompases more than 40 years of development with information spanning all areas of AI research. Here is one sentence of the various explanations given by Grossberg:

> ART provides functional and mechanistic explanations of such diverse topics as laminar cortical circuitry; invariant object and scenic gist learning and recognition; prototype, surface, and boundary attention; gamma and beta oscillations; learning of entorhinal grid cells and hippocampal place cells; computation of homologous spatial and temporal mechanisms in the entorhinal–hippocampal system; vigilance breakdowns during autism and medial temporal amnesia; cognitive–emotional interactions that focus attention on valued objects in an adaptively timed way; item–order–rank working memories and learned list chunks for the planning and control of sequences of linguistic, spatial, and motor information; conscious speech percepts that are influenced by future context; auditory streaming in noise during source segregation; and speaker normalization.

I have been working my way through Grossberg's work for the better part of a year and I still feel ignorant. From what I have gathered so far, ART will be an integral part of my research in the future.

### Summary

Adaptive Resonance Theory defines several entities in the brain which control the flow of information processing throughout the bulk of the memory storage/computational medium. ART does not explain the fine grain details of cortex organization and information processing as [#Numenta][] does. Rather, ART focuses on what information those repeating units are exposed to and assumes those units will process and learn that information interchangeably. Two particularly interesting concepts of ART and its successors (e.g. ARTSCAN) are the "ART search cycle" and "invariant category learning". The former details how a brain might go about combining old, stable memories with novel information without compromising the integrity of the first. The latter combines this with an internal learning switch that inhibits the search cycle while more information is gathered.

## Numenta

Jeff Hawkins and his research group has developed a more localized theory of the brain: Hierarchical Temporal Memory (HTM). Their research attempts to model a single column of neurons in the neocortex. Unlike Deep Learning and similiar algorithms, HTM uses temporal information integrally.

> We demonstrate that HTM networks learn complex high-order sequences from data streams, rapidly adapt to changing statistics in the data, naturally handle multiple predictions and branching sequences, and exhibit high tolerance to system faults. [^cui_continuous_2016]

# Coherence

A system of information is said to be coherent if all statements in the system are logically consistent, i.e. that the implications or propositions of one subsystem are not at odds with other statements. It is an epistemology of relative truth. A system can be the entire universe, a brain, or the energy of a single photon. A system must also contain definitions of the boundaries of that system.

> Implied: Mathematics of propositional logic.<br>
> All men are mortal. -> Draws two boundaries: _Men_ and _Mortals_. Places _men_ within the boundaries of _mortals_.<br>
> Socrates is a man. -> Draws a third boundary: _Socrates_. Places Socrates within the boundaries of _Man_.<br>
> ... Socrates is mortal. -> Implies Socrates is within the boundaries of _Mortal_.

Rather than an implication of the verisimilitude of a person's belief, I use this epistemology to explain one aspect of intelligence: Each new bit of information is judged by its coherence with the brain rather than its truth. The human mind is influenced by the past both immediately perceived information and evolutionary.

# Features of Intelligence

- Memory - method to store past information
- Processing - method to manipulate present information
- Constraints - method(s) to maximize efficiency

# Spatial vs Temporal Invariance

Stimuli can be divided into three classes based upon invariance under spatial and/or temporal invariance. TODO

## Constraints

Constraints on intelligence are necessary in a competitive universe. Natural selection favors maximizing intelligence capability with respect to resource consumption. The same goes for machine learning development and in fact all development. An intelligence capable of incorporating all the information in the universe without constraints would necessarily be the size of the universe. Therefore, to develop a practical AI, constraints on the ability and capacity are necessary. The question is: What constraints do we choose to develop?

### Prediction

Q: Why would evolution produce beings that can predict future events? A: Prediction provides a method to judge the relevance of a stimuli to an internal state. This judgment can be used to reduce processing requirements and increase processing capacity. Natural selection produced brains that assume stimuli in close temporal proximity are more likely to be related to one another than those stimuli which are not. Furthermore, one stimuli that precedes another is more likely to be causative of that stimuli. Or perhaps more definitively: causality does not flow backwards. Stimuli which are not useful in prediction can be excluded from processing in the future. Prediction allows an intelligence to increase the time between stimuli and any reaction caused by that stimuli thus giving the intelligence the advantage of extra processing. Furthermore, prediction reduces the processing requirements by defining irrelevant stimuli. A stimuli judged to be predictive must have two features: advanced temporal proximity and stability. TODO: spatial proximity

#### How is prediction implemented?

# Definitions

## Equivariance

## Stimuli

A stimuli transfers information from the external to the internal environment. The environment can be defined as any arbitrary boundary; e.g. a single neuron or the entire brain.

# Prior Art

## Convolutional Neural Networks

Adds spatially invariant feature recognition.

# Competition

- local groups of units which can represent similar but mutually exclusive objects compete with one another for output by inhibiting the output of others while sharing roughly similar inputs
- unit activity correlates with certainty of output
- feed-back from feed-forward projections of a local group modulate inputs of local group to increase certainty
- all unit activity (certainty) and data transmission decays with time
- Learning rate is correlated with uncertainty and is contingent upon winner selection

Feed-forward information from the senses traverses the hierarchy of processing until it reaches a point of uncertainty. That point is where the mutual activation of a local group of cells and their resultant mutual inhibition reduces the group's output to below the activation threshold of the next layer. Three possibilities can occur as a result of this uncertainty. The first two result in a winning cell in the local group which continues the information propagation upwards. The third does not result in a winner and ends the information processing. The first process uses information from higher layers to fill in missing or manipulate bottom-up data. This provides a means of corroborating feature maps across a larger spatial or temporal space. The second process results as an integration of signal over time and is essentially a measure of the most likely. The extra time that it takes to reach a threshold of activation is the balancing factor between processing efficiency and capacity. More feature sets can be compared if an intelligence has the time to examine all of them at once. Conversely, if an intelligence has been trained to think quickly, less feature sets can be compared. The third process is the terminal fate of all sensory information in the brain. If the uncertainty cannot be clarified by either feed-back or time, the information decays and is lost. The ratio of time to action is a measure of tolerance to uncertainty.

# Ideas

## Use Cases

The space of possible problems for AI to work on:

- linear categorization; entirely feedforward capable inputs; simple input to output mapping
- expected non-occurrence of reward
- unexpected non-occurrence of reward
- specific vs. general inputs
- goal orientated behavior
- external reward
- expectation
- unexpectation
- noise vs. saturation
- one-to-many
- many-to-one
- inhibitory matching
- excitatory matching
- stability vs. plasticity

A global reinforcement center? A global measure of uncertainty prevents spurious, random associations from guiding action. Tonically inhibit action until global convergence of certainty is achieved. This includes measures of physical movement are taught to the cerebellum...

- learning is propagated backward from appropriate outputs
- what if no training signal is defined?

  - learning spans the combinations of inputs to the limit of processing capabilities

- a training signal accelerates development in the wanted direction

  - e.g. given sufficient observation without any reward, a human child has the capacity to learn to speak. However, this is probably not possible given the time it would require and the shear number of possible inputs.

What if consciousness was developed in humans because our brain's capacity outstripped its inputs? I.e. The sensory information (in the mathematical sense) decays as it travels to higher and higher levels of processing and is successively obscured by internal hallucinations (feed-back projections). The sensory information never reaches our highest levels of processing and therefore leaves a certain amount of high level processing available solely for internal computation. In essence, some brain capacity is devoted entirely to processing internal, spontaneous information generation. The amount and capacity of this processing is what we call consciousness. In contrast, lower animals have a lower brain capacity to sensory input ratio and therefore do not possess the ability to think outside the realm of their inputs. Schizophrenia is a disease of too much consciousness.

# Journal
*Not likely useful to anyone.*

## 17 APR 2018
- If you define the set of brain inputs ```I```, the total number of brain nodes ```N```, and stipulate that node inputs are preinstantiated, each node will have ```i <= N+I``` for inputs ```i```. A fully connected brain has ```i = N+I```. A brain with ```i < N+I``` is necessarily hierarchical. A hierarchical brain would be more efficient but less capable: A hierarchical brain can learn faster but with less specificity. A non-recursive node has ```i <= N+I-1```. Recursive connections can be used to define temporal relation of a node to itself, i.e. the decay time of its signal.

### What is the fundamental computational unit of the mind?
Is it the neuronal activation? A collection of neuronal activations, i.e. SDR? What if the fundamental unit of computation is the synapse? Hebbian neurons represent the synapse as a simple transfer function, linear or otherwise. That interpretation permeates the literature. What if synaptic transmission goes both ways? What if the activation of the post-synaptic neuron feeds back to the presynaptic neuron to alter its excitation? Like a confirmation signal. Pre says to Post, "I detect this feature." Post says to Pre, "I detect this class, of which, you say your feature is composed." Post and Pre both increase connection weight. Alternatively, Post says to Pre, "I didn't detect a class, of which, you say your feature is composed." Pre and Post decrement their transmitter release and capture, respectively. Presynaptic reuptake and glial uptake seems to be related here.

**Update** This is sometimes called the retrograde messenger system...[^regehr_activity-dependent_2009]


## 06 APR 2018
### Attributes, Classes, Objects, Properties, Values, Inputs
How does the brain distinguish classes from properties? Take vision for example: When looking at a complex scene, what constitutes a *feature* and what is an *object*? What does it mean to be a feature/object? How does a brain learn this distinction? Different values of features cannot occur simultaneously for a single object. Objects can occur simultaneously in an input space but are always disjoint in space. Put another way: For a given input space, *objects* compete to group inputs based on prior knowledge of typical objects (e.g. a line is a useful object for grouping similarly colored, continuous points). In the brain, object groupings are competitive with similarly sized spatial groupings. Further up the hierarchy, a neuron receives information from larger areas of the retina. Groupings are useful for selective attention or any other sort of transformation of input that applies to a large number of neurons at a time. As in, signals from other brain regions propagate over an entire grouping and stop at object boundaries. Similarly with auditory input: Groupings/objects/classes are assigned to completely partition the inputs into disjoint time slots. Higher levels of the hierarchy correspond to greater time spans from which to establish boundaries. The boundaries between objects stop the propagation of top down signals from spilling over to unrelated objects. The implementation of spatial boundary establishment seems significantly easier than time boundary establishment. The latter seems to require a short term memory, or maybe differing time averaging of inputs. Perhaps different gates that transition from short term to long term activation? The detection of a feature set would activate a object and objects can have different output signal decay times? A friendly face you haven't seen in a long time seems to stay in your thoughts longer than either one you don't recognize or one you seem often... Ionotropic vs metabotropic?? Conscious activation? Low level visual objects like 'line' shouldn't be persistent but they can be with conscious manipulation... Perhaps conscious attention serves to make objects persistent?

What purpose does this serve? If a layer of computation (corresponding to similar receptive fields in time or space) disagrees about the partitioning, computation does not progress. Practically, this means that objects in a single layer inhibit each other's outputs until sufficient agreement is made on the placement of boundaries.

It seems like object partitioning requires two separate processing streams (what/where streams?). The establishment of boundaries shouldn't actually manipulate the inputs, but rather only propagate meta-signals like attention. If that is the case, it would be rather simple to implement a layer on top of existing deep learning systems that simply control partitioning. A deep learning system is capable of learning anything, this framework just makes it faster, less redundant, and probably with greater ontological errors.

This whole system also seems separate from any actual input manipulation like visual averaging. Or perhaps when a layer has completed its partitioning, feature prototype activation leads to averaging? Maybe at sufficiently low processing levels, visual averaging is a learned prototypical feature transformation? As in, visual averaging is included in V1-4 because the objects processed in those layers always benefit from feature averaging. Or perhaps that is something different...

# Bibliography

[^GrossbergAdaptiveResonanceTheory2013]: Grossberg, Stephen. 2013\. "Adaptive Resonance Theory: How a Brain Learns to Consciously Attend, Learn, and Recognize a Changing World." Neural Networks 37: 1–47. <https://doi.org/10.1016/j.neunet.2012.09.017>.
[^cui_continuous_2016]: Cui, Yuwei, Subutai Ahmad, and Jeff Hawkins. 2016\. "Continuous Online Sequence Learning with an Unsupervised Neural Network Model." *Neural Computation* 28 (11): 2474–2504. <https://doi.org/10.1162/NECO_a_00893>.
[^regehr_activity-dependent_2009]: Regehr, Wade G., Megan R. Carey, and Aaron R. Best. 2009. “Activity-Dependent Regulation of Synapses by Retrograde Messengers.” *Neuron* 63 (2): 154–70. <https://doi.org/10.1016/j.neuron.2009.06.021>.



<!--Abbreviations-->
*[TOTD]: Thought of the Day
*[SDR]: Sparse Distributed Representation
