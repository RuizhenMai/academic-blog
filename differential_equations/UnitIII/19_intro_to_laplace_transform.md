---
layout: post
title: Introduction to Laplace Transform
---

Laplace transform, intuitively, is feeding in a function of $f(t)$ and spits out another function $F(s)$. Though it seems magic, the $s$ in fact comes from the *parameter* of the transform. Let's step back a bit and have a sequence $a(n)$, and 

$$
\sum_{n=0}^\infty a(n)x^n=A(x)
$$

This seems similar to with $0<x<1$ a geometric series. If that's so, $a(n)=1$ gives $A(x)=\displaystyle \frac{1}{1-x}$. $a(n)=\displaystyle \frac{1}{n!}$ leads to $e^x$ (regardless of domain of $x$). Rewrite $x^n=e^{n\ln x}$, name $n$ as $t$, $-s=\ln x$ just to look better ($s>0$), and switch to continuous case:

$$
\mathcal L(f(t))=\int_0^\infty f(t)e^{-st}\:dt
$$

This is the Laplace transform, taking an input $f(t)$ and output $F(s)$ since we integrate over all $t$. In fact, from a probabilistic perspective, it's like taking an expectation over one thing and left the parameter. And it should be written as $\mathcal L(·;s)$.  Another notation is $f(t)\rightsquigarrow F(s)$. 

Linearity of Laplace transform:

- $\mathcal L(f+g)=\mathcal L(f)+\mathcal L(g)$
- $\mathcal L(cf)=c\mathcal L(f)$

These come easily from the linearity of integration. 

Let's do some exercise: 

- what's $1\rightsquigarrow?$ 
  
  $$
  \int_0^\infty e^{-st}dt=\left[\frac{e^{-st}}{-s}\right]_0^\infty=\frac{1}{s},\quad s>0
  $$

  (It's meaningless when $s<0$)

- What's $e^{at}\rightsquigarrow?$
  
  $$
  \int_0^\infty e^{-(s-a)t}\:dt=\left[\frac{e^{-(s-a)t}}{-(s-a)}\right]_0^\infty=\frac{1}{s-a},\quad s>a
  $$

- What's $e^{at}f(t)\rightsquigarrow?$
  
  $$
  \int_0^\infty f(t)e^{-(s-t)t}\:dt=F(s-a)
  $$

  This is called the <u>Exponential shift formula</u>. 

- What's $\cos at\rightsquigarrow?$ Note that the exponential shift rule also works for complex number $e^{(a+bi)t}$. And let's remind ourselves the Euler inverse formula: $\displaystyle \cos at=\frac{e^{iat}+e^{-iat}}{2}$, 
  
  $$
  \mathcal L(\cos at)=\frac{1}{2}[\mathcal L(e^{iat})+\mathcal L(e^{-iat})]=\frac{1}{2}[\frac{1}{s-ia}+\frac{1}{s+ia}]=\frac{s}{s^2+a^2}
  $$

  <u>Note that as long as if we change the sigh of</u> $i$ <u>in a complex expression, and the expression does not change, then it's a real number.</u> 

- Similarly, we can write $\sin at=\displaystyle \frac{e^{iat}-e^{-iat}}{2i}$, then

  $$
  \mathcal L(\sin at)=\frac{a}{s^2+a^2}
  $$
  
- What's $t^n\rightsquigarrow?$ (integration by parts and $v'=e^{-st}$)
  
  $$
  \mathcal L(t^n)=\int_0^\infty t^n e^{-st}\:dt=\left[t^n\frac{e^{-st}}{-s}\right]^\infty_0-\int_0^\infty nt^{n-1}\frac{e^{-st}}{-s} dt
  $$
  

let's take a look on the $uv$ part:

$$
  [\lim_{t\rightarrow\infty}-\frac{1}{s}\frac{t^n}{e^{st}}]+0*\frac{1}{s},\quad s>0
$$

Now the the right term is just zero. The left term will go to zero because when we do $n$ times Lopital, the above will be 1 but the bottom remains. Therefore, 

$$
  -\int_0^\infty nt^{n-1}\frac{e^{-st}}{-s} dt=\frac{n}{s}\int_0^\infty t^{n-1}e^{-st}\:dt=\frac{n}{s}\mathcal L(t^{n-1})
$$

We see that $\mathcal L(t^n)=\displaystyle\frac{n}{s}\mathcal L(t^{n-1})$, and therefore we can expect 

$$
  \mathcal L(t^n)=\displaystyle\frac{n!}{s^n}\mathcal L(t^{0})=\frac{n!}{s^{n+1}}
$$


