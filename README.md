## matrix-library

> Python 3.10 package for matrices, matrix operations and methods of linear algebra.

### Table of Contents

* [Description](#description)
* [Features](#features)
* [Testing](#testing)
* [Validation using Numpy](#validation-using-numpy)
* [Changelog](#changelog)

### Description

> The "matrix-library" package is a Python library that provides 
> a comprehensive set of tools for matrix construction, matrix operations
> and linear algebra methods. The package offers a number of useful functionalities, all with
> its support for rational numbers, which is particularly useful when operating with
> fractions or decimals.
> 
> This package allows user to create matrices with rational numbers using various
> techniques like manually entering the values, assigning the entire matrix along with validating the
> contents, or randomly generating them.
> 
> In addition, the "matrix-library" offers an extensive array of functions for analyzing and manipulating matrices. Users can perform
> diverse computations ranging from simple addition, multiplication, transposition, ... to more advanced operations such as 
> determinants, solving systems of linear equations up to, for example, finding matrix inverses or applying the method of least squares.

### Features

##### Logical design

> The library has a logical design that emphasizes the behaviour of functions, providing clear and informative messages
> when an error state occurs, such as when a matrix is singular or system of linear equations doesn't have a unique solution.

##### Logical interface

> The package provides a uniform and intuitive interface for users to interact, ensuring that the order
> of function parameters is consistent across all operations. Additionally, the package 
> adheres to standard conventions for return values and tends to inform user about
> a wide range of possible exceptions.

##### Unit testing

> It also includes a suite of unit tests to ensure the correctness and reliability 
> of its operations. These tests are designed to include all the package's functionalities, 
> cover potential errors or testing edge cases.

##### Validation using NumPy

> The library also uses NumPy for validation, checking the correctness of its results by comparing them 
> against the results obtained using NumPy functions.

##### Matrix operations

* Negation
* Addition
* Subtraction
* Multiplication
* Transposition
* Multiplication
* Scalar multiplication
* ... and more

##### Methods of linear algebra

* Solver of systems of linear equations
* Determinant
* Matrix inverter
* Dot product
* Method of the least squares
* ... and more

### Testing

### Validation using Numpy

> The "matrix-library" package underwent extensive testing to validate its functionality
> and accuracy, which involved comparing its matrix operations and methods of linear algebra
> to those of Numpy. During testing (done by UnitTest), various unit tests
> were performed to verify the correctness of individual functions and methods.
> 
> During testing using UnitTest, various objective tests were performed on randomly
> generated matrices (random number of rows, columns and random elements) to at least 
> guarantee the same precision as the numpy library offers. 
> 
> Furthermore, performance tests were conducted to measure the execution time of the "matrix-library" package's 
> operations on large sparse matrices, and these tests were compared to Numpy's equivalent operations to verify correctness
> of the methods.

### Changelog

* 0.2.0
  * Fixed bugs
  * Added numpy validation, samples, tests
  * Updated import, added docstrings
  * Updated README
  * Added Matrix, Operations classes
    
* 0.1.0
  * Added README, .gitignore, tests, ...
  * Initialized repository, created structure