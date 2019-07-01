---
layout: post
title: Laplace transform with impulse input
date: 2019-6-29
---

An impulse force over interval $[a,b]$ is, by definition, $\displaystyle \int_a^bf(t)\:dt$, if the impulse force is a constant force $F$ over this period, then the impulse becomes $F\cdot(b-a)$. A unit input is s.t. $F\cdot(b-a)=1$, implying that $\displaystyle F=\frac{1}{b-a}$. Let's make the lower bound $a=0$, then the input will become $\displaystyle \frac{1}{b}H_{0b}(t)$, which is

$$
\frac{1}{b}[H(t)-H(t-b)]\tag{1}
$$

The Laplace transform $\mathcal L(·)$ of this is:

$$
\frac{1}{b}[\frac{1}{s}-\frac{e^{-bs}}{s}]\tag{2}
$$

Now what happen if if we let $b$ goes to zero, what is $\displaystyle \lim_{b\rightarrow 0}\frac{1-e^{-bs}}{bs}$? We can use L'Hospital:

$$
\lim_{b\rightarrow 0}\frac{1-e^{-bs}}{bs}=\lim_{u\rightarrow 0}\frac{1-e^{-u}}{u}=\lim_{u\rightarrow 0}\frac{e^{-u}}{1}=1
$$

So the Laplace transform of unit impulse $\displaystyle \frac{1}{b}H_{0b}(t)$ approaches 1 when $b$ approaches $0$, when the interval becomes narrower and narrower. What we can expect is there would be a infinite high straight line at 0. This is not really a function, people call it a generalized function $\delta(t)$ s.t. its Laplace transform is 1, and its definite integral:

$$
\int_{-\infty}^\infty\delta(t)\:dt=1
$$

If you are familiar with probability, this is the PDF of the point mass function at zero. Unsurprisingly, its indefinite integral is

$$
\int_{-\infty}^t\delta(t_1)\:dt_1=H(t)
$$

Go back to convolution, the delta function acts like an identity:

$$
\mathcal L(H(t)f(t)*\delta(t))=\mathcal L(H(t)f(t))
$$

Let's have a spring-mass system with a constant $A$ impulse input at time $\pi/2$:

$$
y''+y=A\delta(t-\frac{\pi}{2}),\quad y(0)=1,y'(0)=0
$$

Now the Laplace transform of this is: (by (2) in [note 20](./20_derivative_formulas) and (2) in [note 22](./22_jump_discontinuities))

$$
\begin{align}
s^2Y-s+Y&=Ae^{-\pi/2\cdot s}\\
Y&=\frac{Ae^{-\pi/2\cdot s}}{s^2+1}+\frac{s}{s^2+1}
\end{align}
$$

Then the inverse Laplace is 

$$
y=\cos t+H(t-\pi/2)A\sin(t-\pi/2)
$$
