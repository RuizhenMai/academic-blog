---
layout: post
date: 2019-6-10
title: Markov Matrices; Fourier Series
---

## Markov Matrices

$$
A=\begin{bmatrix}
.1 & .01 & .3\\
.2 & .99 & .3 \\
.7 & 0 & .4 \\
\end{bmatrix}
$$

This is a Markov matrix because

- All entries >= 0
- All columns sum to 1 

The key point for this matrix is 

- $$\lambda =1$$ Is a eigenvalue
- All other $$0<\rvert \lambda_i\rvert<1$$  

Let's focus on why $$\lambda=1$$ will always be a eigenvalue. If that's true, then $$\det (A-1I)=0$$ should be true, take the above matrix as example:

$$
A-1I=\begin{bmatrix}
-.9 & .01 & .3\\
.2 & -.01 & .3 \\
.7 & 0 & -.6 \\
\end{bmatrix}
$$

We may not see directly why the determinant is zero at a first glance, but for a matrix to be singular, it must have one or more dependent columns (or rows, in square matrix the # of dept. rows should equal to # of dept. cols). Markov matrices shall have all columns sum to 1. And here, after subtracting one, all columns from up to down sum to zero. This means that 

$$
\begin{bmatrix}
1&1&1
\end{bmatrix}\begin{bmatrix}
-.9 & .01 & .3\\
.2 & -.01 & .3 \\
.7 & 0 & -.6 \\
\end{bmatrix}=\begin{bmatrix}
0&0&0
\end{bmatrix}
$$

So their *rows* are dependent. And $$[1,1,1]$$ is in the left null space $$N((A-1I)^\top)$$. Therefore $\det(A-I)=0$, and we can conclude that there exists an eigenvalue $\lambda_1=1$.  

### Eigenvalues of $A$ same as Eigenvalues of  $A^\top$

This is true because of our property 10 of determinant [(link)](./18_properties_of_determinants). 

$$
\det(A-\lambda I)=0=\det(A-\lambda I)^{\top}\\
$$

And $$\det(A-\lambda I)^\top=\det(A^\top-\lambda I)$$. So the eigenvalues $$\lambda$$ for $$A$$ is also true for $$A^\top$$.



### Application

Say we have populations of California and Massachusetts:

$$
\begin{bmatrix}
u_{Cal}\\
u_{Mass}
\end{bmatrix}
$$

And each year there's a portion of people moving from California to Massachusetts, and the other way versa. And this portion is .9 of Cal people will stay, .1 will move; .8 of Mass people will stay and .2 will move. So we can construct the following equation:

$$
\begin{bmatrix}
u_{Cal}\\
u_{Mass}\\
\end{bmatrix}_{t=k+1}=\begin{bmatrix}
.9 & .2 \\
.1 & .8 \\
\end{bmatrix}\begin{bmatrix}
u_{Cal}\\
u_{Mass}
\end{bmatrix}_{t=k}
$$

Since it's $$2\times 2$$, we can use tricks to find eigenvalues. It's a Markov Matrix, so one of its eigenvalue must be 1; since the trace of the matrix is 1.7, the other eigenvalue will be .7. We can find the eigenvector for $$\lambda_1=1$$, that will be $$\mathbf x_1=\begin{bmatrix}
2\\
1\\
\end{bmatrix}$$. The other eigenvector is not that important if we are looking for the steady state, because its eigenvalue < 1 will vanish as k goes to infinity. Then from this vector we can tell the steady state will be $$\begin{bmatrix}
1000*2/3\\
1000*1/3 \\
\end{bmatrix}$$ (I actually don't know why). 



## Fourier Series

Fourier series for a function $$f(t)$$ is:

$$
f(t)=\frac{a_0}{2}+\sum_{n=1}^\infty(a_n\cos nt+b_n\sin nt)\tag{1}
$$

Any functions $$f(t)$$ with period $$2\pi$$ can be approximated by Fourier series with their corresponding coefficients $$a_n$$ and $$b_n$$. 



We say a vector $$\mathbf v$$ or a function $$f$$ is in infinite dimensional ***Hilbert Space***, if and only if it has, of course, infinite items, and has finite lengths $$\lVert\mathbf v\rVert$$ and $$\lVert f\rVert$$:

$$
\begin{align}
\lVert\mathbf v\rVert^2&=\mathbf v\cdot\mathbf v=v_1^2+v_2^2+...<\infty\\
\lVert f\rVert^2&=(f,f)=\int_0^{2\pi}(f(t))^2\:dt<\infty
\end{align}
$$

You've seen how the length of a vector defined. The *length* of a function is defined that way because 

- For convenience, it's just integrated in $$[0,2\pi]$$ because we will only care about periodic functions that's piecewise continuous with period $$2\pi$$, it can also be in $$[-\pi,\pi]$$, but the integrations for these two intervals are the same.
- Length squared is squaring each bit in the element and sum it up, the integration is doing the same thing for each infinitely small bit in the function

One good thing about Fourier series is it has each element/trig function in the series are <u>orthogonal</u> to each other, that is, the inner products: $$(\sin(t),\cos(t))=0$$, $$(\sin(t),\sin(2t))=0$$ except the inner product of the trig function itself. 

Two functions $$u(t),v(t)$$ continuous on $$I$$ are said to be orthogonal if and only if

$$
\int_Iu(t)v(t)\:dt=0
$$

With this, we can calculate the coefficients for the Fourier series for specific function $$f(t)$$, because, integrating both sides of (1):

$$
\begin{align}
f(t)&=\frac{a_0}{2}+\sum_{n=1}^\infty(a_n\cos nt+b_n\sin nt)\\
\int_0^{2\pi}f(t)\:dt&=\int_0^{2\pi}\frac{a_0}{2}+\sum_{n=1}^\infty(a_n\cos nt+b_n\sin nt)\:dt\\
\int_0^{2\pi}f(t)\:dt&=\int_0^{2\pi}\frac{a_0}{2}\:dt\\
\int_0^{2\pi}f(t)\:dt&=a_0\pi
\end{align}
$$

Therefore,

$$
a_0=\frac{1}{\pi}\int_0^{2\pi}f(t)\:dt
$$

Similar things can be done, after we first multiply both sides of (1) by either $\cos nt$ or $\sin nt$, this gives us:

$$
\begin{align}
a_n&=\frac{1}{\pi}\int_0^{2\pi}f(t)\cos nt\:dt\\
b_n&=\frac{1}{\pi}\int_0^{2\pi}f(t)\sin nt\:dt\\
\end{align}
$$


How this correlates with Linear Algebra? First is the orthogonal trig functions in the series. They are not an *orthogonal basis* because it requires the they have length 1. But as long as we divide the length it would be. And you see the squared length is also just summing together. Hilbert space is a vector space as well. It's easy to prove with the property of integration. 

Remember an orthogonal matrix is a square matrix where its columns $$q_1, …,q_n$$ are orthonormal, that is 
$$
q^\top_iq_j=\begin{cases}
0 & if\ i\neq j\\
1 & if\ i=j
\end{cases}
$$

If we have a vector $$\mathbf v=Q\mathbf c$$, where $$\mathbf c$$ is a vector with constants, Q is a orthogonal matrix:

$$
\mathbf v=\begin{bmatrix}
q_1&...&q_n
\end{bmatrix}\begin{bmatrix}
c_1\\
\vdots\\
c_n
\end{bmatrix}
$$

, then $$\mathbf c=Q^{-1}\mathbf v=Q^\top\mathbf v$$ since $$Q$$ is orthogonal. And $$c_1=q_1^\top\mathbf v$$. 

