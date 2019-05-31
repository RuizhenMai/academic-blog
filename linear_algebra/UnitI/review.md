---
layout: post
title: Review
date: 2019-5-31
---

1. Do the invertible matrices form a subspace of the vector space by all $$5\times 5$$ matrices?

   First remember for a matrix to be invertible, it has to be a square matrix. After [lec. 8](./solving_ax_eq_b), in fact an invertible matrix must be in full rank. In full rank means a square matrix has no dependency in rows or columns. Back to the question, the answer is no. Let's use a $$2\times 2$$ example to illustrate:

   $$
   A=\begin{bmatrix}
   1 & 0\\
   0 & 1
   \end{bmatrix},B=\begin{bmatrix}
   0 & 1\\
   1 & 0
   \end{bmatrix},A+B=\begin{bmatrix}
   1 & 1\\
   1 & 1
   \end{bmatrix}
   $$

   Both $$A$$ and $$B$$ are $$2\times 2$$ invertible matrices but their sum is not. We can form similar cases in $$5\times 5$$ matrices. Inversely, do the singular matrices form a subspace of the vector space by all $$5\times 5$$ matrices? The answer is no again:

   $$
   A=\begin{bmatrix}
   -1 & 0\\
   0 & 0
   \end{bmatrix},B=\begin{bmatrix}
   1 & 1\\
   1 & 0
   \end{bmatrix},A+B=\begin{bmatrix}
   0 & 1\\
   1 & 0
   \end{bmatrix}
   $$

2. Find the basis of null space for the following matrix $$B$$ without multiplying the matrix out
   
   $$
   B=CD=\begin{bmatrix}
   1 & 1 & 0\\
   0 & 1 & 0\\
   1 & 0 & 1
   \end{bmatrix}\begin{bmatrix}
   1 & 0 & -1 & 2\\
   0 & 1 & 1 & -1\\
   0 & 0 & 0 & 0
   \end{bmatrix}
   $$
   
   In fact it's not hard to multiply these two matrices, from $$C$$ we see the answer is just one row adding another. But one finding is important. $$C$$ is an invertible matrix. So it has $$C^{-1}C=0$$. Then we have the following:

   $$
   \begin{align}
   B\mathbf x&=0\\
   CD\mathbf x&=\mathbf 0\\
   C^{-1} CD\mathbf x&=C^{-1}\mathbf 0\\
   D\mathbf x&=\mathbf 0
   \end{align}
   $$

   That is, $$N(B)=N(D)$$. The nullspace of $$C$$ does not affect the nullspace of $$D$$ at all. And $$D$$ is already in rref, the third and fourth column is just free variables, so the basis is

   $$
   \begin{bmatrix}
   1\\
   -1\\
   1\\
   0\\
   \end{bmatrix} ,\begin{bmatrix}
   -2\\
   1\\
   0\\
   1\\
   \end{bmatrix}
   $$

3. True or False: $$A$$ and $$-A$$ share the same four subspaces:

   Yes. A subspace always carry a constant in front of it like $$c\begin{bmatrix}
   1\\
   1\\
   -1\\
   \end{bmatrix}$$ to extend the basis to be a space. If $$\mathbf v$$ is in the subspace, so does $$-\mathbf v$$.  

4. True or False: If $$A$$ and $$B$$ share the same four subspaces, is it true that $$A=cB$$. 

   No. An example will be 

   $$
   A=\begin{bmatrix}
   1 & 0 & 0\\
   0 & 1 & 0\\
   0 & 0 & 1
   \end{bmatrix},B=\begin{bmatrix}
   1 & 0 & 0\\
   0 & 2 & 0\\
   0 & 0 & 1
   \end{bmatrix}
   $$
   
   They are both invertible matrices so the nullspace and left nullspace are just zero. And they share the column and row space. One open question you might ask is if $$A,B$$ have same four subspaces, what property do they? (I don't know the anwer)

