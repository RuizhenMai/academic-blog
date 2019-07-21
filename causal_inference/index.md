---
layout: post
title: Causal Inference
---

<span class="newthought">These notes</span>  are taken along with the video series [Causal Infernece](https://www.youtube.com/playlist?list=PL_onPhFCkVQimvhuSAFrC8VWLEyNygQR5). The series of lectures are given by [Jason Roy](https://www.med.upenn.edu/apps/faculty/index.php/g275/p8366265), the professor of Epidemiology and Biostatistics department in Upenn. Some examples used in the videos are medical, but in general they are not hard to understand. The series is very good for introduction. Although some concepts are not explained well, they often can be easily better understood by googling. One that is not clear, as I remember, is marginal structure model. 

As usual, crossover links mean the notes there can be missing or incomplete. 

[Confounders and Unconfoundedness](./confounder)

[Causal Assumptions](./assumptions)

~~[Directed Acyclic Graphs](./directed_graph)~~

[Matching](./matching)

[Propensity Score](./propensity_score)

[Inverse Probability Weighting](./ipw)

[Instrumental Variable](./iv)



## Motivating Example

Causal Inference is about understanding the "causality" between events. By "causality", we refer to one things cause another to *happen*. In general, the *association* that we establish such as $y=kx$, does not mean $x$ causes $y$ to increase. It just means $x$ associates with $y$'s increase. 

To research on causality, modern causality research will refer to Rubin's model. For instance, we're probably interested in if medicine A is effective on curing fever. Our subject $i$ here is a person (which often is). And let $Y_i$ represents one's heat. If medicine A is effective, we would expect persons taking medicine A have a decrease of $Y_i$. Let $W_i=1$ denotes person $i$ takes medicine A, and $W_i=0$ for not take. And let $Y_i^1$ represent the temperature of person $i$ having taken the medicine, $Y^0_i$ not taken. We're interested in 
$$
\tau_i= Y_i^1-Y_i^0
$$
If the medicine is effective, we would expect <u>individual treatment effect</u> (ITE) $\tau_i$ to be negative. But in reality, at the same timestamp, it's impossible for us to know one's temperature with taking medicine A and not taking it, unless there're two persons' medical status is extremely similar (that's why twins are often involved in this kind of studies). Maybe person $i$ will recover after some period of time even he or she does not take the pill. We never know. 

Estimating the treatment effect is the central problem of causal inference. In general, ITE is not known. But we still can estimate the <u>average treatment effect</u> (ATE) as long as some assumptions are met. 

## Observational Studies

Randomized trials are experiments we design and conduct. When we're the conductors of  experiments, we can make it whatever we want. But these can be expensive, we need to plan for it, recruit volunteers, record data and etc. Observational studies generally refer to studies that have been completed by others, and data are available. Since the purpose of other people's studies are different, some variables do not need be randomized, we need to adjust our methods for these studies. This will become clear in the specific section. 









