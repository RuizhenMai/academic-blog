---
layout: post
title: Independence, Basis and Dimension
date: 2019-5-27
---

These notes formalize some concepts on spaces and dimensions of a subspace of a matrix. If you find any of them not intuitive, I suggest you to watch the video of this lecture. 

### Independence

Definition: vectors $$v_1,\ v_2,…,\ v_n$$ are independent if 

$$
c_1v_1+c_2v_2+...+c_nv_n=0
$$

is true only when $$c_1=c_2=…=c_n=0$$. This means that only the zero vector is the solution to $$A\mathbf x=\mathbf b$$ when $$v_1,…,v_n$$ constitute the columns of $$A$$.

### Span a space

Vectors $$v_1,\ v_2,…,v_n$$ span a space means the space consist of all linear combinations of these vectors. (These two expression are equivalent)

### Basis

A basis for a space $$S$$ is a sequence of vectors $$v_1,\ v_2,…,\ v_d$$ that has these properties:

1. They are independent
2. They span the space $$S$$ 

One basis for $$\mathbb R^3$$ is 

$$
\{\left[\begin{matrix}
1\\
0\\
0
\end{matrix}\right],\left[\begin{matrix}
0\\
1\\
0
\end{matrix}\right],\left[\begin{matrix}
0\\
0\\
1
\end{matrix}\right]\}
$$

they are independent of each other and span the whole $$\mathbb R^3$$. Clearly there are other bases, like multiply the above basis by two. In fact there're infinitely many bases for a space. But these bases share one thing in common: they all have same number of vectors. This number is the dimension of that space. Like $$\mathbb R^3$$ has dimension 3. There're exactly $$n$$ vectors in $$\mathbb R^n$$.

### Basis of a column space and nullspace

We use the new language spanning to describe the column space. Before we said the column space of a matrix $$A$$ is the linear combinations of its column. Here we say the columns of $$A$$ span $$C(A)$$. But these columns are not necessarily the basis of $$C(A)$$. When they are not independent, they are not the basis. This happens when $$n\geqslant m$$, the number of columns are greater or equal to the number of rows. For instance:

$$
A=\begin{bmatrix}
1 & 2 & 3 & 1\\
1 & 1 & 2 & 1\\
1 & 2 & 3 & 1
\end{bmatrix}
$$

c4 is the same as c1, and c3 is equal to c1+c2 in this matrix. So we only need the first two vectors to form the basis of $$C(A)$$.

One more thing is that we have discussed

$$
rank(A)=\#\ of\ pivot\ cols\ of\ A
$$

right now, 

$$
rank(A)=\#\ of\ pivot\ cols\ of\ A=dim\ C(A)
$$

The dimension of $$C(A)$$ is equal to how many pivot columns we have for $$A$$. And since 

$$
n-rank(A)=\#\ of\ free\ variables
$$

what's left after we subsract from the dimension of column space forms the null space, that is 

$$
n-rank(A)=\#\ of\ free\ variables=dim\ N(A)
$$
