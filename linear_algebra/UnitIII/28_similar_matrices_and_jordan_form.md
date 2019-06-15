---
layout: post
title: Similar Matrices and Jordan Form
date: 2019-6-15
---

The eigenvalues of the inverse matrix $$A^{-1}$$ is its inverses, because:

$$
\vert A\vert=\lambda_1*\lambda_2*...
$$

And from determinant's property, we know the determinant of $$A^{-1}$$ is the inverses of the determinant of $$A$$

$$
\vert A^{-1}\vert=\frac{1}{\vert A\vert}=\frac{1}{\lambda_1*\lambda_2*...}=\frac{1}{\lambda_1}*\frac{1}{\lambda_2}*...
$$

What comes from this is <u>if I know the matrix $$A$$ is positive definite then $$A^{-1}$$ will also be positive definite.</u> 

Another useful property is <u>if $$A,B$$ are positive definite, then $$A+B$$ is also positive definite.</u> We can use the property learned last note to prove this $$\mathbf x^\top A\mathbf x>0$$, we have:

$$
\mathbf x^\top A\mathbf x>0\\
\mathbf x^\top B\mathbf x>0
$$

Then clearly

$$
\mathbf x^\top (A+B)\mathbf x>0
$$

Now redefine $$A$$ as arbitrary rectangular $$m\times n$$ matrix. Then $$A^\top A$$ is square and symmetric. It is a positive semidefinite matrix because:

$$
\mathbf x^\top A^\top A\mathbf x=(A\mathbf x)^\top(A\mathbf x)=\Vert A\mathbf x\Vert^2\geq0
$$

If we want it to be positive definite, to get rid of the possibility that the length of vector $$A\mathbf x$$ is zero, we just need to get rid of the possibility that except $$\mathbf x$$ is length zero. So we need full column rank fo $$A$$. That's the requirement how $$A^\top A$$ is invertible. 



## Similar Matrices

Note we're no longer expecting symmetric matrices here. But still use <u>square</u> matrices. Square matrices $$A$$ and $$B$$ are similar if and only if there exists an invertible matrix $$M$$ s.t.

$$
B=M^{-1}AM
$$

One example is 

$$
\Lambda=S^{-1}AS
$$

What's special about similar matrices? They have same eigenvalues. Why?

$$
\begin{align}
A\mathbf x&=\lambda \mathbf x\\
AMM^{-1}\mathbf x&=\lambda \mathbf x\\
M^{-1}AMM^{-1}\mathbf x&=\lambda M^{-1}\mathbf x\\
BM^{-1}\mathbf x&=\lambda M^{-1}\mathbf x\\
B\mathbf v&=\lambda\mathbf v\\
\end{align}
$$

This finishes the proof. And of course, the eigenvectors do not stay the same. The new eigenvectors are $$M^{-1}$$ times the eigenvectors of $$A$$. 

### Bad Cases

There're two cases if we have two eigenvalues same. One is we have a diagonal matrix, i.e., some number times the identity matrix, this matrix won't be changed at all for $$M^{-1}AM$$. So this kind of matrix has a small family. The other is just the rest. 