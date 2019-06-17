---
layout: post
title: Singular Value Decomposition
date: 2019-6-16
---

## Singular Value Decomposition(SVD)

$$
A=\underbrace{U}_{orthogonal}\underbrace{\Sigma}_{\ diagonal} \underbrace{V^\top}_{\ orthogonal}
$$

This is the final and best decomposition for a matrix, and it does not require $$A$$ to be square. $$U,V$$ are orthogonal and $$\Sigma$$ is diagonal. If $$A$$ is square, then its svd is just $$A=S\Lambda S^{-1}$$. And if $$A$$ is symmetric then $$A=Q\Lambda Q^\top$$. But we're after an orthogonal matrix, in $$A=S\Lambda S^{-1}$$, $$S$$ is not orthogonal, so no good. (According to the book, eigenvalues are unstable but singular values are) What are $$U,\Sigma$$ and $$V$$ exactly? Imagine, A $$m\times n$$ matrix $$A$$:

$$
A=\begin{bmatrix}
\underbrace{u_1}_{\mathbb R^{m\times 1}} & u_2 & ... & u_{n-1} &  u_n
\end{bmatrix}\tag{1}\\
A=\begin{bmatrix}
v_1^\top\\
v_2^\top\\
\vdots\\
v_{m-1}^\top\\
\underbrace{v_m^\top}_{\mathbb R^{1\times n}}
\end{bmatrix}
$$

can be thought of being constructed in two ways. One is $$A$$ has n column vectors, the other is $$A$$ has m row vectors (neglect the transpose for now). These columns or rows do not have to independent. $$v_1^\top=…=v_m^\top$$ all have size $$1\times n$$. So to make it prettier, we can get rid of the transpose, then they all have size $$n\times 1$$. What happened if we try $$Av_1$$? $$Av_1$$ has size $$m\times 1$$. In fact, $$Av_1$$ is transforming a vector in the row space to the column space. Why? Say $$A$$ has rank $$2\times 3$$ and has rank $$2$$. Then column space is $$\mathbb R^2$$ and row space is in $$\mathbb R^3$$ but only has dimension 2, $$v_1$$ is in such space. And $$Av_1$$ is size $$2\times1$$ which lies exactly in the column space. This can be generalized to any rank and arbitrary sizes. Let $$\mathbf x$$ has size $$n\times 1$$, then 

$$
A\mathbf x=x_1u_1+x_2u_2+...+x_nu_n
$$

is a linear combination of the column space in (1). Now first let $$V_r$$ <u>be a orthonormal basis for the row space</u>. This is saying 

$$
V_r=\underbrace{\begin{bmatrix}
\vert &... & \vert\\
v_1 & ... & v_r\\
\vert &...&\vert\\
\end{bmatrix}}_{\mathbb R^{n\times r}}
$$

but right now $$v$$ has to be a unit vector. When we do $$AV$$, we are just transforming a bunch of vectors into the column space. Let 

$$
U_r=\underbrace{\begin{bmatrix}
\vert &... & \vert \\
u_1 & ... & u_r\\
\vert & ... & \vert \\
\end{bmatrix}}_{\mathbb R^{m\times r}}
$$

be an <u>orthogonal basis for the column space</u>. $$AV_r=m\times n\times n\times r=m\times r$$, which has the same size as $$U_r$$. Since we've known each column of $$AV_r$$ is in the column space and $$U_r$$ is an orthornomal basis for the column space, we have 

$$
AV_r=U_r\Sigma_r
$$

where $$\Sigma_r$$ is a diagonal matrix with a bunch of constants. Now to make the SVD complete, we can extend $$V_r$$ to $$V$$, and $$U_r$$ to $$U$$, (in fact we do not quite care about this):

$$
V=\underbrace{\begin{bmatrix}
\vert &... & \vert & ... &\vert\\
v_1 & ... & v_r&...&v_n\\
\vert &...&\vert&...&\vert\\
\end{bmatrix}}_{\mathbb R^{n\times n}}\\
U=\underbrace{\begin{bmatrix}
\vert &... & \vert & ... &\vert\\
u_1 & ... & u_r&...&u_m\\
\vert &...&\vert&...&\vert\\
\end{bmatrix}}_{\mathbb R^{m\times m}}
$$

You probably notice the size of $$V$$ doesn't quite match what we have on (3). In fact you are right. What we are adding up <u>after</u> $$v_r$$, $$v_{r+1},…,v_n$$ <u>is a basis for null space</u> not left null space. And the diagonal constants $$\sigma_{r+1}…\sigma_{*}$$ are all zero because 

$$
Av_{r+1}=...=Av_{n}=0
$$

So our final SVD:

$$
AV=U\Sigma\\
A=U\Sigma V^{-1}\\
A=U\Sigma V^\top
$$

Line 2 to 3 because $$V$$'s columns is orthonormal. And conventionally, people put values $$\sigma_1…\sigma_*$$ in descending order in  $$\Sigma$$, the greatest comes first. 

## How to find them

So how to find this matrix? Note that 

$$
\begin{align}
A^\top A&=(V\Sigma^\top U^\top)U\Sigma V^\top\\
&=V\Sigma^\top\Sigma V^\top
\end{align}
$$

This is similar to $$A=S\Lambda S$$ right? Therefore, $$\Sigma^\top \Sigma$$ are the eigenvalues for $$A^\top A$$, and $$V$$'s <u>columns are the eigenvectors of</u> $$A^\top A$$. So $$\Sigma$$ <u>is composed of the square root of</u> $$A^\top A$$<u>'s eigenvalues</u>. Similarly $$U$$ is the eigenvectors of $$AA^\top$$ but has the same eigenvalues. Let's do an example:

$$
A=\begin{bmatrix}
4 & 4\\
-3 & 3
\end{bmatrix}
$$

Then 

$$
A^\top A=\begin{bmatrix}
25 & 7\\
7 & 25
\end{bmatrix}
$$

And its eigenvectors and values are

$$
\lambda_1=32\sim\mathbf x_1=\frac{1}{\sqrt 2}\begin{bmatrix}
1\\
1
\end{bmatrix}\\
\lambda_2=18\sim\mathbf x_2=\frac{1}{\sqrt2}\begin{bmatrix}
-1\\
1
\end{bmatrix}
$$

We normalize the eigenvectors because we need an orthonormal basis. Then we have $$\Sigma$$ and $$V^\top$$. 

$$
\Sigma=\begin{bmatrix}
\sqrt{32} & 0\\
0 & \sqrt{18}
\end{bmatrix},V^\top=\frac{1}{\sqrt2}\begin{bmatrix}
1 & 1\\
-1 & 1
\end{bmatrix}
$$

We can find $$U$$ by doing $$AA^\top$$ again or we can write out $$A=U\Sigma V^\top$$ to guess, but anyway: 

$$
A=\begin{bmatrix}
1 & 0\\
0 & 1
\end{bmatrix}\begin{bmatrix}
\sqrt{32} & 0\\
0 & \sqrt{18}
\end{bmatrix}\frac{1}{\sqrt2}\begin{bmatrix}
1 & 1\\
-1 & 1
\end{bmatrix}
$$
