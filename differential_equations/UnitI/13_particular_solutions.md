---
layout: post
title: Finding Particular Solutions to Nonhomogeneous ODEs
date: 2019-6-10
---




## Undetermined Coefficients

Undetermined coefficients is also a "trial solution" like the $y=e^{rt}$ in solving $y_c$. Some examples before we head to the theories. 

### Examples

- Find a particular solution of $$y''+3y'+4y=3x+2$$

  Here the input $f(x)=3x+2$, therefore we will try $y_p=Ax+B$ same form as the input, then:

  $$
  y_p'=A;\ y''_p=0
  $$

  Substitute the trial solutions into original equation:

  $$
  0+3A+4Ax+4B=3x+2\\
  (4A)x+(3A+4B)=3x+2
  $$

  Then we have $A=3/4$, $B=-1/16$, then the particular solution is 

  $$
  y_p=\frac{3}{4}x-\frac{1}{16}
  $$

- Find a particular solution of $$y'^{\prime}-4y=2e^{3x}$$

  Input $f(x)=2e^{3x}$ then our trial solution is

  $$
  y_p=Ae^{3x};\ y'_p=3Ae^{3x};\ y''_p=9Ae^{3x}
  $$

  These give:

  $$
  9Ae^{3x}-4Ae^{3x}=2e^{3x}
  $$

  Clearly $A=\displaystyle \frac{2}{5}$ and 

  $$
  y_p=\frac{2}{5}e^{3x}
  $$

- Find the particular solutions of $$3y''+y'-2y=2\cos x$$

  For cos and sin, we try the whole trial solution 

  $$
  \begin{align}
  y_p&=A\cos x+B\sin x\\
  y'_p&=-A\sin x+B\cos x\\
  y''_p&=-A\cos x-B\sin x
  \end{align}
  $$

  because they appear in each other's derivative, then 

  $$
  \begin{align}
  y_p&=-\frac{5}{13}\cos x+\frac{1}{13}\sin x
  \end{align}
  $$


The above examples are designed to work. But it's not always that lucky. If we just follow the form of $f(x)$, it may happen that the trial solution ends up in the $y_c$ that makes the equation go to zero, regardless of value of $x$. In that case we will never make $0=f(x)$. Thus we have some rules to handle these situations. 

### General Approach

In principle, the method of undetermined coefficients applies whenever the input $f(x)$ is a linear combination of the products of the following three types:

1. A polynomial in $x$
2. An exponential function $e^{rx}$
3. $\cos kx$ or $\sin kx$ 

Such function is, for example:

$$
f(x)=(3-4x^2)e^{5x}-4x^3\cos 10x
$$

In practice, we first find the $y_c$ that satisfy the homogeneous solution $Ly_c=0$, and we check if $f(x)$ is in $y_c$ or any derivatives of $f(x)$ is in $y_c$, If there's no terms in $y_c$, then we can take $f(x)$ and formulae our trial solutions. 

If we found there exists a duplicate, we need to multiply the trial solution by a $x^s$ to make duplicates term disappear. $s$ should be the order of polynomial in $y_c$ plus 1. 











## Exponential Input theorem 

$$p(D)e^{\alpha x}=p(\alpha)e^{\alpha x}$$
$$
y_p=\frac{e^{\alpha x}}{p(\alpha)}
$$

## Exponential Shift Rule

Assuming $$p(\alpha)\neq 0$$. What if $$p(\alpha)=0$$ ? We have exponential shift rule:
$$
p(D)e^{\alpha x}
$$


