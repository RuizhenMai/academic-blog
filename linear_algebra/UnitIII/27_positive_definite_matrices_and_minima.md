---
layout: post
title: Positive Definite Matrices and Minima
date: 2019-6-14
---

This lecture brings the whole course together. 

## Test for Positive Definiteness

One way introduced last time, is to check if a symmetric matrix has all positive eigenvalues. Another way is to check if all the determinants of all leading submatrices are positive, that is, given matrix $$A=\begin{bmatrix}
a & b\\
c & d
\end{bmatrix}$$, see if 1. $$a>0$$ and 2. $$ad-b^2>0$$. Similar patterns go on with larger matrices. The third way is to check if the pivots are all positive. The most important test we're going to look at is the following 
$$
\mathbf x^\top A\mathbf x>0
$$
Except $$\mathbf x=\mathbf 0$$.