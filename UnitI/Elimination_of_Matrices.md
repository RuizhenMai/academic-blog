---
layout: post
title: Elimination with Matrices
date: 2019-5-20
---

### Elimination

A *pivot* in a matrix is the first non-zero element in each row. And we want the column postiion of a pivot is equal to its row position, i.e., we want the pivot in row 1 in column 1, in row 2 in column 2 etc. If we cannot find a pivot for each row, then it's a failure. 

So our task it to do operations between or among rows to achieve the ideal stage where the pivots are in their positions. 

Exmaple:

$$
A=\left[\begin{matrix}
1 & 2 & 1\\
3 & 8 & 1\\
0 & 4 & 1
\end{matrix}\right] \ \begin{matrix}
r1\\
r2\\
r3
\end{matrix} ,\ \ \ \mathbf{b} =\left[\begin{matrix}
2\\
12\\
2
\end{matrix}\right]
$$

Let's care about matrix $$A$$ for now. I have labeled each row as $$r1,r2,r3$$. As the first number in $$r1$$ is non-zero, the pivot for this row is found automatically. Then we find the pivot of second row. To do so, we do $$r2-r1\cdot3$$, and this results in

$$
\left[\begin{matrix}
1 & 2 & 1\\
0 & 2 & -2\\
0 & 4 & 1
\end{matrix}\right] \ \begin{matrix}
r1\\
r2-r1*3\\
r3
\end{matrix}\tag{1}
$$

Then we found the second pivot by eliminating $$3$$ in $$r2$$. Note that the first element in $$r3$$ is zero, so we don't have to do extra steps to eliminate it. If it were non-zero, we still have to make it zero in order to find the third pivot $$r3$$. Right now to find the third pivot, we just need to do 

$$
U=\left[\begin{matrix}
1 & 2 & 1\\
0 & 2 & -2\\
0 & 0 & 5
\end{matrix}\right] \ \begin{matrix}
r1\\
r2-r1*3\\
r3-2*r2'
\end{matrix}\tag{2}
$$

where I coined the new $$r2$$ as $$r2'$$. Then finally we have found the final upper triangle matrix $$U$$. This is the ideal form we want to achieve. But don't forget that we also need to do same operations on $$b$$, which leads to $$\left[\begin{matrix}
2\\
6\\
-10
\end{matrix}\right]$$ and this final constant vector we call it $$\mathbf{c}$$. The new equation is then $$Ux=\mathbf{c}$$. In general, we want to *augment* the coefficient matrix $$A$$ in case we forgot the steps to obtain $$U$$, that is, to attach $$\mathbf{b}$$ into it
$$
A=\left. \left[\begin{matrix}
1 & 2 & 1\\
3 & 8 & 1\\
0 & 4 & 1
\end{matrix} \right\rvert \begin{matrix}
2\\
12\\
2
\end{matrix}\right]
$$


### Back Substitution

Right now our equations are

$$
\begin{aligned}
x+2y+z=2,\ & x=2\\
2y-2z=6,\ & y=1\\
5z=-10,\ & z=-2\\    
\end{aligned}
$$

First we see $$z=-2$$ from the last row. And substitute $$z$$ into the second row we get $$y=1$$. And finally $$x=2$$. 

### Matrix Operations 

Not stated clearly before, when we multiply matrix $$A$$ with the unknown vector $$\mathbf{x}$$ we expand the unknowns $$x, y, z$$ to each column of $$A$$. In fact, when we want to do operations on a matrix's column, we multiply a column on the *right*. 

Oh, before we start, note that multiplying a constant with any matrices:

$$
\lambda \left[\begin{matrix}
- & - & -\\
- & - & -\\
- & - & -
\end{matrix}\right]=\left[\begin{matrix}\lambda&0&0\\0&\lambda&0\\0&0&\lambda\end{matrix}\right] \left[\begin{matrix}
- & - & -\\
- & - & -\\
- & - & -
\end{matrix}\right]=\lambda I\left[\begin{matrix}
- & - & -\\
- & - & -\\
- & - & -
\end{matrix}\right]
$$

where $$I$$ is the identity matrix. This is true when we put lambda on the right side of the matrix. 

### Column

When multiplying a vector on the right of a matrix, we are manipulating its columns:

$$
\left[\begin{matrix}
- & - & -\\
- & - & -\\
- & - & -
\end{matrix}\right]*\left[\begin{matrix}
3\\
4\\
5
\end{matrix}\right]=\Biggr[3*Col\ 1+4*Col\ 2+5*Col\ 3\Biggr]
$$

Note each column is 3 x 1 so the final answer is a vector of 3 x 1. Similarly, if it's a matrix not a vector:

$$
\left[\begin{matrix}
- & - & -\\
- & - & -\\
- & - & -
\end{matrix}\right] *\left[\begin{matrix}
3 & 0 & 0\\
4 & 1 & 0\\
5 & 0 & 1
\end{matrix}\right] =\left[\begin{matrix}
 &  & \\
3*Col\ 1+4*Col\ 2+5*Col\ 3 & Col\ 2 & Col\ 3\\
 &  & 
\end{matrix}\right]
$$

only the first column of the new matrix changes, the second and the third one remain because we put one in the middle and the lower right. 

### Row

$$
\left[\begin{matrix}
3 & 4 & 5
\end{matrix}\right]\left[\begin{matrix}
- & - & -\\
- & - & -\\
- & - & -
\end{matrix}\right] =\left[\begin{matrix}
3*Row\ 1+4*Row\ 2+5*Row\ 3
\end{matrix}\right]
$$

Note the output vector is 1 x 3.

Thus if we want to reproduce the elimination on $$(2)$$, we can do 

$$
\left[\begin{matrix}
1 & 0 & 0\\
-3 & 1 & 0\\
0 & 0 & 1
\end{matrix}\right] \left[\begin{matrix}
1 & 2 & 1\\
3 & 8 & 1\\
0 & 4 & 1
\end{matrix}\right]=\left[\begin{matrix}
1 & 2 & 1\\
0 & 2 & -2\\
0 & 4 & 1
\end{matrix}\right]
$$

on the second row of the leftmost matrix we are producing same effect of $$r2-3*r1$$ on row exchange on the original matrix. Let's call this matrix $$E_{21}$$ because it anchors the r2c1 element(though I prefer to call it $$E_{22}$$). And then we can add another matrix $$E_{32}$$ to simulate $$(2)$$

$$
\left[\begin{matrix}
1 & 0 & 0\\
0 & 1 & 0\\
0 & -2 & 1
\end{matrix}\right] \left[\begin{matrix}
1 & 2 & 1\\
0 & 2 & -2\\
0 & 4 & 1
\end{matrix}\right]=\left[\begin{matrix}
1 & 2 & 1\\
0 & 2 & -2\\
0 & 0 & 5
\end{matrix}\right]
$$

### Permutation

$$
\left[\begin{matrix}
0 & 1\\
1 & 0
\end{matrix}\right]\left[\begin{matrix}
a & b\\
c & d
\end{matrix}\right] =\left[\begin{matrix}
c & d\\
a & b
\end{matrix}\right]
$$



### Inverse
In summary, to express the whole operations, it is 

$$
E_{32}(E_{21}A)=U
$$

By associative law, 

$$
(E_{32}E_{21})A=U
$$

But notice that we cannot mess around the order of the multiplication when multiplying matrices. So to find the elimination matrix $$E$$ which does the whole job of converting $$A$$ to $$U$$, there's two way, we can multiply $$E_{32}$$ with $$E_{21}$$, or, the way the professor introduces, do *Inverse*. We can find the inverse. We will introduce the simple concept here. 

To find the inverse of a matrix, we find the matrix that can offset its effect let's say we want to find the inverse of $$E_{21}=\left[\begin{matrix}
1 & 0 & 0\\
-3 & 1 & 0\\
0 & 0 & 1
\end{matrix}\right]$$

$$
\left[\begin{matrix}
1 & 0 & 0\\
3 & 1 & 0\\
0 & 0 & 1
\end{matrix}\right] \left[\begin{matrix}
1 & 0 & 0\\
-3 & 1 & 0\\
0 & 0 & 1
\end{matrix}\right]=\left[\begin{matrix}
1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 1
\end{matrix}\right]
$$

we offset the effect of substracting three $$r1$$ by adding three of it back. 

