---
title: Properties of Determinants
layout: post
date: 2019-6-5
---


Every square matrix has a determinant associated with it. The determinant will be a test for invertibility, since it is faster(?) to compute it than to use eliminations to check if we have a full rank matrix. If determinant of some matrix is 0 then it is not invertible. And determinant got a lot more than that. We use $$\|A\|$$ or $$\det A$$ to represent matrix $$A$$'s determinant.

There're three properties of a determinant, and we can infer another seven from the basic ones:

1. $$\det I=1$$. 

2. Exchanging rows reverse the sign of determinant. Therefore $$\det P= 1/-1$$ if the number of exchanges is even/if odd

3. (a) If we multiply a row of the matrix with factor $$t$$, then the determinant will also be multiplied by $$t$$, that is $$\begin{vmatrix}
   ta & tb\\
   c & d
   \end{vmatrix} =t\begin{vmatrix}
   a & b\\
   c & d
   \end{vmatrix}$$

   (b) $$\begin{vmatrix}
   a+a' & b+b'\\
   c & d
   \end{vmatrix} =\begin{vmatrix}
   a & b\\
   c & d
   \end{vmatrix} +\begin{vmatrix}
   a' & b'\\
   c & d
   \end{vmatrix}$$ note that this is not saying $$\det(A+B)=\det(A)+\det(B)$$. This is linear in each row, separately. 

4. 2 equal rows $$\rightarrow \det=0$$. We can infer this from property 2. When we have two rows the same in a matrix, we can exchange those rows and get a inverse determinant. But the matrix in fact isn't changed at all just by switching rows. Adding these two determinant will give us zero. 

5. Subtracting a multiple of one row from the other does not change the determinant. This is saying, by property 3b. $$\begin{vmatrix}
   a & b\\
   c-ka & d-kb
   \end{vmatrix} =\begin{vmatrix}
   a & b\\
   c & d
   \end{vmatrix} +\begin{vmatrix}
   a & b\\
   -ka & -kb
   \end{vmatrix}$$. And from property 3a., $$\begin{vmatrix}
   a & b\\
   c & d
   \end{vmatrix} +\begin{vmatrix}
   a & b\\
   -kb & -kb
   \end{vmatrix} =\begin{vmatrix}
   a & b\\
   c & d
   \end{vmatrix} -k\begin{vmatrix}
   a & b\\
   a & b
   \end{vmatrix}$$, we factor out the $$-k$$, we finally see by property 4 same rows give us zero determinant, so it does not change the determinant of the original matrix. 

6. If any rows of a matrix is zero, then the determinant will be 0. We can use $$t=0$$ from 3a to obtain this.

7. Determinant of an upper triangular matrix $$U$$ is the product of all its diagonal items $$d_1*d_2*…*d_n$$. Suppose all $$d_i$$ are non-zeros. Then we can get a symmetric matrix by subtracting all numbers above the diagonal line. Note this does not affect the determinant by property 5. And we can use 3a to factor out each row's $$d_i$$ one by one, and what's left in the matrix is identity $$I$$. If there's any zero $$d_i$$,  we can make the whole row to zero by elimination, and get $$\det=0$$. 

8. $$\det A=0$$ iff $$A$$ is singular. For <-, If A is singular, we can get a row of zero. If A is non-singular, we get D and what's happened in property 7. 

9. $$\det{AB}=\det A *\det B$${%include sidenote.html note='This can be proved when later we know eigenvalues. We are just multiplying the eigenvalues of these two matrices'%}. From this we can get $$\det I=\det {A^{-1}A}=\det A*\det A^{-1}=1$$, then $$\det A^{-1}=\frac{1}{\det A}$$. Similar things happen for $$A^2$$ and etc. But note that $$\det 2A=2^n\det A$$ because we have 2 on every row. By property 3a we can get this, where $$n$$ is the number of rows.

10. $$\det A^\top=\det A$$ {%include sidenote.html note='$$\begin{aligned}
    \begin{vmatrix}
    A^{\top }
    \end{vmatrix} & =\begin{vmatrix}
    A
    \end{vmatrix}\\
    \begin{vmatrix}
    U^{\top } L^{\top }
    \end{vmatrix} & =\begin{vmatrix}
    LU
    \end{vmatrix}\\
    \begin{vmatrix}
    U^{\top }
    \end{vmatrix}\begin{vmatrix}
    L^{\top }
    \end{vmatrix} & =\begin{vmatrix}
    L
    \end{vmatrix}\begin{vmatrix}
    U
    \end{vmatrix}
    \end{aligned}$$ and both triangular, tranposed determinants are the same'%}. One implication is that from property 6, any column is zero will lead to determinant as 0. 

