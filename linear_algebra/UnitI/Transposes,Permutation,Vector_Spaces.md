---
layout: post
title: Transposes, Permutation, Vector Spaces
date: 2019-5-23
---

### PA=LU

To extend and finish the factorization of $$A=LU$$. As matrix $$A$$ may not be in the ideal form of all pivots are non-zero, we need to do $$PA$$ to exchange rows into their pivot positions. 

## Transposes and Symmetry

We know that transposing a matrix is switching its columns with rows, that is, $$A_{ij}^T$$  is $$A_{ji}$$. A <u>symmetric matrix</u> is first a square matrix and $$S_{ij}=S_{ji}, \forall i,j$$ or equivalently $$S^\top =S$$. For example,

$$
S=\left[\begin{matrix}
3 & 1 & 7\\
1 & 2 & 9\\
7 & 9 & 4
\end{matrix}\right]
$$

is a symmetric matrix. 

#### Prop 1. For any given rectangular matrix $$R$$, $$R^TR$$ is always symmetric.

Let $$R=\left[\begin{matrix}
1 & 2 & 4\\
3 & 3 & 1
\end{matrix}\right]$$, then 

$$
R^TR=\left[\begin{matrix}
1 & 3\\
2 & 3\\
4 & 1
\end{matrix}\right]\left[\begin{matrix}
1 & 2 & 4\\
3 & 3 & 1
\end{matrix}\right] =\left[\begin{matrix}
10 & 11 & 7\\
11 & 13 & 11\\
7 & 11 & 17
\end{matrix}\right]
$$

We see for this particular $$R$$, $$(R^TR)^T=R^TR$$. More formally, we can use the lemma that $$(AB)^T=B^TA^T$$ from [lecture 4](./Factorization_into_A_eq_LU) and $$(R^TR)^T=R^T(R^T)^T=R^TR$$ and we can conclude $$R^TR$$ is always symmetric. Same for $$RR^T$$. 

## Vector Spaces

While we do not list the formal definition of vector spaces and the requirement a space should follow here, an intuitive definition is that a *vector space* is any space we can perform linear combinations on vectors. Linear combinations are we can add vectors, multiply a vector with a constant. Also remember we also need to be able to multiply a vector with 0. 

The most common vector space is $$\mathbb{R}^2$$, the set of (column) vectors with two real numbers. Examples are $$\left[\begin{matrix}
2\\
-1
\end{matrix}\right]\left[\begin{matrix}
0\\
0
\end{matrix}\right]\left[\begin{matrix}
\pi \\
e
\end{matrix}\right]$$. Another exmaple is $$\mathbb{R}^n$$. 

### Subspaces

A vector space that is contained inside another vector space is a $$subspace$$ of that space. Any lines pass through origin (Note vectors start from origin) in $$\mathbb{R}^2$$ is a subspace of $$\mathbb{R}^2$$. Lines that do not pass through origin are not because when you multiply a vector on this line with $$0$$ it becomes a zero vector, and this is not on that line. 

The subspaces of $$\mathbb R^2$$ are:

1. all of $$\mathbb R^2$$
2. any line through origin
3. the zero vector itself($$Z$$)

The subspaces of $$\mathbb R^3$$ are:

1. all of $$\mathbb R^3$$
2. any planes through origin
3. any lines through origin
4. zero vector

### Column Space

The space formed by the columns of a matrix is the column space of this vector. Let 

$$
A=\left[\begin{matrix}
1 & 3\\
2 & 3\\
4 & 1
\end{matrix}\right]
$$

the column space of $$A$$, $$C(A)$$ is the plane containing vector $$\left[\begin{matrix}
1\\
2\\
4
\end{matrix}\right]$$ and $$\left[\begin{matrix}
3\\
3\\
1
\end{matrix}\right]$$, and undoubtedly this plane goes through origin.