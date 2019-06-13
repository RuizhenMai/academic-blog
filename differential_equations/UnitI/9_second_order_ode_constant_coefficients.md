---
layout: post
title: Linear Second Order ODE w/ constant Coefficients
date: 2019-6-6
---

(Video 9-10) (Book 2.1, 2.3)

The second order linear ODE is:

$$
A(t)y''+B(t)y'+C(t)y=f(t)
$$

This is not in standard form, but it's ok. In these notes we will only examine second order linear ODE with constant coefficients and no input $$f(t)=0$$:

$$
Ay''+By'+Cy=0\tag{1}
$$

When $$f(t)=0$$, the second order ODE is called homogeneous (this is different from the one in first order). The ODE is analytically solvable. Let's assume below is true and we will come back to why there're only those cases later. 

## Characteristic Equation and Three Cases

The characteristic equation comes from the following: *suppose* solution has the form $$y=e^{rt}$$, then we substitute to check:

$$
\begin{align}
A(e^{rt})''+B(e^{rt})'+C(e^{rt})&=0\\
Ar^2e^{rt}+Bre^{rt}+Ce^{rt}&=0\\
(Ar^2+Br+C)e^{rt}&=0\\
Ar^2+Br+C&=0\tag{2}\\
\end{align}
$$

The e.q. (2) is called <u>characteristic equation</u> for the linear DE. To make $$y=e^{rt}$$ work (in fact it works), there're three cases for the equation:

- Case 1. Real Roots $$r_1\neq r_2$$ 	

- Case 2. Real Roots $$r_1=r2$$ 

- Case 3. Roots are complex conjugate

### Case 1: 

If the characteristic equation has two distinct real roots, then we can find a $$y_1=e^{r_1t}$$ and a $$y_2=e^{r_2t}$$ satisfying (2). And our final, general solution will be 

$$
y=c_1e^{r_1t}+c_2e^{r_2t}
$$

because of the Theorem for general solutions for homogeneous DE which would be discussed in [note 11](./11_theory_of_second_order_ode). $$y$$ contains all possible solutions to the second order linear ODE with constant coefficients. 

For example, DE:

$$
2y''-7y'+3y=0
$$

has a characteristic equation:

$$
\begin{align}
2r^2-7r+3&=0\\
(2r-1)(r-3)&=0\\
\end{align}
$$

The roots $$r_1=1/2$$ and $$r_2=3$$ are real and distinct, thus the solution is 

$$
y=c_1e^{t/2}+c_2e^{3t}
$$

### Case 2:

If we have repeated real roots, then our solution will be

$$
y=(c_1+tc_2)e^{rt}
$$

The reasoning behind this will be discussed [note 11](./11_theory_of_second_order_ode). For example, DE:

$$
\begin{align}
y''+2y'+y&=0\\
\end{align}
$$

has a characteristic equation:

$$
\begin{align}
r^2+2r+r&=0\\
(r+1)^2&=0
\end{align}
$$

And we have $$r=-1$$. So the solution to this DE is:

$$
y=(c_1+tc_2)e^{-t}
$$

### Case 3:

If the root to the characteristic equation is complex conjugate $$r=a\pm bi$$, then $$Re(e^{rt})$$ and *coefficient* of $$Im(e^{rt})$$ are the basis for general solutions. This can have a quick proof.

*Proof*: expand $$y=e^{rt}$$ where $$r=a\pm bi$$

$$
y=e^{rt}=e^{(a+bi)t}=e^{at}(\cos bt+i\sin bt)=e^{at}\cos bt+ie^{at}\sin bt
$$

Let $$u = e^{at}\cos bt,\ v=e^{at}\sin bt$$, then $$y=u+iv$$. Substitute this into (1):

$$
\begin{align}
A(u+iv)''+B(u+iv)'+C(u+iv)&=0\\
Au''+iAv''+Bu'+iBv'+Cu+iCv&=0\\
\underbrace{Au''+Bu'+Cu}_{real\ part}+\underbrace{i(Av''+Bv'+Cv)}_{imaginary}&=0\\
\end{align}
$$

To make the equation true, both the real part and imaginary part should be equal to zero. Equal to zero means substituting $$u$$ or $$v$$ into (1), the equation holds. Thus they are the solutions. And 

$$
\begin{align}
y&=c_1u+c_2v=c_1e^{at}\cos bt+c_2e^{at}\sin bt\\
&=e^{at}(c_1\cos bt+c_2\sin bt)
\end{align}
$$
