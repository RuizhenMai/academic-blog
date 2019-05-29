---
layout: post
title: Factorization into A = LU
date: 2019-5-22
---

## Inverses Continued

### Useful Facts:

Inverses:

$$
\begin{aligned}
(AB)B^{-1}A^{-1}&=I\\
(AB)^{-1}&=B^{-1}A^{-1}
\end{aligned}
$$

Transposes:

$$
(AB)^T=B^TA^T
$$

because

$$
((AB)^{T})_{ij}=(AB)_{ji}=\sum_{k=1}^{n}a_{jk}b_{ki}
$$

when we transpose a matrix the row and column are switched, and

$$
(B^{T}A^{T})_{ij}=\sum_{k=1}^n B^T_{ik} A^T_{kj}=\sum_{k=1}^n b_{ki} a_{jk}
$$

Therefore we have

$$
\begin{align}
AA^{-1}&=I\\
(AA^{-1})^{T}&=I^{T}\\
(A^{-1})^{T}A^{T}&=I\\
\end{align}
$$

## Factorization into A = LU

$$U$$ is same as previously defined as the upper trianular matrix([lecture 2](./Elimination_of_Matrices)) obtained after row eliminations on $$A$$, that is

$$
EA=U
$$

where $$E$$ is the elimination matrix. Multiply both side of $$(1)$$ to theft by $$E^{-1}$$. We will have $$A=E^{-1}U$$. $$E^{-1}$$ is the $$L$$ we are looking for today. A simple example:

$$
\begin{aligned}
\begin{matrix}
E_{21}\\
\begin{bmatrix}
1 & 0\\
-4 & 1
\end{bmatrix}
\end{matrix}
\begin{matrix}
A\\
\begin{bmatrix}
2 & 1\\
8 & 7
\end{bmatrix}
\end{matrix}
& =
\begin{matrix}
U\\
\begin{bmatrix}
2 & 1\\
0 & 3
\end{bmatrix}
\end{matrix}
\end{aligned}
$$

In this $$2\times2$$ case, $$L$$ is easily obtained by "canceling" the matrix $$E_{21}$$ ([lecture 2](./Elimination_of_Matrices)). And we will see it's called $$L$$ because all of its items are in the lower triangular part, as opposed to $$U$$.

$$
\begin{aligned}
\begin{matrix}
A\\
\begin{bmatrix}
2 & 1\\
8 & 7
\end{bmatrix}
\end{matrix}
& =
\begin{matrix}
L\\
\begin{bmatrix}
1 & 0\\
4 & 1
\end{bmatrix}
\end{matrix}\begin{matrix}U\\\begin{bmatrix}
2 & 1\\
0 & 3
\end{bmatrix}
\end{matrix}
\end{aligned}
$$

Sometimes $$U$$ is further reduced into a diagonal matrix $$D$$ with a $$U'$$(not important). 

To see why $$U$$ is preferred to $$E$$, we need a $$3\times3$$ example. Suppose 

$$
\begin{aligned}
E_{32} \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ E_{21} \ \ \ \ \ \ \  & \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ E\\
\left[\begin{matrix}
1 & 0 & 0\\
0 & 1 & 0\\
0 & -5 & 1
\end{matrix}\right]\left[\begin{matrix}
1 & 0 & 0\\
-2 & 1 & 0\\
0 & 0 & 1
\end{matrix}\right] & =\left[\begin{matrix}
1 & 0 & 0\\
-2 & 1 & 0\\
10 & -5 & 1
\end{matrix}\right]
\end{aligned}
$$

The 10 in the lower left corner arises because we subtracted twice the first row from the second row, then subtracted five times the new second row from the third. But we do not want that to be there. Here $$L=E^{-1}=E_{21}^{-1}E_{32}^{-1}$$

$$
\begin{aligned}
E^{-1}_{21} \ \ \ \ \ \ \ \ \ \ \ \ E^{-1}_{32} \ \ \ \ \ \ \  & \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ L\\
\left[\begin{matrix}
1 & 0 & 0\\
2 & 1 & 0\\
0 & 0 & 1
\end{matrix}\right]\left[\begin{matrix}
1 & 0 & 0\\
0 & 1 & 0\\
0 & 5 & 1
\end{matrix}\right] & =\left[\begin{matrix}
1 & 0 & 0\\
2 & 1 & 0\\
0 & 5 & 1
\end{matrix}\right]\\
 & 
\end{aligned}
$$

The 10 is gone and the matrix $$L$$ is much cleaner and easier to calculate than $$E$$.

## How Many operations on eliminating n x n A

We have $$n$$ rows and $$n$$ columns. A typical elimination will involve row mulipled by a constant and substracted by another row. Since there're $$n$$ elements in a row, typically a row multiplied by a constant and substracted by a row will take $$n$$ operations(should be $$2n$$ but we omit the constant for now). And since we have $$n$$ rows, eliminating one column, say the leftmost column, on a matrix will take $$n^2$$ operations. Remember eliminating one column means make all number in this colulmn under the pivot to be come zero. And this operates on the lower triangle of the matrix. In general, we need 

$$
n^2+(n-1)^2+...+2^2+1^2=\sum_{i=1}^ni^2\approx\int_0^nx^2\,dx=\frac{1}{3}n^3
$$

operations to eliminate $$A$$ to obtain $$U$$. And we can store the operations during the process of eliminating, then around $$n^{3}$$ operations are needed to factorize $$A$$ into $$LU$$.

## Row Exchanges

As mentioned in [lecture 2](./Elimination_of_Matrices), permutation matrices are matrices that just change the order of rows. For e.g.

$$
P_{12}=\left[\begin{matrix}
0 & 1 & 0\\
1 & 0 & 0\\
0 & 0 & 1
\end{matrix}\right]
$$

switch row 1 and row 2. There are total $$n!$$ permutation matrices for $$n\times n$$ matrix(including the one leaves all rows unchanged). And also note that for permutation matrices, $$P^{-1}=P^T$$. This means that to get back to the stage before being permutated is equal to doing a transposed permutation. 

(In fact I think the notation $$P_{12}$$ is bad, $$P_{213}$$ is much better which refers to order of row 1 and 2 switched and row 3 unchanged)