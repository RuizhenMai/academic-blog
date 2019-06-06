---
layout: post
title: Linear Second Order ODE w/ constant Coefficients
date: 2019-6-6
---

In standard form, with a constant zero input, sometimes called homogenous
$$
y''+Ay'+By=0
$$
For now, assume the general solution
$$
y=c_1y_1+c_2y_2
$$
where $$y_1$$ and $$y_2$$ are solutions. We have a simple physical model: spring-mass-dashpot:

graph
$$
\begin{array}{}
mx''&=-cx-kx'\\
mx''+kx'+cx&=0\\
x''+\frac{k}{m}x'+\frac{c}{m}x&=0\\
\end{array}
$$

### Basic methods

Try $$y=e^{rt}$$, $$t$$ is the independent variable . Above $$x$$ is the dependent variable.

Characteristic equations of the system.

Case 1. Roots $$r_1\neq r_2$$ 	

Case 2. Roots complex conjugate

