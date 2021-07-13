---
layout: post
title: AI Research
date: 2017-08-30T00:00:00.000Z
tags: school
category: active
phase: research
author: Elijah K. Dunn
zotero-collection: https://www.zotero.org/ekdunn/items/collectionKey/VJCJE86P
abstract: >
  Artificial intelligence has held my interest longer than any other topic I have researched. Here are my notes on AI. They are not really for the benefit of reading, just the writing. I rarely even read it.
---

# Algorithm

1. Neuron duty cycle is proportional to input duty cycle but always less.

2. Neuron activation is proportional to confidence.

3.

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

# Work Log
This work log, perhaps more than others, is a work in progress. In terms of AI, the only thing that really matters is the final algorithm. So unless there is actual code being proposed, none of this is considered true.

## 30 Jun 2021
Deep learning is slow because of the elimination of local maxima. It will always have difficulty explaining itself.

What we determine to be a singular class of objects (e.g. chair) is a collection of disparate classes. Form, function, etc. The class is not concentrated in a single area of the brain.

## 27 Apr 2021
Abductive reasoning: The process of determining the most likely cause of a surprising event by searching the mind for plausible causal chains after the fact.
> Harman [62] labels this process “inference to the best explanation”. Thus, one canthink of abductive reasoning as the following process: (1) observe some (presumablyunexpected or surprising) events; (2) generate one or more hypothesis about these events;(3) judge the plausibility of the hypotheses; and (4) select the ‘best’ hypothesis as theexplanation [78]. [@miller_explanation_2019]

This is the same search and reset cycle from ART. Perhaps the single most important feature of the human mind. The ability to think backward in time and space.

Novel information penetrates the mind to the exact point where it is either entirely known or minimally known. Some global evaluation of unknown/known is necessary to generate counterfactuals.

## 10 Mar 2021
HTM is fundamentally a spatial algorithm. By that I mean that HTM is a basically a regular neural network but one that relies on similar concepts being physically close together. This works well for concepts that are naturally related by proximity. The number *1000* is very similar to the number *1001* and thus representing them in spatial proximity adequately captures their relatedness. All the algorithm has to do is learn that spatial proximity equals related and it works. Its basically just an engine for determining relatedness that's already predefined, although perhaps not consciously, by the programmer.

HTM is less effective for something like words where the concept that a word represents is almost entirely divorced from the actual spelling of the word.

All of the real work is in HTM's spatial pooler. That work being essentially done by the user.

> A second constraint requires that the permanence value be a function of the distance between the SP column’s position and the input column’s position, such that the closer the input is to the column the larger the value should be. [@mnatzaganian_mathematical_2016]

And, with that, you have spatial correlation.

https://en.wikipedia.org/wiki/Is-a
https://en.wikipedia.org/wiki/Tf%E2%80%93idf
https://en.wikipedia.org/wiki/Ontology_learning
https://en.wikipedia.org/wiki/Automatic_taxonomy_construction

## 02 Mar 2021
Top-down only differs from bottom-up by connection strength?

Why does top-down even exist? If the features that indicate some top-down activation are sufficient to distinguish some related concepts, then why don't they simply become features of that concept? Physical limitations of the brain, perhaps?

Or is it to preserve the order of information? A conversation about animals shouldn't always bring up "Python", but when someone says the word *Python* in a conversation about animals, one does not suddenly think the conversation switched to talking about the Python programming language.

Top-down represents the necessary but not the sufficient causes. Bottom-up represents the sufficient causes.

Then the question becomes, can/should a top-down connection ever become a bottom-up connection (are they of different kind and not just magnitude)?

What happens if the Python programming language changes its name to Py or something? In this example, whenever someone says the word python they necessarily mean the animal (obviously neglecting the Monty- version).

## 31 Jan 2021
[REBUS and the Anarchic Brain: Toward a Unified Model of the Brain Action of Psychedelics](https://pharmrev.aspetjournals.org/content/71/3/316)

I should read more of the literature. A lot of the concepts that I have been talking about here have specific, broadly-recognizable names. I am such an amateur.

## 18 Dec 2020
While reading some Le Guin this morning, I can to a realization. In science fiction, it is often the job of the author to imagine things that have never been conceived previously. When writing about unknown and wholly foreign societies, how could an author determine their features, habits, culture, thoughts, etc.?

To that I say: The logical not.

One of the most useful techniques for exploring new frontiers of thought is the consideration of the logical *not* of a concept. Once you have determined the name for a thing (e.g. a circle), you can think about the inverse of that thing (e.g. not a circle). In this way, you can systematically imagine exactly everything in the universe, since everything is either a thing or not thing.

When you think of *not a circle* nothing immediately springs to (my) mind that typifies that concept. For what, exactly, is the opposite of a composite thing? Instead of *not a circle* we can think of the inverse of certain base features of an object such as *not perfectly round* or *not in 2 dimensions*. I think that this process indicates two features of our mind.

First, that *logical not* is not explicitly codified in our brains. Rather it is the absence of top-down signaling and corresponding resurgence.

The same phenomenon responsible for the "negative photo afterimage" illusion applies to internal signals as well. By constantly activating a particular thing and then removing that activation, competition from things at the same conceptual are reinforced.

Second, that the benefits of the logical not of a thing are most pronounced when a thorough ontology surrounding the thing has been established. For example, the logical not of circle may be hard to interpret if you only understand *circle* to mean *a round thing*. If instead, you know a circle consists of all points equidistant from a given point in a single plane, then the logical not of that thing is "not all points equidistant from a given point not in a single plane" or some other derivations.

Perhaps more clearly: What is the opposite of white? Black, quite obviously. What is the opposite of red? Green? What is the opposite of fuscia? Html #4F1AA3?

You will find that the simpler a concept is, the easier it is to find the opposite of it is. This is, in part, because simpler concepts can be physically (and therefore conceptually) close together in the brain. More complex ideas must be physically spread out to account for all the complexity.

## 08 Dec 2020

If we can focus on the written word for a moment... Specifically machine-readable characters with the penultimate goal being to determine the necessary ingredient of an AI that are required to interpret the grammar of, say, a JSON file without supervision.

The smallest input unit that we can define for the English language would be the letter. Or more accurately in terms of the digital representations would be ASCII or probably UTF-8 characters more broadly.

We define the smallest unit based on partitionability. The physical makeup of these units are not related, e.g. the letter *A* doesn't share any physical characteristics with the letter *Q* that are useful in determining their meaning. I know there is a word for this phenomenon, but I can't think of it at the moment.

This is not true for the spoken word, however. Phonemes are considered the smallest unit of speech. You cannot use letters as the fundamental unit because the pronunciation of the letter depends on the context in which it resides. E.g. the sound a *C* makes depends on whether it's followed by a *H*. This interdependence makes letters an unsuitable fundamental unit of speech.

Characters are also binary in their existence. They either exist or they don't--there is not gradient of character. Similarly, the temporal information in the written word is discrete--each character occupies the same unit of time as any other character.

I am using written word as a thought experiment, but hopefully this method can be applied to any GAI problem eventually.

So how do we derive meaning from a series of characters? How do we determine the difference between randomness and information? Why would an intelligence do such a thing to begin with?

*We can expose a brick to every input in the universe, but nothing about the brick will change.*

We must first define some sort of goal--Some characteristic response of the intelligence.

I think this is where the current approach to AI is fundamentally flawed. Most AI algorithms are treated as automata: A black box of inputs and required outputs. Humans do not function that way. Our "goal" is not necessarily to generate some output. I cannot say exactly what out goal truly is, but it sure isn't simply "output".

What would happen if we gave the intelligence the response of prediction? As in, the goal of this AI is to predict future input.

Back to the written word: If our intelligence is exposed to a series of characters and has the intention to predict the next character we can start to see how information can be gathered.

The intelligence starts by forming simple, linear predictions between and two coincident characters. E.g. *q* is 90% probably followed by *u*.

This would be a simple, single layer system. Each computational unit would respond to a specific character and then output a prediction for the next character.

Several requirements arise from even this simple setup.

By what standard would each unit judge its accuracy and, by extension, its compliance with the main goal?

Would the predictions be singular? As in, could a single unit only make a single prediction or should it be an array of connections to all other possible units with accompanying probabilities?

Also, the processing time for each unit must be less than the character input timing. In order to be considered a "prediction" it must occur before. So the *q* unit must predict *u* before the character *u* has inputted. Similarly, the prediction should only be predictive for the next iteration. This sets up a refractory period in which a unit is awaiting feedback from the next iteration on a prediction.

This would provide some higher level grouping simply by processing time. I.e. single character units tend to predict other single character units but not multicharacter units.

If we assume only local information is available to these units, then feedback mechanisms must also be local. As in, there isn't a mechanism (atm) that determines global goal satisfaction. But this means that there are at least four types of information transfer to a computational unit: input, output, prediction, feedback.

A prediction cannot be treated the same as an input. For if there is some feedback mechanism that is proportional to the inputs, then the prediction can self-strengthen.

Similarly, feedback cannot be treated as input for the same looping problem. The gain on both of these information transfers must be < 1.

...

Given the infinite complexity of language, single step linear prediction can only go so far. For even if you could predict the next letter within a word with perfect accuracy, the next word would be a mystery.

This brings us to the concept of meta characters: characters that do not inherently contain information rather they serve to alter the information of other input(s). The *space* character is a good example. Spaces serve to partition groups of characters.


## 07 Dec 2020

### Principles of Relatedness

*Relatedness* is some measure of inter-predictability between things: i.e. they share some properties.

Thing *A* is more related to thing *B* if:

1. *A* and *B* are temporally coincident
2. *A* and *B* are spatially coincident

Of course, not all that is coincident is related, or rather, relatedness is only proportional to temporal and spatial coincidence. These two premises are actually derivatives of the central axiom or relatedness:

> *A* and *B* are related if they share properties.

But that statement relies heavily on the definition of properties since "properties" can be *things* themselves.

This is mostly a restatement of coherence since coincidence is also a *thing*.

In fact, there is no way for me to imagine much less describe a concept other than *thing*. I can't even describe the issue without tautology. That's why all ontologies start from the all encompassing *Thing*.

Anyway...

Almost as important as coincidence is non-coincidence or non-relatedness and you cannot determine one without the other. This is how we partition the universe: things that are related and things that are not. (Predicate) Logic is built this way.

One might imagine that specialization in either temporal or spatial coincidence could be beneficial. And that those specialized be physically separate (perhaps one to the left and one to the right of center?) to reduce interference.

Interference arises because the temporal coincidence and spatial coincidence are themselves mostly unrelated. There are two cases of this: spatially coincident things which are temporally disparate, and temporally coincident things which are spatially disparate.

An example of the former is the concept of a *seat* defined as a surface that exerts a normal force on a body balance the forces. You have encountered many chairs throughout your life (temporally disparate) but they are all share a common spatially defined feature set (the size, position, and orientation of a surface). The fact that they are temporally disparate would negate any spatial coincidence if they were processed together.

Nothing about these chairs across time is temporally coincident.

An example of the latter is sound. The phonemes of speech are temporally coincident but have no inherent spatial information. I believe that this form of information processing is the least developed evolutionarily speaking.

That leads to the question of whether or not temporal and spatial coincidence are ever related. Take reading the words on this page right now. Is the process of reading purely a spatial phenomenon? Subvocalization and speed reading are a phenomenon, but is that just a consequence of internal connections spontaneously generating the alternative representation? If so, what is the purpose of those cross connections and what is their nature?

## 01 Dec 2020

It is a question of time and space.

Take writing, for example. With just 26 characters in the English language, every conscious thought of humans can be represented given sufficient time. A single complex thought can be represented by a sequence chosen from a  small set of features (the English character set). It's a serialization problem. One that solves a bottleneck of information transfer, and is thus probably not applicable to computers.

However, the allowable time interval over which to link a single concept varies. Even among different regions in the same brain.

This conversion happens with complex visual phenomenon. Saccadic eye movements turn large visual scenes into a rapid serial segments of visually discontinuous snapshots. As long as the saccades occur within a short time frame and they are standardized, the conversion is equitable.

This is akin to *windowing* or *segmentation* in convolutional neural networks except that the window placement and shape are plastic instead of a rigid or total system.

There are two methods to "decoding" this serialized data: reconstruction or sequence memory. The first basically recombines the segments into their correct location and then processes the chunk altogether. The second is to process the segments individually. Although I suspect the two processes occur in tandem.

Because of how combinatorics works, sequential memory has a much higher capacity than parallel memory. Furthermore, the length of your sequence is proportional to the capacity.

Of course, at some point you have to collapse the sequence back down to concretize an output. So it makes sense that humans have a massive set of similarly structured computational units that are capable of either sequential information processing when the information is insufficiently processed or output when it is. Basically a giant set of repeating units sandwiched between input and output layers. The switch between the processing state and output state being determined by internal coherence (expectation).

## 02 Oct 2020
Let me be clear: given sufficient time and training, any Turing complete algorithm could generate perfect intelligence. The time and training necessary could be countably infinite, but countable nonetheless.

The goal of AI research is to find the algorithm with enough predetermined features to reduce the time and training to a minimum. Of course, this results in a a wide spectrum of algorithms, each tailored to a specific maximization of features.

In this way, general artificial intelligence is fighting directly against usability. The age old, "Jack of all trades. Master of none." dilemma.

Signal transduction between neurons has two independent sets of gain: pre and post. This division is important for determining false positive and false negatives, which have different effects on learning.

In a sufficiently large brain, coherence learning becomes problematic. What is the time-space correlation between feedback and learning? A brain with indefinite persistence will have infinite coherence.

Perhaps more concretely, how much time is allotted for a brain to explain a new phenomenon?

One method to limit the scope of coherence learning is to have each signal come with a certain decay rate. Essentially, the time allotted is determined by the initial magnitude of the signal. This system requires a continuous feed of signals and perhaps is a necessary feature of consciousness for that reason.

Another method is to artificially prop up a signal until more important signals are detected. The *more important* signal can be determined by signal magnitude or by signal mismatch.

There is probably some window of coherence learning: not too novel but just novel enough to not be discarded as a false positive.

### Locality
Locality of neurons serves to limit the possible combinations of connections to a minimum. After all, infinite connections means infinite possibilities (including ones that can't exist).

The fundamental laws of logic provide some clues as to why neurons have inhibitory connections concentrated in their immediate surroundings and their input excitatory connections have some physically grouped distal area.

Take the composition of words with letters for example. A word is always composed of letters. One word is mutually exclusive from another word (the physical signifier is mutually exclusive not necessarily the meaning, which is a higher function).

In this example, the exitatory input connections all come from a single conceptual (also physical) area which is *letters*. Each word also inhibits all other competing words because *P is not non-P*.

In less logically rigorous areas of the brain, the connections may not be so organized. This is erroneous thinking and the making of the appropriate categorical connections is the subject of much ontological work.

Alternatively, a group of neurons might not directly inhibit one another, but the feedforward signal from lower layers might be the inhibitor. Such is the on-center, off-surround system from ART.

The first suggested implementation of mutual exclusivity requires some level of activity at the neuron level; Activity which also indicates signal presence. ART-type exclusivity is also easier to implement in a computer system, since it doesn't require asynchronous programming.

The different implementations of mutual exclusivity can be summed up like this:

In ART:  
*the presence of A indicates AB and not XB*

Otherwise:  
*the presence of AB indicates not XB*

There are other possibilities, however. The input layer to a single region may essentially be a copy of the inputs or may very well be the only instantiation of those inputs.

### Consciousness
When a brain becomes temporally large enough that the total time for a signal to process through the layers is longer than the individual learning window time and that sufficient feedback exists, consciousness is born.

By that, I mean, when a signal can persist in the brain indefinitely, consciousness is born. The requirement for persistence is achieved by feedback loops and storage times in some areas of the brain exceeding the computational times in others.

SWIM has experienced what it is like to lose persistence memory. Certain drugs induce a state where crosstalk between neurons is so cacophonous as to virtually eliminate any possiblity of persistence. I.e. when everyone is talking at once, it is impossible to hear one person.

In this state, counting is practically impossible. A single distraction causes a complete loss of information. The reset is so complete that you don't even remember that you were counting, let alone what number you are on.

This is what it is like to live as a dog: flitting from moment to moment with no memory of what happened ten minutes ago except from the physical changes of the perception-action engine that is the brain.

Speech is a perfect representation of this concept.

Persistence memory is a necessary but not sufficient cause of language and consciousness.

## 01 Oct 2020

## Learning Rate
The change in gain between two computational units. E.g. the synaptic connection strength between pre and post neurons.

The learning rate should be proportional to how correct (epistemic truth) a new piece of information is. Since we cannot know, especially in advance, how correct a piece of information is, intelligences have to use some substitute for correctness.

In the brain, the learning rate is proportional to coherence. That coherence varies from the simple neuronal level or complex from the whole-brain level. As stated before, this leads to many logical errors but is a good compromise of information acquisition rate and usability.

The brain also has a sort of variable learning rate that is a sliding function of previous coherence rates. This is what drives adaptive resonance in ART and the optional sliding boosting scale in HTM.

In traditional AI algorithms, the learning rate is predetermined by the user/programmer. It is calculated based on feedback predictive power (supervised learning and multiple tests) or in-advance by guessing the coherence of a dataset.

In a sense, a dataset has multiple truth values. More specifically, if we are attempting to derive some predictive power from a data set, some data will be more or less predictive. A constant learning rate is a balancing act between predictive power and can be thought of as the average truthiness of the data as it pertains to a given use case.

Since the truthiness is variable, so is the error rate when exposed to new information. A lot of time has been devoted, in vain IMO, to determining the optimal learning rate for a given problem.

I'm going to call the variable learning rate as a function of how well a new datum conforms to the existing knowledge base *coherence learning rate*.

As stated before, coherent learning is self-reinforcing--subject to all the good and bad that entails.

Along with this, we must also distinguish the changes in learning rate as a function of activation and the changes in learning rate as a function of correctness.

Pure, non-coherent learning would be changing the gain by one unit if both pre and post neurons are active. Coherent learning starts when the learning rate is adjusted to the magnitude of the activation or the coincidence of signals.

Again, a lot of research has attempted to find the optimal balance of coherence and learning rate.

`coherenceLearningRate`: A lambda function (including a constant function).

## Prediction
Both HTM and ART have distinguished prediction as separate from other states.

Prediction is a form of sub-learning-threshold information processing. It lies in the gray area between confirmed-false and confirmed-true. This is again a form of coherence learning.


## 28 Sep 2020
The fact that pre neuronal activation is necessary for learning gives rise to an imbalance in the learning rate and ultimately results in confirmation bias and similar high-level phenomenon. Although those are more of an extension of this idea at a larger scale by adaptive resonance.

It also means that once a connection is formed, and by extension knowledge is gained, it is more difficult to lose, which I consider to be somewhat beneficial. The benefit, I suppose, is in the balance between false positive and false negatives, accuracy and specificity.

Adaptive Resonance is a high level implementation of low-level boosted learning such that all of the neurons that contribute to a single concept are simultaneously induced to learn. It is reinforcement after confirmation on a grand scale. It also sets the activation necessary for learning requirement higher than simple cell-to-cell reinforcement learning forming two separate levels of cognition. One that favors learning and one that favors usage. The two levels are intimately linked such that learning follows usage *iff* confirmed.

This allows for phenomenon such as *the mind's eye*, hypothesis testing, planning, and imagination in general to proceed without massively (and therefore permanently) changing the physical structure of the brain.

Adaptive resonance is necessary for an intelligence system where the lowest level processing proceeds as a faster pace than the higher levels.

Take the recognition and learning of a 3D object (say a coffee mug) by examining all the viewing angles over several seconds. At the highest level of processing it is beneficial to think of this object as a single entity: A mug. That means the brain is tasked with being able to recognize all the various viewing angles, properties, and varied instantiations of mugs as a single concept.

At the lowest levels of processing a myriad of colors are impressed upon the retina. These images are rapidly changing on the order of tens of milliseconds as your eye saccades about the object and it rotates in your hands. Low level neuronal learning has a temporal learning bin of a few hundred milliseconds; i.e. neurons can only assimilate new knowledge that is within a few hundred milliseconds of their own firing.

This presents a problem for low level learning. When a new view of the mug is presented, our brain no longer has the internal "mug" concept activated. So how does a connection form spanning many seconds when neurons are limited to perhaps 500 ms intervals?

There are several solutions:  
You could suggest that there is some temporary storage mechanism set apart from the rest of processing that holds important concepts. Like RAM on a computer, this internal loop has feedback mechanisms such that a particular pattern, once instantiated, does not degrade quickly. In the human brain, this is "short term memory".

The existence of general purpose programmable neurons is represented very well in the cerebellum.

This would be greatly benefited by a somewhat rigid structure to the data being stored since the input and output of such a system is also quite rigid. I suspect the rigidity is on a spectrum, with greater coherence leading to better retention. This structure I am speaking of is language.

A prediction in line with this hypothesis: The vocabulary of a person should correlate with their short term word memory retention time.

An alternate solution might be that each level of the processing hierarchy has a variable temporal binning. A neuron's output duty cycle is correlated with the input duty cycle and is necessarily slightly lower giving longer and longer on-times further up the hierarchy.

The lowest levels of processing that respond to changes over many tens of milliseconds also have outputs that last tens of milliseconds. Similarly, the highest levels of processing have inputs that last several minutes and, therefore, have outputs with similar durations.

Unfortunately, this system leads to problems. Most importantly, mistakes in processing can negatively affect the organism for many minutes or hours and result in erroneous learning.

There are, of course, practical limitations to this method. A neuron is not physically capable of producing hour-long spike trains nor is it efficient to do so. So the organism must have some other method to cause change over large time scales.

In complex animals, this system is instantiated by long lasting compounds called hormones. A single short-term event (say the sighting and belief that a tiger is chasing you) leads to many minutes or even hours of bodily changes. And once the hormone is released, there is no taking it back within the same time scale as is required for its release.

Many emotional responses can be thought of as "long term memory". Without them, a prey animal might only run away from a predator for only as long as the predator isn't directly visible.

For example, hunger is a response to a specific stimuli (low concentrations of particular nutrients in the blood) that leads to potentially many hours of a particular pattern of activity.

And, in fact, if you take the definition of memory to mean any information system which collects and interprets data over some definite time scale, there are many forms of memory that span all the way to eons (if you include evolution as a form of genetically encoded memory).

Another problem with this type of system is the imbalance between the learning and activation time. In most cases, the time required to use an object does not match the time required to learn about an object. Two systems that maximize learning and separately maximize usability would be better.

## 27 Sep 2020

How does a neuron know when to fire and when to learn based purely on local phenomenon? Or, at least, how *could* a neuron know those things?

The information that a neuron has access to is as follows: the activity of inputs (post-synaptic receptor activity), self activity (action potentials), output activity (via reuptake feedback mechanisms). They also have temporal coincidence measures by instituting an activity decay rate.

### Pre-Post Learning
**A neuron's usefulness is a coherent phenomenon.**

If the postsynaptic neuron's activity matches that of the presynaptic neuron, then the strength of the connection increases.

```
if self.active:
  if post_connection.active:
    increase pre_connection
  else:
    decrease pre_connection
```

Note that it doesn't matter which activation (pre or post) came first.

If a post synaptic neuron fires without any activation of the pre synaptic neuron, then the post neuron decreases the connection strength. So this leads to two different connection strengths: one to handle false positives and one to handle false negatives.

Similarly, a post connection activation opens up the possibility for accepting new connections that occurred before or during activation.

The temporal overlap between pre and post neurons determines the magnitude of the learning change.

A post synaptic neuron might also have some base firing rate which adjusts to match its surroundings to some extent. This would cause temporal and physical semantic grouping and leads to a preference for disjoint classifications (i.e. strict partitions). [@andreae_role_2014] [@regehr_activity-dependent_2009] [@edwards_neurotransmitter_2007]

### HTM Key Concepts

[HTM School | YouTube](https://www.youtube.com/watch?v=R5UoFNtv5AU&list=PL3yXMgtrZmDqhsFQzwUC9V8MeeVOQ7eZ9)

- sparsity
- overlap
- inhibition radius
- learning
- boosting
- active duty cycle

In HTM *sparsity* and *active duty cycle* maintains a fixed activity rate. This is a specified implementation of the energy limitations in human neurons. Or perhaps more precisely, it sets the ratio of information content to information capacity.

HTM *sparsity*, *inhibition*, *overlap*, *potential pool*, and *neighbors* are meant to imitate the physicality of human neurons. If each neuron has a physical location and those neurons inhibit the action of their closest neighbors either directly or indirectly, then competitive inhibition, signal overlap (i.e. semantic grouping), and sparsity will emerge.

HTM accomplishes this by initializing the column with spatially (neighbors) derived coefficients (i.e. neurons start with a radially diminishing connection strength with a bit of randomness added).

This is akin to the initial growth stage of the human brain: neuronal connections are at least somewhat random and then go through a process of pruning which eliminates unused (and therefore distant) connections.

I suspect that temporal pooling also works in this way but instead of physical locality determining inhibition, temporal coincidence also inhibits firing within a certain physical and temporal coincidence range.

One of the problems with HTM is that temporal coincidence windows are predetermined. In order to gather semantic meaning from temporal data, you need to discretize the data and set a specific time frame during intialization: i.e., temporal data is [binned](https://en.wikipedia.org/wiki/Data_binning). Depending on the bins, temporal data may lose all semantic meaning or have too much noise.

A true temporal learning algo requires that the binning windows be mutable. In a real neuron, the base activity rate (and by extension, the input activity rate) and signal decay rate changes and therefore the temporal binning also changes.

## 01 Dev 2018
I have noticed a lot of commonalities between ART and HTM theories. In ART, the problem of input complexity is solved by concatenating the input with its logical *not*. In HTM, the input is converted to a Sparse Distributed Representation. Both allow the AI to accept far more input than a one-hot system. Similarly, boosting in HTM accomplishes the same task as the set-reset mechanism in ART. Namely, a learning speed that varies with the comprehension of the AI in response to a particular input. One idea that is not currently (well) represented in HTM but is present in ART is visual grouping. In some sense, the spatial pooler accomplishes this task but at a network level. Unlike ART which does it at a cellular level... Something to include in future version of HTM perhaps.

## 12 Nov 2018

### Principles
- fast, local inhibition
    - fast -> predicted cells are more likely to fire than non-predicted cells
    - prediction becomes a self-reinforcing behavior; centering a neuron on a set of temporally coincident inputs
    - local -> spatial coincidence and local inhibition results in differentiation of similar inputs
    - spatial coincidence is a practical way to group similar neurons; grouping neurons by inputs (from a programming standpoint) is more difficult
      - Maybe using some sort of bitmask to identify groupings? But that wouldn't work with hashed values like in SDR theory
      - In HTM, the spatial coincidence is set up during initialization and cannot be changed at runtime; something I wish to avoid
- feedforward input
    - the set of neurons must completely encompass the input set (field) to be capable of understanding the input
- prediction
    - the ability to bridge temporally or spatially disparate signals
    - should a basal connection transition to a proximal connection with sufficient input presentation?
- expectation
    - top-down signal similar to basal connections in that it predisposes a neuron to fire
    - the difference is that proximal and basal inputs only cover a narrow, continuous field whereas apical connection cover a wider breadth
      - the dark pattern that constitutes the pupils of a person's face can be learned by basal and proximal dendrites; the complex patters that encompass the entire face can be learned only through apical expectation
    - can be used as temporary storage of information

### Sparse Distributed Representations
An ANN according to [@hawkins_why_2016] requires three types of inputs: proximal, basal, and apical. Proximal connections drive the action potential at the soma robustly. This constitutes the classic receptive field of the neuron and the basis for almost all ANN's to date. Basal connections cannot directly stimulate and action potential, rather they provide contextual prediction that predisposes an action potential to fire sooner. HTM theory does not deal with apical connects except to say they are somehow involved in feedback or top-down expectations. This whole system is reminiscent of the how the visual system is portrayed in the work of Grossberg. Probably because they are studying the same systems...

Using the HTM/NuPIC system [@taylor_numenta_2018] is a real pain: So many settings and hyperparameters. For instance, one of the key parameters you have to figure out is how many sequences your HTM system should be capable of knowing. If I knew that, I wouldn't need an ANN...

Apical dendrites provide top-down context: linking successively broader regions of inputs into a single concept. This is an ideal system for backpropagation, but with the added benefit of competetive inhibition.

The main problem that I have with this theory is not in its accuracy. I think it is very accurate, and that's my problem. Sequence learning and HTM theory exactly capture what is known in psychology as superstition. Cause and effect can only be linked by a *sequence* of learned behaviors. Even if the cause is seconds or minutes beforehand, every temporal step propagating back from the reinforcement must be occupied by a behavior. This may be one of the differences in human cognition: we can ascertain causes (somehow) without establishing a perfect chain of events leading from cause to effect. E.g. Humans can deduce that a knock on the door at 6pm is the result of our calling Pizza Hut 30 minutes prior. We don't need to establish a ritualistic sequence of events that results in that knock. We have made a connection between disparate events by some feature of human cognition that is not (pronounced?) in lower animals.

This same feature of cognition can be seen in the work surrounding Neam Chimpsky (Nim). Human language can often separate a key concept and its disambiguation by many words, sentences, or even entire pages of text. Whereas Nim could only string together a few words (signs) to signify a single thought. This *suspension of clarification* is a key concept that requires more thought/research.

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
