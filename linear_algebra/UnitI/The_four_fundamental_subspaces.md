---
layout: post
date: 2019-5-28
title: The Four Fundamental Subspaces
---

## Four subspaces

The four fundamental subspaces associated with a $$m\times n$$ matrix $$A$$ is 

* Column Space, $$C(A)$$: the $$C(A)$$ is in $$\mathbb R^m$$, as there're $$m$$ elements per vector. The $$\dim C(A)=rank\ r$${%include sidenote.html note='in $$\mathbb R^m$$ means like in $$\mathbb R^3$$ but we only have a 2 dimensional plane this is the dimension'%}. The basis is the pivot columns 
* Nullspace, $$N(A)$$: the nullspace is in $$\mathbb R^n$$, as the maximum number of free variables/columns will not exceed $$n$$. $$\dim N(A)=n-r$$ 
* Row Space, $$C(A^T)$${% include sidenote.html note='Here we just want to stick to the column space notation, nothing special. The column space of $$A^T$$ is same as the row space of $$A$$' %}: in $$\mathbb R^n$$. The $$\dim C(A^T)=rank\ r$$ same dimension as column space. This is clear when you check the dependency between rows, and the number of independent rows at most is just the rank. 
* Left Nullspace, $$N(A^T)$$: in $$\mathbb R^m$$. $$\dim N(A^T)=m-r$$.

You will probably notice that $$\dim C(A)+\dim N(A^T)=m$$ and $$\dim C(A^T)+\dim N(A)=n$$. 

## Basis

### Row Space

From last class we've seen the basis of a column space is just the pivot columns. What about the basis for a row space? One thing we can do is to do elimination on $$A^T$$ again and find out the pivot columns on $$A^T$$ and that's the basis for the row space of $$A$$, $$C(A^T)$$. 

But note that eliminations will change the column space:

$$
A=\begin{bmatrix}
1 & 2 & 3 & 1\\
1 & 1 & 2 & 1\\
1 & 2 & 3 & 1
\end{bmatrix}\rightarrow \begin{bmatrix}
1 & 0 & 1 & 1\\
0 & 1 & 1 & 0\\
0 & 0 & 0 & 0
\end{bmatrix}=R\tag{1}
$$

the first two columns are independent, we can use it as the basis, it means the first two columns of $$A$$ because on $$R$$ the columns are $$\begin{bmatrix}
1\\
0\\
0
\end{bmatrix}$$ and $$\begin{bmatrix}
0\\
1\\
0
\end{bmatrix}$$ that's definitely not in column space spanned by  $$\begin{bmatrix}
1\\
1\\
1
\end{bmatrix}$$ and $$\begin{bmatrix}
2\\
1\\
2
\end{bmatrix}$$. $$C(R)\neq C(A)$$. However, the row spaces are remained. Eliminations are one row subtracting a multiple of another rows and etc. These row vectors stay in the original space. Thus the basis for the row space is the first $$r$$ rows in $$R$$. Why not $$A$$? It's possible, but because first $$r$$ rows in $$A$$ may be dependent, and we want independent rows{%include sidenote.html note='this does not mean the row space is different, we just want independent rows; the column space is "messed up"'%}. By undoing the eliminations, we can see the first $$r$$ rows will span the whole row space. 

### Left Null Space

If

$$
A^T\mathbf y=\mathbf 0
$$

then all $$\mathbf y$$ together is the nullspace of $$A^T$$ and left nullspace of $$A$$. The reason why it's called the left null space:

$$
\begin{align}
A^T\mathbf y&=\mathbf 0\\
\mathbf y^TA^{TT}&=\mathbf 0^T\\
\mathbf y^TA&=\mathbf 0
\end{align}
$$

$$\mathbf y$$ is staying on the left. How to find the basis of the $$N(A^T)$$? Remember we've done something like this:

$$
E\begin{bmatrix}
A&I
\end{bmatrix}\rightarrow\begin{bmatrix}
I&A^{-1}
\end{bmatrix}
$$

where $$E$$ is the elimination matrix. Here our $$A$$ is not an invertible matrix thus we do not have $$A^{-1}$$. But $$E$$ remembers our steps to get a rref $$R$$.

$$
E\begin{bmatrix}
A&I
\end{bmatrix}\rightarrow\begin{bmatrix}
R&E
\end{bmatrix}
$$

 Remember a null space is the combination of columns that produce a zero *column*. Right now we need a combination of rows that can produce a zero *row*. So when $$A$$ is $$m\times n$$,  in example $$(1)$$, 

$$
E=\begin{bmatrix}
-1&2&0\\
1&-1&0\\
-1&0&1
\end{bmatrix}
$$

And the last row of $$R$$ is all zeros! So from $$E$$ we see we produced an all-zero row by $$\begin{bmatrix}
-1&0&-1
\end{bmatrix}$$. This is the basis of left null space. 

## New Vector Space

We can make the collection of all $$3\times 3$$ matrices a vector space, call it $$M$$. A space is a vector space because we can have linear combinations of vectors in it. So does we can do it in a $$3\times 3$$ matrix. We can add, substract and multiply by constant to a matrix. 

Some subspaces of $$M$$ includes:

* all upper triangular matrices
* all symmetric matrices
* all diagonal matrices



