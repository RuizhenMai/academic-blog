---
layout: post
title: Method of Moments
---

Let's start with something usual from analysis. The Weiestrass Approximation Theorem says that:

Let $f$ be a continuous functions on interval $[a,b]$, then for any $\epsilon >0$, there exists coefficients $a_0, a_1,…,a_d\in\mathbb R$ such that 

$$
\max\lvert f(x)-\sum_{k=0}^d a_kx^k\rvert<\epsilon
$$

In English, this is saying continuous functions can be well approximated by polynomials. 

The application of WAT to statistics is to give us an idea to approximate the distribution, more precisely the PDF or PMF. Assume that we have a distribution $\mathbb P_\theta$ for a bunch of samples $X_1,…,X_n$ where its optimal parameter is $\theta^*$. If we find a $\theta$ such that 

$$
\int h(x)f_\theta(x)\:dx=\int h(x)f_{\theta^*}(x)\:dx
$$

for all bounded continuous (I actually don't know why bounded continuous is enough) functions $h(·)$, then $\theta=\theta^*$. Keep in mind that our ultimate goal is to find an estimator $\hat \theta$ that can actually do this equality for all bounded continuous $h(\cdot)$. Now we don't know $\int h(x)f_{\theta^*}(x)\:dx$, given the samples we have, we can replace it with averages:

$$
\int h(x)f_{\hat\theta}(x)\:dx=\frac{1}{n}\sum_{i=1}^nh(X_i)
$$

But to evaluate this equation for all $h(\cdot)$ is unrealistic since we have infinite such functions. We need to try to reduce the number of functions that we need to check. From WAT, we know any functions can be approximated by polynomials $\sum_{k=0}^da_kx^k$, thus we apply the trick to $h(\cdot)$ on both sides of equation:

$$
\int \sum_{k=0}^da_kx^k f_{\hat\theta}(x)\:dx=\frac{1}{n}\sum_{i=1}^n\sum_{k=0}^da_kX_i^k
$$

Now the $h(\cdot)$ breaks down and it seems more doable. Even though there's still infinite $a_0,a_1,…,a_d\in\mathbb R$ to check, in fact, since both sides have the polynomials, we only need to check the degrees of the polynomial $k$, because the coefficients $a_.$ will always be the same. The final equation is 

$$
\int x^kf_{\hat\theta}(x)\:dx=\frac{1}{n}\sum_{i=1}^nX_i^k,\quad \forall k=0,..,d
$$

This is the equation we need to evaluate for, there is $d+1$ of them. The kth moment of (continuous) distribution $\mathbb P_\theta$ is 

$$
m_k=\mathbb E[X^k]=\int x^kf_\theta(x)\:dx
$$

And it's obviously approximated by the sample: $\frac{1}{n}\sum_{i=1}^nX_i^k$. But the problem is WAT doesn't tell us what $d$ (# of moments) should be. (It has other problems such as it only works on intervals $[a,b]$, if the PDF is on $\mathbb R$ then it can be annoying to approximate). 

In turns, we consider an easy case: r.v. $X$ is discrete. Then $X=\{x_1,x_2,…,x_r\}$ is finite with $r$ possible values. The PMF of $X$ has at most $r-1$ parameters, which is the probability of every number $X$ can take; this is different than PDF s.t. $X$ can take infinite many numbers:

$$
p(x_1),p(x_2),...,p(x_{r-1})
$$

Because the last one can be obtained by: $p(x_r)=1-\sum_{j=1}^{r-1}p(x_j)$. With $r-1$ parameters, the distribution of $X$ is fully specified. Actually, the number of moments $d$ we need to check is $d=r-1$. Note, 

$$
m_k=\mathbb E[X^k]=\sum_{j=1}^rp(x_j)x_j^k
$$

and

$$
\sum_{j=1}^rp(x_j)=1
$$

We can decompose these two into matrix form:

$$
\begin{bmatrix}
1 & 1 & 1 & 1\\
x_{1} & x_{2} & \dotsc  & x_{r}\\
x^{2}_{1} & x^{2}_{2} & \dotsc  & x^{2}_{r}\\
\vdots  & \vdots  & \ddots  & \vdots \\
x^{r-1}_{1} & x^{r-1}_{2} & \dotsc  & x^{r-1}_{r}
\end{bmatrix}\begin{bmatrix}
p( x_{1})\\
p( x_{2})\\
p( x_{3})\\
\vdots \\
p( x_{r})
\end{bmatrix} =\begin{bmatrix}
1\\
m_{1}\\
m_{2}\\
\vdots \\
m_{r-1}
\end{bmatrix}
$$

Then we check whether the matrix is invertible, the determinant of it is called Vandermonde determinant: 

$$
\det\begin{bmatrix}
1 & 1 & 1 & 1\\
x_{1} & x_{2} & \dotsc  & x_{r}\\
x^{2}_{1} & x^{2}_{2} & \dotsc  & x^{2}_{r}\\
\vdots  & \vdots  & \ddots  & \vdots \\
x^{r-1}_{1} & x^{r-1}_{2} & \dotsc  & x^{r-1}_{r}
\end{bmatrix}=\prod_{1\leq i\leq j\leq n}(x_j-x_i)
$$

If its determinant is not zero, meaning there's a one to one mapping for $\mathbf p(x_j)$, we can invert it: 

$$
\begin{bmatrix}
p( x_{1})\\
p( x_{2})\\
p( x_{3})\\
\vdots \\
p( x_{r})
\end{bmatrix} =\begin{bmatrix}
1 & 1 & 1 & 1\\
x_{1} & x_{2} & \dotsc  & x_{r}\\
x^{2}_{1} & x^{2}_{2} & \dotsc  & x^{2}_{r}\\
\vdots  & \vdots  & \ddots  & \vdots \\
x^{r-1}_{1} & x^{r-1}_{2} & \dotsc  & x^{r-1}_{r}
\end{bmatrix}^{-1}\begin{bmatrix}
1\\
m_{1}\\
m_{2}\\
\vdots \\
m_{r-1}
\end{bmatrix}
$$

And thus we can have all the parameters we need for the PMF. The takeaway is that moments contain important information to recover the PMF or PDF. If we can estimate the moments accurately, we may be able to recover the distribution. The rule thumb is if $\theta\subset\Theta\subset\mathbb R^d$, we need $d$ moments. In general, if there exists an invertible mapping $\psi:\theta \subset\mathbb R^d\rightarrow m\subset\mathbb R^d$ , then the moment estimator is 

$$
\hat \theta^{MM}=\psi^{-1}(\hat m_1,\hat m_2,...\hat m_d)
$$

It can be easily that, since empirical moments are consistent to the population moments, the moment estimator $\hat\theta^{MM}$ is also consistent. And it follows the central limit theorem seen by applying delta methods to $\hat M\xrightarrow{(d)} M$ where $M=(m_1,m_2,…)$. 

## Generalized Method of Moments

No need of exact likelihood, i.e., no need to specify the distribution 