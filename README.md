## matrix-library (user documentation)

> Python 3.10 package for matrices, matrix operations and methods of linear algebra.

### Table of Contents

* [Description](#description)
* [Features and Usage](#features-and-usage)
* [How to Install and Run](#how-to-install-and-run)
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

### Features and Usage

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
> against the resuts obtained using NumPy functions.

### How to Install and Run

### Testing

### Validation using Numpy

### Changelog

* 0.2.0
    * Updated import, added docstrings
    * Updated README
    * Added Matrix, Operations classes
    
* 0.1.0
  * Added README, .gitignore, tests, ...
  * Initialized repository, created structure