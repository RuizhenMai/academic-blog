---
layout: post
title: Finding Particular Solutions via Fourier Series
date: 2019-6-19
---

A typical periodic input is sound. Sound can consist of different tones, each tone corresponds to a sine or cosine function, and they sum up become a single periodic function. This input can be decomposed by Fourier series.  

## Techniques of Moving Fourier Series

Recall the square wave function, but let it have half-period 1 and goes between 0 and 1 instead of $-1/2$ and $1/2$. 

 <figure><img style="align-content: center; margin-left: auto; margin-right: auto; display: block; size:50%" src="../../assets/graph28.png">
  <figcaption style="text-align: center; font-family: MJXc-TeX-math-I,MJXc-TeX-math-Ix,MJXc-TeX-math-Iw; font-size: 1.1rem;">Figure 1. Shrinked Shifted Square Wave </figcaption>
</figure>

How does one from the following go to the shrink and shifted one? 

<figure><img style="align-content: center; margin-left: auto; margin-right: auto; display: block;" src="../../assets/graph19.png">
  <figcaption style="text-align: center; font-family: MJXc-TeX-math-I,MJXc-TeX-math-Ix,MJXc-TeX-math-Iw; font-size: 1.1rem;">Figure 1. A square-wave function</figcaption>
</figure>

Let the normal square-wave and its Fourier series be $g(u)$, the irregular one be $f(t)$. The relation between a $2\pi$ period input $u$ and general period input $t$ is $u=\displaystyle\frac{\pi}{L}t$. We have:
$$
\begin{align}
f(t)&=\frac{1}{2}g(u)+\frac{1}{2}\\
\end{align}
$$
The modified function is we squash the original one by half and shift it by 1/2 upper. Then:
$$
\begin{align}
f(t)&=\frac{1}{2}g(u)+\frac{1}{2}\\
&=\frac{1}{2}\frac{4}{\pi}\sum_{n\ odd}\frac{\sin nt}{n}+\frac{1}{2}\\
&=\frac{2}{\pi}\sum_{n\ odd}\frac{\sin nt}{n}+\frac{1}{2}
\end{align}
$$


## Use Fourier series to find Particular Solution

The undamped 2nd order DE with input is 
$$
x''+\omega_0 x=f(t)
$$
We've already known how to find the input as sin or cos using undetermined coefficients or complex exponential. 