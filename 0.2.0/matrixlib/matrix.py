from numbers import Rational
from fractions import Fraction
from random import choice
from matrixlib.exceptions import *

class Matrix:

    def __init__(self, __rows: int, __cols: int):
        """
        Initializes the Matrix class
        Args:
            __rows: number of matrix's rows
            __cols: number of matrix's columns
        Returns:
            None
        Raises:
            InvalidDimension: if either there aren't any rows or columns
        """
        if __rows <= 0 or __cols <= 0:
            raise InvalidDimension
        self.__rows = __rows
        self.__cols = __cols
        self.__matrix = [[0 for i in range(__cols)] for j in range(__rows)]

    def __getitem__(self, row = None, col = None):
        """
        Getter for the Matrix class
        Args:
            row: None or row coordinate
            col: None or column coordinate
        Returns:
            Element, Matrix, row or column
        Raises:
            InvalidDimension: row or col out of bounds
        """
        if (row != None and (row < 0 or row >= self.__rows)) or (col != None and (col < 0 or col >= self.__cols)):
            raise InvalidDimension
        if row != None and col != None:
            return self.__matrix[row][col]
        elif row != None:
            return self.__matrix[row]
        elif col != None:
            return [[self.__matrix[i][col]] for i in range(self.__rows)]
        else:
            return self.__matrix

    def __setitem__(self, value, row = None, col = None):
        """
        Setter for the Matrix class
        Args:
            value: Matrix, 2D list, row, column or element
            row: None or row coordinate
            col: None or column coordinate
        Returns:
            None
        Raises:
            InvalidDimension: row or col out of bounds, differing value dimension
            TypeError: not rational, not 2D list
        """
        if row != None and (row < 0 or row >= self.__rows):
            raise InvalidDimension
        if col != None and (col < 0 or col >= self.__cols):
            raise InvalidDimension
        if row != None and col != None:
            if isinstance(value, Rational):
                self.__matrix[row][col] = value
                return
            else:
                raise TypeError
        if not isinstance(value, list):
            raise TypeError
        if row == None and col == None:
            if len(value) != self.__rows:
                raise InvalidDimension
            for i in range(len(value)):
                if len(value[i]) != self.__cols:
                    raise InvalidDimension
            if not all(isinstance(value[i][j], Rational) for i in range(self.__rows) for j in range(self.__cols)):
                raise TypeError
            self.__matrix = value
            return
        if row != None:
            if not all(isinstance(value[i], Rational) for i in range(len(value))):
                raise TypeError
            if len(value) == self.__cols:
                self.__matrix[row] = value
                return
            else:
                raise InvalidDimension
        if col != None:
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

    def __delitem__(self, row = None, col = None):
        """
        Deleter of rows or columns for the Matrix class
        Args:
            row: None or row coordinate
            col: None or column coordinate
        Returns:
            None
        Raises:
            InvalidDimension: row or col out of bounds
        """
        if row != None and (row < 0 or row >= self.__rows):
            raise InvalidDimension
        if col != None and (col < 0 or col >= self.__cols):
            raise InvalidDimension
        if row != None and col != None:
            raise ValueError
        if row != None and self.__rows != 1:
            self.__rows -= 1
            del self.__matrix[row]
        elif col != None and self.__cols != 1:
            self.__cols -= 1
            for i in range(self.__rows):
                del self.__matrix[i][col]
        else:
            raise ValueError

    def __contains__(self, value):
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

    def __eq__(self, other):
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
                    if self.__matrix[i][j] != other[i][j]:
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

    def __rand__(self, start : int = -10, stop : int = 10):
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

    def __repr__(self):
        """
        Representative method for the Matrix class
        Returns:
             string representation of Matrix
        """
        top = max(len(str(self.__matrix[i][j])) for i in range(self.__rows) for j in range(self.__cols))
        return "\n".join(["| " + " ".join([str(i).ljust(top) for i in self.__matrix[j]]) + " |" for j in range(self.__rows)])