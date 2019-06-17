---
layout: post
title: Sketching solutions for 2x2 First order System w/ constant coefficients
date: 2019-6-16
---

Let 
$$
\begin{align}
x'&=-x+by\\
y'&=cx-3y
\end{align}
$$
The $$x$$ and $$y$$ are departures from normal advertising budgets for Mass. states and NH. First let's try $$b=2,c=0$$. Then we solve for solutions:
$$
\begin{bmatrix}
x\\
y
\end{bmatrix}=c_1\begin{bmatrix}
1\\
-1
\end{bmatrix}e^{-3t}+c_2\begin{bmatrix}
1\\
0
\end{bmatrix}e^{-t}
$$


To plot the solutions, let's first start with easy solutions. The easy ones are $$c_1=\pm 1,\ c_2=0$$ and $$c_1=0,\ c_2=\pm 1$$. 