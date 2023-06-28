## matrix-library (user documentation)

>  Python 3.10 package for matrices, matrix operations and methods of linear algebra.


### Table of Contents

* [How to Install and Setup](#how-to-install-and-setup)
* [Matrix class](#matrix-class)
  * [Initialization](#initialization)
  * [Accessing row, column or element](#accessing-row-column-or-element)
  * [Modifying element, row, column or entire matrix](#modifying-element-row-column-or-entire-matrix)
  * [Deleting row or column](#deleting-row-or-column)
  * [Checking containment](#checking-containment)
  * [Comparing two matrices](#comparing-two-matrices)
  * [String representation](#string-representation)
  * [Object representation](#object-representation)
  * [Generating random matrix](#generating-random-matrix)
  * [Completing to diagonal (unitary) matrix](#completing-to-diagonal-unitary-matrix)
  * [Matrix validation and instance checkup](#matrix-validation-and-instance-checkup)
* [Operations](#operations)
  * [Negation](#negation)
  * [Addition](#addition)
  * [Subtraction](#subtraction)
  * [Multiplication](#multiplication)
  * [Scalar multiplication](#scalar-multiplication)
  * [Exponentiation and transposition and inverse](#exponentiation-and-transposition-and-inverse)
  * [Solver of system of linear equations](#solver-of-system-of-linear-equations)
  * [Determinant](#determinant)
  * [Matrix inverter](#matrix-inverter)
  * [Dot product](#dot-product)
  * [Least squares regression](#least-squares-regression)
* [Error and Exception handling](#error-and-exception-handling)
  * [TypeError](#typeerror)
  * [ValueError](#valueerror)
  * [Undefined](#undefined)
  * [InvalidDimension](#invaliddimension)
  * [ZeroDeterminant](#zerodeterminant)  
  * [NoSolution](#nosolution)


### How to Install and Setup

##### Installation

1. Download the **matrix-library** GitHub repository and extract its contents.
2. Using command terminal, navigate to the directory where the **setup.py** file is located.
3. Make sure Python 3.10 is installed and operational and enter `python setup.py install`.

##### Setup

1. At the beginning of your Python script or in the interactive Python shell, add the 
following `import matrixlib`.
2. You can now use **matrix-library** module in your code.


### Matrix class

> The following section is only a guide to the command structure and package techniques, for usage
> examples visit `samples`.

#### Initialization

> To create a matrix, initialize a **Matrix** class object by providing the number of rows, columns and
> key, where key is set to None by default (creates an empty Matrix), but may be set to a rational (every element is
> then this rational) or a list of lists of given size (rows by columns).

```
matrix = matrixlib.Matrix(rows, cols, key) # key is by default None, may be a rational or a list of lists
```

#### Accessing row, column or element

> You can access elements, rows, columns or the entire matrix using the `__getitem__` dunder method.
> Pass the row (row) and column (col) coordinates in the format of [row, col] to retrieve specific output
> (element, row, column, matrix). Let `matrix = matrixlib.Matrix(rows, cols)` be an object of the **Matrix** class.

```
element = matrix[row, col]
row = matrix[row, None]
column = matrix[None, col]
matrix = matrix[None, None]
```

#### Modifying element, row, column or entire matrix

> You can modify elements, row, column or entire matrix using the `__setitem__` dunder method. 
> Pass the row (row) and column (col) coordinates in the format of [row, col] to set specific value
> (rational, row, column or the entire matrix). Let `matrix = matrixlib.Matrix(rows, cols)` 
> be an object of the **Matrix** class.

```
matrix[row, col] = value # value must be of type number and the element at position row and col is set to value
matrix[row, None] = value # value must be of type row list and it modifies the row at position row to the new value
matrix[None, col] = value # value must be of type column list and it modifies the column at position col to the new value
matrix[None, None] = value # value must be of type Matrix or 2D list and it sets the entire matrix to the value
```

#### Deleting row or column

> You can delete row or column from a matrix using the `__delattr__` dunder method. Pass the row or column coordinate (None or within range)
> in the format of "(row)(col)", where for None is "x" and (row/col) is the number coordinate, to delete specific row or column. Let `matrix = matrixlib.Matrix(rows, cols)` be an object of the **Matrix** class.

```
delattr(matrix, "(row)x") # deletes the row with coordinate of row
delattr(matrix, "x(col)") # deletes the col with coordinate of col
```

#### Checking containment

> You can check whether a specific value is present in the matrix using the `__contains__` dunder method.
> Pass the value (rational) to check for containment. Let `matrix = matrixlib.Matrix(rows, cols)` be an object of the **Matrix** class.

```
value in matrix # returns True if value is present in matrix, false if value is not
```

#### Comparing two matrices

> You can compare two matrices for equality using the `__eq__` dunder method. Pass 
> the other matrix (either object of **Matrix** class or matrix list) to compare.
> Let `matrix = matrixlib.Matrix(rows, cols)` be an object of the **Matrix** class.
> Let `other = matrixlib.Matrix(rows, cols)` be an object of the **Matrix** class or 
> other is matrix list of dimensions rows and cols.

```
matrix is other # returns True if matrix == other, false if matrix != other
```

#### String representation

> You can represent a matrix with the provided string representation `__str__` dunder method. It returns
> a formatted string representation representing the matrix in a readable format.
> Let `matrix = matrixlib.Matrix(rows, cols)` be an object of the **Matrix** class.

```
string = str(matrix) # string now represents the formatted string matrix representation of the matrix
```

#### Object representation

> You can represent a matrix with the `__repr__` dunder method. It returns an object representation
> of the given matrix. Let `matrix = matrixlib.Matrix(rows, cols)` be an object of the **Matrix** class.

```
string = repr(matrix) # string is now "Matrix object of dimensions rows by cols"
```

#### Generating random matrix

> You can generate a random matrix with fractional elements using the `rand` method. 
> Using optional arguments start, stop you can set the range of generated fraction(a,b), where
> start <= a <= stop and start <= b <= stop. Let `matrix = matrixlib.Matrix(rows, cols)` be an 
> object of the **Matrix** class.

```
matrix.rand(start, stop) # randomly fills the matrix elements
```

#### Completing to diagonal (unitary) matrix

> You can transform a matrix to a diagonal matrix using the `unit` method. Pass a key, that is by default 1 (to create a unitary matrix) 
> or may be a rational or a list of length of the smaller dimension (either number rows or columns). Let `matrix = matrixlib.Matrix(rows, cols)` be an 
> object of the **Matrix** class.

```
matrix.unit() # matrix is now a unitary matrix
matrix.unit(-1/20) # matrix is now diagonal with -1/20 on its diagonal
matrix.unit(list) # matrix is now diagonal with elements of list on its diagonal, suppose list is of length min(rows, cols)
```

#### Matrix validation and instance checkup

> You can validate if a matrix contains only non-Nonetype elements using the `validate` method. Let `matrix = matrixlib.Matrix(rows, cols)` be an 
> object of the **Matrix** class.

```
matrix.validate() # returns True if all elements are rational, False if there is a None value
```

> You can use the overriden `isinstance` method for checking whether a matrix is of rational elements or a 2D list can be a matrix, 
> meaning it has same length of columns and only rational elements. Let `matrix = matrixlib.Matrix(rows, cols)` be an 
> object of the **Matrix** class and list is a 2D list.

```
isinstance(matrix, matrixlib.Matrix) # returns True if matrix has only rational elements, else False
isinstance(list, matrixlib.Matrix) # returns True if list has the same length of its nested lists and only rational elements, else False
```

### Operations

> The following section is only a guide to the command structure and package techniques, for usage
> examples visit `samples`.

#### Negation

> Dunder method `__neg__` performs matrix negation on a matrix `a`. The object of **Matrix** class must 
> have rational elements or the ValueError is raised. Returns the negated matrix. Let `matrix = matrixlib.Matrix(rows, cols)`.

```
-matrix # returns the negated matrix
```

#### Addition

> The `__add__` dunder method performs matrix addition. The matrices must be of same dimensions, or the InvalidDimension is raised, and consist of only
> rational elements or the ValueError is raised. Let `matrix = matrixlib.Matrix(rows, cols)` and `other = matrixlib.Matrix(rows, cols)`.

```
matrix + other # returns matrix of addition between matrix and other
```

#### Subtraction

> The `__sub__` dunder method performs matrix subtraction. The matrices must have the same dimensions,
> otherwise an InvalidDimension error will be raised. Both matrices should consist of only rational elements or
> a ValueError is raised. Let `matrix = matrixlib.Matrix(rows, cols)` and `other = matrixlib.Matrix(rows, cols)`.

```
matrix - other # returns matrix of subtraction between matrix and other
```

#### Multiplication

> The `__matmul__` dunder method performs matrix multiplication. It allows you to multiply two matrices together.
> The number of columns in the first matrix must be equal to the number of rows in the second matrix, otherwise an
> InvalidDimension error will be raised. Both matrices must consist of only rational elements or a ValueError is raised.
> Let `matrix = matrixlib.Matrix(m, n)` and `other = matrixlib.Matrix(n, p)`.

```
matrix @ other # returns matrix of multiplication between matrix and other
```

#### Scalar multiplication

> The `__rmul__` dunder method performs scalar multiplication, which consists of multiplying a matrix by a 
> scalar value (single rational). The matrix must have rational elements, or a ValueError is raised, and 
> the scalar value must be a rational, otherwise a TypeError is raised. Let `matrix = matrixlib.Matrix(rows, cols)`
> and `a` is rational.

```
a * matrix # returns matrix that is a scalar multiple a of Matrix matrix
```

#### Exponentiation and transposition and inverse

> The `__pow__` dunder method performs matrix exponentiation. It allows to raise a matrix to a specified non-negative
> integer or "t" as transposed or (-1) as inverse, if matrix is regular, otherwise ZeroDeterminant occurs. The matrix must be square, otherwise an InvalidDimension is raised and must consist of only
> rational elements, or a ValueError is raised. Let `matrix = matrixlib.Matrix(rows, cols)`.

```
matrix**0 # returns a null matrix
matrix**"t" # returns transposed matrix
matrix**10 # returns a matrix raised to the power of 10
matrix**(-1) # returns an inverse matrix, if matrix is regular
```

#### Dot product

> The `__mul__` dunder method can be used to perform dot product between two vectors. The matrices must be 
> vectors of same dimensions, matrices of same row dimension and 1 column, otherwise InvalidDimension is raised. Also the matrices
> must contain non None values, or a ValueError appears. Let `matrix = matrixlib.Matrix(rows, 1)` and `other = matrixlib.Matrix(rows, 1)`.

```
matrix * other # returns the dot product between matrix and other
```

#### Solver of system of linear equations

> The method `lin_sol` is used to solve a system of linear equations created from a matrix and the vector of the right side.
> Pass the `other` vector as the argument. The matrix must be regular and square, and both the matrix and other vector must contain only 
> rational elements. Let `matrix = matrixlib.Matrix(rows, cols)` and `other = matrixlib.Matrix(rows, 1)`.

```
matrix.lin_sol(other) # returns the solution vector of the system of linear equations of matrix by other
```

#### Determinant

> The method `det` calculates the determinant of the given matrix. The matrix must be square, otherwise Undefined is thrown, and
> must not consist of any None elements. It returns a number representing its determinant. Let `matrix = matrixlib.Matrix(rows, rows)`.

```
matrix.det() # returns the matrix's determinant
```

#### Least squares regression

> The `least_squares` method performs the least squares regression on a matrix that has linear independent columns. Pass the `other` vector as the argument.
> The number of rows of matrix and other must be equal, otherwise an InvalidDimension error is raised, and matrix and other must not contain any None elements or
> a ValueError is raised. Let `matrix = matrixlib.Matrix(rows, cols)` and `other = matrixlib.Matrix(rows, 1)`.

```
matrix.least_squares(other) # returns the solution vector of the least squares regression on other
```


### Error and exception handling

#### TypeError

> This error is raised when an unsupported type is used as a matrix element, list, ...

#### ValueError

> Raised when an incorrect value is provided, such as if a value is not rational ...

#### Undefined

> This exception is raised when attempting to execute an operation that is not defined. Such as
> trying to compute a determinant of non-square matrix.

#### InvalidDimension

> This exception is raised when a matrix does not have a valid dimension for a specific operation
> or condition. It typically occurs when indices are out of range or negative, matrix is expected to be square, matrix
> is supposed to be a vector, ...

#### ZeroDeterminant

> This exception is raised when attempting to execute an operation requiring a regular matrix. For example when
> using the solver of system of linear equations and the provided matrix can't have a unique solution or using the 
> least squares regression on the same principle.

#### NoSolution

> This exception is raised when attempting to solve a system of linear equations that either does not
> have a solution or doesn't have a unique solution. Such as if equations are contradictory, leading to an impossible solution
> or if the system is consistent, but has multiple solutions and underdetermined, therefore allowing for an infinite number of
> valid solutions.