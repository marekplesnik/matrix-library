## matrix-library (samples)

>  Python 3.10 package for matrices, matrix operations and methods of linear algebra.


### Table of Contents

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
* [Error and exception handling](#error-and-exception-handling)
  * [TypeError](#typeerror)
  * [ValueError](#valueerror)
  * [Undefined](#undefined)
  * [InvalidDimension](#invaliddimension)
  * [ZeroDeterminant](#zerodeterminant)  
  * [NoSolution](#nosolution)


### Matrix class

> Let's suppose we have successfully imported matrixlib package by `import matrixlib`.

#### Initialization

```
matrix1 = matrixlib.Matrix(10, 12) # creates an empty matrix of dimensions 10 by 12
matrix2 = matrixlib.Matrix(4, 3, 0) # creates a null matrix of dimensions 4 by 3
matrix3 = matrixlib.Matrix(3, 3, [[1,2,3],[4,5,6],[7,8,9]]) # creates a matrix from the given 2D list of dimensions 3 by 3
```

#### Accessing row, column or element

> Let `matrix = matrixlib.Matrix(3, 3)` be a matrix with values `[[1,2,3],[4,5,6],[7,8,9]]`.

```
element = matrix[1, 1] # returns 5
row = matrix[2, None] # returns list with values [[7,8,9]]
column = matrix[None, 1] # returns list with values [[2],[5],[8]]
matrix = matrix[None, None] # return original matrix in list format
```

#### Modifying element, row, column or entire matrix

> Let `matrix = matrixlib.Matrix(3, 4)` be a matrix with values `[[1,2,3,4],[5,6,7,8],[9,10,11,12]]`.

```
matrix[2, 2] = 144 # sets the element at position 2 and 2 to 144, would return [[1,2,3,4],[5,6,7,8],[9,10,144,12]]
matrix[0, None] = [[0,0,0,0]] # sets the row at position 0 to [[0,0,0,0]], would return [[0,0,0,0],[5,6,7,8],[9,10,11,12]]
matrix[None, 1] = [[0],[0],[0]] # sets the column at position 1 to [[0],[0],[0]], would return [[1,0,3,4],[5,0,7,8],[9,0,11,12]]
matrix[None, None] = [[0,0,0,0],[0,0,0,0],[0,0,0,0]] # sets the matrix to matrix [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
```

#### Deleting row or column

> Let `matrix = matrixlib.Matrix(3, 3)` be a matrix with values `[[1,2,3],[4,5,6],[7,8,9]]`.

```
delattr(matrix, "1x") # matrix is now [[1,2,3],[7,8,9]]
delattr(matrix, "x0") # matrix is now [[2,3],[5,6],[8,9]]
```

#### Checking containment

> Let `matrix = matrixlib.Matrix(3, 4)` be a matrix with values `[[1,2,3,4],[5,6,7,8],[9,10,11,12]]`.

```
11 in matrix # return True, 11 is at position 2 and 2
144 in matrix # return False, 144 isn't in the matrix
```

#### Comparing two matrices

> Let `matrix = matrixlib.Matrix(3, 3)` be a matrix with values `[[1,2,3],[4,5,6],[7,8,9]]`.

```
other1 = matrixlib.Matrix(3, 3)` be a matrix with values `[[1,2,3],[4,5,6],[7,8,9]]`
other_list1 = [[1,2,3],[4,5,6],[7,8,9]]
other2 = matrixlib.Matrix(3, 3)` be a matrix with values `[[0,0,0],[0,0,0],[0,0,0]]`
other_list2 = [[0,0,0],[0,0,0],[0,0,0]]
```

```
matrix == other1 # returns True
matrix == other_list1 # returns True
matrix == other2 # returns False
matrix == other_list2 # returns False
```

#### String representation

> Let `matrix = matrixlib.Matrix(3, 4)` be a matrix with values `[[-9/7,5/9,-4/5,1],[-5/6,-5/6,-1,1],[-4,-7/9,-7/6,-2]]`.

```
string = str(matrix) # string would output the following
```

```
| -9/7 5/9  -4/5 1    |
| -5/6 -5/6 -1   1    |
| -4   -7/9 -7/6 -2   |
```

#### Object representation

> Let `matrix = matrixlib.Matrix(3, 4)` be a matrix with values `[[-9/7,5/9,-4/5,1],[-5/6,-5/6,-1,1],[-4,-7/9,-7/6,-2]]`.

```
string = repr(matrix) # string would output the following
```

```
Matrix object of dimensions 3 by 4
```

#### Generating random matrix

> Let `matrix = matrixlib.Matrix(3, 4)` be an object of the **Matrix** class.

```
matrix.rand() # would return "for example" [[-9/7,5/9,-4/5,1],[-5/6,-5/6,-1,1],[-4,-7/9,-7/6,-2]]
```

#### Completing to diagonal (unitary) matrix

> Let `matrix1 = matrixlib.Matrix(3, 4)` and `matrix2 = matrixlib.Matrix(5, 3)` 
> and `matrix3 = matrixlib.Matrix(5, 5)` be objects of the **Matrix** class.

```
matrix1.unit() # would return [[1,0,0,0],[0,1,0,0],[0,0,1,0]]
matrix2.unit(5) # would return [[5, 0, 0], [0, 5, 0], [0, 0, 5], [0, 0, 0], [0, 0, 0]]
matrix3.unit([1,2,3,4,5]) # would return [[1, 0, 0, 0, 0], [0, 2, 0, 0, 0], [0, 0, 3, 0, 0], [0, 0, 0, 4, 0], [0, 0, 0, 0, 5]]
```

#### Matrix validation and instance checkup

> Let `matrix1 = matrixlib.Matrix(3, 3)` be a matrix with values `[[1,2,3],[4,5,6],[7,8,9]]` and
> `matrix2 = matrixlib.Matrix(3,3)` be a matrix with values `[[None,2,3],[4,5,6],[7,None,9]]` and 
> `list1 = [[1,2,3],[4,5,6]]` and `list2 = [[1,2,3],["a",5,6]]`.

```
matrix1.validate() # returns True, it doesn't consist of any None elements
matrix2.validate() # returns False, it consists of some None elements
```

```
isinstance(matrix1, Matrix) # returns True
isinstance(matrix2, Matrix) # returns False, None elements
isinstance(list1, Matrix) # returns True, can be a Matrix object
isinstance(list2, Matrix) # returns False, contains None elements
```


### Operations

> Let's suppose we have successfully imported matrixlib package by `import matrixlib`.

#### Negation

> Let `matrix = matrixlib.Matrix(3, 3)` be a matrix with values `[[1,2,3],[4,5,6],[7,8,9]]`.

```
-matrix # returns a matrix with values [[-1,-2,-3],[-4,-5,-6],[-7,-8,-9]]
```

#### Addition

> Let `a = matrixlib.Matrix(3, 3)` be a matrix with values `[[1,2,3],[4,5,6],[7,8,9]]` and 
> `b = matrixlib.Matrix(3,3)` be a matrix with values `[[1,2,3],[4,5,6],[7,8,9]]`.

```
a + b # returns a matrix with values [[2,4,6],[8,10,12],[14,16,18]].
```

#### Subtraction

> Let `a = matrixlib.Matrix(3, 3)` be a matrix with values `[[1,2,3],[4,5,6],[7,8,9]]` and 
> `b = matrixlib.Matrix(3,3)` be a matrix with values `[[1,2,3],[4,5,6],[7,8,9]]`.

```
a - b # returns a matrix with values [[0,0,0],[0,0,0],[0,0,0]]
```

#### Multiplication

> Let `a = matrixlib.Matrix(3, 2)` be a matrix with values `[[1,1],[0,1],[0,1]]` and 
> `b = matrixlib.Matrix(2,2)` be a matrix with values `[[1,1],[0,1]]`.

```
a @ b # returns a matrix with values [[1,2],[0,1],[0,1]]
```

#### Scalar multiplication

> Let `a = matrixlib.Matrix(3,3)` be a matrix with values `[[1,2,3],[-1,0,1],[-18,-19,-20]]` and `x = -1`.

```
x * a # returns a matrix with values [[-1, -2, -3], [1, 0, -1], [18, 19, 20]]
```

#### Exponentiation and transposition and inverse

> Let `a = matrixlib.Matrix(3,3)` be a matrix with values `[[1,2,3],[2,3,4],[4,2,1]]`.

```
a**0 # returns the matrix a raised to 0th power, a matrix with values [[0,0,0],[0,0,0],[0,0,0]]
a**3 # returns the matrix a raised to 3rd power, a matrix with values [[101, 104, 121], [154, 155, 178], [128, 114, 121]]
a**"t" # returns the transposed matrix of a with values [[1, 2, 4], [2, 3, 2], [3, 4, 1]]
a**(-1) # returns the inverse matrix of a with values [[5,-4,1],[-14,11,-2],[8,-6,1]]
```

#### Dot product

> Let `a = matrixlib.Matrix(3,1)` be a matrix with values `[[2],[7],[1]]` and 
> `b = matrixlib.Matrix(3,1)` be a matrix with values `[[8],[2],[8]]`.

```
a * b # returns dot product of a and b with value of 38
```

#### Solver of system of linear equations

> Let `a = matrixlib.Matrix(3,3)` be a matrix with values `[[1,2,3],[1,0,1],[0,0,1]]` and
> `b = matrixlib.Matrix(3,1)` be a matrix with values `[[32],[10],[8]]`.

```
a.lin_sol(b) # returns a matrix list with values [[2],[3],[8]]
```

#### Determinant

> Let `a = matrixlib.Matrix(5,5)` be a matrix with values `[[0,1,0,-2,1],[1,0,3,1,1],[1,-1,1,1,1],[2,2,1,0,1],[3,1,1,1,2]]`.

```
a.det() # returns 4
```

#### Least squares regression

> Let `a = matrixlib.Matrix(3,2)` be a matrix with values `[[2,1],[1,2],[1,1]]` and
> `b = matrixlib.Matrix(3,1)` be a matrix with values `[[0],[-2],[3]]`.

```
a.least_squares(b) # returns the solution of the least squares or a matrix with values [[1],[-1]]
```


### Error and exception handling

> Let's suppose we have successfully imported matrixlib package by `import matrixlib`.

#### TypeError

```
matrix = matrixlib.Matrix(3,3,"a") # trying to create a matrix with key of type <string>
```

#### ValueError

> Let `a = matrixlib.Matrix(3,2)` be a matrix.

```
-a # trying to negate an empty matrix
```

#### Undefined

> Let `a = matrixlib.Matrix(3,2)` be a matrix with values `[[1,2],[3,4],[5,6]]`.

```
a.det() # trying to compute determinant on a non-square matrix
```

#### InvalidDimension

> Let `a = matrixlib.Matrix(3,2)` be a matrix with values `[[1,2],[3,4],[5,6]]`.

```
a**(-1) # trying to calculate the inverse of a non-square matrix, operation is supported only for square matrices
```

#### ZeroDeterminant

> Let `a = matrixlib.Matrix(3,3)` be a matrix with values `[[1,1,1],[1,0,1],[0,1,0]]`.

```
a**(-1) # trying to compute the inverse of a singular matrix, singular square matrix does not have an inverse
```

#### NoSolution

> Let `a = matrixlib.Matrix(3,3)` be a matrix with values `[[1,1,1],[1,0,1],[0,1,0]]` and 
> `b = matrixlib.Matrix(3,1)` be a matrix with values `[[1],[1],[1]]`.

```
a.lin_sol(b) # trying to solve a system of linear equations without a unique solution
```