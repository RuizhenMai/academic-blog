---
layout: post
title: Projections onto Subspaces
date: 2019-6-2
---

## Projections

<figure><img style="align-content: center; margin-left: auto; margin-right: auto; display: block;"  src="https://tex.s2cms.ru/svg/%5Cbegin%7Btikzpicture%7D%5Bscale%3D1.0544%5D%5Csmall%0A%5Cbegin%7Baxis%7D%5Baxis%20line%20style%3Dgray%2C%0A%09samples%3D120%2C%0A%09width%3D6.0cm%2Cheight%3D6.4cm%2C%0A%09xmin%3D-1.5%2C%20xmax%3D3.5%2C%0A%09ymin%3D-1.5%2C%20ymax%3D3.5%2C%0A%09%25restrict%20y%20to%20domain%3D-2%3A2%2C%0A%09ytick%3D%7B-1%2C0%2C1%2C2%2C3%7D%2C%0A%09xtick%3D%7B-1%2C0%2C1%2C2%2C3%7D%2C%0A%09axis%20equal%2C%0A%09axis%20x%20line%3Dcenter%2C%0A%09axis%20y%20line%3Dcenter%2C%0A%09xlabel%3D%24x%24%2Cylabel%3D%24y%24%5D%0A%5Caddplot%5B-%3E%2Ccolor%20%3D%20%7Brgb%3Ared%2C181%3Bgreen%2C23%3Bblue%2C23%7D%2C%20line%20width%20%3D%201pt%5D%20coordinates%0A%20%20%20%20%20%20%20%20%20%20%20%7B(0%2C0)%20(3%2C1.5)%7D%3B%0A%5Caddplot%5B-%3E%2Ccolor%20%3D%20%7Brgb%3Ared%2C16%3Bgreen%2C133%3Bblue%2C152%7D%2C%20line%20width%20%3D%201pt%5D%20coordinates%20%7B(0%2C0)%20(1%2C2)%7D%3B%0A%25p%0A%5Caddplot%5B-%3E%2Ccolor%20%3D%20%7Brgb%3Ared%2C16%3Bgreen%2C133%3Bblue%2C152%7D%2C%20line%20width%20%3D%201pt%5D%20coordinates%20%7B(0%2C0)%20(1.6%2C0.8)%7D%3B%0A%25e%0A%5Caddplot%5Bdashed%2C%20-%3E%2Ccolor%20%3D%20%7Brgb%3Ared%2C66%3Bgreen%2C177%3Bblue%2C8%7D%2C%20line%20width%20%3D%201pt%5D%20coordinates%20%7B(1.6%2C0.8)%20(1%2C2)%7D%3B%0A%25%20red%20vector%20label%0A%5Caddplot%5Bcolor%20%3D%20%7Brgb%3Ared%2C181%3Bgreen%2C23%3Bblue%2C23%7D%5D%20coordinates%20%7B(3%2C1.8)%7D%20node%7B%24%5Cmathbf%20a%24%7D%3B%0A%25%20blue%20vector%20label%0A%5Caddplot%5Bcolor%20%3D%20%7Brgb%3Ared%2C16%3Bgreen%2C133%3Bblue%2C152%7D%5D%20coordinates%20%7B(1%2C2.3)%7D%20node%7B%24%5Cmathbf%20b%24%7D%3B%0A%25%20dashed%20vector%20label%0A%5Caddplot%5Bcolor%20%3D%20%7Brgb%3Ared%2C66%3Bgreen%2C177%3Bblue%2C8%7D%5D%20coordinates%20%7B(1.5%2C1.5)%7D%20node%7B%24%5Cmathbf%20e%24%7D%3B%0A%25%20p%20vector%20label%0A%5Caddplot%5Bcolor%20%3D%20%7Brgb%3Ared%2C16%3Bgreen%2C133%3Bblue%2C152%7D%5D%20coordinates%20%7B(1.5%2C0.4)%7D%20node%7B%24%5Cmathbf%20p%24%7D%3B%0A%25zero%20node%0A%5Cpath%20(axis%20cs%3A0%2C0)%20node%20%5Banchor%3Dnorth%20west%2Cyshift%3D-0.07cm%5D%20%7B0%7D%3B%0A%5Cend%7Baxis%7D%0A%5Cend%7Btikzpicture%7D" alt="\begin{tikzpicture}[scale=1.0544]\small
\begin{axis}[axis line style=gray,
	samples=120,
	width=6.0cm,height=6.4cm,
	xmin=-1.5, xmax=3.5,
	ymin=-1.5, ymax=3.5,
	%restrict y to domain=-2:2,
	ytick={-1,0,1,2,3},
	xtick={-1,0,1,2,3},
	axis equal,
	axis x line=center,
	axis y line=center,
	xlabel=$x$,ylabel=$y$]
\addplot[-&gt;,color = {rgb:red,181;green,23;blue,23}, line width = 1pt] coordinates
           {(0,0) (3,1.5)};
\addplot[-&gt;,color = {rgb:red,16;green,133;blue,152}, line width = 1pt] coordinates {(0,0) (1,2)};
%p
\addplot[-&gt;,color = {rgb:red,16;green,133;blue,152}, line width = 1pt] coordinates {(0,0) (1.6,0.8)};
%e
\addplot[dashed, -&gt;,color = {rgb:red,66;green,177;blue,8}, line width = 1pt] coordinates {(1.6,0.8) (1,2)};
% red vector label
\addplot[color = {rgb:red,181;green,23;blue,23}] coordinates {(3,1.8)} node{$\mathbf a$};
% blue vector label
\addplot[color = {rgb:red,16;green,133;blue,152}] coordinates {(1,2.3)} node{$\mathbf b$};
% dashed vector label
\addplot[color = {rgb:red,66;green,177;blue,8}] coordinates {(1.5,1.5)} node{$\mathbf e$};
% p vector label
\addplot[color = {rgb:red,16;green,133;blue,152}] coordinates {(1.5,0.4)} node{$\mathbf p$};
%zero node
\path (axis cs:0,0) node [anchor=north west,yshift=-0.07cm] {0};
\end{axis}
\end{tikzpicture}" /><figcaption style="text-align: center; font-family: MJXc-TeX-math-I,MJXc-TeX-math-Ix,MJXc-TeX-math-Iw; font-size: 1.1rem;">Figure 1. Vector p projecting into vector a; resulting in p=xa; e=b-p</figcaption></figure>



Let's start with an example. On Figure 1, We have $$\mathbf a$$ and $$\mathbf b$$ both are one dimensional line in $$\mathbb R^2$$. We project $$\mathbf b$$ into $$\mathbf a$$, and obtain its <u>projected vector</u> $$\mathbf p=x\mathbf a$$ where $$x$$ (fraction here) is a constant, and the <u>distance</u> between the original and projected one $$\mathbf e=\mathbf b - \mathbf p$$. Since $$\mathbf a$$ and $$\mathbf e$$ is orthogonal, we have the following equation: 

$$
\begin{align}
\mathbf a^\top\mathbf e&=0\tag{1}\\
\mathbf a^\top(\mathbf b-\mathbf p)&=0\\
\mathbf a^\top(\mathbf b-x\mathbf a)&=0\\
\end{align}
$$

Solving it we get $$\displaystyle x=\frac{\mathbf a^\top \mathbf b}{\mathbf a^\top \mathbf a}$$, and thus (x is constant so we can put it left or right)

$$
\mathbf p=\mathbf a \frac{\mathbf a^\top \mathbf b}{\mathbf a^\top \mathbf a}\tag{2}
$$

Right now let's separate $$\mathbf {a\ b}$$ in eq. (2). Let $$\displaystyle P=\frac{\mathbf a \mathbf a^\top}{\mathbf a^\top \mathbf a}$$ be the <u>projection matrix</u> . We rewrite eq. (1) as $$\mathbf p=P\mathbf b$$. $$P$$ is a very interesting matrix. What's the column space of it? Since $$\mathbf b$$ is an arbitrary vector put to the right of $$P$$, and we get $$\mathbf p$$ from it, no doubt:

$$
C(P)=the\ line\ thru\ \mathbf a;\\
rank(P)=1
$$

What else? Hope you notice $$P$$ is symmetric by looking at the numerator [(lecture 5)](UnitI/Transposes,Permutation,Vector_Spaces). One other thing is that when we project a vector into $$\mathbf a$$ twice, it's the same vector (checkout multiply $$\mathbf p$$ by $$P$$ again). Therefore 

$$
P^\top=P;P^2=P
$$

### Why project?

We've talked last time that $$A\mathbf x=\mathbf b$$ may not have solutions. $$A\mathbf x$$ is in the column space but $$\mathbf b$$ may not. What can we do is to solve the closest equation to $$A\mathbf x=\mathbf b$$, which is 

$$
A\mathbf x=\mathbf p\tag{3}
$$

where $$\mathbf p$$ is the projection of $$\mathbf b$$ into the column space of $$A$$. And we can name this $$\mathbf x$$ as $$\hat{\mathbf x}$$ since it's not the original $$\mathbf x$$. So how to do this projection? Similar to above, but this time we want a general formula rather than when $$\mathbf a$$ is a line. So imagine $$C(A)$$ is a plane, constituted by the linear combinations of column vectors in $$A$$ which are $$\mathbf a_1,\mathbf a_2,…\mathbf a_n$$. What projection can project $$\mathbf b$$ into $$C(A)$$ and the distance between $$\mathbf b$$ and $$\mathbf p$$, which is $$\mathbf e$$ is perpendicular to the plane $$C(A)$$ ? That is, first $$\mathbf a_1^\top \mathbf e=0$$. The vectors on the plane of $$C(A)$$ is perpendicular to $$\mathbf e$$, so are other vectors $$\mathbf a_2^\top \mathbf e=0,…,\mathbf a_n^\top \mathbf e=0$$. Therefore,

$$
\begin{align}
\mathbf a_1^\top \mathbf e+\mathbf a_2^\top \mathbf e+…+\mathbf a_n^\top \mathbf e&=0\\
\begin{bmatrix}
\mathbf a_1^\top&...&\mathbf a_n^\top
\end{bmatrix}&\mathbf e=0\\
A^\top \mathbf e&=0\\
\end{align}
$$

What's $$\mathbf e$$? It's same as before $$\mathbf e=\mathbf b-\mathbf p$$. $$\mathbf p$$ is on eq. (3), we just change $$\mathbf x$$ into $$\hat{\mathbf x}$$:

$$
\begin{align}
A^\top \mathbf e&=0\\
A^\top (\mathbf b-A\hat{\mathbf x})&=0\\
\end{align}\tag{4}
$$

Solve eq. (4):

$$
\begin{align}
A^\top (\mathbf b-A\hat{\mathbf x})&=0\\
A^\top \mathbf b&=A^\top A\hat{\mathbf x}\\
A^\top A\hat{\mathbf x}&=A^\top \mathbf b\\
\hat{\mathbf x}&=(A^\top A)^{-1}A^\top \mathbf b
\end{align}\tag{5}
$$

Then the projected vector $$\mathbf p$$ is just 

$$
\mathbf p=A(A^\top A)^{-1}A^\top \mathbf b
$$

And the projection matrix $$P$$ is 

$$
P=A(A^\top A)^{-1}A^\top 
$$

<u>Warning</u>: since $$A$$ is not required to be a square matrix, we cannot do $$(A^\top A)^{-1}=A^{-1}A^{\top -1}$$. $$A^\top A$$ is square. But still, $$A^\top A$$ is invertible if only if $$A$$ is full column rank or square. 

### Least Square preview

@todo

