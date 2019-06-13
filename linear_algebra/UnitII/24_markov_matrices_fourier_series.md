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

So their *rows* are dependent. And $$[1,1,1]$$ is in the left null space $$N(A^\top)$$. Thus the dimension of $$N(A^\top)$$ is not zero, and we must have at least one eigenvector $$\mathbf x_1$$ corresponds to $$\lambda_1=1$$. 

### Eigenvalues of $$A$$ same as Eigenvalues of  $$A^\top$$ 

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

Fourier series is based upon orthonormal (orthogonal) basis (matrix).  An orthogonal matrix is a square matrix where its columns $$q_1, …,q_n$$ are orthogonal, that is 

$$
q_i^\top q_j=0,\forall i,j\in[1,n],i\neq j
$$

If $$i=j$$, then $$q_i^\top q_j=1$$. If we have a vector $$\mathbf v=Q\mathbf c$$, where $$\mathbf c$$ is a vector with constants, Q is a orthogonal matrix:

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

Now Fourier series itself is an infinite orthonormal matrix where its $$q_1,…,q_n$$ are $$a_0*1, a_1cos(x), b_1sin(x), a_2cos(2x), b_2\sin(2x) … $$and etc (it's not a $$\mathbf v$$ bc its column inner product needs to be 1).

$$
f(x)=a_0+a_1\cos x+b_1\sin x+a_2\cos 2x+b_2\sin 2x+...
$$

This is also a vector, though it has infinitely many elements/dimensions. Since it's a vector, we can a dot product is similar to $$\mathbf v^\top \mathbf w=v_1w_1+v_2w_2+…$$ each element of these two vectors are multiplied and summed. So it is:

$$
f^\top g=\int_0^{2\pi}f(x)g(x)\ dx
$$

It is integrated from 0 to $$2\pi$$ because all $$\sin,\cos$$ are periodic functions and its one period does not exceed $$2\pi$$. And to check its bases are orthogonal, we can pick any columns/elements of it, like $$a_1\cos(x)\ \mathrm{and}\ b_1\sin(x), a_2\cos(2x)\ \mathrm{and}\  b_2\sin(2x)$$, their inner product (integration) will all be zero. If they are the same element, then the inner product shall be 1. To find a *Fourier Coefficient*:

$$
\begin{align}
1&=q^\top_iq_i\\
&=\int_0^{2\pi} \cos x\ f(x)dx\\
&=\int_0^{2\pi} \cos x\ a_1\cos(x)dx\\
&=a_1\pi
\end{align}
$$

Therefore, $$\displaystyle a_1=\frac{1}{\pi}\int_0^{2\pi} \cos x\ f(x)dx\\$$

 

