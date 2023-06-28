from numbers import Rational
from fractions import Fraction
from random import choice
from matrixlib.exceptions import *
from copy import deepcopy


class MatrixMeta(type):

    def __instancecheck__(cls, instance): # overriden isinstance checkup
        """
        isinstance method for the Matrix class
        Args:
            instance: Matrix, 2D list
        Returns:
            True or False
        Raises:
            TypeError: not Matrix, not 2D list
        """
        if isinstance(instance, list):
            if all(isinstance(instance[i], list) for i in range(len(instance))):
                if all(len(instance[i]) == len(instance[0]) for i in range(len(instance))):
                    if all(isinstance(instance[i][j], Rational) for i in range(len(instance)) for j in range(len(instance[0]))):
                        return True
        return False


class Matrix(metaclass=MatrixMeta):

    def __init__(self, __rows: int, __cols: int, __key: Rational = None): # constructor
        """
        Initializes the Matrix class
        Args:
            __rows: number of matrix's rows
            __cols: number of matrix's columns
            __key: default value for all matrix's elements, 2D list of dimensions __rows by __cols
        Returns:
            None
        Raises:
            InvalidDimension: if either there are not any rows or columns
            TypeError: key is not rational, __key cannot be instance of Matrix class
        """
        if __rows <= 0 or __cols <= 0:
            raise InvalidDimension
        if __key == None:
            self.__matrix = [[None for i in range(__cols)] for j in range(__rows)]
        elif isinstance(__key, Rational):
            self.__matrix = [[__key for i in range(__cols)] for j in range(__rows)]
        elif isinstance(__key, Matrix) and __rows == len(__key) and __cols == len(__key[0]):
            self.__matrix = __key
        else:
            raise TypeError
        self.__rows = __rows
        self.__cols = __cols

    def __getitem__(self, key): # getter
        """
        Getter for the Matrix class
        Args:
            key: list [row, col], where row, col are None or coordinates
        Returns:
            Specific element, row or column
        Raises:
            InvalidDimension: row or col out of bounds
        """
        row, col = key
        if (row != None and (row < 0 or row >= self.__rows)) or (col != None and (col < 0 or col >= self.__cols)):
            raise InvalidDimension
        if row == None and col == None:
            return self.__matrix
        elif row != None:
            return self.__matrix[row]
        elif col != None:
            return [[self.__matrix[i][col]] for i in range(self.__rows)]
        else:
            return self.__matrix[row][col]

    def __setitem__(self, key, value): # setter
        """
        Setter for the Matrix class
        Args:
            key: list [row, col], where row, col are None or coordinates
            value: Matrix, 2D list, row, column or element
        Returns:
            None
        Raises:
            InvalidDimension: row or col out of bounds, differing value dimension
            TypeError: not rational, not 2D list or not Matrix
        """
        row, col = key
        if (row != None and (row < 0 or row >= self.__rows)) or (col != None and (col < 0 or col >= self.__cols)):
            raise InvalidDimension
        if row != None and col != None:
            if isinstance(value, Rational):
                self.__matrix[row][col] = value
                return None
            raise TypeError
        if row == None and col == None:
            if isinstance(value, Matrix) and not isinstance(value, list):
                if self.__rows == value._Matrix__rows and self.__cols == value._Matrix__cols:
                    self.__matrix = value._Matrix__matrix
                else:
                    raise InvalidDimension
            elif isinstance(value, list):
                if len(value) != self.__rows:
                    raise InvalidDimension
                for i in range(len(value)):
                    if len(value[i]) != self.__cols:
                        raise InvalidDimension
                if not all(isinstance(value[i][j], Rational) for i in range(self.__rows) for j in range(self.__cols)):
                    raise TypeError
                self.__matrix = value
            else:
                raise TypeError
            return None
        if row != None:
            if not isinstance(value, list) and isinstance(value, Matrix):
                if self.__cols != value.__cols or value.__rows != 1:
                    raise InvalidDimension
                for i in range(self.__cols):
                    self.__matrix[row][i] = value.__matrix[0][i]
            elif isinstance(value, list):
                if not all(isinstance(value[i], Rational) for i in range(len(value))):
                    raise TypeError
                if len(value) == self.__cols:
                    self.__matrix[row] = value
                    return
                else:
                    raise InvalidDimension
            else:
                raise TypeError
        if col != None:
            if not isinstance(value, list) and isinstance(value, Matrix):

                if self.__rows != value.__rows or value.__cols != 1:
                    raise InvalidDimension
                for i in range(self.__rows):
                    self.__matrix[i][col] = value.__matrix[i][0]
            elif isinstance(value, list):
                if not all(isinstance(value[i], list) for i in range(len(value))):
                    raise TypeError
                if not all(isinstance(value[i][j], Rational) for i in range(len(value)) for j in range(len(value[0]))):
                    raise TypeError
                for i in range(len(value)):
                    if len(value[0]) != len(value[i]):
                        raise InvalidDimension
                if len(value) == self.__rows:
                    for i in range(self.__rows):
                        self.__matrix[i][col] = value[i][0]
                    return
                else:
                    raise InvalidDimension
            else:
                raise TypeError

    def __delattr__(self, key): # attribute (row, column) deleter
        """
        Attribute deleter of rows or columns for the Matrix class
        Args:
            key: list [row, col], where row, col are None or coordinates
        Returns:
            None
        Raises:
            InvalidDimension: row or col out of bounds
            ValueError: attempt to delete specific element or entire Matrix
        """
        row, col = key.strip()
        if (row != "x" and (int(row) < 0 or int(row) >= self.__rows)) or (
                col != "x" and (int(col) < 0 or int(col) >= self.__cols)):
            raise InvalidDimension
        if row != "x" and col != "x":
            raise ValueError
        if row != "x" and self.__rows != 1:
            self.__rows -= 1
            del self.__matrix[int(row)]
        elif col != "x" and self.__cols != 1:
            self.__cols -= 1
            for i in range(self.__rows):
                del self.__matrix[i][int(col)]
        else:
            raise ValueError

    def __contains__(self, value): # checking containment
        """
        Container for a Matrix class
        Args:
            value: element
        Returns:
            True or False
        Raises:
            TypeError: not rational
        """
        if isinstance(value, Rational):
            return any(self.__matrix[i][j] == value for i in range(self.__rows) for j in range(self.__cols))
        else:
            raise TypeError

    def __eq__(self, other): # equality comparator
        """
        Comparator for the Matrix class
        Args:
            other: Matrix or 2D list
        Returns:
            True or False
        """
        if isinstance(other, Matrix) and self.__rows == other.__rows and self.__cols == other.__cols:
            for i in range(self.__rows):
                for j in range(self.__cols):
                    if self.__matrix[i][j] != other._Matrix__matrix[i][j]:
                        return False
            return True
        if len(other) != self.__rows:
            return False
        for i in range(len(other)):
            if len(other[i]) != self.__cols:
                return False
        for i in range(self.__rows):
            for j in range(self.__cols):
                if self.__matrix[i][j] != other[i][j]:
                    return False
        return True

    def __repr__(self): # object representation
        """
        Representative method for the Matrix class
        Returns:
            string representation of Matrix object
        """
        return f'Matrix object of dimensions {self.__rows} by {self.__cols}'

    def __str__(self): # string representation
        """
        String method for the Matrix class
        Returns:
            string representation of Matrix
        """
        top = max(len(str(self.__matrix[i][j])) for i in range(self.__rows) for j in range(self.__cols))
        return "\n".join(["| " + " ".join([str(i).ljust(top) for i in self.__matrix[j]]) + " |" for j in range(self.__rows)])

    def rand(self, start: int = -10, stop: int = 10): # random matrix generator
        """
        Random matrix generator method for the Matrix class
        Args:
            start: -10(default), integer
            stop: 10(default), integer
        Returns:
            Matrix of given dimensions with elements in form of Fraction(...,...)
        """
        for i in range(self.__rows):
            for j in range(self.__cols):
                r = list(range(start, stop))
                a = choice(r)
                r.remove(0)
                b = choice(r)
                self.__matrix[i][j] = Fraction(a, b)
        return self

    def unit(self, key=1): # diagonal (unitary) matrix generator
        """
        Generates either a unitary or a diagonal matrix that can be non-square
        Args:
            key:
        Returns:
            Diagonal (unitary) matrix
        Raises:
            TypeError:
        """
        if key == 1:
            self.__matrix = [[0 for i in range(self.__cols)] for j in range(self.__rows)]
            for i in range(min(self.__rows, self.__cols)):
                self.__matrix[i][i] = 1
            return self
        elif isinstance(key, Rational):
            self.__matrix = [[0 for i in range(self.__cols)] for j in range(self.__rows)]
            for i in range(min(self.__rows, self.__cols)):
                self.__matrix[i][i] = key
            return self
        elif isinstance(key, list) and len(key) == min(self.__rows, self.__cols):
            self.__matrix = [[0 for i in range(self.__cols)] for j in range(self.__rows)]
            for i in range(min(self.__rows, self.__cols)):
                self.__matrix[i][i] = key[i]
            return self
        else:
            raise TypeError

    def validate(self): # matrix validation for non Nonetype elements
        """
        Method for validation of not NoneType elements
        Returns:
            True or False
        """
        for i in range(self.__rows):
            for j in range(self.__cols):
                if self.__matrix[i][j] == None:
                    return False
        return True

    def __neg__(self): # matrix negation
        """
        Method for negating a matrix
        Returns:
            negated matrix
        Raises:
            ValueError: elements with None value
        """
        if not self.validate():
            raise ValueError
        a = Matrix(self.__rows, self.__cols)
        for i in range(self.__rows):
            for j in range(self.__cols):
                a.__matrix[i][j] = -self.__matrix[i][j]
        return a

    def __add__(self, a): # matrix addition
        """
        Method for matrix addition
        Args:
            a: Matrix object, 2D list
        Returns:
            matrix of addition with a
        Raises:
            InvalidDimension: differing dimension
            ValueError: elements with None value
        """
        if not isinstance(a, Matrix):
            raise TypeError
        if isinstance(a, list):
            if len(a) != self.__rows or len(a[0]) != self.__cols:
                raise InvalidDimension
            b = Matrix(len(a), len(a[0]), a)
        else:
            if a.__rows != self.__rows or a.__cols != self.__cols:
                raise InvalidDimension
            b = a
        if not self.validate() or not b.validate():
            raise ValueError
        for i in range(self.__rows):
            for j in range(self.__cols):
                self.__matrix[i][j] += b.__matrix[i][j]
        return self

    def __sub__(self, a): # matrix subtraction
        """
        Method for matrix subtraction
        Args:
            a: Matrix object, 2D list
        Returns:
            matrix of subtraction by a
        Raises:
            InvalidDimension: differing dimension
            ValueError: elements with None value
        """
        if not isinstance(a, Matrix):
            raise TypeError
        if isinstance(a, list):
            if len(a) != self.__rows or len(a[0]) != self.__cols:
                raise InvalidDimension
            b = Matrix(len(a), len(a[0]), a)
        else:
            if a.__rows != self.__rows or a.__cols != self.__cols:
                raise InvalidDimension
            b = a
        if not self.validate() or not b.validate():
            raise ValueError
        for i in range(self.__rows):
            for j in range(self.__cols):
                self.__matrix[i][j] -= b.__matrix[i][j]
        return self

    def __matmul__(self, a): # matrix multiplication
        """
        Method for matrix multiplication
        Args:
            a: Matrix object, 2D list
        Returns:
            matrix of multiplication by a
        Raises:
            Undefined: differing dimension of columns of a and rows of b
            ValueError: elements with None value
        """
        if not isinstance(a, Matrix):
            raise TypeError
        if isinstance(a, list):
            if self.__cols != len(a):
                raise Undefined
            b = Matrix(len(a), len(a[0]), a)
        else:
            if self.__cols != a.__rows:
                raise Undefined
            b = a
        if not self.validate() or not b.validate():
            raise ValueError
        c = Matrix(self.__rows, b.__cols, 0)
        for i in range(self.__rows):
            for j in range(b.__cols):
                for k in range(self.__cols):
                    c.__matrix[i][j] += self.__matrix[i][k] * b.__matrix[k][j]
        return c

    def __rmul__(self, a): # scalar multiplication
        """
        Method for matrix scalar multiplication
        Args:
            a: Rational
        Returns:
            matrix multiplied by the given scalar
        Raises:
            TypeError: not rational
        """
        if not isinstance(a, Rational):
            raise TypeError
        b = Matrix(self.__rows, self.__cols, self.__matrix)
        for i in range(self.__rows):
            for j in range(self.__cols):
                b.__matrix[i][j] *= a
        return b

    def __pow__(self, exponent): # matrix exponentiation, "t" for transposition, (-1) for inverse
        """
        Method for matrix exponentiation
        Args:
            exponent: integer
        Returns:
            exponentiated matrix (or transposed matrix)
        Raises:
            ValueError: elements with None value
            InvalidDimension: non-square matrix
        """
        if not self.validate():
            raise ValueError
        if self.__rows != self.__cols:
            raise InvalidDimension
        if exponent == "t":
            return self.transposition()
        if not isinstance(exponent, int):
            raise ValueError
        if exponent == 0:
            return Matrix(self.__rows, self.__cols, 0)
        if exponent == -1:
            return self.inverse()
        elif exponent > 0:
            a = self
            for i in range(1, exponent):
                self *= a
            return self

    def transposition(self): # transposed matrix
        """
        Method for matrix transposition
        Returns:
            transposed matrix
        Raises:
            ValueError: elements with None value
        """
        if not self.validate():
            raise ValueError
        a = Matrix(self.__cols, self.__rows)
        for i in range(self.__rows):
            for j in range(self.__cols):
                a.__matrix[j][i] = self.__matrix[i][j]
        return a

    def lin_sol(self, a): # system of linear equations solver
        """
        Method for solving system of linear equations represented by a square regular matrix and a vector
        Args:
            a: Matrix object, 2D list
        Returns:
            vector of solution of a system of linear equations
        Raises:
            NoSolution: matrix self is not regular
            InvalidDimension: differing dimension, a not vector
        """
        if not isinstance(a, Matrix):
            raise TypeError
        if self.__rows != self.__cols:
            raise InvalidDimension
        if isinstance(a, list):
            if len(a) != self.__rows or len(a[0]) != 1:
                raise InvalidDimension
            b = Matrix(len(a), len(a[0]), a)
        else:
            if a.__rows != self.__rows or a.__cols != 1:
                raise InvalidDimension
            b = a
        if not self.validate() or not b.validate():
            raise ValueError
        t = 0
        for i in range(self.__rows):
            if self.__matrix[i][i] == 0:
                for j in range(i+1, self.__rows):
                    if self.__matrix[j][i] != 0:
                        self.__matrix[j], self.__matrix[i] = self.__matrix[i], self.__matrix[j]
                        b.__matrix[j][0], b.__matrix[i][0] = b.__matrix[i][0], b.__matrix[j][0]
                        break
            pivot = self.__matrix[i][i]
            if pivot == 0:
                raise NoSolution
            for j in range(i, self.__rows):
                self.__matrix[i][j] = Fraction(self.__matrix[i][j], pivot)
            b.__matrix[i][0] = Fraction(b.__matrix[i][0], pivot)
            for j in range(self.__rows):
                if i == j or self.__matrix[j][i] == 0:
                    continue
                k = self.__matrix[j][i]
                for l in range(t, self.__rows):
                    self.__matrix[j][l] -= k*self.__matrix[i][l]
                b.__matrix[j][0] -= k*b.__matrix[i][0]
            t += 1
        return b

    def det(self): # determinant
        """
        Method for computing matrix's determinant
        Returns:
            Rational ... determinant of matrix self
        Raises:
            ValueError: Nonetype elements in self
            Undefined: Matrix/2D list not square
        """
        if not self.validate():
            raise ValueError
        if self.__rows != self.__cols:
            raise Undefined
        if self.__rows == 1:
            return self.__matrix[0][0]
        if self.__rows == 2:
            return (self.__matrix[0][0]*self.__matrix[1][1] - self.__matrix[0][1]*self.__matrix[1][0])
        d, t = 1, 1
        for i in range(self.__rows):
            if self.__matrix[i][i] == 0:
                for j in range(i + 1, self.__rows):
                    if self.__matrix[j][i] != 0:
                        self.__matrix[j], self.__matrix[i] = self.__matrix[i], self.__matrix[j]
                        t *= (-1)
                        break
            pivot = self.__matrix[i][i]
            if not pivot:
                return 0
            for j in range(i + 1, self.__rows):
                k = Fraction(self.__matrix[j][i], pivot)
                for l in range(i, self.__rows):
                    self.__matrix[j][l] -= k * self.__matrix[i][l]
        for i in range(self.__rows):
            d *= self.__matrix[i][i]
        return d * t

    def inverse(self): # inverse
        """
        Method for computing square matrix's inverse matrix using system of linear equations
        Returns:
            inverse matrix of self
        Raises:
            ValueError: Nonetype elements in self
            InvalidDimension: differing dimension
            ZeroDeterminant: singular matrix
        """
        if not self.validate():
            raise ValueError
        if self.__rows != self.__cols:
            raise InvalidDimension
        c = deepcopy(self)
        if c.det() == 0:
            raise ZeroDeterminant
        b = Matrix(self.__rows, self.__rows, 0)
        for i in range(self.__rows):
            c = deepcopy(self)
            b[None, i] = c.lin_sol([[1] if j==i else [0] for j in range(self.__rows)])
        return b

    def __mul__(self, a): # dot product
        """
        Method for computing matrix's (standard) dot product
        Args:
            a: Matrix, 2D list
        Returns:
            Rational ... dot product of a and b
        Raises:
            InvalidDimension: differing dimension, not vectors
            ValueError: NoneType elements in either self or a
        """
        if not isinstance(a, Matrix):
            raise TypeError
        if self.__cols != 1:
            raise InvalidDimension
        if isinstance(a, list):
            if len(a) != self.__rows or len(a[0]) != 1:
                raise InvalidDimension
            b = Matrix(len(a), len(a[0]), a)
        else:
            if a.__rows != self.__rows or a.__cols != 1:
                raise InvalidDimension
            b = a
        if not self.validate() or not b.validate():
            raise ValueError
        d = 0
        for i in range(self.__rows):
            d += self.__matrix[i][0]*b.__matrix[i][0]
        return Fraction(d)

    def least_squares(self, a): # least squares
        """
        Method for calculating approximate solution using the least squares
        Args:
            a: Matrix object, 2D list
        Returns:
            vector of solution of the least squares regression between self and a
        Raises:
            InvalidDimension: differing dimension, a not vector
            ValueError: NoneType elements in either self or a
            NoSolution: columns of self are not linear independent
        """
        if not isinstance(a, Matrix):
            raise TypeError
        if isinstance(a, list):
            if len(a) != self.__rows or len(a[0]) != 1:
                raise InvalidDimension
            b = Matrix(len(a), len(a[0]), a)
        else:
            if a.__rows != self.__rows or a.__cols != 1:
                raise InvalidDimension
            b = a
        if not self.validate() or not b.validate():
            raise ValueError
        c = deepcopy(self).transposition()
        d, e = c @ self, c @ b
        return d.lin_sol(e)