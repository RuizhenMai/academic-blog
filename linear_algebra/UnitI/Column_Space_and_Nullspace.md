---
layout: post
title: Column Space and Nullspace
date: 2019-5-23
---

## Union and Intersection of Subspaces

Let's have abitrary two vector subspaces $$S$$ and $$T$$. The subspace $$S\cup T$$ is then the space that contains all vectors $$v\in S$$ and $$w\in T$$. But $$S\cup T$$ is not a vector space. Imagine $$S$$ and $$T$$ as two lines in $$\mathbb R^2$$ that go through origin, say $$x-axis$$ and $$y-axis$$. Then $$v=\left[\begin{matrix}
1\\
0
\end{matrix}\right], w=\left[\begin{matrix}
0\\
1
\end{matrix}\right]$$, but $$v+w=\left[\begin{matrix}
1\\
1
\end{matrix}\right]$$ is neither in $$S$$ nor $$T$$. 

But $$S\cap T$$ is a vector space. $$S\cap T = \min(S,T,S\cap T)$$, the new space will be always *smaller* than the old ones, therefore  the new space will always be vector spaces. If $$S=x-axis,T=y-axis$$, $$S\cap T=\mathbf{0}$$, zero vector is a vector space. This is true for whatever vector subspaces. {% include sidenote.html note='More formally, let $$t,u\in S\cap T$$, as $$t,u\in S\cap T$$, $$t,u\in S$$ and $$t,u\in T$$, as $$S$$ and $$T$$ are both vector spaces, we can perform any linear combinations on $$t,u$$, and thus $$S\cap T$$ is a vector space because $$t,u$$ are abitrary vectors in $$S\cap T$$' %} 

## Column Spaces Continued

Let 
$$
A=\left[\begin{matrix}
1 & 1 & 2\\
2 & 1 & 3\\
3 & 1 & 4\\
4 & 1 & 5
\end{matrix}\right]
$$
and we want to solve the system of equations $$A\mathbf{x}=\mathbf{b}$$. For what $$\mathbf b$$ there's a solution to this system? There's not always an answer to a system of equations, like in two-equation system, there's no answer to $$2x+2y=0, 2x+2y=1$$. To solve $$A\mathbf{x}=\mathbf{b}$$, $$\mathbf b$$ must be a linear combination of the columns of $$A$$. Remember a vector/matrix on the right of $$A$$ is manipulating its columns. Namely, $$\mathbf b$$ must be in $$A$$'s column space(by definition of column space). 

A preview of independence: here the third column of $$A$$ is equal to the sum of the first one and the second one. We say this column is dependent, and this column will not play a role in contrusting the column space of $$A$$(you can image this column lies on the plane spanned by $$\left[\begin{matrix}
1\\
2\\
3\\
4\\
\end{matrix}\right]$$ and $$\left[\begin{matrix}
1\\
1\\
1\\
1
\end{matrix}\right]$$). And thus the $$C(A)$$ is plane in $$\mathbb R^4$$.

## Nullspace

The definition of *nullspace* of a matrix $$A$$ is the collection of all vectors $$\mathbf x$$ s.t. $$A\mathbf x=\mathbf 0$$. Let $$A$$ is same as above, the equation will be:

$$
\left[\begin{matrix}
1 & 1 & 2\\
2 & 1 & 3\\
3 & 1 & 4\\
4 & 1 & 5
\end{matrix}\right]\left[\begin{matrix}
x_1\\
x_2\\
x_3
\end{matrix}\right]=\left[\begin{matrix}
0\\
0\\
0\\
0
\end{matrix}\right]
$$

a simple case of $$\mathbb x$$ is just make it all zeros. But here it can be more than just zeros. We can also solve the equation with $$\mathbb x= \left[\begin{matrix}
1\\
1\\
-1
\end{matrix}\right]$$ and $$\mathbb x=\left[\begin{matrix}
2\\
2\\
-2
\end{matrix}\right]$$, in fact, $$c\left[\begin{matrix}
1\\
1\\
-1
\end{matrix}\right]$$ will work. And this is the nullspace of $$A$$, a line in $$\mathbb R^3$$. We often write $$N(A)$$ as the nullspace of $$A$$. 

Note that nullspace's dimension is dependent on the row size of $$A$$. $$A$$ is $$4\times 3$$ here. But the column space is related to column size which is 4.

### Other values of b

Why we call the solution to $$A\mathbf x=\mathbf b$$ when $$\mathbf b=\mathbf 0$$ as a *space*? Let's make $$\mathbf b=\left[\begin{matrix}
1\\
2\\
3\\
4\\
\end{matrix}\right]$$. A solution will be $$\mathbf x=\left[\begin{matrix}
1\\
0\\
0
\end{matrix}\right]$$, and we can also do $$\mathbf x=\left[\begin{matrix}
0\\
-1\\
1
\end{matrix}\right]$$ but we cannot do all zeros. The point we cannot make $$\mathbf x$$ all zeros make these solutions not a space. The solutions to this $$\mathbf b$$ is a plane that does not go through origin in $$\mathbb R^3$$.  

