---
layout: post
title: Orthogonal Vectors and Subspaces
date: 2019-6-1
---

## Orthogonal

<u>Orthogonal vectors</u>: two vectors are orthogonal (perpendicular) if the angle between them is 90˚ angle; or their inner product is 0:

$$
\mathbf x^\top \mathbf y=0\tag{1}
$$

If you want it more algebraically, we can use Pythagoras theorem:

$$
||\mathbf x||^2+||\mathbf y||^2=||\mathbf {x+y}||^2
$$

Note that this can be converted to e.q. (1):

$$
\begin{align}
||\mathbf x||^2+||\mathbf y||^2&=||\mathbf {x+y}||^2\\
\mathbf x^\top\mathbf x+\mathbf y^\top\mathbf y&=(\mathbf {x+y})^\top(\mathbf {x+y})\\
...&=\mathbf x^\top\mathbf x+\mathbf x^\top\mathbf y+\mathbf y^\top\mathbf x+\mathbf y^\top\mathbf y\\
\mathbf 0&=\mathbf x^\top\mathbf y+\mathbf y^\top\mathbf x\\
\mathbf 0&=2\mathbf x^\top\mathbf y\\
\mathbf x^\top\mathbf y&=\mathbf 0\\
\end{align}
$$

Another takeaway is zero vector is orthogonal to any vectors. 

<u>Orthogonal Subspaces</u>: subspace $$S$$ is orthogonal to subspace $$T$$ means every vector $$v\in S$$ is orthogonal to every vector $$u\in T$$. 

#### Prop.1: Row space is orthogonal to nullspace

This comes straightly from $$A\mathbf x=\mathbf 0$$:

$$
A\mathbf x=\mathbf 0\Leftrightarrow \begin{bmatrix}
row\ 1\ of\ A\\
row\ 2\ of\ A\\
row\ 3\ of\ A\\
...\\
row\ m\ of\ A
\end{bmatrix}\begin{bmatrix}
\\
 \\
x\\
 \\
 \\
\end{bmatrix}=\begin{bmatrix}
0\\
0\\
0\\
...\\
0\\
\end{bmatrix}
$$

Use the traditional matrix multiplication perspective, every row of $$A$$ is multiplying the whole $$\mathbf x$$ column vector:

$$
(row\ 1)^\top \mathbf x=0\\
(row\ 2)^\top \mathbf x=0\\
...\\
(row\ m)^\top \mathbf x=0\\
$$

From these we can easily obtain any combination of the row vectors times $$\mathbf x$$ is still 0:

$$
c_1(row\ 1)^\top \mathbf x=0\\
c_2(row\ 2)^\top \mathbf x=0\\
...\\
c_m(row\ m)^\top \mathbf x=0\\
[c_1(row\ 1)^\top+
c_2(row\ 2)^\top+...+
c_m(row\ m)^\top ]\mathbf x=0\\
$$

This finishes proving that the solution space $$\mathbf x$$ to 0 is orthogonal to any combination of row vectors, i.e., nullspace is orthogonal to the row space.

We say Row space and nullspace are <u>orthogonal complements</u> in $$\mathbb R^n$$

We know that for $$m\times n$$ matrix, 

$$
\dim N(A)+\dim R(A)=n
$$

Their dimensions are complementary and add up to $$n$$. In $$\mathbb R^3$$, if row space is just a line, then the nullspace is the plane that contains all vectors perpendicular to this line, not just some vectors.

## $A^\top A$

Due to measurement error, $$A\mathbf x=\mathbf b$$ is often unsolvable if $$m>n$$ (check if there's one by elimination). The next challenge will be to find a best possible solution for this kind of equations. The matrix $$A^\top A$$ will be crucial in them. What's good about $$A^\top A$$? It is square,  symmetric. And 

#### Prop. 2

$$
N(A^\top A)=N(A)
$$

This is easy to spot since 

$$
\begin{align}
A\mathbf x&=\mathbf 0\\
A^\top A\mathbf x&=\mathbf 0
\end{align}
$$

And from **Prop. 2**, the same nullspace will give us, first, same nullspace  dimension: $$\dim N(A^\top A)=\dim N(A)$$, and we know rank it's just $$n-dimension\ of\ nullspace$$. Therefore, the following is true

#### Prop. 3

$$
rank\ of\ A^\top A=rank\ of\ A
$$

What we know from these are the next proposition:

#### Prop. 4: $A^\top A$ is invertible if $A$ has independent columns, i.e., $r=n$, full column rank

This will be explained in the next lecture