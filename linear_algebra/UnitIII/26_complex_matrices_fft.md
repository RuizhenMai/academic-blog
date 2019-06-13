---
layout: post
title: Complex Matrices; Fast Fourier Transform (FFT)
date: 2019-6-13
---

## Fourier Matrix and FFT

The $$4\times 4$$ <u>Fourier matrix</u> is in the following form: 
$$
F_4=\begin{bmatrix}
1 & 1 & 1  &1\\
1 & i & i^2 & i^3\\
1 & i^2 & i^4 & i^6\\
1 & i^3 & i^6 & i^9
\end{bmatrix}
$$
where $$F_{ij}=w^{ij}_n$$ and $$w_n^{n}=1$$. And since $$w^{n}_n=1$$, we have:
$$
w_n=e^{i\cdot2\pi/n}
$$
Here $$n=4$$. $$w_4=e^{i\cdot2\pi/4}=i$$ because $$i^4=1$$. And $$n\times n$$ Fourier matrix is
$$
F_n=\begin{bmatrix}
1 & 1 & 1  &1 & ...\\
1 & w & w^2 & w^3 &...\\
1 & w^2 & w^4 & w^6 & ...\\
1 & w^3 & w^6 & w^9 &... \\
... & ... & ... & ... & ...
\end{bmatrix}
$$
One fact is that $$w_{n/2}^2=w_n$$, for instance, $$w_4^2=w_8$$. Therefore there would be some connections between $$F_{n/2}$$ and $$ F_n$$, if we make it right. 