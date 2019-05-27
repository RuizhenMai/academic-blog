---
layout: post
title: "Solving Ax = b: Row Reduced Form R"
date: 2019-5-26
---

Remember we have talked about other values of b on [lecture 6](./Column_Space_and_Nullspace). Today we will explore further how a non-zero $$\mathbf b$$ lead to not-a-space solution, and discuss what values of $$\mathbf b$$ can have a solution, many solutions, or no solution, extending from [lecture 1](./The_Geometry_of_Linear_Equations) and [lecture 7](./solving_ax_eq_0).

## Solvability conditions on b

Let's again use the example:

$$
A=\begin{bmatrix}
1 & 2 & 2 & 2\\
2 & 4 & 6 & 8\\
3 & 6 & 8 & 10
\end{bmatrix}\tag{1}
$$

Actually not many b's can have a solution. You can try throw some random numbers in. We have known that the r3 of $$A$$ is r1 + r2. When we have a much more larger matrix, that will not come in a very clear way, say maybe r8 = 2\*r4+1/2\*r. So we need elimination to discover what exactly the relations on rows of $$A$$ and then find out what conditions we need for $$\mathbf b$$. Augment the matrix $$A$$ with $$\mathbf b$$, and do elimination real quick:

$$
\left[\left.\begin{matrix}
1 & 2 & 2 & 2\\
2 & 4 & 6 & 8\\
3 & 6 & 8 & 10\ 
\end{matrix}\right\rvert \begin{matrix}
b_1\\
b_2\\
b_3
\end{matrix}
\right]\rightarrow...\rightarrow\left[\left.\begin{matrix}
1 & 2 & 2 & 2\\
0 & 0 & 2 & 4\\
0 & 0 & 0 & 0\ 
\end{matrix}\right\rvert \begin{matrix}
b_1\\
b_2-2b_1\\
b_3-b_2-b_1
\end{matrix}
\right]
$$

By elimination we see that the constant vector $$\mathbf b$$ must follow the rules on the augemented side. Picking the zero row is most convenient to phrase the condition. If and only if $$b_3-b_2-b_1=0$$, we have a solution to $$A\mathbf x=\mathbf b$$. A particular one will be $$\mathbf b=\begin{bmatrix}1\\5\\6\end{bmatrix}$$. **The zeros rows are conditions for solving the equations.**

Note that this is equivalent to say $$\mathbf b$$ is in $$C(A)$$ which we have discussed before(idk formally why yet, probably this is a way of checking if b is in the column space of A). 

### Solutions to Ax=b if there's one 

To find the solution to $$A\mathbf x=\mathbf b$$, we first set the free variables to zero to get $$\mathbf x_{particular}$$ and then get $$\mathbf x_{null}$$ by setting one free variable as 1 each time. For our example $$A$$, we let $$x_2=x_4=0$$. 

$$
\begin{align}
2x_3&=3\Rightarrow x_3=3/2\\
x_1+2x_3&=1\Rightarrow x_1=-2\\
\end{align}
$$

then 

$$
\mathbf x_{particular}=
\begin{bmatrix}
-2\\
0\\
3/2\\
0
\end{bmatrix}
$$

But why we need to add the solutions in nullspace? It's because 

$$
\begin{align}
A\mathbf x_{particular}&=\mathbf b\\
A\mathbf x_{null}&=0\\
A(\mathbf x_{particular}+\mathbf x_{null})&=\mathbf b
\end{align}
$$

Copy the null solutions from the last lecture notes, 

$$
\mathbf x_{complete}=\begin{bmatrix}
-2\\
0\\
3/2\\
0
\end{bmatrix}+c_1\begin{bmatrix}
-2\\
1\\
0\\
0
\end{bmatrix}+c_2\begin{bmatrix}
2\\
0\\
-2\\
0
\end{bmatrix}
$$

Note that we don't have a constant in front of $$\mathbf x_{particular}$$ because it solves $$A\mathbf x=\mathbf b$$ for the particular $$\mathbf b$$. Remember the null solution is a *nullspace*. But this solution to the particular $$\mathbf b$$ does not have a space. It's the plane formed by the $$\mathbf x_{null}$$ shifted by the vector $$\mathbf x_{particular}$$. It does not go through the origin. 

## Rank

$$r$$ is ranks and equal to the number of pivots in the matrix.

### Full Column rank: r=n

Full column rank means there's a pivot in every *column*. For example

$$
A=\begin{bmatrix}
1 & 2 & 3\\
4 & 5 & 6\\
7 & 8 & 9\\
0 & 0 & 0
\end{bmatrix}
$$

In this case the $$N(A)$$ is just the $$\mathbf 0$$ because we have *no* free variables can be assigned to the nullspace. The solution to $$A\mathbf x=\mathbf b$$ is just $$\mathbf x_{particular}$$, if there's one, determined by the checking solvability technique mentioned above. We have either 0 or 1 solution.  

In addition, the rref(A) or $$R$$ for full column rank matrix will always be $$\begin{bmatrix}
I\\
0\\
\end{bmatrix}$$.

### Full Row rank: r=m

Every row will have a pivot. For example

$$
A=\begin{bmatrix}
1 & 2 & 3 & 0\\
4 & 5 & 6 & 0\\
7 & 8 & 9 & 0\\
\end{bmatrix}
$$

You see first there will not be any zero rows after elimination. This promises us there will always be a solution. Also since we have at least one free variable in this case, there will be infinitely many solutions([check out how to find the null solutions](./solving_ax_eq_0.md)). And the rref(A) will be $$\begin{bmatrix}
I & F\\
\end{bmatrix}$$ (Or there can be a mix between columns). 

### Full rank r=m=n 

$$
A=\begin{bmatrix}
1 & 2 & 3\\
4 & 5 & 6\\
7 & 8 & 9\\
\end{bmatrix}
$$

Since $$r=n$$, no free variables, the nullspace for this matrix is just zero only. Since $$r=m$$, no zero rows, there won't be any constraint on $$\mathbf b$$. There will always be one and only one solution  to full rank matrix. rref(A) = $$I$$. 

### r<m, r<n

The $$R$$ will be $$\begin{bmatrix}
I & F\\
0 & 0
\end{bmatrix}$$. The $$A$$ in (1) is this case. Remember from last lectures we may not have a solution or there're infinitely many solutions to this one.