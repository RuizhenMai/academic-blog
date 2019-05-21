---
layout: post
title: Multiplication and Inverse Matrices
date: 2019-5-21
---

## Review of Matrix Multiplication

### A Row $$\times$$ A Column

Let's have 

$$
AB=C
$$

where they are all matricies. If $$A$$ and $$B$$ are not square matricies, then let's assume $$A:M\times N$$ and $$B:N\times P$$. Then the dimenstion of $$C$$ will be $$M\times P$$.  Let $$c_{ij}$$ be the element at row $$i$$ and column $$j$$ in matrix $$C$$. Say we want to find $$c_{34}$$:

$$
\begin{aligned}
c_{34}&=(row\ 3\ of\ A)\cdot(column\ 4\ of\ B)\ \ Note:\ dot\ product\\
&=a_{31}b_{14}+a_{32}b_{24}+a_{33}b_{34}+...\\
&=\sum_{k=1}^{n}a_{3k}b_{k4}
\end{aligned}
$$

This is $$a\ Row\ of\ A\ \times\ a\ Column\ of\ B$$ 

### A Matrix $$\times$$ Columns

To build on this, let's think of multiplying two matricies. Each column in $$C$$ is equal to matrix $$A$$ times each column in $$B$$

$$
\begin{aligned}
B_{c1} \ B_{c2} \ B_{c3} \ \ \  & \ \ \ \ \ \ AB_{c1} \ AB_{c2} \ AB_{c3}\\
A\left[ \ \ \begin{matrix}
| &  & \\
| &  & \\
| &  & 
\end{matrix} \ \ \ \ \ \ \right] & =\left[ \ \ \begin{matrix}
| &  & \\
| &  & \\
| &  & 
\end{matrix} \ \ \ \ \ \ \ \ \right]
\end{aligned}\\
\\
\\
\begin{aligned}
A_{c1} \ A_{c2} \ A_{c3} \  \ \ B_{c1} \ B_{c2} \ B_{c3} \ \ \  & \ \ \ \ \ \ AB_{c1} \ AB_{c2} \ AB_{c3}\\
\begin{matrix}
A_{r1}\\
A_{r2}\\
A_{r3}
\end{matrix}\left[\begin{matrix}
| &  & \\
| &  & \\
| &  & 
\end{matrix} \ \ \ \ \ \right]\left[ \ \ \begin{matrix}
| &  & \\
| &  & \\
| &  & 
\end{matrix} \ \ \ \ \ \ \right] & =\left[ \ \ \begin{matrix}
| &  & \\
| &  & \\
| &  & 
\end{matrix} \ \ \ \ \ \ \ \ \right]
\end{aligned}
$$

Column 1 in the new matrix is equal to $$A c1$$(matrix multiply vector) . To expand the onf of the  multiplication:

$$
AB_{c1}=A_{c1}B_{r1,c1}+A_{c2}B_{r2,c1}+A_{c3}B_{r3,c1}+...
$$

where $$A_i,\ i\in N$$ are columns of $$A$$.  This tells us that *columns* of $$C$$ are combinations of  columns of $$A$$

### Rows $$\times$$ A Matrix

Similarly, *rows* of $$C$$ are combinations of rows of $$B$$

$$
\begin{aligned}
A_{c1} \ A_{c2} \ A_{c3}\ \ \ \ \ \ \ \ \ \ \ \ B_{c1} \ B_{c2} \ B_{c3} \ \ \  & \ \ \ \ \ \ \\
\begin{matrix}
A_{r1}\\
A_{r2}\\
A_{r3}
\end{matrix}\left[\begin{matrix}
- & - & -\\
 &  & \\
 &  & 
\end{matrix} \ \ \ \ \ \right]\left[ \ \ \begin{matrix}
- & - & -\\
 &  & \\
 &  & 
\end{matrix} \ \ \right] & =\begin{matrix}
A_{r1} B\\
A_{r2} B\\
A_{r3} B
\end{matrix}\left[ \ \ \begin{matrix}
- & - & -\\
 &  & \\
 &  & 
\end{matrix} \ \right]
\end{aligned}
$$

$$
A_{r1}B=A_{r1,c1}B_{r1}+A_{r1,c2}B_{r2}+...
$$



### A Column $$\times$$ A Row

A column of $$A$$ will be dimension $$M\times 1$$ and a row of $$B$$ will be $$1\times P$$. For example, let's have 

$$
\left[\begin{matrix}
2\\
3\\
4
\end{matrix}\right]\left[\begin{matrix}
1 & 6
\end{matrix}\right] =\left[\begin{matrix}
2 & 12\\
3 & 18\\
4 & 24
\end{matrix}\right]
$$

The output matrix is very special. Each column of the output is a multiple of $$\left[\begin{matrix}
2\\
3\\
4
\end{matrix}\right]$$. Each row of the output is a multiple of $$\left[\begin{matrix}
1 & 6
\end{matrix}\right]$$. And later we will see this is a minimal matrix, where the row space and column space are both just lines. Thus the 4th way of multiplying two matrices are

$$
AB=sum\ of\ (A\ col\ of\ A\ \times \ A\ col\ of B)
$$

that is, for example, 

$$
\left[\begin{matrix}
2 & 7\\
3 & 8\\
4 & 9
\end{matrix}\right]\left[\begin{matrix}
1 & 6\\
0 & 0
\end{matrix}\right] =\left[\begin{matrix}
2\\
3\\
4
\end{matrix}\right]\left[\begin{matrix}
1 & 6
\end{matrix}\right] +\left[\begin{matrix}
7\\
8\\
9
\end{matrix}\right]\left[\begin{matrix}
0 & 0
\end{matrix}\right]
$$

### Blocks 

$$
\left[\begin{matrix}
A_{1} & A_{2}\\
A_{3} & A_{4}
\end{matrix}\right]\left[\begin{matrix}
B_{1} & B_{2}\\
B_{3} & B_{4}
\end{matrix}\right] =\left[\begin{matrix}
A_{1} B_{1} +A_{2} B_{3} & ...\\
... & ...
\end{matrix}\right]
$$



## Inverses(square matrices)

Not all matrices have inverses. For a square matrix $$A$$ that has an inverse,

$$
A^{-1}A=I=AA^{-1}
$$

Note for a non-square matrix the left inverse is not same as the right inverse. A matrix that has an inverse is called invertible or non-singular.

Let's talk about the singular case first. 

$$
A=\left[\begin{matrix}1 & 3\\2&6\end{matrix}\right]
$$

There are various way we can say why a matrix has no inverse. The professor think the best is to say if there's a non-zero vector $$\mathrm{x}$$ s.t.

$$
A\mathrm{x}=\mathbf{0}
$$

here $$\mathrm{x}=\left[\begin{matrix}
3\\
-1
\end{matrix}\right]$$. The straightfoward reasoning is that if there's an $$A^{-1}$$ exists, 
$$
\begin{aligned}
A^{-1}A\mathrm{x}&=A^{-1}\mathbf{0}\\
I\mathrm{x}&=0\\
\mathrm{x}&=0
\end{aligned}
$$

but that's not true, we have assumed that $$\mathrm{x}$$ is not zero. 

### Gaussian-Jordan(solve 2 euqations at once)

$$
\begin{aligned}
\left[\begin{matrix}
1 & 3\\
2 & 7
\end{matrix}\right]\left[\begin{matrix}
a & b\\
c & d
\end{matrix}\right] & =\left[\begin{matrix}
1 & 0\\
0 & 1
\end{matrix}\right]\\
A\ \ \ \ \ \ \ \ \ \ \ A^{-1}\ \  & =I
\end{aligned}
$$

Finding an inverse of a matrix can be viewed as solving $$n$$ systems of equations, in this case 2 systems of equations

$$
\begin{aligned}
\left[\begin{matrix}
1 & 3\\
2 & 7
\end{matrix}\right]\left[\begin{matrix}
a\\
b
\end{matrix}\right] & =\left[\begin{matrix}
1\\
0
\end{matrix}\right]\\
\left[\begin{matrix}
1 & 3\\
2 & 7
\end{matrix}\right]\left[\begin{matrix}
c\\
d
\end{matrix}\right] & =\left[\begin{matrix}
0\\
1
\end{matrix}\right]
\end{aligned}
$$

and $$A\times column\ j\ of\ A^{-1}=column\ j\ of\ I$$. To solve systems of equations, we use Gaussian-Jordan method. First we augment the matrix we want to find the inverse with $$I$$, 

$$
\left.\left[\begin{matrix}
1 & 3\\
2 & 7
\end{matrix} \right\rvert\begin{matrix}
1 & 0\\
0 & 1
\end{matrix}\right]\\
A \ \ \ \ \ \ \ I
$$

then we do row $$eliminations$$ first to get the upper triangular form, this idea is from Gauss. Then with Jordan's idea, from the upper triangular form we eliminate the terms on the upper triangular porition. on the lefthand side to turn $$A$$ into $$I$$ then $$I$$ will become $$A^{-1}$$

$$
\left.\left[\begin{matrix}
1 & 3\\
2 & 7
\end{matrix} \right\rvert\begin{matrix}
1 & 0\\
0 & 1
\end{matrix}\right]\rightarrow \left.\left[\begin{matrix}
1 & 3\\
0 & 1
\end{matrix} \right\rvert\begin{matrix}
1 & 0\\
-2 & 1
\end{matrix}\right]\rightarrow \left.\left[\begin{matrix}
1 & 0\\
0 & 1
\end{matrix} \right\rvert\begin{matrix}
-7 & 3\\
-2 & 1
\end{matrix}\right]\rightarrow A^{-1} =\left[\begin{matrix}
-7 & 3\\
-2 & 1
\end{matrix}\right]
$$

Why this work? First we have talked before that row eliminations is equivalent to multiply an elimination matrix on the left of $$A$$ (the matrix we want to find inverse)

$$
EA=I
$$

And obviously $$E=A^{-1}$$, then 

$$
E\begin{bmatrix}A\rvert I\end{bmatrix}=E\begin{bmatrix}I|A^{-1}\end{bmatrix}
$$
