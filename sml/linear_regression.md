---
layout: post
title: "Linear Regression: Assumptions and Inference"
---

Linear regression model, using vector notations to write is

$$
\mathbf y=\mathbf X\boldsymbol\beta+\boldsymbol\epsilon
$$

### Assumption 1: Linearity 

This means that the interaction between the parameter $\boldsymbol\beta$ and the variable $\mathbf x_i$ is just in linear way:

$$
\mathbf x_i^\top\boldsymbol\beta=x_{i1}\beta_1+...+x_{ip}\beta_p
$$

(Assuming there're total p variable)  Variables cannot interact with each other such as $x_{i1}*x_{i2}$ .This assumptions is somewhat but not entirely relaxed in generalized linear model. In GLM, the linearity is allowed to happened in the exponents of $e$. For instance, logistic regression and poisson. 

### Assumption 2: Exogeneity

In mathematical notations:

$$
E[\epsilon\vert x_1,...,x_p]=0
$$

This is saying that the error term does not correlate with the variables. Setting the above $E[\cdot]$ to zero is just for convenience, as long as the right-hand does not contain any $x$ terms it's fine. Because any constants can be moved to the right of the constant parameter. To test for exogeneity/endogeneity, we can just do a regression of $\boldsymbol\epsilon$ on the data we collected $\mathbf X$, and see if it gives all $\mathbf x_i$ relatively 0 coefficients. Or more efficiently we can just look at the Residuals vs Fitted plot and check if the expected value of $\epsilon$ is centered at 0. 

By law of total expectation, we can have 

$$
E_{\mathbf x}[E[\epsilon\vert x_1,...,x_p]]=E[\epsilon]=0
$$

Strict exogeneity involves with data, asides from requiring the error $\epsilon_i$ independent of its own data subject's predictor $\mathbf x^{(i)}$, the error also needs to be independent of other predictor $\mathbf x^{(k)}$. Rewrite the original exogeneity a bit:

$$
E[\epsilon_i\vert{x}_1^{(i)},..., x_p^{(i)}]
$$

The strict exogeneity is:

$$
E[\epsilon_i\vert\mathbf x^{(i=1)},...,\mathbf x^{(n)}]=E[\epsilon_i\vert \mathbf X]=0
$$

Exogeneity implies a lot of useful stuffs. 

@todo 

If exogeneity is violated, the estimated $\beta_k,k\in\{1,..,p\}$ will be biased. 

### Assumption 3: Full Rank

This means the "design" matrix $\mathbf X$ is full column rank, otherwise $\mathbf X^\top\mathbf X$ is not invertible. In high-dimension setting, $\mathbf X$ is doomed to not have full column rank because $\mathbf X:n\times p$ has $n< p$.  (Like I have one data $n=1$, and two variable equal 1 and 2, it's not full rank) 

Note, a nearly not full column rank $\mathbf X$ is not a violation of this assumption. It's more of violating the homoskedacity assumption

### Assumption 4: Homoskedacity

There could be other names but, generally this assumption involves:
$$
Var[\epsilon]=\sigma^2;\\
E[\epsilon_i\epsilon_j]=0
$$


### Assumption 5: Normal distributed 



### What happened if we copy the whole dataset $\mathbf X$ and $\mathbf y$ exactly once?

Let's state the answer first. The estimated coefficients won't change, but the standard error will go down and it's more prone to a type I error. 

First off, 
$$
\hat\beta=\arg\min_\beta\Vert\mathbf y-\mathbf X\boldsymbol\beta\Vert_2^2
$$
It probably makes more intuitive sense than just look at the equation. As we're copying the original information, there's no new information added, there's no need to change $\hat \beta$ to adjust for any things. But the standard error of $\hat\beta$ will change. Refer to [interview prep](./math_finance/interview_prep), the t statistic for $\hat\beta$ is
$$
t:=\frac{\hat\beta_k}{\sqrt{s^2*(\mathbf X^\top \mathbf X)^{-1}_{kk}}}
$$
The bottom is the standard error. If we use an OLS estimate to population variance, then $\displaystyle s^2=\frac{(\mathbf y-\hat{\mathbf y})^\top(\mathbf y-\hat{\mathbf y})}{n-p}$. If we double the size, clearly $n$ will become $2n$ and $s^2$ goes down. Also, let's say 
$$
\mathbf X=\begin{bmatrix}1\\2\\3\\4\end{bmatrix}
$$
Then $X^\top X=30$, if we double the size, $X^\top X$ becomes 60 (it has $[1,2,3,4,1,2,3,4]^\top$). Thus $X^\top X$ increases and its inverse $(X^\top X)^{-1}$ decreases. Thus the absolute value of t statistic will go up. 