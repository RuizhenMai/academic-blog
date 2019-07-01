---
layout: post
title: Laplace of derivative 
date: 2019-6-22
---

## Conditions of Existence

The Laplace transform doesn't always exist. Examine the form $\mathcal L(f(t))=\int_0^\infty f(t)e^{-st}\:dt$, if $f(t)$ grows too rapidly, $e^{-st}$ cannot hold it down, the integral will not converge. To quantify what's rapidly growing, if a function's absolute value $\vert f(t)\vert$ is less or equal than some constant times $Ce^{kt}$, the function is said to be of <u>"exponential type"</u>. For example, 

- $\vert \sin t\vert\leq 1e^{0t}$
- $\vert t^n\vert<Me^{t}$ because $\displaystyle \left\vert\frac{t^n}{e^t}\right\vert\rightarrow0$ as $t\rightarrow \infty$ which can be seen from taking nth derivative above and below by L'Hospital 

Some cases that does not converge, for these functions, the Laplace transform does not exist: 

- $\displaystyle \frac{1}{t}$ because this function goes to $\infty$ when $t$ goes to zero, and $e^{-st}$ is 1 when $t=0$ so it cannot constrain the growth
- $e^{t^2}$ just goes too fast, it will always outgrow $e^{kt}$ at some value of $t$ 

## Laplace for derivative

In order to perform Laplace transform on the whole equation $$Ay''+By'+Cy=f(t)$$, we need to know the formula for $y''$ and $y'$. 

$$
\begin{align}
\mathcal L(f'(t))&=\int_0^\infty f'(t)e^{-st}\: dt\\
&=\left[\frac{f(t)}{e^{st}}\right]_0^\infty-\int_0^\infty -se^{-st}f(t)dt\\
\end{align}
$$

As long as $f(t)$ satisfy the it's of the "exponential type", the infinity end will be converging to zero. The zero end will just be $f(0)$. (Recall $\mathcal L(f(t))=F(s)$)

$$
\begin{align}
\mathcal L(f'(t))&=-f(0)+s\int_0^\infty e^{-st}f(t)\:dt\\
&=sF(s)-f(0)
\end{align}\tag{1}
$$

With this we can apply $$f''$$ into this formula:

$$
\begin{align}
\mathcal L(f''(t))&=s\mathcal L(f'(t))-f'(0)\\
&=s(sF(s)-f(0))-f'(0)\\
&=s^2F(s)-sf(0)-f'(0)
\end{align}\tag{2}
$$

## Solving DE

From above we see that if we want to use Laplace transform we need to have initial conditions. But the benefit of Laplace transform is we avoid all the messy steps of getting complementary and then particular and the substitution to get the constants. Laplace can give all answers at once. The general procedure of using Laplace transform to solve the DE is 

1. Perform Laplace transform on both side of the DE
2. Separate the transformed equations into $F(s)=...$ or $Y(s)=...$
3. Partial fraction decomposition on the right hand side 
4. Laplace inverse transform

Let's see an <u>example</u>: $$y''-y=e^{-t},y(0)=1,y'(0)=0$$

1&2. Laplace transform on both side, and separate the equations:

$$
\begin{align}
s^2Y-sy(0)-y'(0)-Y&=\frac{1}{s+1}\\
(s^2-1)Y&=\frac{1}{s+1}+s\\
(s^2-1)Y&=\frac{s^2+s+1}{s+1}\\
Y&=\frac{s^2+s+1}{(s+1)^2(s-1)}
\end{align}
$$

3 Then we decompose the fractions:

$$
\frac{s^2+s+1}{(s+1)^2(s-1)}=\frac{A}{(s+1)^2}+\frac{B}{s+1}+\frac{C}{s-1}
$$

By covering up, we can get $C=3/4$, $A=1/-2$, and we can do (I don't know the method name) setting both side of $s=0$, $-1=A+B-C$, and $B=1/4$. Therefore

$$
\begin{array}{l}
\displaystyle\mathcal L^{-1}(-1/2\frac{1}{(s+1)^2})&=\displaystyle-\frac{1}{2}te^{-t}\\
\displaystyle\mathcal L^{-1}(1/4\frac{1}{s+1})&=\displaystyle\frac{1}{4}e^{-t}\\
\displaystyle\mathcal L^{-1}(3/4\frac{1}{s-1})&=\displaystyle\frac{3}{4}e^t
\end{array}
$$

Therefore the solution is 

$$
y=-\frac{1}{2}te^{-t}+\frac{1}{4}e^{-t}+\frac{3}{4}e^t
$$

where the first one is the particular solution?