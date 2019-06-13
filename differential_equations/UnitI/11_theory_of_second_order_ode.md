---
layout: post
date: 2019-6-8
title: Theory of General Second-order Linear Homogeneous ODE's
---

(Book 2.1)

Recall a second order homogeneous linear ODE is:

$$
y''+p(t)y'+q(t)y=0\tag{1}
$$

## Superposition principle

Let $$y_1$$ and $$y_2$$ be the solutions to the homogeneous ODE, and $$c_1,c_2$$ are constants. Then 

$$
y=c_1y_1+c_2y_2
$$

is also a solution to the ODE.

*Proof*: (Since this is simple) If $$y=c_1y_1+c_2y_2$$, then

$$
\begin{align}
y'=c_1y_1'+c_2y_2'\ \mathrm{and}\ y''=c_1y_1''+c_2y_2''
\end{align}
$$

And:

$$
\begin{align}
y+py'+qy''&=c_1y_1+c_2y_2+p(c_1y_1'+c_2y_2')+q(c_1y_1''+c_2y_2'')\\
&=c_1(y_1+py_1'+qy_1'')+c_2(y_2+py_2'+qy_2'')\\
&=c_1\cdot0+c_2\cdot0\\
&=0
\end{align}
$$

because $$y_1$$ and $$y_2$$ are solutions, their substitution into (1) at line 2 will result in 0. Thus $$y=c_1y_1+c_2y_2$$ also results in zero and it is a solution. 

What this implies is that there're "twofold infinity"

## Existence and Uniqueness for Linear Equations

Let the second order inhomogeneous linear ODE is:

$$
y''+p(t)y'+q(t)y=f(t)\tag{2}
$$

This equation has one and only one solution satisfying the initial conditions:

$$
y(a)=b_0,\ \ \ y'(a)=b_1
$$

Eq. (1) is also called the associated homogeneous eq. for eq. (2). The proof is hard so I will leave it out here. 



## Def. Linearly Independent 

Two functions defined on an open interval $$I$$ are said to be <u>linearly independent</u> if neither is a constant multiple of the other. 



## Wronskians

The <u>Wronskian</u> of f and g is 

$$
W(f,g)=\begin{vmatrix}
f & g\\
f' & g'
\end{vmatrix}=fg'-f'g
$$

We can either write $$W(f,g)$$ or $$W(t)$$, maybe I will write $$W(f,g)(t)$$ because $$f,g$$ are functions of $$t$$. But if $$f$$ and $$g$$ are linearly dependent, that is, $$f=kg$$, then 

$$
W(f,g)=\begin{vmatrix}
kg & g\\
kg' & g'
\end{vmatrix}=kgg'-kg'g=0
$$

This leads to if $$y_1$$ and $$y_2$$ are solutions to (1), then 

- If $$y_1$$ and $$y_2$$ are linearly dependent, then $$W(y_1,y_2)=0$$ 
- If $$y_1$$ and $$y_2$$ are linearly independent, then $$W(y_1,y_2)\neq 0$$ 

This leads to the theorem for general solutions of homogeneous equations.



## General Solutions of Homogeneous Equations

Let $$y_1$$ and $$y_2$$ are two linearly independent solutions to (1),

$$
y''+p(t)y'+q(t)y=0
$$

Then if $$Y$$ is any solutions whatsoever of (2),  there must exist $$c_1$$ and $$c_2$$ s.t. 

$$
Y(t)=c_1y_1(t)+c_2y_2(t)
$$

This is saying that if we can find two linearly independent solutions to a second order homogeneous solutions (2), then we found *all* solutions. 

*Proof*: Assume there does not exist a linear combinations of $$y_1,y_2$$ that can constitute $$Y(t)$$. Despite that, we set up the following simultaneous equations:

$$
\begin{align}
c_1y_1(a)+c_2y_2(a)&=Y(a)\\
c_1y_1'(a)+c_2y_2'(a)&=Y'(a)\\
\end{align}
$$

where $$c_1,\ c_2$$ are the unknowns. By Wronskian $$W(y_1,y_2)(a)\neq 0$$ because $$y_1,y_2$$ are independent, we know that there must exist $$c_1,\ c_2$$ that satisfy such system of equations. Let such $$c_1,\ c_2$$ be the coefficients of the linear combinations:

$$
G(t)=c_1y_1(t)+c_2y_2(t)
$$

We have the following, when $$G(t)$$ is evaluated at $$t=a$$,

$$
\begin{align}
G(a)&=c_1y_1(a)+c_2y_2(a)=Y(a)\\
G'(a)&=c_1y_1'(a)+c_2y_2'(a)=Y'(a)\\
\end{align}
$$

By Existence and Uniqueness theorem, there must be one and only one solution $$y$$ to (1) s.t. 

$$
y(a)=Y(a),\ y'(a)=Y'(a)
$$

therefore, since $$G(t)$$ satisfies the condition $$G(a)=Y(a)$$ and $$G'(a)=Y'(a)$$, $$G(t)$$ and $$Y(t)$$ are the same function. 



All these theorem can be generalized for higher order differential equations. 



## Polynomial Differential Operator

Let $$D=d/dt$$ denotes the operation of differentiation w.r.t. to $$t$$, so that 

$$
Dy=y',\ D^2y=y'',\ D^3y=y^{(3)}
$$

and so on. In terms of $$D$$, we can define another operator $$P(D)(·)$$ s.t.

$$
\begin{align}
P(D)&=a_nD^n+a_{n-1}D^{n-1}+...+a_2D^2+a_1D^1+a_0\\
P(D)y&=a_ny^{(n)}+a_{n-1}y^{(n-1)}+...+a_2y''+a_1y'+a_0
\end{align}
$$

It's probably useful to denote $$L(·)=P(D)(·)$$ because generally we won't have things other than $$D$$ to put in ($$L$$ stands for linear which I will explain a bit later). And we will restrict our discussion to second order linear ODE. The benefit of differential operators is we can write the factorization of characteristic equation into the original DE, say if we have 

$$
y''-5y+6=0
$$

its characteristic equation will be

$$
r^2-5y+6=0
$$

The corresponding $$P(D)y$$ is

$$
\begin{align}
(D^2-5D+6)y&=0\\
(D-3)(D-2)y&=0
\end{align}
$$

Also note that $$L=P(D)$$ is a linear operator, this is saying

$$
\begin{align}
L(x+y)&=L(x)+L(y)\\
L(cy)&=cL(y)\\
\end{align}
$$

This is obvious because $$D$$ is linear s.t. $$D(x+y)=D(x)+D(y)$$ and etc. One useful property is *commute*:

$$
\begin{align}
(D-a)(D-b)y&=(D-a)(y'-by)\\
&=y''-by'-ay'+aby\\
&=D(y'-ay)-b(y'-ay)\\
&=(D-b)(D-a)y
\end{align}
$$


## Repeated Real Roots

So we would like to use the differential operator to find the repeated roots. Let's consider an arbitrary order linear ODE with constant coefficients:

$$
a_ny^{(n)}+...+a_1y'+a_0=0
$$

Then it has a characteristic equation:

$$
a_nr^n+...+a_1r+a_0=0
$$

Suppose the characteristic equation can be factored into

$$
(r-r_1)^k(r-r_0)=0
$$

where $$k=n-1$$. Solving this equation will only give us two distinct roots $$r_1$$ and $$r_0$$, but we need total $$n$$ independent roots. Similar to the factored characteristic equation, $$Ly$$ can also be factored:

$$
\begin{align}
Ly=(D-r_1)^k(D-r_0)y&=0\\
(D-r_0)[(D-r_1)^ky]&=0
\end{align}
$$

Therefore our problem reduced to find the solutions for the kth-order equation:

$$
(D-r_1)^ky=0\tag{3}
$$

The fact that $$y_1=e^{r_1t}$$ suggests (??) that we can try substitute $$y=u(t)e^{r_1t}$$ into the equation (3). Before that, observe

$$
(D-r_1)[ue^{r_1t}]=u'e^{r_1t}+ur_1e^{r_1t}-r_1ue^{r_1t}=(Du)e^{r_1t}
$$

Therefore,

$$
(D-r_1)^k[ue^{r_1t}]=(D^ku)e^{r_1t}
$$

The only solution that satisfy $$(D^ku)e^{r_1t}=0$$ is $$u^{(k)}=0$$. This only happens when $$u$$'s derivative is constant at $$k-1$$ differentiation. This can happen when:

$$
u(t)=(c_1+c_2t+c_3t^2+...+c_kt^{k-1})
$$

Note we don't need to have t's exponential goes to $$k-1$$, but since we need $$k+1$$ independent solutions, this is the best we can have. Therefore,

$$
y(t)=u(t)e^{r_1t}=(c_1+c_2t+c_3t^2+...+c_kt^{k-1})e^{r_1t}
$$

When we have two repeated roots for second order linear ODE, $$k=2$$:

$$
(r-r_1)^k=0
$$

The solution is 

$$
y(t)=(c_1+c_2t)e^{rt}
$$


