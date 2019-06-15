---
layout: post
title: "Solving Ax = 0: Pivot Variables, Special Solutions"
date: 2019-5-25
---

This lecture we continue to talk about null space and the case where there're free variables. 

## Free Variables

Remember a pivot is the first non-zero value in each row. But sometimes there can be a row without a pivot, when a row is all zeros. 

Let 

$$
A=\begin{bmatrix}
1 & 2 & 2 & 2\\
2 & 4 & 6 & 8\\
3 & 6 & 8 & 10\ 
\end{bmatrix}
$$

be the example. What comes out right away is the r3 of $$A$$ is r1 + r2 of $$A$$. This will be more obvious when we do elimination on it. When we are doing eliminations, we are *not* changing the nullspace. When we subtract one row from the other on $$A$$, we are not changing the solution to $$A\mathbf x =\mathbf b$$ (but they do affect the column space). Do the elimination:

$$
\begin{bmatrix}
1 & 2 & 2 & 2\\
2 & 4 & 6 & 8\\
3 & 6 & 8 & 10\ 
\end{bmatrix}\rightarrow \begin{bmatrix}
1 & 2 & 2 & 2\\
0 & 0 & 2 & 4\\
3 & 6 & 8 & 10\ 
\end{bmatrix}\rightarrow\\ \begin{bmatrix}
1 & 2 & 2 & 2\\
0 & 0 & 2 & 4\\
0 & 0 & 2 & 4\ 
\end{bmatrix}\rightarrow \begin{bmatrix}
1 & 2 & 2 & 2\\
0 & 0 & 2 & 4\\
0 & 0 & 0 & 0\ 
\end{bmatrix}=U\tag{1}
$$

We see that the third row is all zeros. In other words, we only have 2 pivots for this matrix. We say the matrix $$U$$ is in *echelon* (staircase) form because it only contains values in "upper" side of the matrix, similar to the upper triangular form but that naming requires the matrix to be square{% include sidenote.html note='A matrix is said to be in row-echelon form if (1) any rows made
completely of zeroes lie at the bottom of the matrix and (2) the first nonzero
entries of the various rows form a staircase pattern: the first nonzero entry
of the k + 1st row is to the right of the first nonzero entry of the k
th row. (https://web.ma.utexas.edu/users/sadun/S08/427K/matrix.pdf) '%}. The *rank* of a matrix is equal to the # of pivots in the echelon form.

Once we’ve found $$U$$ we can use back-substitution to find the solutions $$\mathbf x$$ to the
equation $$U\mathbf x = \mathbf 0$$. Now comes the important step:

$$
U=\begin{array}{c}

\begin{bmatrix}
1 & 2 & 2 & 2\\
0 & 0 & 2 & 4\\
0 & 0 & 0 & 0\ 
\end{bmatrix}\\
\begin{matrix}
c1\! & c2\! &c3\! &c4
\end{matrix}
\end{array}
$$

We see that $$c1$$ and $$c3$$ are pivot columns. $$c2$$ and $$c4$$ are the *free columns*, corresponding to $$x_2$$ and $$x_4$$. We call it free because we can assign the 2nd and 4th unknown variable to any number we want. Since we can assign whatever values we want, one particular solution is to make $$x_2=1$$ and $$x_4=0$$ (convenienet for now), now we have: 

$$
\begin{align}
2x_3+4x_4&=0\Rightarrow x_3=0\\ 
x_1+2x_2+2x_3+2x_4&=0\Rightarrow x_1=-2\\
\end{align}
$$

by back-substitution. As we have shown before, a multiple of this solution $$\mathbf x$$ can also work. So

$$
\mathbf x =c\begin{bmatrix}
-2\\
1\\
0\\
0
\end{bmatrix}\\
$$

is in our null space. But this is not the complete null space yet. Let's make another choice on the free variable: $$x_2=0,\ x_4=1$$. Do the back-substitution to get $$x_1,\ x_3$$ again, we get

$$
\mathbf x =d\begin{bmatrix}
2\\
0\\
-2\\
1
\end{bmatrix}\\
$$

The complete null space is the linear combination of the two *special* solutions where we make $$x_2=1,\ x_4=0$$ and $$x_2=0,\ x_4=1$$, 

$$
\mathbf x =c\begin{bmatrix}
-2\\
1\\
0\\
0
\end{bmatrix}+d\begin{bmatrix}
2\\
0\\
-2\\
1
\end{bmatrix}\\
$$


In general, when we have a $$A\in \mathbb R^{m\times n}$$, we have $$n-r$$ free variabels, where $$r$$ is the number of rank or pivot variables (consider the number of pivot variables are those we cannot choose freely). Here we have $$4-2=2$$ free variables and the null space is a 2-d plane in $$\mathbb R^4$$.

### Reduced-row echelon form

The matrix $$U$$ in equation $$(1)$$ is in row echelon form, now we want to further simplify it to row-reduced echelon form (rref) $$R$$. 

$$
U=\begin{bmatrix}
1 & 2 & 2 & 2\\
0 & 0 & 2 & 4\\
0 & 0 & 0 & 0\ 
\end{bmatrix}\rightarrow \begin{bmatrix}
1 & 2 & 0 & -2\\
0 & 0 & 2 & 4\\
0 & 0 & 0 & 0\ 
\end{bmatrix}\rightarrow\\ \begin{bmatrix}
1 & 2 & 0 & -2\\
0 & 0 & 1 & 2\\
0 & 0 & 0 & 0\ 
\end{bmatrix}=R
$$

This form requires an echelon-form matrix to (1) have 1 in the pivots, (2) have zeros above and below the pivots. Exchange the c2 and c3 of $$R$$:

$$
R=\begin{bmatrix}
1 & 0 & 2 & -2\\
0 & 1 & 0 & 2\\
0 & 0 & 0 & 0\ 
\end{bmatrix}=\begin{bmatrix}
I & F\\
0 & 0
\end{bmatrix}
$$

we see an identity matrix, a "free matrix"(containing the free variables), and a/some row(s) of zeros (when there're linearly dependent rows in $$A$$). Right now to solve the system of equations where the righthand side is all zeros:

$$
\begin{align}
R\mathbf x&=\mathbf b\\
\begin{bmatrix}
I & F\\
0 & 0
\end{bmatrix}\mathbf x&=\begin{bmatrix}
0\\
0
\end{bmatrix}
\end{align}
$$

Let's set the particular solution of $$\mathbf x=N$$ Remember the row operations on matrix. To offset the effect of $$R$$, we have

$$
\mathbf N=\begin{bmatrix}
-F\\
I
\end{bmatrix}=\begin{bmatrix}
-2 & 2\\
0 & -2\\
1 & 0\\
0 & 1
\end{bmatrix}
$$

The columns of $$N$$ are the special solutions (remember we have exchanged the columns of $$R$$). Note the dimension of $$I$$ in $$N$$ is $$(n-r)\times (n-r)$$, the number of free variables multiply the number of free variables. 

