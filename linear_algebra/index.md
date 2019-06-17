---
layout: post
title: Linear Algebra Study Notes
---

<span class="newthought">These notes</span>  are taken along with my review on linear algebra by MIT's online course. As I began my journey on Machine Learning, the problem of my unsturdy understanding of Linear Algbera and Matrices arised. Many of important concepts in Machine Learning require a solid comprehension of these knowledge, like column spaces, eigenvector and etc. There can be typos and misclear explanation. If you find any typos or want to contribute{% include sidenote.html note='The notes are still **under construction**!'%}, please let me know by sending an email to mairuizhen1998@gmail.com including a [linear algebra] in the subject, or just submit a pull request with your fixes to the [GitHub repository](https://github.com/RuizhenMai/academic-blog) I really hope the notes can help out more people who find linear algbera boring or hard to grasp. {% include marginnote.html note=" Thanks for Stanford's CS228 notes on probabilistic models. They are very concise and insightful. And thanks for the modification on Tufte's template. If the usage of this template violates the copyright, please let me know and I will delete this template. "%} 

<a href="https://ocw.mit.edu/courses/mathematics/18-06sc-linear-algebra-fall-2011/index.htm">MIT 18.06</a>
<br>
<a href="https://www.youtube.com/playlist?list=PLE7DDD91010BC51F8">Youtube Video Playlist</a>


## Preliminaries

1. [Vector and Matrix](preliminaries/vector_and_matrix)


## I: Ax = B and Four Subspaces

1. [The Geometry of Linear Equations](UnitI/The_Geometry_of_Linear_Equations): A major application of linear algebra is to solving systems of linear equations. This lecture presents three ways of thinking about these systems. The "row method" focuses on the individual equations, the "column method" focuses on combining the columns, and the "matrix method" is an even more compact and powerful way of describing systems of linear equations.{% include sidenote.html note='These introductory decsriptions are copied from the course page'%}

2. [Elimination with Matrices](UnitI/Elimination_of_Matrices): 	This session introduces the method of elimination, an essential tool for working with matrices. The method follows a simple algorithm. To help make sense of material presented later, we describe this algorithm in terms of matrix multiplication.

3. [Multiplication and inverse matrices](UnitI/3_Multiplication_and_inverse_matrices): This lecture looks at matrix multiplication from five different points of view. We then learn how to find the inverse of a matrix using elimination, and why the Gauss-Jordan method works.

4. [Factorization into A = LU](UnitI/Factorization_into_A_eq_LU): This session explains inverses, transposes and permutation matrices. We also learn how elimination leads to a useful factorization A = LU and how hard a computer will work to invert a very large matrix.

5. [Transposes, Permutations, Vector Spaces](UnitI/Transposes,Permutation,Vector_Spaces): To account for row exchanges in Gaussian elimination, we include a permutation matrix P in the factorization PA = LU. Then we learn about vector spaces and subspaces; these are central to linear algebra.

6. [Column Space and Nullspace](UnitI/Column_Space_and_Nullspace): The column space of a matrix A tells us when the equation Ax = b will have a solution x. The null space of A tells us which values of x solve the equation Ax = 0.

7. [Solving Ax = 0: Pivot Variables, Special Solutions](UnitI/solving_ax_eq_0): We apply the method of elimination to all matrices, invertible or not. Counting the pivots gives us the rank of the matrix. Further simplifying the matrix puts it in reduced row echelon form R and improves our description of the null space.

8. [Solving Ax = b: Row Reduced Form R](UnitI/solving_ax_eq_b): We describe all solutions to Ax = b based on the free variables and special solutions encoded in the reduced form R.

9. [Independence, Basis and Dimension](UnitI/Independence_Basis_and_Dimension): A basis is a set of vectors, as few as possible, whose combinations produce all vectors in the space. The number of basis vectors for a space equals the dimension of that space.

10. [The Four Fundamental Subspaces](UnitI/The_four_fundamental_subspaces): For some vectors b the equation Ax = b has solutions and for others it does not. Some vectors x are solutions to the equation Ax = 0 and some are not. To understand these equations we study the column space, nullspace, row space and left nullspace of the matrix A.

11. [Matrix Spaces; Rank 1; Small World Graphs](UnitI/matrix_spaces): As we learned last session, vectors don't have to be lists of numbers. In this session we explore important new vector spaces while practicing the skills we learned in the old ones. Then we begin the application of matrices to the study of networks.

12. [Graphs, Networks, Incidence Matrices](UnitI/graphs_networks_incidence_matrices):This session explores the linear algebra of electrical networks and the Internet, and sheds light on important results in graph theory.

13. [Review](UnitI/review): The [video](https://youtu.be/l88D4r74gtM?list=PLE7DDD91010BC51F8) goes through the review question thoroughly. I will write down a few that I think the prof. did not explain quite clearly and those that might be insightful

    ## II: Least Squares, Determinants and Eigenvalues

14. [Orthogonal Vectors and Subspaces](UnitII/14_orthogonal_vectors_and_subspaces): Vectors are easier to understand when they're described in terms of orthogonal bases. In addition, the Four Fundamental Subspaces are orthogonal to each other in pairs. If A is a rectangular matrix, Ax = b is often unsolvable. The matrix ATA will help us find a vector x̂ that comes as close as possible to solving Ax = b.
    
15. [Projections onto Subspaces](UnitII/15_projections_onto_subspaces): We often want to find the line (or plane, or hyperplane) that best fits our data. This amounts to finding the best possible approximation to some unsolvable system of linear equations Ax = b. The algebra of finding these best fit solutions begins with the projection of a vector onto a subspace

16. [Projection Matrices and Least Squares](UnitII/16_projection_matrices_and_least_squares): Linear regression is commonly used to fit a line to a collection of data. The method of least squares can be viewed as finding the projection of a vector. Linear algebra provides a powerful and efficient description of linear regression in terms of the matrix ATA.

17. [Orthogonal Matrices and Gram-Schmidt](UnitII/17_orthogoonal_marices_and_gram_schmidt): Many calculations become simpler when performed using orthonormal vectors or othogonal matrices. In this session, we learn a procedure for converting any basis to an orthonormal one.

18. [Properties of Determinants](UnitII/18_properties_of_determinants): The determinant of a matrix is a single number which encodes a lot of information about the matrix. Three simple properties completely describe the determinant. In this lecture we also list seven more properties like detAB = (detA)(detB) that can be derived from the first three.

19. [Determinant Formulas and Cofactors](UnitII/19_determinant_formulas_and_cofactors): One way to compute the determinant is by elimination. In this lecture we derive two related formulas for the determinant using the properties from last lecture. 

20. [Cramer's Rule, Inverse Matrix and Volume](UnitII/20_cramers_rule_inverse_matrix_and_volume): Now we start to use the determinant. Understanding the cofactor formula allows us to show that A-1 = (1/detA)CT, where C is the matrix of cofactors of A. Combining this formula with the equation x = A-1b gives us Cramer's rule for solving Ax = b. Also, the absolute value of the determinant gives the volume of a box.

21. [Eigenvalues and Eigenvectors](UnitII/21_eigenvalues_and_eigenvectors): If the product Ax points in the same direction as the vector x, we say that x is an eigenvector of A. Eigenvalues and eigenvectors describe what happens when a matrix is multiplied by a vector. In this session we learn how to find the eigenvalues and eigenvectors of a matrix.

22. [Diagonalization and Powers of A](UnitII/22_diagonalization): If A has n independent eigenvectors, we can write A = SΛS−1, where Λ is a diagonal matrix containing the eigenvalues of A. This allows us to easily compute powers of A which in turn allows us to solve difference equations uk+1 = Auk. 

23. [Differential Equations and exp(At)](UnitII/23_differential_equations): We can copy Taylor's series for ex to define eAt for a matrix A. If A is diagonalizable, we can use Λ to find the exact value of eAt. This allows us to solve systems of differential equations du / dt = Au the same way we solved equations like dy / dt = ky.

24. [Markov Matrices; Fourier Series](UnitII/24_markov_matrices_fourier_series): Like differential equations, Markov matrices describe changes over time. Once again, the eigenvalues and eigenvectors describe the long term behavior of the system. In this session we also learn about Fourier series, which describe periodic functions as points in an infinite dimensional vector space.
    
    ## III: POSITIVE DEFINITE MATRICES AND APPLICATIONS

25. [Symmetric Matrices and Positive Definiteness](UnitIII/25_symmetric_matrices_and_positive_definiteness)

26. [Complex Matrices; Fast Fourier Transform (FFT)](UnitIII/26_complex_matrices_fft)

27. [Positive Definite Matrices and Minima](UnitIII/27_positive_definite_matrices_and_minima)

28. [Similar Matrices and Jordan Form](UnitIII/28_similar_matrices_and_jordan_form) 

29. [Singular Value Decomposition](UnitIII/29_svd) 