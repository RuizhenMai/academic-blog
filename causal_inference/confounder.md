---
layout: post
title: Confounders and Unconfoundedness
---

## Notations and General Definitions

Some notations for observed data:

- $$W_i$$ (or $$T_i$$, $$Z_i$$) $$=1$$ treated, $$=0$$ if untreated or control; these are observed in the observational experiments setting; these are assigned in control experiment
- $$Y_i$$: observed response
- $$\mathbf X_i$$: other covariates (that may affect the response); $\mathbf X^{(i)}$ also used, depending on the context

Some notations for things that are never observed:

- $$Y_i^{W_i=0,1}$$: individual "actual" response; in reality we only know one (this is also an assumption that will be discussed a bit later); that is, 
  $$
  \begin{align}
  Y_i=\begin{cases}
  Y_i^1\ \ \mathrm{if}\ W_i=1\\
  Y_i^0\ \ \mathrm{if}\ W_i=0\\
  \end{cases}
  \end{align}
  $$
  More concisely,
  $$
  Y_i=W_iY_i^1+(1-W_i)Y_i^0
  $$

- $$\tau_i=Y_i^1-Y_i^0$$ : individual treatment effect, same as above; 

Things that we want: (the expectations below, if not specified, are all approximated by i.i.d)

<u>Average treatment/causal effect</u>:
$$
\begin{align}
\overline\tau&=\frac{1}{n}\sum_i^n\tau_i\\
&=\mathbb E[\tau]\\
&=\mathbb E[Y_i^1-Y_i^0]\\
&=\mathbb E[Y_i^1]-\mathbb E[Y_i^0]\\
&=\mathbb E[Y^1]-\mathbb E[Y^0]
\end{align}
$$
The last line follows because the second-to-last line is the "approximation" we made by taking the sample average. It's estimating the real expectation. But in reality it can be written either way. 

Things we have:
$$
\begin{align}
\mathbb E[Y_i\rvert W_i=1]&=\mathbb E[W_iY_i^1+(1-W_i)Y_i^0\rvert W_i=1]\\
&=\mathbb E[W_iY_i^1\rvert W_i=1]\\
&=\mathbb E[Y_i^1\rvert W_i=1]\\
\end{align}
$$
Similarly, we have:
$$
\mathbb E[Y_i\rvert W_i=0]=\mathbb E[Y_i^0\rvert W_i=0]\\
$$
But they are actually different:
$$
\begin{align}
\mathbb E[Y_i\rvert W_i=1]-\mathbb E[Y_i\rvert W_i=0]=\mathbb E[Y_i^1\rvert W_i=1]-\mathbb E[Y_i^0\rvert W_i=0]&\neq\mathbb E[Y_i^1]-\mathbb E[Y_i^0]
\end{align}
$$
Intuitively speaking, they are different because conditioning on $$W_i=1$$ or the other way around is restricting to the population receives the treatment. But the population receiving the treatment are, possibly, *more likely* to have higher potentials. For example, people at higher risk for flu (outcome) are more likely to choose to get a flu shot (treatment, meant to reduce the risk for flu). Also, this is comparing two different populations of people, whereas the true ATE is on same population. 

They are equal if and only if 
$$
(Y_i^1,Y_i^0)\perp W_i\tag{1}
$$
This is saying, the potential outcomes are independent of treatment received. More plainly, we shall assign, if possible, treatment randomly, or at least independent of potential outcomes{%include sidenote.html note='This does not mean the assignment probability shall be equal in each group, for e.g., 0.2 of assigning a treatment to one of the five groups. In fact, as long as these probabilities are not affected by the potentials, then our assumption holds, even we always have 0.9 probability of giving treatment to one group/invidual '%}. For example, the Federal Government consider allocating subsidies to fix water pollution to some states. Let the state's water quality be $$Y$$. Then the state shall give these money no matter the state's current water quality (this will become $$Y^0$$remain if untreated) is good or bad, and possible water quality improvement. 

You probably think that's not possible, from the perspective of policy makers. What's more probably is there are some regions $$\mathbf X_i=X_1,… X_n$$  s.t. in a region of states with poor water quality, maybe $$z_1$$, the government gives them an (somewhat) equally high amount of subsidy. And for another region, say $$z_2$$, the government give them an equally low amount of subsidy. This is saying 
$$
(Y_i^1,Y_i^0)\perp W_i\rvert \mathbf X^{(i)}\tag{2}
$$
That is, in each group, the treatment assignment is random. These groups $$z_1,..,z_n$$ may or maybe observed. More often, these groups are called *covariate* because it affects the assignment and treatment, or *confounders*. 

The condition (2) is often called *unconfoundedness*, no unmeasured confounders, or *ignorability* condition. 



## Other Causal Effects

Causal effects other than average treatment effect are used:

- $$\displaystyle \mathbb E\left[\frac{Y^1_i}{Y^0_i}\right]$$: causal relative risk/ratio. This would be more probable if $$Y_i$$ is a binary outcome
- $$\mathbb E[Y_i^1-Y^0_i\rvert W_i=1]$$: causal effect on the treated. We might be interested in this when we only care about the effect among the treated. 



## Confounder

Confounders are defined as variables that affect treatment and *at the same time* directly affect the outcome. Below are examples not the confounder:

- We assign treatment based on coin flip(biased or not), but the result of coin flip does not affect treatment
- People with a family history cancer are more likely to develop cancer(the outcome), but (as long as) family history is not affecting the treatment decision, then family history is not a confounder

In turns let's have a confounder example:

- If older people are at higher risk of cardiovascular(the outcome) and are more likely to receive statins(the treatment), then *age* is a confounder

Note that a set of confounders should *not* include any descendants of treatment. That is, it shall not block the front door path. A set of variables X is sufficient to control for confounding if:

- It blocks all backdoor paths from treatment to the outcome
- It does not block the front door paths 

Also this set of variables is not necessarily unique. For example: 

<figure><img style="align-content: center; margin-left: auto; margin-right: auto; display: block;" src="../assets/graph11.png">
  <figcaption style="text-align: center; font-family: MJXc-TeX-math-I,MJXc-TeX-math-Ix,MJXc-TeX-math-Iw; font-size: 1.1rem;">Figure 2. Exmaple of backdoor path</figcaption>
</figure>



