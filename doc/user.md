## matrix-library (user documentation)

>  Python 3.10 package for matrices, matrix operations and methods of linear algebra.

### Table of Contents

* [How to Install and Setup](#how-to-install-and-setup)
* [Matrix class](#matrix)
* [Operations](#operations)
* [Error and Exception handling](#error-and-exception-handling)

### How to Install and Setup

##### Installation

1. Download the **matrix-library** GitHub repository and extract its contents.
2. Using command terminal, navigate to the directory where the **setup.py** file is located.
3. Make sure Python 3.10 is installed and operational and enter `python setup.py install`.

##### Setup

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

##### Example:

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

##### Example:

> Let `matrix = matrixlib.Matrix(3, 3)` be a matrix with values `[[1,2,3],[4,5,6],[7,8,9]]`.

```
element = matrix.__getitem__(1, 1) # returns 5
row = matrix.__getitem__(2, None) # returns list with values [[7,8,9]]
column = matrix.__getitem__(None, 1) # returns list with values [[2],[5],[8]]
matrix = matrix.__getitem__(None, None) # return original matrix in list format
```

#### Modifying elements, row, column or entire matrix

> You can modify elements, row, column or entire matrix using the `__setitem__` method. Pass the value (either number,
>  row list, column list or matrix list) and the row (optional) and column (optional) coordinates. Let `matrix = matrixlib.Matrix(rows, cols)` 
> be an object of the **Matrix** class.

```
matrix.__setitem__(value, row, col) # value must be of type number and the element at position row and col is set to value
matrix.__setitem__(value, row, None) # value must be of type row list and it modifies the row at position row to the new value
matrix.__setitem__(value, None, col) # value must be of type column list and it modifies the column at position col to the new value
matrix.__setitem__(value, None, None) # value must be of type matrix list and it sets the entire matrix to the value
```

##### Example:

> Let `matrix = matrixlib.Matrix(3, 4)` be a matrix with values `[[1,2,3,4],[5,6,7,8],[9,10,11,12]]`.

```
matrix.__setitem__(144, 2, 2) # sets the element at position 2 and 2 to 144, would return [[1,2,3,4],[5,6,7,8],[9,10,144,12]]
matrix.__setitem__([[0,0,0,0]], 0, None) # sets the row at position 0 to [[0,0,0,0]], would return [[0,0,0,0],[5,6,7,8],[9,10,11,12]]
matrix.__setitem__([[0],[0],[0]], None, 1) # sets the column at position 1 to [[0],[0],[0]], would return [[1,0,3,4],[5,0,7,8],[9,0,11,12]]
matrix.__setitem__([[0,0,0,0],[0,0,0,0],[0,0,0,0]], None, None) # sets the matrix to matrix [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
```

#### Deleting row or column

> You can delete rows or columns from a matrix using the `__delitem__` method. Pass the row or column coordinate (optional)
> to delete specific rows or columns. Let `matrix = matrixlib.Matrix(rows, cols)` be an object of the **Matrix** class.

```
matrix.__delitem__(row, None) # deletes the row with coordinate of row
matrix.__delitem__(None, col) # deletes the column with coordinate of col
```

##### Example:

> Let `matrix = matrixlib.Matrix(3, 3)` be a matrix with values `[[1,2,3],[4,5,6],[7,8,9]]`.

```
matrix.__delitem__(1, None) # would return [[1,2,3],[7,8,9]]
matrix.__delitem__(None, 0) # would return [[2,3],[5,6],[8,9]]
```

#### Checking containment

> You can check whether a specific value is present in the matrix using the `__contains__` method.
> Pass the value (number) to check for containment. Let `matrix = matrixlib.Matrix(rows, cols)` be an object of the **Matrix** class.

```
matrix.__contains__(value) # returns true if value is present, false if isn't
```

##### Example:

> Let `matrix = matrixlib.Matrix(3, 4)` be a matrix with values `[[1,2,3,4],[5,6,7,8],[9,10,11,12]]`.

```
matrix.__contains__(11) # return True, 11 is at position 2 and 2
matrix.__contains__(144) # return False, 144 isn't in the matrix
```

#### Comparing two matrices

> You can compare two matrices for equality using the `__eq__` method. Pass 
> the other matrix (either object of **Matrix** class or matrix list) to compare.
> Let `matrix = matrixlib.Matrix(rows, cols)` be an object of the **Matrix** class.
> Let `other = matrixlib.Matrix(rows, cols)` be an object of the **Matrix** class or 
> other is matrix list of dimensions rows and cols.

```
matrix.__eq__(other) # returns True if matrix == other, false if matrix != other
```

##### Example:

> Let `matrix = matrixlib.Matrix(3, 3)` be a matrix with values `[[1,2,3],[4,5,6],[7,8,9]]`.

```
other1 = matrixlib.Matrix(3, 3)` be a matrix with values `[[1,2,3],[4,5,6],[7,8,9]]`
other_list1 = [[1,2,3],[4,5,6],[7,8,9]]
other2 = matrixlib.Matrix(3, 3)` be a matrix with values `[[0,0,0],[0,0,0],[0,0,0]]`
other_list2 = [[0,0,0],[0,0,0],[0,0,0]]
```

```
matrix.__eq__(other1) # returns True
matrix.__eq__(other_list1) # returns True
matrix.__eq__(other2) # returns False
matrix.__eq__(other_list2) # returns False
```

#### Generating random matrix

> You can generate a random matrix with fractional elements using the `__rand__` method. 
> Using optional arguments start, stop you can set the range of generated fraction(a,b), where
> start <= a <= stop and start <= b <= stop. Let `matrix = matrixlib.Matrix(rows, cols)` be an 
> object of the **Matrix** class.

```
matrix.__rand__(start, stop) # randomly fills the matrix elements
```

##### Example:

> Let `matrix = matrixlib.Matrix(3, 4)` be an object of the **Matrix** class.

```
matrix.__rand__() # would return "for example" [[-9/7,5/9,-4/5,1],[-5/6,-5/6,-1,1],[-4,-7/9,-7/6,-2]]
```

#### String representation

> You can represent a matrix with the provided string representation `__repr__` method. It returns
> a formatted string representation representing the matrix in a readable format.
> Let `matrix = matrixlib.Matrix(rows, cols)` be an object of the **Matrix** class.

```
string = matrix.__repr__() # returns the formatted string matrix representation of the matrix
```

##### Example:

> Let `matrix = matrixlib.Matrix(3, 4)` be a matrix with values `[[-9/7,5/9,-4/5,1],[-5/6,-5/6,-1,1],[-4,-7/9,-7/6,-2]]`.

```
string = matrix.__repr__() # string would output the following
```

```
| -9/7 5/9  -4/5 1    |
| -5/6 -5/6 -1   1    |
| -4   -7/9 -7/6 -2   |
```

### Operations

#### Validate

> Operation `validate(a)` is used to validate if an object is of type **Matrix** or if matrix list
> meets the criteria to be an object of **Matrix**. Pass the **Matrix** or matrix list `a` as argument.
> Returns **Matrix** object of the matrix list or the original **Matrix** argument.
> Let a = matrixlib.Matrix(rows, cols).

```
matrix = matrixlib.validate(a)
```

##### Example:

> Let `a = matrixlib.Matrix(3, 3)` be a matrix with values `[[1,2,3],[4,5,6],[7,8,9]]`. 
> Let `a_list = [[1,2,3],[4,5,6],[7,8,9]]`. Let `b_list = [[1,2,3],[d,e,f],[7,8,9]]`.

```
matrix = matrixlib.validate(a) # returns the original object
matrix_a = matrixlib.validate(a_list) # returns a Matrix object with values of a_list
```

#### Negation

> Operation `neg(a, out = False)` performs matrix negation on a matrix `a`. The input 
> parameter `a` may be **Matrix** object or a matrix list. The optional parameter `out` 
> specifies whether to return a matrix list (out = False) or return a **Matrix** object (out = True).
> Returns the negated matrix. Let a = matrixlib.Matrix(rows, cols).

```
matrix = matrixlib.neg(a, out = False) # returns the negated matrix a in matrix list output format
```

##### Example:

> Let `a = matrixlib.Matrix(3, 3)` be a matrix with values `[[1,2,3],[4,5,6],[7,8,9]]`.

```
matrix = matrixlib.neg(a) # returns a matrix list with values [[-1,-2,-3],[-4,-5,-6],[-7,-8,-9]]
```

#### Addition

> The operation `add(a, b, out = False)` is used to perform matrix addition between matrices
> `a` and `b`. The input parameters `a` and `b` may be matrix lists or **Matrix** objects of same dimensions.
> The optional parameter `out` specifies whether to return a matrix list (out = False) or 
> return a **Matrix** object (out = True). It returns the sum of matrices `a` and `b`.
> Let a = matrixlib.Matrix(rows, cols) and b = matrixlib.Matrix(rows, cols).

```
matrix = matrixlib.add(a, b, out = False) # returns the sum of matrices a and b in a matrix list output format
```

##### Example:

> Let `a = matrixlib.Matrix(3, 3)` be a matrix with values `[[1,2,3],[4,5,6],[7,8,9]]` and 
> `b = matrixlib.Matrix(3,3)` be a matrix with values `[[1,2,3],[4,5,6],[7,8,9]]`.

```
matrix = matrixlib.add(a, b, out = False) # returns a matrix list with values [[2,4,6],[8,10,12],[14,16,18]].
```

#### Subtraction

> Matrix subtraction between matrices `a` and `b` is performed by operation
> `sub(a, b, out = False)`. The input parameters `a` and `b` may be matrix 
> lists or **Matrix** objects of same dimensions. The optional parameter `out` 
> specifies whether to return a matrix list (out = False) or return a **Matrix** 
> object (out = True). It returns the difference of matrices `a` and `b`.
> Let a = matrixlib.Matrix(rows, cols) and b = matrixlib.Matrix(rows, cols).


```
matrix = matrixlib.sub(a, b, out = False) # returns matrix a subtracted from b
```

##### Example:

> Let `a = matrixlib.Matrix(3, 3)` be a matrix with values `[[1,2,3],[4,5,6],[7,8,9]]` and 
> `b = matrixlib.Matrix(3,3)` be a matrix with values `[[1,2,3],[4,5,6],[7,8,9]]`.

```
matrix = matrixlib.sub(a, b, out = False) # returns a matrix list with values [[0,0,0],[0,0,0],[0,0,0]]
```

#### Transposition

> The operation `tpose(a, out = False)` transposes matrix `a`. The input parameter `a` 
> may be a matrix list or a **Matrix** object. The optional parameter `out` 
> specifies whether to return a matrix list (out = False) or return a **Matrix** 
> object (out = True). Let a = matrixlib.Matrix(rows, cols). 

```
matrix = matrixlib.tpose(a, out = False) # returns matrix transposition of a in matrix list output format
```

##### Example:

> Let `a = matrixlib.Matrix(3, 3)` be a matrix with values `[[1,1,1],[0,1,1],[0,0,1]]`.

```
matrix = matrixlib.tpose(a, out = False) # returns a matrix list with values [[1,0,0],[1,1,0],[1,1,1]]
```

#### Multiplication

> 

```

```

##### Example:

>

```

```

#### System of linear equations solver

> 

```

```

##### Example:

>

```

```

#### Determinant

> 

```

```

##### Example:

>

```

```

#### Matrix inverter

> 

```

```

##### Example:

>

```

```

#### Scalar multiplication

> 

```

```

##### Example:

>

```

```

#### Dot product

> 

```

```

##### Example:

>

```

```

#### Method of the least squares

> 

```

```

##### Example:

>

```

```

### Error and Exception handling

> 

```

```

##### Example:

>

```

```
