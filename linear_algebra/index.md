---
layout: post
title: Linear Algebra Study Notes
---

<span class="newthought">These notes</span>  are taken along with my review on linear algebra by MIT's online course. As I began my journey on Machine Learning, the problem of my unsturdy understanding of Linear Algbera and Matrices arised. Many of important concepts in Machine Learning require a solid comprehension of these knowledge, like column spaces, eigenvector and etc. There can be typos and misclear explanation. If you find any typos or want to contribute{% include sidenote.html note='The notes are still **under construction**!'%}, please let me know by sending an email to mairuizhen1998@gmail.com including a [linear algebra] in the subject, or just submit a pull request with your fixes to the [GitHub repository](https://github.com/RuizhenMai/academic-blog) I really hope the notes can help out more people who find linear algbera boring or hard to grasp. {% include marginnote.html note=" Thanks for Stanford's CS228 notes on probabilistic models. They are very concise and insightful. And thanks for the modification on Tufte's template. If the usage of this template violates the copyright, please let me know and I will delete this template. "%} 

## Preliminaries

1. [Vector and Matrix](preliminaries/vector_and_matrix)

## Unit I: Ax = B and Four Subspaces

1. [The Geometry of Linear Equations](UnitI/The_Geometry_of_Linear_Equations): A major application of linear algebra is to solving systems of linear equations. This lecture presents three ways of thinking about these systems. The "row method" focuses on the individual equations, the "column method" focuses on combining the columns, and the "matrix method" is an even more compact and powerful way of describing systems of linear equations.{% include sidenote.html note='These introductory decsriptions are copied from the course page'%}

2. [Elimination with Matrices](UnitI/Elimination_of_Matrices): 	This session introduces the method of elimination, an essential tool for working with matrices. The method follows a simple algorithm. To help make sense of material presented later, we describe this algorithm in terms of matrix multiplication.

3. [Multiplication and inverse matrices](UnitI/Multiplication_and_inverse_matrices): This lecture looks at matrix multiplication from five different points of view. We then learn how to find the inverse of a matrix using elimination, and why the Gauss-Jordan method works.

4. [Factorization into A = LU](UnitI/Factorization_into_A_eq_LU): This session explains inverses, transposes and permutation matrices. We also learn how elimination leads to a useful factorization A = LU and how hard a computer will work to invert a very large matrix.

5. [Transposes, Permutations, Vector Spaces](UnitI/Transposes,Permutation,Vector_Spaces): To account for row exchanges in Gaussian elimination, we include a permutation matrix P in the factorization PA = LU. Then we learn about vector spaces and subspaces; these are central to linear algebra.

6. [Column Space and Nullspace](UnitI/Column_Space_and_Nullspace): The column space of a matrix A tells us when the equation Ax = b will have a solution x. The null space of A tells us which values of x solve the equation Ax = 0.

7. [Solving Ax = 0: Pivot Variables, Special Solutions](UnitI/solving_ax_eq_0): We apply the method of elimination to all matrices, invertible or not. Counting the pivots gives us the rank of the matrix. Further simplifying the matrix puts it in reduced row echelon form R and improves our description of the null space.

8. [Solving Ax = b: Row Reduced Form R](UnitI/solving_ax_eq_b): We describe all solutions to Ax = b based on the free variables and special solutions encoded in the reduced form R.

9. [Independence, Basis and Dimension](UnitI/Independence_Basis_and_Dimension): A basis is a set of vectors, as few as possible, whose combinations produce all vectors in the space. The number of basis vectors for a space equals the dimension of that space.

10. [The Four Fundamental Subspaces](UnitI/The_four_fundamental_subspaces): For some vectors b the equation Ax = b has solutions and for others it does not. Some vectors x are solutions to the equation Ax = 0 and some are not. To understand these equations we study the column space, nullspace, row space and left nullspace of the matrix A.

11. [Matrix Spaces; Rank 1; Small World Graphs](UnitI/matrix_spaces): As we learned last session, vectors don't have to be lists of numbers. In this session we explore important new vector spaces while practicing the skills we learned in the old ones. Then we begin the application of matrices to the study of networks.

12. [Graphs, Networks, Incidence Matrices](UnitI/graphs_networks_incidence_matrices):This session explores the linear algebra of electrical networks and the Internet, and sheds light on important results in graph theory.