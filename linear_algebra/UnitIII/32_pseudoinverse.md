---
layout: post
title: Left and Right Inverses; Pseudoinverse
date: 2019-6-18
---

## Left and Right Inverses

A regular inverse $$AA^{-1}=I$$ is a 2-sided inverse. This happens if and only if square matrix $$A$$ is full rank $$r=m=n$$.  If $$A$$ is not square and full column rank, then there's 0 or 1 solution to $$A\mathbf x=\mathbf b$$, depending on if $$\mathbf b$$ is in the column space of $$A$$ (there can be more rows than columns so columns are not spanning the whole space). 

In [note 28](./28_similar_matrices_and_jordan_form) we have good, square and symmetric matrix $$A^\top A$$. It's invertible as long as we have $$A$$ as full column rank. We say that <u>rectangular</u> $$A$$ has <u>left inverse</u> since 

$$
\underbrace{(A^\top A)^{-1}A^\top }_{A^{-1}_{left}}A=I
$$

For full row rank, we have independent rows, and infinitely many solutions to $$A\mathbf x=\mathbf b$$. In this case we have right inverse of $$A$$:

$$
A\underbrace{A^\top(A A^\top)^{-1}}_{A_{right}^{-1}}=I
$$

What happen if we don't put the $$A$$ in order? Recall [note 15](../UnitII/15_projections_onto_subspaces), the projection matrix is $$P=A(A^\top A)^{-1}A^\top$$, 

$$
AA^{-1}_{left}=P_{col}
$$

When we put the A to the left of its left inverse, it's the projection matrix into the column space. If we put A to the right of its right inverse, we got another projection matrix, but to the row space:

$$
A_{right}^{-1}A=P_{row}
$$


## Pseudoinverses

When we have neither full column rank nor full row rank, we cannot do left or right inverses. But $$A$$ is still a invertible mapping (from row space) onto column space. As long as we let go the null space and left null space, everything is good. So how to find this pseudoinverse $$A^+$$? We can use SVD:

$$
A^+=V\Sigma^+U^\top
$$
