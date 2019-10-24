---
layout: post
title: Preparation for Quant Interviews Technical
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

Generalized random forest is a weighted random forest. Each tree has different weights. By the weighting, it has some benefits like unbiasedness, and the prediction produced by the forest is asymptotically normal so that we can produce a valid confidence invervals. The reason why is called "generalized", ... 



Generalized random forest is "generalized" in a sense that they can fit any moment conditions. So for different optimization problem they have different moment conditions, such as Maximum Likelihood Estimation the moment condition is expected gradient of log likelihood is zero. But OLS is expected inner product between x and error is zero. And for quantile regression and instrumental variable regression they have different ones as well. 



### How to avoid overfitting in neural network?

We can do regularization on the target function. A more deep learning way is to randomly drop some neurons during each iteration of training. That way each time there're fewer neurons trained to fit the data averagely thus avoiding overfitting. 



### Why not use sigmoid as activation function

The largest problem is that on very positive and very negative values, sigmoid will kill the gradient. This makes the gradient descent hard; the gradient may vanish. And exponential is a bit expensive to compute. 

### How did you use CNN to perform sentiment analysis?

So instead of doing a 2d convolution when processing image, we use 1d convolution on texts. Then after convolving the texts into a sequence of scores, we use these scores to predict or output the class that this piece of text belongs to. Obviously at first the output would be inaccurate, then we train the neural network with the data we had. 

### Nuisances of Tommaso's research (NLP)

The original goal of performing the sentiment analysis was to analyze not only the positivity of user's review, but it's also for whether a review demonstrates a "taste". So in marketing they like defining vertical and horizontal differentiation. Vertical is just difference in quality, and horizontal is like they have different traits, one is good at A the other good at B things like that. So to apply the concept here, we're testing whether an user's review demonstrate vertical and horizontal differentiation. So it's just a binary evaluation. 

And ultimately we want to regress variance of a review's rating on these two differentiation, and we're interested in seeing the horizontal variation of a review will contribute more to the variance of rating. (Meaning there exists different opinions)

### Some goals of Tommaso's research

1. Introduce the setup, background, need, problems to be solved
2. Tell the assumptions of the model
3. The detailed approach of the model
4. Results, limit of the model 

There're several objective of Tommas's research, it makes me feel that it can be divided into two to three papers to be published. One that I'm most familiar with is variance of ratings for a polarizing product will be smaller, and its rating will be biased upward. The other is that user, or in this setting, readers actually converge individually in their taste, but as an entity diverges. To put it simple, it means that if a new reader starts browswing around all kinds of books, maybe sci-fi, suspense, politics and so on; then this user becomes more experienced, he will become more focused on one specific, maybe scifi. 



## OOP

### How did you implement the chat feature?

So we used web socket. Web sockets are like openings on both ends server side and client side. Unlike the HTML requests or something, there's no additional requests being sent, as long as we put the socket codes on both end. That is, if user A types a message want to send to the chat room, the server receives the message, and it broadcasts or sends to the particular user, including user A itself because we see what we send. 

### Default Constructor

Python doesn't have default constructor. We have to explicitly write it out. 

### Overloading

Note, python does not support *overloading*. It's done so by specifying default parameters, and check if the default parameters exist to create "branches" to work like overloading. 

Thus, note that Java does not support *default parameters*. 

But, C++ supports both. 

### Stack vs Heap Memory

Stack and Heap are two big chunks of memory in the RAM; there're others but they don't occupy that much. Stack is for static allocation, while Heap is for dynamic allocation. For data in stack, they're removed after the scope of the function/class is finished; as for data in heap, they need to be deleted manually, and they exist until we delete it. 

### Static variables and static methods

Static variable is unique across all object instances. In other words, it is non-instance variable. So for example, an employee class have instance variables for an employee's names, phone numbers and email addresses. But all employee can share a common pay increase, then this is a static variable. Often static variable cannot be modified by an object instance, it has to be accessed through the class. A static method is similar, it's a method that only access the static variables. 

In Python there's a bit different, a static variable does not have the keyword static, they're just defined outside the init constructor. And static methods in python is called classmethod, python's static method is only used when it does not access anything in the class. 

By private and static, we can utilize its property that static variable is same across instances and cannot be modified through instance to define a singleton class. 

### Polymorphism, overriding 

Polymorphism basically just means that a subclass can override the methods in superclass, so that the methods in subclass can be different; in this way they are in different forms. 

Overriding means the subclass can redefine the methods in superclass by having the exact same method signature, but the contents of the methods can be different. 

### Interface, Abstract, Virtual

First off, an interface in java is a complete abstract class where there cannot exist a non-abstract method. But an abstract class can have concrete methods, it just cannot be instantiated as an object. A virtual method in C++ means a function needs to be override in subclasses. To make a class "virtual" or abstract in the way java does, we need to add a equal 0 in the end of the function. That way the class cannot be instantiated either now. 

Also, interface does not have a constructor.

### Null and Void pointer

Void is a type, while null is a value. Void pointer just means the pointer doesn't have a type like int or float. Null is a position in the memory space that cannot be accessed. 

### Pointer Arithmetic

Pointer arithmetic just means a `ptr++` will result in the pointer's address increment by the type's byte, like 4, if the pointer is a integer pointer. 

### Design Pattern

...

## SQL & MongoDB

...



## CUDA

### Superscalar(Pipeline)

This is an instruction level parallelism, or hardware level. A superscalar CPU can executes different instructions at the same time. Say the process of executing an instruction is fetch, decode and execute, after fetching one  command, the fetching unit can be used to fetch another and so on.

### Process, Thread, Multiprocessing and Multithreading

A process is a collection of threads, threads in a process share a common memory space and virtual memory table. Different processes do not share anything. (Data Parallelism, data parallelism means we pass a collection of data, like array, and then an instruction is executed on every element in this array at the same time)The most common forms of multiprocessing is probably MPI(Message Passing Interface). It's used like when we have a server and many computer nodes in this server, then these nodes do not share a common memory space and then we need a way for them to communicate to perform a task in parallel. Multithreading in CPU is openmp, on GPU is cuda. It means we don't need to communicate the data we have, we have common memory spaces. 

### Amadhl's Law

Speedup is equal to sequential time/parallel time. The law says the maximum speed up is less or equal than 1/(s+(1-s)/p), where s is the inherently sequential portion, like overheads, then 1-s is the part can be parallel, and p is number of processors we have. 

Global, shared keyword in cuda

### Overheads in CUDA

There're general two overheads in GPU, one is transferring the data from computer memory to gpu memory, the other is launching the kernel function itself, gpu needs to schedule all the grids, blocks and threads. There're other happens in executing the programs, like synchronizations(loading data is small).



### One Sorting Algorithm

Common sorting algorithms are bubble sort, selection sort, insertion sort, and two quicker ones quick sort and merge sort. 

Bubble sort is just of the most simple sorting. We walk through the array many times, in fact O(n^2) times, during the walk through we compare the element right neighboring element i+1 , if it's smaller than the i-th element, then we swap it. So each walk-through will make sure the last element is in position. Then each time we end one step earlier, in total we have O(n^2) running time.

Selection sort is similar, it each time finds the smallest element in the remaining list and then swap it with the first. 

Merge sort is a quicker sorting algorithm, only taking O(nlogn) time in worst case, its disadvantage is it needs extra O(n) space. The general procedure is we divide the array to be sorted into half each time, until the length of the divided array is one. And then we merge these half arrays back, during the merging we put the element in sorted order. 

### Binary Search Tree

Binary search tree is a tree that has the following property

- All nodes in left subtree must be smaller than the root
- All nodes in the right subtree must be larger than the root
- And left subtrees and right subtrees must also be binary search tree

### Choosing among languages

Python is the language I use most frequently. It's best for deep learning, the Pytorch and tensorflow framework, good for machine learning, like the scikit learn package. Java I use the least, but I know java's (Linkedin,2sigma) performance is comparable to c++ in some situations and it's good for building oop application. C++ and C it's definitely the number one choice for performance. For C, I used it for writing system related stuff and parallel computing. C++ I used it, but not very often. 



### What's your favorite Machine Learning Algorithm? advertise? How it connects to finance?

1. Introduce the setup, background, need, problems to be solved
2. Tell the assumptions of the model
3. The detailed approach of the model
4. Results, limit of the model 

Up to now, my favorite machine learning algorithm is cyclegan. （Introduce the setup) CycleGAN is a generative neural network and its main task is to perform image style transfer, meaning that, it can convert a summer landscape picture into a winter one. CycleGAN is a combined two GAN. GAN is generative adversial network, (...). CycleGAN(...) Limit is... 



## Probability

Refer to the [probability tips](./probability)

## Behavioral Questions

Impression; Personal brand;



Know my strengths and weakness 



Talk about the top resume events first 



This is just similar to steps for behavior questions:

1. Situation or task 
2. action
3. results



First explain the nouns, what is it;

Benefit; why I did that; what I learnt; 

Generalized random forest; weighted; why rewrite; why blabla; 