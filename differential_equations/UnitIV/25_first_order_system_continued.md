---
layout: post
title: First Order System Continued
date: 2019-6-14
---

Rewrite the dependent variables $$T_1,\: T_2$$ into $$x,\: y$$, the system of equations from last lecture is

$$
\begin{align}
x'&=-2x+2y\\
y'&=2x-5y
\end{align}\tag{1}
$$

And the final solution we got

$$
\begin{align}
x&=c_1e^{-6t}+c_2e^{-t}\\
y&=-2c_1e^{-6t}+\frac{1}{2}c_2e^{-t}
\end{align}\tag{2}
$$

Let's rewrite the system (1) into matrices

$$
\begin{bmatrix}
x\\
y 
\end{bmatrix}'=\begin{bmatrix}
-2 & 2\\
2 & -5
\end{bmatrix}\begin{bmatrix}
x\\
y 
\end{bmatrix}\tag{3}
$$

Here $$x',y'$$ are taken w.r.t to independent variable $$t$$. And put the (2) into matrices again, but we won't exploit the fact that $$c_1,\: c_2$$ can be columns:

$$
\begin{bmatrix}
x\\
y
\end{bmatrix} =c_1\begin{bmatrix}
1 \\
-2
\end{bmatrix}e^{-6t}+c_2\begin{bmatrix}
 1 \\
 \frac{1}{2} 
\end{bmatrix}e^{-t}\tag{4}
$$

We will utilize the matrices to solve differential equations. And similar to before, trial solutions: $$e^{rt}$$, but we will do it in a way that resembles the solution in (4). 

$$
\begin{align}
\begin{bmatrix}
 x\\
 y
\end{bmatrix}&=\begin{bmatrix}
 a_1\\
 a_2
\end{bmatrix}e^{\lambda t}\\
\begin{bmatrix}
 x\\
 y
\end{bmatrix}'&=\lambda\begin{bmatrix}
 a_1\\
 a_2
\end{bmatrix}e^{\lambda t}
\end{align}\tag{5}
$$

Now we've got these two equations and we substitute them into (3):

$$
\begin{align}
\lambda\begin{bmatrix}
 a_1\\
 a_2
\end{bmatrix}e^{\lambda t}&=\begin{bmatrix}
-2 & 2\\
2 & -5
\end{bmatrix}\begin{bmatrix}
 a_1\\
 a_2
\end{bmatrix}e^{\lambda t}\\
\\
\lambda\begin{bmatrix}
 a_1\\
 a_2
\end{bmatrix}&=\begin{bmatrix}
-2 & 2\\
2 & -5
\end{bmatrix}\begin{bmatrix}
 a_1\\
 a_2
\end{bmatrix}\\
\\
\mathbf 0&=\begin{bmatrix}
-2-\lambda & 2\\
2 & -5-\lambda
\end{bmatrix}\begin{bmatrix}
 a_1\\
 a_2
\end{bmatrix}
\end{align}
$$

This can look quite similar to you if you remember eigenvalues, if you don't, no problem. The only way to get non-trivial solutions, that is $$a_1\neq 0,\:a_2\neq0$$, is the matrix on the left is singular. That is, the determinant is zero

$$
\begin{align}
\begin{vmatrix}
-2-\lambda & 2\\
2 & -5-\lambda
\end{vmatrix}&=0\\
(-2-\lambda)(-5-\lambda)-4&=0\\
\lambda^2+7\lambda+6&=0\\
\lambda_1=-6,\lambda_2=-1
\end{align}
$$

The equation $$\lambda^2+7\lambda+6=0$$ is also called the characteristic equation. Then after finding the $$\lambda$$, for corresponding $$\lambda_1$$ and $$\lambda_2$$, we need to find the corresponding eigenvectors (basis) $$\mathbf x_1=\begin{bmatrix}
 a_1\\
 a_2
\end{bmatrix}$$ and another $$\mathbf x_2$$ with different $$a_1,a_2$$ (they have nothing to do with the dependent variables). So

$$
\begin{bmatrix}
4 & 2\\
2&1
\end{bmatrix}\begin{bmatrix}
 a_1\\
 a_2
\end{bmatrix}=\mathbf0\\
\Rightarrow\\
\lambda_1=-6\sim\mathbf x_1=\begin{bmatrix}
1\\
-2
\end{bmatrix}
$$

And:

$$
\begin{bmatrix}
-1 & 2\\
2&-4
\end{bmatrix}\begin{bmatrix}
 a_1\\
 a_2
\end{bmatrix}=\mathbf0\\
\Rightarrow\\
\lambda_2=-1\sim\mathbf x_2=\begin{bmatrix}
2\\
1
\end{bmatrix}
$$

And we have a similar solution as (4):

$$
\begin{bmatrix}
x\\
y
\end{bmatrix} =c_1\begin{bmatrix}
1 \\
-2
\end{bmatrix}e^{-6t}+\tilde c_2\begin{bmatrix}
 2 \\
 1
\end{bmatrix}e^{-t}\tag{6}
$$
 $$\tilde c_2=2c_2$$ , but they are just constants, you got it.

In short, from a second order DE, with coefficient matrix as:

$$
A(t)=\begin{bmatrix}
a & b\\
c & d
\end{bmatrix}
$$

We can construct the characteristic equation

$$
\lambda^2-(a+d)\lambda+ad-bc=0\\
\lambda^2-\mathrm{tr}(A)+\det A=0
$$

To write (3) into a more concise form

$$
\mathbf x'=A\mathbf x\tag{7}
$$

And the trial solutions (4), not to confuse the $$\mathbf x$$, let the eigenvectors be $$\mathbf v$$, 

$$
\mathbf x=\mathbf ve^{\lambda t}\\
\mathbf x'=\lambda\mathbf ve^{\lambda t}\tag{8}
$$

Substitute in we get

$$
\lambda\mathbf ve^{\lambda t}=A\mathbf ve^{\lambda t}\\
\lambda\mathbf v=A\mathbf v
$$
