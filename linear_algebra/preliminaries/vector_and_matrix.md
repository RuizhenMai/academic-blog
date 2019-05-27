---
layout: post
title: Vector and Matrix 
date: 2019-5-26
---

These are some useful points that Prof. Gilbert did not mention in the class but still I think that will help you get started better, in case you did not know.

### Vector

You are probably familiar with vectors from Calculus. That's the column vector. And in my notes I use brackets to represent vectors. In some notes you may see they use parenthesis.

$$
u=\begin{bmatrix}
2\\
1
\end{bmatrix},v=\begin{bmatrix}
\pi\\
e
\end{bmatrix}
$$

Bold characters are used to represent unknown variable vector, sometimes short for unknown vector, to differentiate with single variable unknown.

$$
\mathbf{x}=\begin{bmatrix}
x_1\\
x_2\\
x_3\\
...
\end{bmatrix}
$$

### Row then column

In convention, the subscript of a matrix's item $$a_{ij}$$ is ith row jth column. When I say a matrix is $$4\times3$$ or in $$\mathbb R^{4\times3}$$, it means it has 4 rows and 3 columns.

### Matrix

You have probably known that marix muliplication in this form:

$$
c_{ij}=\sum_{k=1}^Na_{ik}b_{kj}
$$

An item in the product matrix is equal to a row in the left matrix times a column in the right matrix. What is useful to remember before the lecture notes or the video series is:

$$
\begin{bmatrix}
1 & 2 & 3\\
4 & 5 & 6\\
7 & 8 & 9\\
\end{bmatrix}\begin{bmatrix}
x\\
y\\
z
\end{bmatrix}=\begin{bmatrix}
1x+2y+3z\\
4x+5y+6z\\
7x+8y+9z
\end{bmatrix}=x\begin{bmatrix}
1\\
4\\
7
\end{bmatrix}+y\begin{bmatrix}
2\\
5\\
8
\end{bmatrix}+z\begin{bmatrix}
3\\
6\\
9
\end{bmatrix}
$$

we can rewrite the multiplication as a combination of the left matrix's columns. This is true for any matrix multiplication. The situations the vector $$\begin{bmatrix}
x\\
y\\
z
\end{bmatrix}$$ has more than one column will be illustrated in later course notes.

