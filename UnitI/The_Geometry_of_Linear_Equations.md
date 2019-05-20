---
layout: post
title: Introduction 
date: 2019-5-20
---



The fundamental problem is linear algebra is to solve a system of equation. 

A normal, nice case(for now) is to have N equations and N unknowns. 

An exmaple, 

$$
\begin{aligned}
2x-y & =0\\
-x+2y & =3
\end{aligned}
$$

writing in the form of a product of coefficient matrix and unknown vector, 

$$
\left[\begin{matrix}
2 & -1\\
-1 & 2
\end{matrix}\right]
\left[\begin{matrix}
x\\
y
\end{matrix}\right]=\left[\begin{matrix}\tag{1}
0\\
3
\end{matrix}\right]
$$

in short, this matrix is in the form of:

$$
A\mathbf{x}=\mathbf{b}
$$

### Row picture: 

<p align="center" style="text-align: center;"><img align="center" src="https://tex.s2cms.ru/svg/%5Cbegin%7Btikzpicture%7D%5Bscale%3D1.0544%5D%5Csmall%0A%5Cbegin%7Baxis%7D%5Baxis%20line%20style%3Dgray%2C%0A%09samples%3D120%2C%0A%09width%3D6.0cm%2Cheight%3D6.4cm%2C%0A%09xmin%3D-2.5%2C%20xmax%3D2.5%2C%0A%09ymin%3D-2.5%2C%20ymax%3D2.5%2C%0A%09%25restrict%20y%20to%20domain%3D-2%3A2%2C%0A%09ytick%3D%7B-2%2C-1%2C0%2C1%2C2%7D%2C%0A%09xtick%3D%7B-2%2C-1%2C0%2C1%2C2%7D%2C%0A%09axis%20equal%2C%0A%09axis%20x%20line%3Dcenter%2C%0A%09axis%20y%20line%3Dcenter%2C%0A%09xlabel%3D%24x%24%2Cylabel%3D%24y%24%5D%0A%25%5Caddplot%5Bred%2Cdomain%3D-2%3A1%2Csemithick%5D%7Bexp(x)%7D%3B%0A%5Caddplot%5Bcolor%20%3D%20%7Brgb%3Ared%2C181%3Bgreen%2C23%3Bblue%2C23%7D%2Cline%20width%20%3D%201pt%5D%7Bx%2F2%2B3%2F2%7D%3B%0A%5Caddplot%5Bcolor%20%3D%20%7Brgb%3Ared%2C16%3Bgreen%2C133%3Bblue%2C152%7D%2C%20line%20width%20%3D%201pt%5D%7B2*x%7D%3B%0A%5Caddplot%5B%5D%20coordinates%20%7B(2%2C3)%7D%20node%7B%242x-y%3D0%24%7D%3B%0A%5Caddplot%5B%5D%20coordinates%20%7B(-1.5%2C1.5)%7D%20node%7B%24-x%2B2y%3D3%24%7D%3B%0A%5Caddplot%5Bcolor%20%3D%20%7Brgb%3Ared%2C146%3Bgreen%2C98%3Bblue%2C74%7D%2Cmark%3D*%5D%20coordinates%20%7B(1%2C2)%7D%3B%0A%25zero%20node%0A%5Cpath%20(axis%20cs%3A0%2C0)%20node%20%5Banchor%3Dnorth%20west%2Cyshift%3D-0.07cm%5D%20%7B0%7D%3B%0A%5Cend%7Baxis%7D%0A%5Cend%7Btikzpicture%7D" alt="\begin{tikzpicture}[scale=1.0544]\small
\begin{axis}[axis line style=gray,
	samples=120,
	width=6.0cm,height=6.4cm,
	xmin=-2.5, xmax=2.5,
	ymin=-2.5, ymax=2.5,
	%restrict y to domain=-2:2,
	ytick={-2,-1,0,1,2},
	xtick={-2,-1,0,1,2},
	axis equal,
	axis x line=center,
	axis y line=center,
	xlabel=$x$,ylabel=$y$]
%\addplot[red,domain=-2:1,semithick]{exp(x)};
\addplot[color = {rgb:red,181;green,23;blue,23},line width = 1pt]{x/2+3/2};
\addplot[color = {rgb:red,16;green,133;blue,152}, line width = 1pt]{2*x};
\addplot[] coordinates {(2,3)} node{$2x-y=0$};
\addplot[] coordinates {(-1.5,1.5)} node{$-x+2y=3$};
\addplot[color = {rgb:red,146;green,98;blue,74},mark=*] coordinates {(1,2)};
%zero node
\path (axis cs:0,0) node [anchor=north west,yshift=-0.07cm] {0};
\end{axis}
\end{tikzpicture}" /></p>

By finding a line for the first equation and for second equation(two point method) in the example, we can see an intersection point $$(1,2)$$ that can solve both equations.  

### Column Picture:

Rewriting the equation $$(1)$$ to expand $$x$$ and $$y$$, 


$$
x\left[\begin{matrix}
2\\
-1
\end{matrix}\right] +y\left[\begin{matrix}
-1\\
2
\end{matrix}\right] =\left[\begin{matrix}
0\\
3
\end{matrix}\right]
$$


right now the equation is asking us to find the right amount of $$x$$ and $$y$$ to combine the two vectors on the right of them to produce the correct output $$\left[\begin{matrix}0\\3\end{matrix}\right]$$. This is equivalent to find the right linear combination of the columns(vectors). Finding a linear combination of something is a fundemental operation in linear algbera. View it in picture:

<p align="center" style="text-align: center;"><img align="center" src="https://tex.s2cms.ru/svg/%5Cbegin%7Btikzpicture%7D%5Bscale%3D1.0544%5D%5Csmall%0A%5Cbegin%7Baxis%7D%5Baxis%20line%20style%3Dgray%2C%0A%09samples%3D120%2C%0A%09width%3D6.0cm%2Cheight%3D6.4cm%2C%0A%09xmin%3D-2.5%2C%20xmax%3D2.5%2C%0A%09ymin%3D-1.5%2C%20ymax%3D3.5%2C%0A%09%25restrict%20y%20to%20domain%3D-2%3A2%2C%0A%09ytick%3D%7B-1%2C0%2C1%2C2%2C3%7D%2C%0A%09xtick%3D%7B-2%2C-1%2C0%2C1%2C2%7D%2C%0A%09axis%20equal%2C%0A%09axis%20x%20line%3Dcenter%2C%0A%09axis%20y%20line%3Dcenter%2C%0A%09xlabel%3D%24x%24%2Cylabel%3D%24y%24%5D%0A%5Caddplot%5B-%3E%2Ccolor%20%3D%20%7Brgb%3Ared%2C181%3Bgreen%2C23%3Bblue%2C23%7D%2C%20line%20width%20%3D%201pt%5D%20coordinates%0A%20%20%20%20%20%20%20%20%20%20%20%7B(0%2C0)%20(2%2C-1)%7D%3B%0A%5Caddplot%5B-%3E%2Ccolor%20%3D%20%7Brgb%3Ared%2C16%3Bgreen%2C133%3Bblue%2C152%7D%2C%20line%20width%20%3D%201pt%5D%20coordinates%20%7B(0%2C0)%20(-1%2C2)%7D%3B%0A%5Caddplot%5Bdashed%2C%20-%3E%2Ccolor%20%3D%20%7Brgb%3Ared%2C16%3Bgreen%2C133%3Bblue%2C152%7D%2C%20line%20width%20%3D%201pt%5D%20coordinates%20%7B(2%2C-1)%20(1%2C1)%7D%3B%0A%5Caddplot%5Bdashed%2C%20-%3E%2Ccolor%20%3D%20%7Brgb%3Ared%2C16%3Bgreen%2C133%3Bblue%2C152%7D%2C%20line%20width%20%3D%201pt%5D%20coordinates%20%7B(1%2C1)%20(0%2C3)%7D%3B%0A%5Caddplot%5B-%3E%2Ccolor%20%3D%20%7Brgb%3Ared%2C66%3Bgreen%2C177%3Bblue%2C8%7D%2C%20line%20width%20%3D%201pt%5D%20coordinates%20%7B(0%2C0)%20(0%2C3)%7D%3B%0A%5Caddplot%5Bcolor%20%3D%20%7Brgb%3Ared%2C66%3Bgreen%2C177%3Bblue%2C8%7D%5D%20coordinates%20%7B(0.7%2C3)%7D%20node%7B%24%5Cleft%5B%5Cbegin%7Barray%7D%7B%40%7B%7Dc%40%7B%7D%7D%0A%20%20%20%200%20%5C%5C%0A%20%20%20%203%20%5C%5C%0A%20%20%20%20%5Cend%7Barray%7D%20%5Cright%5D%24%7D%3B%0A%5Caddplot%5Bcolor%20%3D%20%7Brgb%3Ared%2C181%3Bgreen%2C23%3Bblue%2C23%7D%5D%20coordinates%20%7B(2.5%2C-1)%7D%20node%7B%24%5Cleft%5B%5Cbegin%7Barray%7D%7B%40%7B%7Dc%40%7B%7D%7D%0A%20%20%20%202%20%5C%5C%0A%20%20%20%20-1%20%5C%5C%0A%20%20%20%20%5Cend%7Barray%7D%20%5Cright%5D%24%7D%3B%0A%5Caddplot%5Bcolor%20%3D%20%7Brgb%3Ared%2C16%3Bgreen%2C133%3Bblue%2C152%7D%5D%20coordinates%20%7B(-1%2C2.5)%7D%20node%7B%24%5Cleft%5B%5Cbegin%7Barray%7D%7B%40%7B%7Dc%40%7B%7D%7D%0A%20%20%20%20-1%20%5C%5C%0A%20%20%20%202%20%5C%5C%0A%20%20%20%20%5Cend%7Barray%7D%20%5Cright%5D%24%7D%3B%0A%25zero%20node%0A%5Cpath%20(axis%20cs%3A0%2C0)%20node%20%5Banchor%3Dnorth%20west%2Cyshift%3D-0.07cm%5D%20%7B0%7D%3B%0A%5Cend%7Baxis%7D%0A%5Cend%7Btikzpicture%7D" alt="\begin{tikzpicture}[scale=1.0544]\small
\begin{axis}[axis line style=gray,
	samples=120,
	width=6.0cm,height=6.4cm,
	xmin=-2.5, xmax=2.5,
	ymin=-1.5, ymax=3.5,
	%restrict y to domain=-2:2,
	ytick={-1,0,1,2,3},
	xtick={-2,-1,0,1,2},
	axis equal,
	axis x line=center,
	axis y line=center,
	xlabel=$x$,ylabel=$y$]
\addplot[-&gt;,color = {rgb:red,181;green,23;blue,23}, line width = 1pt] coordinates
           {(0,0) (2,-1)};
\addplot[-&gt;,color = {rgb:red,16;green,133;blue,152}, line width = 1pt] coordinates {(0,0) (-1,2)};
\addplot[dashed, -&gt;,color = {rgb:red,16;green,133;blue,152}, line width = 1pt] coordinates {(2,-1) (1,1)};
\addplot[dashed, -&gt;,color = {rgb:red,16;green,133;blue,152}, line width = 1pt] coordinates {(1,1) (0,3)};
\addplot[-&gt;,color = {rgb:red,66;green,177;blue,8}, line width = 1pt] coordinates {(0,0) (0,3)};
\addplot[color = {rgb:red,66;green,177;blue,8}] coordinates {(0.7,3)} node{$\left[\begin{array}{@{}c@{}}
    0 \\
    3 \\
    \end{array} \right]$};
\addplot[color = {rgb:red,181;green,23;blue,23}] coordinates {(2.5,-1)} node{$\left[\begin{array}{@{}c@{}}
    2 \\
    -1 \\
    \end{array} \right]$};
\addplot[color = {rgb:red,16;green,133;blue,152}] coordinates {(-1,2.5)} node{$\left[\begin{array}{@{}c@{}}
    -1 \\
    2 \\
    \end{array} \right]$};
%zero node
\path (axis cs:0,0) node [anchor=north west,yshift=-0.07cm] {0};
\end{axis}
\end{tikzpicture}" /></p>


As we have already found the solution to $$x$$ and $$y$$ which is 1 and 2, we can plug in and get the combination of column vectors to produce the final output. This is, 1 of column vector 1($$\left[\begin{matrix}2\\-1\end{matrix}\right]$$), 2 of column vector 2 then we can get $$\left[\begin{matrix}0\\3\end{matrix}\right]$$. Next class the professor will discuss the general method of solving system of equations.

We also see why this is a "column picture" because the column vectors are part of the coefficient matrix. 

Let's do a more complex example with three unknowns:

$$
A=\left[\begin{matrix}
2 & -1 & 0\\
-1 & 2 & -1\\
0 & -3 & 4
\end{matrix}\right] ,b=\left[\begin{matrix}
0\\
-1\\
4
\end{matrix}\right]
$$

Then if we do a row picture, then we have 


$$
\begin{aligned}
2x-y&=0\\
-x+2y-z&=-1\\
-y+4z&=4
\end{aligned}
$$


The first and third equation will be a line. The second one will be a plane. It's much harder to visualize in 3-D where the intersection will be. You can try draw it out. Then we can resort to column picture:


$$
x\left[\begin{matrix}2\\-1\\0\end{matrix}\right]+y\left[\begin{matrix}-1\\2\\-3\end{matrix}\right]+z\left[\begin{matrix}0\\-1\\4\end{matrix}\right]=\left[\begin{matrix}0\\-1\\4\end{matrix}\right]
$$


It's easy to see that the righthand side column is equal to 1 of the z's column vector. Then the solution point will be $$(0,0,1)$$. 

### Linear Independence:

Can we solve $$A\mathbf{x}=\mathbf{b}$$ for every righthand side? In other words, do the linear combination of the columns fill 3-D space? The answer is yes in this case, because the three vectors are independent. Any two of them cannot constitute the third one. This reasoning is same in high dimensional case. If there's some of the vectors, in general $$n-1$$, can compose another vector in the matrix, then this matrix cannot span the whole space.






