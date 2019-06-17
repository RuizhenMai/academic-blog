---
layout: post
title: Symmetric Matrices and Positive Definiteness
date: 2019-6-12
---

Symmetric matrices are good – their eigenvalues are real and each has a complete set of orthonormal eigenvectors. Positive definite matrices are even better. 

A real symmetric (square) matrix $$A=A^\top$$  

- The eigenvalues are REAL
- The eigenvectors can be chosen perpendicularly 



And a symmetric matrix $$A$$ can be factored into

$$
A=Q\Lambda Q^{-1}=Q\Lambda Q^\top
$$

where $$Q$$ is an orthogonal (orthonormal if A is not square) matrix. 

### Real Eigenvalues

Why all the eigenvalues are real? Suppose $$A\mathbf x=\lambda\mathbf x$$, and suppose there're complex eigenvalues and complex eigenvectors, we can take the conjugate of all components in the equation, this leads to $$\overline A\overline{\mathbf x}=\overline \lambda \overline{\mathbf x}$$. Since $$A$$ is a real matrix, $$A=\overline A$$, this gives

$$
A\overline{\mathbf x}=\overline \lambda \overline{\mathbf x}\tag{1}
$$

Now let's transpose e.q. (1), we get $$\overline{\mathbf x}^\top A^\top=\overline{\mathbf x}^\top \overline \lambda ^\top$$. Since $$A$$ is symmetric, $$A=A^\top$$. $$\overline\lambda$$ is just a constant so $$\overline \lambda=\overline\lambda^\top$$Then multiplying both side by $$\mathbf x$$ to the right:

$$
\overline{\mathbf x}^\top A\mathbf x=\overline{\mathbf x}^\top \overline \lambda\mathbf x\tag{2}
$$

And multiply both side of $$A\mathbf x=\lambda\mathbf x$$ by $$\overline{\mathbf x}^\top$$to the left:

$$
\overline{\mathbf x}^\top A\mathbf x=\overline{\mathbf x}^\top\lambda\mathbf x\tag{3}
$$

Now we see the left-hand side of (2) and (3) are equal, therefore, as long as $$\overline{\mathbf x}^\top\mathbf x\neq 0$$, 

$$
\lambda=\overline \lambda
$$

then $$\lambda$$ is real. Why $$\overline{\mathbf x}^\top\mathbf x\neq 0$$? First and foremost, an eigenvector $$\mathbf x$$ is non-zero. Then 

$$
\overline{\mathbf x}^\top\mathbf x=\begin{bmatrix}
\overline x_1 & \overline x_2&... &\overline x_n\\
\end{bmatrix}\begin{bmatrix}
 x_1 \\
 x_2 \\
 \vdots \\
 x_n
\end{bmatrix}=\vert x_1\vert^2+...\vert x_n\vert^2\geq0
$$

Since $$\mathbf x$$ is not equal to zero vector, then $$\overline{\mathbf x}^\top\mathbf x>0$$. If $$A$$ is not a real matrix, the proof follows the same pattern because $$A=\overline A^\top$$. 

### Information about eigenvalues

For very large matrices like $$50\times 50$$, it's very impractical to compute eigenvalues using the way we learned. One information we can learn is 

$$
\mathrm{number\ of\ positive\ pivots=number\ of\ positive\ eigenvalues}
$$

Let's bring up the definition for pivots again. It's the first non-zero value in each row in the *row-echelon* form, not the reduced one (require the pivots to be 1 and entries above the pivots should be 0). 

Also, from [note 21](../UnitII/21_eigenvalues_and_eigenvectors), 

$$
\mathrm{number\ of\ free\ variables=number\ of\ zero\ eigenvalues}
$$


## Positive Definite Matrices

Positive Definite Matrices is technically Positive Definite symmetric Matrices. Symmetric matrices are good. <u>A positive definite matrix is a symmetric matrix for which all of its eigenvalues are positive</u>. A good way to check this is to see if all of its pivots are positive. 

One consequence from all eigenvalues are positive is the determinant must also be positive. But the reverse is not true. Positive determinant does not bring to all positive eigenvalues. 