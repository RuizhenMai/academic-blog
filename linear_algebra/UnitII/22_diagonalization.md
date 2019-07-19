---
layout: post
title: Diagonalization and Powers of A
date: 2019-6-9
---

## A=$$S^{-1}\Lambda S$$

Diagonalize a matrix is, (or the other way around)

$$
\Lambda=S^{-1}AS\tag{1}
$$

Suppose we have $$n$$ independent eigenvectors, and we put them into the columns matrix $$S$$. So let's just call this matrix the <u>eigenvector matrix</u>. What happen we do $$AS$$? ($$\lambda$$ is the eigenvalue)

$$
AS=A\begin{bmatrix}
\mathbf {x_1 x_2...} \\  
\end{bmatrix}=\begin{bmatrix}
\lambda_1 \mathbf {x_1} \lambda_2 \mathbf{x_2...} \\  
\end{bmatrix}=\underbrace{\begin{bmatrix}
\mathbf {x_1} &\mathbf{x_2...} \\  
\end{bmatrix}}_{S}\underbrace{\begin{bmatrix}
\lambda_1&0&...\\ 
0&\lambda_2&...\\
...&...&...
\end{bmatrix}}_{\Lambda}
$$

And we call the matrix filled with eigenvalues the <u>eigenvalue matrix</u>. What we have right now is 

$$
AS=S\Lambda
$$

Since we have $$n$$ independent eigenvalues, we can invert the matrix $$S$$, writing it to the right hand side 

$$
A=S\Lambda S^{-1}
$$

Still, it's possible that there're some small number of matrices that do not have independent eigenvalues, as mentioned in the end of the [last note](./21_eigenvalues_and_eigenvectors.md). 



### Square eigenvalues

If $$A\mathbf x=\lambda\mathbf x$$, then 

$$
A\mathbf x=\lambda A\mathbf x=\lambda^2\mathbf x
$$

This is saying if the matrix is squared, the eigenvalues will get squared as well but the eigenvectors remain. We can also use the factorization learned above

$$
A^2=S\Lambda S^{-1}S\Lambda S^{-1}=S\Lambda^2 S^{-1}
$$

This is true for any kth power. 

Right now we can say $$A$$ is sure to be diagonalizable if it has all the $$\lambda$$'s different. But same $$\lambda$$ does not mean the matrix is not diagonalizable. 



### Difference Equation $$u_{k+1}=Au_k$$

Let's have a difference equation $$u_{k+1}=Au_k$$, and rewrite it into

$$
\begin{align}
u_k&=A^ku_0\\
\end{align}
$$

If we can, somehow, write $$u_0$$ into a combinations of $$A$$'s eigenvectors, then 

$$
u_0=c_1\mathbf x_1+c_2\mathbf x_2+...+c_n\mathbf x_n\tag{2}
$$

And:

$$
\begin{align}
u_k&=A^ku_0\\
&=c_1\lambda_1^k\mathbf x_1+c_2\lambda_2^k\mathbf x_2+...+c_n\lambda_n^k\mathbf x_n\\
&=S\Lambda^k\mathbf c
\end{align}
$$

In general, $c_1$ is essential to know about infinity, but other coefficients will pop up as we are solving (2). The scalar-form second equation is used more. 

## Fibonacci Sequence 

Fibonacci sequence is 

$$
F_{k+2}=F_{k+1}+F_k
$$

If we manually add another equations:

$$
\begin{array}{}
F_{k+2}&=F_{k+1}+F_k\\
F_{k+1}&=F_{k+1}
\end{array}
$$

We can rewrite this into matrix form:

$$
\begin{bmatrix}
F_{k+2}\\
F_{k+1}
\end{bmatrix}=\begin{bmatrix}
F_{k+1} & F_k\\
F_{k+1} & 0
\end{bmatrix}
$$

By letting $$\mathbf u_k=\begin{bmatrix}
F_{k+1}\\
F_{k}
\end{bmatrix}$$, we can:

$$
\mathbf u_{k+1}=\begin{bmatrix}
1 & 1\\
1 & 0
\end{bmatrix}\mathbf u_{k}
$$

Thus $$A=\begin{bmatrix}
1 & 1\\
1 & 0
\end{bmatrix}$$. The eigenvalue of the matrix is $$\displaystyle \lambda_1=\frac{1}{2}(1+\sqrt5), \lambda_2=\frac{1}{2}(1-\sqrt5)$$. And the eigenvectors are $$\mathbf x_1=\begin{bmatrix}
\lambda_1 \\
 1
\end{bmatrix},\mathbf x_2=\begin{bmatrix}
\lambda_2 \\
 1
\end{bmatrix} $$.  And we know $$\mathbf u_0=\begin{bmatrix}
1 \\
0
\end{bmatrix}$$. What's left is to find out the right combination $$c_1,\ c_2$$. Note we only have $$\lambda_1,\ \lambda_2$$ two eigenvalues, so we only have two terms from (2). 

$$
c_1\mathbf x_1+c_2\mathbf x_2=\begin{bmatrix}
1 \\
0
\end{bmatrix}
$$

The important idea here is that eigenvalues are dominating the growth. (Note that because $$\mathbf x_1,\mathbf x_2$$ are independent, they span the space, we can always find such combination $$c_1,c_2$$)

