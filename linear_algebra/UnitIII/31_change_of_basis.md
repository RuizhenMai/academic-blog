---
layout: post
title: Change of Basis
date: 2019-4-17
---

Chang of basis for a vector $$\mathbf p$$ representing coefficients/coordinates for the old basis into a new vector of coordinates $$\mathbf c$$ with base $$W$$ is

$$
\mathbf p=W\mathbf c\\
\mathbf c=W^{-1}\mathbf p
$$


Good Basis is

- Fast at getting inverses
- Fast at multiplying a vector  
- Good for compression, some columns do not matter that much

## Change of Basis w/ Linear Transformation

Let the transformation $$T(·)$$ has matrix $$A$$ in $$\mathbb R^n$$ with basis $$v_1,…v_n$$, and it transforms into $$\mathbb R^m$$ with basis $$w_1,…,w_m$$. So $$A:m\times n$$ . We know $$T(·)$$ completely if know its output on every base vectors: $$T(v_1),T(v_2),…,T(v_n)$$. Let's say we have a vector $$\mathbf x=c_1v_1+c_2v_2+…+c_nv_n$$, then $$T(\mathbf x)=c_1T(v_1)+…+c_nT(v_n)$$. Along with $$A=T(·)$$, we need to make sure $$A\mathbf x=c_1Av_1+c_2Av_2+…+c_nAv_n$$ can produce the same effect of $$T(\mathbf x)$$. Let 

$$
A=\begin{bmatrix}
a_{11} & ... & a_{1n}\\
\vdots&\times&\vdots\\
a_{m1}&...&a_{mn}\\
\end{bmatrix}
$$

<u>and</u> $$T(v_1)=T(\begin{bmatrix}
1\\0\\\vdots
\end{bmatrix})$$ <u>because it's only the first vector in the basis</u> $$\begin{bmatrix}
\vert & ... & \vert\\
v_1&…&v_n\\
\vert&…&\vert\\
\end{bmatrix}$$. <u>Therefore</u> $$Av_1$$ <u>is equal to the first column of $$A$$ multiplying</u> $$v_1$$. Thus $$a_{11}…a_{m1}$$ satisfy $$a_{11}w_1+…a_{m1}w_m=T(v_1)$$ (just the $$a$$ the coefficients matters, $$w_i$$ are unknowns). 

