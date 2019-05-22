---
layout: post
title: Linear Algebra Study Notes
---

<span class="newthought">These notes</span>  are taken along with my review on linear algebra by MIT's online course. As I began my journey on Machine Learning, the problem of my unsturdy understanding of Linear Algbera and Matrices arised. Many of important concepts in Machine Learning require a solid comprehension of these knowledge, like column spaces, eigenvector and etc. This is my first time writing markdown+latex notes on math and there will be many unclear words and typos. The first version of this does not mean to be complete nor cover all the details but give a brief summary to myself to those who bump into this.{% include sidenote.html note='The notes are still **under construction**! If you find any typos or want to contribute, you can let me know, or just submit a pull request with your fixes to the [GitHub repository](https://github.com/RuizhenMai/academic-blog).'%} Later if there is a chance, or if many find this helpful, I will clean these up and prettify it to make it more formal and comprehensive. {% include marginnote.html note=" Also, thanks for Stanford's CS228 notes on probabilistic models. They are very concise and insightful. And thanks for the modification on Tufte's template. If the usage of this template violates the copyright, please let me know and I will delete this template. "%} 


## Unit I: Ax = B and Four Subspaces

1. [The Geometry of Linear Equations](UnitI/The_Geometry_of_Linear_Equations): A major application of linear algebra is to solving systems of linear equations. This lecture presents three ways of thinking about these systems. The "row method" focuses on the individual equations, the "column method" focuses on combining the columns, and the "matrix method" is an even more compact and powerful way of describing systems of linear equations.

2. [Elimination with Matrices](UnitI/Elimination_of_Matrices): 	This session introduces the method of elimination, an essential tool for working with matrices. The method follows a simple algorithm. To help make sense of material presented later, we describe this algorithm in terms of matrix multiplication.

3. [Multiplication and inverse matrices](UnitI/Multiplication_and_inverse_matrices): This lecture looks at matrix multiplication from five different points of view. We then learn how to find the inverse of a matrix using elimination, and why the Gauss-Jordan method works.

4. [Factorization into A = LU](UnitI/Factorization_into_A_eq_LU): This session explains inverses, transposes and permutation matrices. We also learn how elimination leads to a useful factorization A = LU and how hard a computer will work to invert a very large matrix.