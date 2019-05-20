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
r2-r1*6\\
r3
\end{matrix}
$$

Then we found the second pivot by eliminating $$3$$ in $$r2$$. Note that the first element in $$r3$$ is zero, so we don't have to do extra steps to eliminate it. If it were non-zero, we still have to make it zero in order to find the third pivot $$r3$$. Right now to find the third pivot, we just need to do 

$$
U=\left[\begin{matrix}
1 & 2 & 1\\
0 & 2 & -2\\
0 & 0 & 5
\end{matrix}\right] \ \begin{matrix}
r1\\
r2-r1*6\\
r3-2*r2'
\end{matrix}
$$

where I coined the new $$r2$$ as $$r2'$$. Then finally we have found the final upper triangle matrix $$U$$. This is the ideal form we want to achieve. But don't forget that we also need to do same operations on $$b$$, which leads to $$\left[\begin{matrix}
2\\
6\\
-10
\end{matrix}\right]$$ and this final constant vector we call it $$\mathbf{c}$$.The new equation is then $$Ux=\mathbf{c}$$. In general, we want to *augment* the coefficient matrix $$A$$ in case we forgot the steps to obtain $$U$$, that is, to attach $$\mathbf{b}$$ into it


$$
A=\left. \left[\begin{matrix}
1 & 2 & 1\\
3 & 8 & 1\\
0 & 4 & 1
\end{matrix} \right| \begin{matrix}
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

