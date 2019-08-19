---
layout: post
title: Preparation for Quant Interviews
---

Know the [Assumptions of Linear Regression](../sml/linear_regression) 

Regularization, Bias-Variance Trade off 

Why Gaussian Mixture fails at MLE gradient descent? (PRML)

### Little's test on Missingness

Little's test on Missingnessis is a test for checking whether the data is completely missing at random, which they term MCAR. So if some data are MCAR, missing completely at random, it means the missingness does not depend on anything. It just disappears at random, maybe because of measurement errors. In contrast, a lighter assumption is missing at random MAR; it means that the missingness depends on the observed data. So apparently this test is quite a strong one--can only test MCAR--and only for continuous variables, so it is in fact not widely used. And later during our research we gave up focusing on this test and moved to MICE. 

### EM

Jenson's inequality: let $f(·)$ be a convex function, then
$$
E[f(X)]\geq f(E[X])
$$
So as how the textbooks approach, the EM has E step and M step, which stand for expectation and maximization, and it's typically illustrated in the setting of gaussian mixture model. The E step is to build a lower bound on the likelihood function based on the current value of parameter of interest, in Gaussian Mixture it's mean vector, covariance matrix and class label; and the bound is often called ELBO, evidence lower bound and it's the same bound as variational inference; the M step is maximize the the parameter of interest w.r.t this lower bound instead of the whole likelihood function. 

(Why not MLE on GMM?)  

### MIRL

First off I have to admit MIRL is not a common techniques used to impute data. It is like a mashup of a handful of commonly used techniques. So the setting of this algorithm is to do regressions, but we have missing covariates X. The complete process is a bit complicated; in short, it first imputes the data by MICE, and unlike regular MICE we just do OLS on each imputed dataset and average the coefficients, they pooled the coefficients in a complex way such that they use random lasso to get an importance measure--basically it's just how big the imputed value, the bigger the more important--then they pool the coefficients along with these importance measure. 

But the real process involves much more delicacy such that they do bootstraps after MICE and they actually do not directly use the importance measure but instead use the importance measure as a probability, and things like that. 

In fact, the paper has many, I wouldn't say flaws, but ambiguity. Like they barely explain how they come up a such complex process. My professor and I guessed that they probably want to fix lasso used in imputations. So lasso has the problem that it may wrongly select the correlated variable. But the whole point of MICE is just to predict a somewhat reasonable dataset. Thus at this stage we just think why not ridge regression. It's good at prediction. And we don't really care about the variable selection because as their process presents, finally when they pool the coefficients they still don't have a sparse structure. 



(For these imputed datasets they bootstrapped them to generate B samples. Then they do random lasso. Random lasso is a two-step algorithms. First on each bootstrapped samples they estimate coefficients by LASSO, and based on these coefficients they calculate an importance measure. More importance this variable is, it's more likely on step 2, it's got selected on a regular OLS model. )

### Why not use EM?

because it requires us to have joint distribution assumptions on the variables. Sometimes, a conditional model would be more plausible. 



### Two-sample t-test 

First off, a $\chi^2$ random variable $U=\sum_{j=1}^mZ_j^2$ where $Z_1,Z_2,...$ are standard normal random variables. For instance,
$$
\frac{(n-1)S^2}{\sigma^2}=\frac{1}{\sigma^2}\sum_{i=1}^n(Y_i-\overline Y)^2
$$
 has a $\chi^2$ distribution with $n-1$ degrees of freedom. 

Then a t distributed random variable is
$$
T_n=\displaystyle\frac{Z}{\sqrt{\frac{U}{n}}}
$$
The bottom is $U$ with $n$ degrees of freedom.  One example would be testing the estimated coefficients on regression $\hat\beta_k$. To test if it has significant difference from $\beta_k$, it is a t statistic:
$$
t:=\frac{\hat\beta_k-\beta_k}{SE(\hat\beta_k)}=\frac{\hat\beta_k-\beta_k}{\sqrt{s^2*(\mathbf X^\top \mathbf X)^{-1}_{kk}}}
$$
Where the $s^2$ is the OLS estimate of the variance
$$
s^2=\frac{(\mathbf y-\hat{\mathbf y})^\top(\mathbf y-\hat{\mathbf y})}{n-p}
$$
And $p$ is the total number of variables/predictors ($\vert\mathbf x\vert$) we have.  Often we test against if we can reject the null hypothesis that $\beta_k=0$. In that case the test statistics is reduced to $\displaystyle \frac{\hat\beta_k}{\sqrt{s^2*(\mathbf X^\top \mathbf X)^{-1}_{kk}}}$. 



There're generally two cases of two-sample t-test, given that we often do not know the population variance (if we know that's a "normal" test). When we assume the two sample $X$ and $Y$ have the same population variance, the t statistic is
$$
t=\frac{\overline X-\overline Y}{s_p\sqrt{\frac{1}{n_X}+\frac{1}{n_Y}}}
$$
where
$$
s_p^2=\frac{(n_X-1)s^2_X+(n_Y-1)s^2_Y}{n_X+n_Y-2}
$$
If we assume they have different population variance, then
$$
t=\frac{\overline X-\overline Y}{\sqrt{\frac{s_X^2}{n_X}+\frac{s_Y^2}{n_Y}}}
$$
This is also known as the Welch's t-test. After we got the t statistic (this is the test statistic, a statistic is what's known from the sample, not a varying thing), then we calculate the p-value, which is $P(T>t)+P(T<-t)$, the probability of getting the test statistic under a standard t distribution. 

### What's Random Forest?

Random forest is a bunch of decision trees such that we build each tree using bootstrapped samples and during each split we only consider a limited number of variables.  

### What's generalized random forest? 

Generalized random forest is "generalized" in a sense that they can fit any moment conditions. That's an econometric model. So for different optimization problem they have different moment conditions, such as Maximum Likelihood Estimation the moment condition is expected gradient of log likelihood is zero. But OLS is expected inner product between x and error is zero. And for quantile regression and instrumental variable regression they have different ones as well. 



### How to avoid overfitting in neural network?

We can do regularization on the target function. A more deep learning way is to randomly drop some neurons during each iteration of training. That way each time there're fewer neurons trained to fit the data averagely thus avoiding overfitting. 



### Why not use sigmoid as activation function

The largest problem is that on very positive and very negative values, sigmoid will kill the gradient. This makes the gradient descent hard; the gradient may vanish. And exponential is a bit expensive to compute. 

### How did you use CNN to perform sentiment analysis?

So instead of doing a 2d convolution when processing image, we use 1d convolution on texts. Then after convolving the texts into a sequence of scores, we use these scores to predict or output the class that this piece of text belongs to. Obviously at first the output would be inaccurate, then we train the neural network with the data we had. 

### Nuisances of Tommaso's research (NLP)

The original goal of performing the sentiment analysis was to analyze not only the positivity of user's review, but it's also for whether a review demonstrates a "taste". So in marketing they like defining vertical and horizontal differentiation. Vertical is just difference in quality, and horizontal is like they have different traits, one is good at A the other good at B things like that. So to apply the concept here, we're testing whether an user's review demonstrate vertical and horizontal differentiation. So it's just a binary evaluation. 

And ultimately we want to regress variance of a review's rating on these two differentiation, and we're interested in seeing the horizontal variation of a review will contribute more to the variance of rating. 

## CS

### How did you implement the chat feature?

So we used web socket. Web sockets are like openings on both ends server side and client side. Unlike the HTML requests or something, there's no additional requests being sent, as long as we put the socket codes on both end. That is, if user A types a message want to send to the chat room, the server receives the message, and it broadcasts or sends to the particular user, including user A itself because we see what we send. 

### Challenge

The most difficult task up to now is probably the machine learning class project. On that final project, the professor requires us to read cutting-edge research paper and come up with interesting application idea or modify current methods. It took me and my teammate a lot of time to find the appropriate idea, one that is not boring but not agonizingly difficult to tackle. Then the coding part was torturing somehow because deep learning model is like a maze and very difficult to search out the not-working part in a limited amount of time. 

I finally get that through by understanding the author's code and modify it. As I said, we were modifying other's ideas. At first the author's code seemed desparatedly complicated. But with patience and carefulness we finally managed to correctly change the part we need and obtain the expected results. What I learnt the most was probably never give up ... there're a lot of moments that I or my teammate try to give up the idea but we encourage each other and finally made it through 



## Behavioral Questions

Impression; Personal brand;

Your Story; Tell the story in an engaging way so make others want to become part of it

Know my strengths and weakness 





MS: Raise, invest and manage money 

















Why Quant?







markov matrix；恶补sto 



