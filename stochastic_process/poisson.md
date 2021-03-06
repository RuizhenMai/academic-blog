---
layout: post
title: Poisson Process
---

Similar to Bernoulli process, <u>a poisson process is a sequence of independent Poisson trials</u> $X_1,X_2…$,<u>all of which are Poisson random variables.</u> Poisson variable is from a binomial random variable $Bin(n,p)$ s.t. $n\rightarrow \infty,p\rightarrow0$. It's like stretching in both ends. 

Therefore, for <u>an independent trial</u> $X_i$, at each trial, let $\lambda=np$,:

- $P(X_i=k;\lambda)=\lim_{n\rightarrow\infty}\begin{pmatrix}n\\\ k\end{pmatrix}\displaystyle \left(\frac{\lambda}{n}\right)^k\left(1-\frac{\lambda}{n}\right)^{n-k}=e^{-\lambda}\frac{\lambda^k}{k!}$ 

- $\mathbb E[X_i]=\lambda$ 
- $\mathbb V(X_i)=\lambda$ 

where $\lambda$ <u>is the arrival rate, measuring how frequent, in a very short period of time, how many arrivals should there be</u>. Given these, let's try to answer the same important questions for Bernoulli trials last time. 

 <figure><img style="align-content: center; margin-left: auto; margin-right: auto; display: block;" src="../assets/graph24.png">
  <figcaption style="text-align: center; font-family: MJXc-TeX-math-I,MJXc-TeX-math-Ix,MJXc-TeX-math-Iw; font-size: 1.1rem;">Figure 1. Poisson pmf </figcaption>
</figure>

## Number of Expected arrivals within time n

Since it's Poisson process also consists of independent trials, the memoryless property comes in. Also I don't quite remember how the pmf is same as independent trial. 

- $P(N_n=k)=\displaystyle e^{-\lambda}\frac{\lambda^k}{k!}$ 

- $\mathbb E[N_n]=\lambda n$ 
- $\mathbb V(N_n)=\lambda n$ 



## Expected number of trials to reach the first arrival (interarrival)

Exponential (special case of erlang). <u>Note that these distribution are all governed by the independent Poisson trial's arrival rate parameter</u> $\lambda$. 

- $P(Y_1=y)=\lambda e^{-\lambda y}$ 
- $\mathbb E[Y_1]=\displaystyle\frac{1}{\lambda}$ 
- $\mathbb V(Y_1)=\displaystyle \frac{1}{\lambda^2}$ 



 <figure><img style="align-content: center; margin-left: auto; margin-right: auto; display: block;" src="../assets/graph25.png">
  <figcaption style="text-align: center; font-family: MJXc-TeX-math-I,MJXc-TeX-math-Ix,MJXc-TeX-math-Iw; font-size: 1.1rem;">Figure 2. Exponential pdf </figcaption>
</figure>

One takeaway from the expected inter-arrival time $E[Y_1]=\frac{1}{\lambda}$ is if it's given by a question, then we can tell the arrival rate parameter $\lambda$, i.e., the expected number of arrivals by that. For instance, if a question tell you a bus's expected arrival time is 10 mins, then from that we know $\lambda=0.1bus/mins$. 

## Expected number of trials to reach the kth arrival

Erlang, which is also a special case of Gamma distribution 

- $P(Y_k=y;k)=\displaystyle \frac{\lambda^ky^{k-1}e^{-\lambda y}}{(k-1)!}$ 





We have continuous time:

 <figure><img style="align-content: center; margin-left: auto; margin-right: auto; display: block;" src="../assets/graph21.png">
  <figcaption style="text-align: center; font-family: MJXc-TeX-math-I,MJXc-TeX-math-Ix,MJXc-TeX-math-Iw; font-size: 1.1rem;">Figure 1. Continuous Time </figcaption>
</figure>

## Merging of Poisson

Others are left out. One important thing to remember is that merging two poisson process with $\lambda_1$ and $\lambda_2$, the merged process has rate of arrival $\lambda_1+\lambda_2$; and for *every* arrival (including the *first*), the probability the arrival is from the first poisson process is $\lambda_1/(\lambda_1+\lambda_2)$. 

Say there're two exponential random variables $Y$, $Z$ with $\lambda_1$ and $\lambda_2$ as the parameter. We're interested in $P(Y<Z)$. We can view $Y,Z$ as the first arrival time of two poisson process. Let's merge this two independent process. To have $Y<Z$, we must have the first arrival of the merged process comes from $Y$, thus $P(Y<Z)=\lambda_1/(\lambda_1+\lambda_2)$. 

