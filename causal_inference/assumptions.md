---
layout: post
title: Causal Assumptions
---

## Assumptions

The followings are causal assumptions (those not explained inline will be explained below):

- Stable Unit Treatment Value Assumptions (SUTVA)
- Consistency: what you observed (under one of the treatment) is equal to the true underlying potentials $$Y_i=Y_i^{W_i}$$ 
- Ignorability
- Positivity:  $$P(W_i=w\rvert \mathbf X=\mathbf x)>0$$ for all covariates $$\mathbf x,\ w=\{0,1\}$$, because if some group is never treated, $$P=0$$, then we cannot learn the effect

Assumptions can be about observed outcome $$Y_i$$, observed treatment $$W_i$$, and covariates $$Z$$.  

### Stable Unit Treatment Value Assumptions (SUTVA) 

<u>No interference</u>: units of interest do not interfere with each other. In most settings units are people. Situations that these are violated: 

- Contagion: The sickness of one people affect the other; or Vaccine 
- Behavioral Study: when people's behaviors are interacting with others 

<u>One version of treatment</u>

SUTVA allows us to write potential outcome for the ith person in terms of only that person's treatment. This simplifies the problem. 

### Ignorability

This is (2). I will elaborate it more intuitively here. They can be ages, gender, places living in, as long as they affect both the treatment and outcomes. And this assumptions is saying: <u>Among people with the same values of </u>$$\mathbf X=\mathbf x$$, <u>we can think of treatment </u>$$W_i$$ <u>are randomly are assigned.</u>  The following example helps:

<figure><img style="align-content: center; margin-left: auto; margin-right: auto; display: block;" src="../assets/graph10.png">
  <figcaption style="text-align: center; font-family: MJXc-TeX-math-I,MJXc-TeX-math-Ix,MJXc-TeX-math-Iw; font-size: 1.1rem;">Figure 1. Exmaple of Ignorability</figcaption>
</figure>

And we need to figure it out what $$\mathbf X$$ we need to collect in order to make that assumption satisfied. 



## Standardization

Standardization is a way of dealing with confounders. We use the law of total expectation to marginalize out the covariates: 
$$
\begin{align}
\mathbb E[Y_i|W_i=w, \mathbf X=\mathbf x]&=\mathbb E[Y_i^w|W_i=w, \mathbf X=\mathbf x](by\ consistancy)\\
&=\mathbb E[Y_i^w|\mathbf X=\mathbf x](by\ ignorability)
\end{align}
$$
If we want *marginal causal effect*, we can average over all $$\mathbf X=\mathbf x$$, 
$$
\begin{align}
\mathbb E[Y_i^w]&=\mathbb E_{\mathbf x}[\mathbb E[Y_i^w|\mathbf X=\mathbf x]]\\
&=\sum_i\mathbb E[Y_i^w|\mathbf X=\mathbf x]P(\mathbf X=\mathbf x^{(i)})\\
\end{align}
$$
The crucial caveat is that our $P(\mathbf X=\mathbf x^{(i)})=\frac{I(X=x^{(i)})}{N}$ is approximated by the sample. But even when $\mathbf X$ is a scalar $X$, if it's continuous, we won't have all of its values and it's possible there's some values we don't have. This become more severe if $\mathbf X$ is vector. We won't have a good estimate for $P$. We use many techniques such as matching to deal with this problem. 