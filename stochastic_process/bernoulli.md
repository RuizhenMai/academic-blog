---
layout: post
title: Bernoulli Process
---

<u>A Bernoulli process is a sequence of independent Bernoulli trials</u> $$X_1, X_2…$$, which is nothing but coin flips. 

For <u>an independent trial</u> $$X_i$$, we know, at each trial:

- P(success) = $$P(X_i=1)=p$$ 
- P(failure) = $$P(X_i=0)=1-p$$

The success rate $$p$$ does not vary with time. It will remain constant throughout the trials. <u>This property is essential throughout the discussion of the process</u>. Often time we use the term <u>arrival</u> as success. We also know:

- $$\mathbb E[X_i]=p\cdot 1+(1-p)\cdot 0=p$$<u></u>
- $$\mathbb V[X_i]=p(1-p)$$<u></u>

In general, we are more interested in <u>a collection of trials</u>. That's what makes it a *process*. Important questions of a process are:

- Within $$n$$ time slots (we have discrete time for Bernoulli Process), what's the # of expected arrivals $$\mathbb E[N_n]$$?
- Expected # of trials (time) to have the first arrival $$\mathbb E[Y_1]$$ 
- Expected # of trials (time) to have the kth arrival $$\mathbb E[Y_k]$$  



(All success quesiton)

## Number of Expected arrivals within n time slots

This is a very familiar random variable. The random variable $$N_n$$ is in fact a sum of all trials $$X_1,..X_n$$ within the time slots, and thus is a binomial variable. So within $$n$$ time slots, (note always $$n>k$$)

- $$P(N_n=k)=\begin{pmatrix}
   n\\
   k\\
  \end{pmatrix}p^k(1-p)^k$$ <u></u>
- $$\mathbb E[N_n]=\mathbb E[X_1+…+X_n]=np$$ <u></u>
- $$\mathbb V(N_n)=np(1-p)$$ <u></u>



## Expected number of trials to reach the first arrival (interarrival)

Similar to above, to find the expectation, we'd probably need to know the probability first. Since if we do not get the success, we keep trying, it follows that the random variable $$Y_1$$ is just geometric with parameter $$p$$ (as determined by the independent trial). 

- $$P(Y_1=t)=(1-p)^{t-1}p$$ <u></u>
- $$\displaystyle \mathbb E[Y_1]=\frac{1}{p}$$ (Proof tips: because of derivative of infinite sum of geometric sequence)
- $$\displaystyle\mathbb V(Y_1)=\frac{1-p}{p^2}$$. <u></u>

The picture of geometric pmf:

 <figure><img style="align-content: center; margin-left: auto; margin-right: auto; display: block;" src="../assets/graph23.png">
  <figcaption style="text-align: center; font-family: MJXc-TeX-math-I,MJXc-TeX-math-Ix,MJXc-TeX-math-Iw; font-size: 1.1rem;">Figure 1. Geometric pmf </figcaption>
</figure>

This is also the <u>interarrival</u> time as an immediate consequence of independence between trial. Each time we have one success is not going to affect how the next success arrives. This is called the <u>memoryless</u> property. So the interarrival time will not change and same as the first arrival time. 

 <figure><img style="align-content: center; margin-left: auto; margin-right: auto; display: block;" src="../assets/graph22.png">
  <figcaption style="text-align: center; font-family: MJXc-TeX-math-I,MJXc-TeX-math-Ix,MJXc-TeX-math-Iw; font-size: 1.1rem;">Figure 2. Interarrival </figcaption>
</figure>

## Expected number of trials to reach the kth arrival

The probability of having k arrivals at the $$t$$th trial is $$P(Y_k=t)$$. This is equivalent to saying having $$k-1$$ arrivals with $$t-1$$ trials and then have another arrival at the $$t$$th trial. (This is a nice trick to get the probability otherwise we will need to do convolution)

- $$P(Y_k=t)=\begin{pmatrix}
   t-1\\
   k-1\\
  \end{pmatrix}p^{k-1}(1-p)^{t-k}p$$ <u></u>

From another perspective, note that $$Y_1$$ is the interarrival times. This means that the time took have kth arrival is equal the k * the time needed for the interarrival time. 

- $$\mathbb E[Y_k]=k\mathbb E[Y_1]=\displaystyle \frac{k}{p}$$ <u></u>
- $$\mathbb V(Y_k)=\displaystyle k\frac{1-p}{p^2} $$ <u></u>

Similar trick can be applied to variance because each of the random variables are independent. 

## Merging and Splitting of Bernoulli Process

This will be updated in the future. 