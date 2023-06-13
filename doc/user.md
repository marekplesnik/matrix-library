## matrix-library (user documentation)

>  Python 3.10 package for matrices, matrix operations and methods of linear algebra.

### Table of Contents

* [How to Install and Setup](#how-to-install-and-setup)
* [Matrix class](#matrix)
* [Operations](#operations)
* [Error and Exception handling](#error-and-exception-handling)

### How to Install and Setup

###### Installation

1. Download the **matrix-library** GitHub repository and extract its contents.
2. Using command terminal, navigate to the directory where the **setup.py** file is located.
3. Make sure Python 3.10 is installed and operational and enter `python setup.py install`.

###### Setup

1. At the beginning of your Python script or in the interactive Python shell, add the 
following `import matrixlib`.
2. You can now use **matrix-library** module in your code.

### Matrix

> The **Matrix** class provides a way to dynamically create and manipulate
> matrices. It supports these following operations: initialization, accessing and 
> modifying elements, deleting elements, checking containment, comparison between matrices,
> generating random matrices and string representation.

#### Creating a matrix

> To create a matrix, initialize a **Matrix** class object by providing the number of rows 
> and columns as arguments, where rows represents the number of rows and cols represents the number
> of columns:

```
matrix = matrixlib.Matrix(rows, cols)
```

###### Example:

```
matrix = matrixlib.Matrix(10, 12) # creates matrix of dimensions 10 by 12
```

#### Accessing elements, row, column or entire matrix

> You can access elements, rows, columns or entire matrix using the `__getitem__` method.
> Pass the row coordinates (optional) and the column coordinates (optional) to retrieve
> specific output in the format of list. Let `matrix = matrixlib.Matrix(rows, cols)` be an object of the **Matrix** class.

```
element = matrix.__getitem__(row, col)
row = matrix.__getitem__(row, None)
column = matrix.__getitem__(None, col)
matrix = matrix.__getitem__(None, None)
```

###### Example:

> Let `matrix = matrixlib.Matrix(3, 3)` be a matrix with values `[[1,2,3],[4,5,6],[7,8,9]]`.

```
element = matrix.__getitem__(1, 1) # returns 5
row = matrix.__getitem__(2, None) # returns list with values [[7,8,9]]
column = matrix.__getitem__(None, 1) # returns list with values [[2],[5],[8]]
matrix = matrix.__getitem__(None, None) # return original matrix in list format
```

#### Modifying elements, row, column or entire matrix

#### Deleting row or column

#### Checking containment

#### Comparing two matrices

#### Generating random matrix

#### String representation





### Operations

### Error and Exception handling