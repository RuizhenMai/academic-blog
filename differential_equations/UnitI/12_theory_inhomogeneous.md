---
layout: post
title: Theory for Inhomogeneous ODE's
date: 2019-6-9
---

## General Solution

If an n-th order linear non-homogeneous equations is in this form:
$$
y^{(n)}+p_1y^{(n-1)}+...+p_{n-1}y=f(t)\tag{1}
$$
then its associated homogeneous equation is:
$$
y^{(n)}+p_1y^{(n-1)}+...+p_{n-1}y=0
$$
We know that there exists $$n$$ independent solutions for an n-th order homogeneous DE:
$$
y_c=c_1y_1+...+c_ny_n
$$
$$y_c$$ here is called complementary solution. Suppose there's a $$y_p$$ that can solve (1), (1)'s general solution is
$$
Y=y_c+y_p
$$
*Proof*: substitute $$Y$$ into (1):
$$
\begin{align}
Y^{(n)}+p_1Y^{(n-1)}+...+p_{n-1}Y&=f(t)\\
y_c^{(n)}+y_p^{(n)}+p_1(y_c^{(n-1)}+y_p^{(n-1)})+...+p_{n-1}(y_c+y_p)&=f(t)\\
y_c^{(n)}+p_1y_c^{(n-1)}+...+p_{n-1}y_c+(...)&=f(t)\\
0+(...)&=f(t)
\end{align}
$$
thus adding $$y_c$$ does not affect the equation and $$Y$$ is the general solution.



## Variation of Parameters

