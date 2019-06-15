---
layout: post
date: 2019-6-8
title: Eigenvalues and Eigenvectors
---

<u>Eigenvectors</u>: The *non-zero* vector  $$\mathbf x$$  s.t.$$A\mathbf x$$ Parallel to $$\mathbf x$$. That is, $$A\mathbf x$$ is a multiple of $$\mathbf x$$, $$A\mathbf x=\lambda \mathbf x$$. These vectors won't be many. The $$\lambda$$ is the <u>Eigenvalue</u>. It can be negative and zero. 

### Zero Eigenvalue

One thing that can be sure is that singular matrix $$A$$, even it's not square, will always have eigenvalue 0. In the special case where the matrix is not full column rank, we will have non-zero eigenvector with zero eigenvalue. This will be explained later in singular value.

If the matrix is square and singular. Then 

$$
\#\ of\ \lambda=0=n-r
$$

The number of zero eigenvalues are equal to (at least, because there're can be equal eigenvalues, but the number of eigenvectors are) the dimension of the null space $$N(A)$$, i.e., # of free variables. Remember null space is all $$\mathbf x$$ s.t.

$$
A\mathbf x=0
$$

If there're two free variables, then $$\mathbf x=c_1\mathbf x_1+c_2\mathbf x_2$$ and 

$$
A\mathbf x_1=0;\ A\mathbf x_2=0
$$

This suggests that there're $$\lambda_1=\lambda_2=0$$ corresponding to eigenvector $$\mathbf {x_1,x_2}$$ s.t.

$$
A\mathbf x_1=\lambda_1\mathbf x_1\\
A\mathbf x_2=\lambda_2\mathbf x_2
$$

### Identity Matrix

The Identity matrix has all vectors as eigenvectors, because $$\lambda=1$$ is an eigenvalue, then:

$$
(A-1I)\mathbf{x}=\begin{bmatrix}
0 & ... & ...\\
...&0&...\\
...&...&0\\
\end{bmatrix}\mathbf{x}
$$

will give a all zero matrix. Any vectors having same dimension as # of cols will make this equation true and thus are eigenvectors. 

### Examples

Now let's look at the projection matrix $$P$$ which projects a vector $$\mathbf b$$ onto a plane. The projected vector $$\mathbf p=P\mathbf b$$ is (generally) not an eigenvector because it is not at the same direction as the original vector. One exception is that $$\mathbf b$$ is already on the plane. Then we no longer need to project and $$P=I$$ in this case. Then in this case any vectors in the plane is one of the eigenvector of $$P$$, with eigenvalue $$\lambda$$ equal to 1. Another eigenvector is any vectors $$\mathbf e$$ that is perpendicular to the plane, then its projection will be $$\mathbf 0$$, with $$\lambda=0$$. 



Let's look at another example, a permutation matrix:

$$
A=\begin{bmatrix}
0 & 1\\
1 & 0 
\end{bmatrix}
$$

A permutation matrix is switching rows(or columns if you want) of a vector. What vector will stay the same if we switch its row 1 and row? It is when 

$$
\mathbf x_1=\begin{bmatrix}
1\\
1
\end{bmatrix},\lambda=1
$$

And the corresponding eigenvalue is 1.  Another possibility is 

$$
\mathbf x_2=\begin{bmatrix}
1\\
-1
\end{bmatrix},\lambda=-1
$$

You may notice that any constant times $$\mathbf x_1$$ or $$\mathbf x_2$$ will also work. This is true. In fact, they are <u>basis</u> of the eigenvectors, we have a line of eigenvectors. But note that eigenvalue is not changed for $$\mathbf x_1$$ and $$\mathbf x_2$$ even they are multiplied by constants. 



One neat fact is that sum of eigenvalues $$\lambda$$'s is equal to the matrix's sum of diagonals. So on the $$A$$ as permutation matrix above, the sum of eigenvalues are equal to 0. 

## How to solve Ax=$$\lambda x$$

Rewrite it into

$$
(A-\lambda I)\mathbf x=0
$$

And we are interested in non-zero eigenvector. To make $$\mathbf x$$ non-zero, we need the matrix $$(A-\lambda I)$$ to be singular, or have free columns to be exact. In this case $$\det (A-\lambda I)=0$$. Then we can find $$\lambda$$ first, and then find $$\mathbf x$$. For example, let's find the eigenvalues and eigenvectors for 

$$
A=\begin{bmatrix}
3 & 1\\
1 & 3
\end{bmatrix}
$$

Then,

$$
A-\lambda I=\begin{bmatrix}
3-\lambda & 1\\
1 & 3-\lambda
\end{bmatrix}\\
\Rightarrow\\
\det A-\lambda I=(3-\lambda)^2-1=0\\
\lambda^2-6\lambda+8=0\\
\lambda_1=4,\lambda_2=2
$$

Before we continue, it's important to note the equation

$$
\begin{align}
\lambda^2-6\lambda+8&=0\\
\Leftrightarrow\\
\lambda^2-\mathrm{trace}(A)\cdot\lambda&+\det A=0
\end{align}
$$

And we know any such functions can be factored into:

$$
(\lambda-\lambda_1)(\lambda-\lambda_2)...=0
$$

The constant left on the very right is equal to the product of all eigenvalues. And you may guess the <u>product of all eigenvectors equal to the determinant</u>, that's in fact true. Knowing there're always eigenvalues even though it's zero gives us the following equation:

$$
\det(A-\lambda I)=(\lambda-\lambda_1)(\lambda-\lambda_2)..\\
$$

Set $$\lambda=0$$ gives us the desired result. 

Back to finding eigenvectors. For each eigenvalue we find its corresponding eigenvector by substitution,

$$
\begin{bmatrix}
-1 & 1\\
1 & -1
\end{bmatrix}\begin{bmatrix}
x_1\\
x_2
\end{bmatrix}=\mathbf 0\\
\Rightarrow\\
\lambda_1=4\sim \mathbf x_1=\begin{bmatrix}
1\\
1
\end{bmatrix}
$$

And,

$$
\begin{bmatrix}
1 & 1\\
1 & 1
\end{bmatrix}\begin{bmatrix}
x_1\\
x_2
\end{bmatrix}=\mathbf 0\\
\Rightarrow\\
\lambda_2=2\sim \mathbf x_2=\begin{bmatrix}
1\\
-1
\end{bmatrix}
$$

One useful observation from this, comparing to the permutation matrix above, is that we add 3 to each diagonals there, we got our eigenvalues added 3 as well, and eigenvectors are not changed. So what's happened is

$$
A\mathbf x=\lambda \mathbf x\\
\Rightarrow\\
(A+3I)\mathbf x=\lambda\mathbf x+3\mathbf x=(\lambda+3)\mathbf x
$$

### Complex Eigenvalues

Let's have another example

$$
Q=\begin{bmatrix}
0 & -1\\
1 & 0
\end{bmatrix}
$$

This matrix rotates all vectors counterclockwise 90 degrees. If you imagine, there shall not be any vectors s.t. $$Q\mathbf x$$ will still be parallel to the original vector $$\mathbf x$$ because it rotates the vector. But things can still work out. 

$$
\det(Q-\lambda I)=\begin{vmatrix}
-\lambda & -1\\
1 & -\lambda
\end{vmatrix}=\lambda^2+1=0\\
\Rightarrow\\
\lambda_1=i,\ \lambda_2=-i
$$

These two eigenvalues are complex number, and they are complex conjugate of each other, that is, their real parts are the same (zero) and imaginary part has different signs. In general, when we have symmetric matrix or close to symmetric, we will have real eigenvalues. But in this case when the matrix $$Q$$ is way far from symmetric, it rotates the vector, we will have complex eigenvalues. 

### Triangular Matrix

Let 

$$
A=\begin{bmatrix}
3 & 1\\
0 & 3
\end{bmatrix}
$$

Then for $$\det (A-\lambda I)$$ will lead to

$$
(3-\lambda)^2=0\\
\Rightarrow\\
\lambda_1=\lambda_2=3
$$

Then

$$
A-\lambda I =\begin{bmatrix}
0 & 1\\
0 & 0
\end{bmatrix}
$$

If we try to solve $$(A-\lambda I)\mathbf x$$, we will only have one eigenvector basis:

$$
\begin{bmatrix}
0 & 1\\
0 & 0
\end{bmatrix}\mathbf x=0\\
\mathbf x_1=\begin{bmatrix}
1\\
0
\end{bmatrix}
$$
