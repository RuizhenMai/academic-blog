---
layout: post
title: Linear Transformation and their Matrices 
date: 2019-6-17
---

Projection is a linear transformation, for example. Its linear transformation $$T$$ is $$\mathbb R^2\rightarrow \mathbb R^2$$. Linear transformation can happen without any coordinates or matrices.

Rules for linear transformation:

- $$T(v+w)=T(v)+T(w)$$ <u></u>
- $$T(cv)=cT(v)$$ <u></u>

It's like what we can do with vectors. <u>Shifting a vector</u> $$v$$ by $$v+v_0$$ is <u>not</u> linear since $$T(2v)=2v+v_0$$ does not end up with $$2T(v)=2v+2v_0$$. <u>Taking a vector's norm is also not linear</u> since $$T(-2v)=2\Vert v\Vert$$. 

<u>In fact, all transformation produced by matrix are linear transformations</u>. 

$$
T(v)=Av\tag{1}
$$

This satisfies the rules above easily. Some easy matrices: 

- Flip a graph along x-axis: $$\begin{bmatrix}1 & 0\\0&-1 \end{bmatrix}$$
- Rotate a graph counterclockwise 90 degrees: $$\begin{bmatrix}0 &-1\\1&0 \end{bmatrix}$$

How much do we need to know about a transformation to know $$T(v)$$? We only need to know the effect of $$T(v_1), T(v_2),…,T(v_n)$$ for any input basis $$v_1,…,v_n$$. We do not need to know its effect to all vectors but only the basis. 



## Write a transformation into Matrix

In fact, all the things we need to write a transformation with matrix is 

- Basis for the input $$v_1,…v_n$$
- Basis for the output $$w_1,…w_m$$

Then a matrix with size $$m\times n$$, its numbers are, in fact $$T(v_1)=a_{11}w_1+a_{21}w_2+…+a_{m1}w_m$$ the a's are the elements in the matrix (more details in next lectures). Picking the right basis is important. The linear combination of the basis gives the <u>coordinates</u> $$(c_1,c_2,…,c_n)$$. But different bases give different coordinates. 

### Pick the good basis

Let's take projection as an example. If we want a projection in $$\mathbb R^2$$ that project the vectors into the 45 degrees line (but they are both in $$\mathbb R^2$$), if we use a regular basis (for input and output basis) $$\begin{bmatrix}1 & 0\\0&1 \end{bmatrix}$$, then the transformation matrix will be $$\begin{bmatrix}1/2 & 1/2\\1/2&1/2 \end{bmatrix}$$. But if we just pick the (it's like cheating but ok) 45 degree line and its perpendicular one as basis, then'll be left with $$\begin{bmatrix}1 & 0\\0&0 \end{bmatrix}$$ because we're like clearing the vector's y coordinates. 