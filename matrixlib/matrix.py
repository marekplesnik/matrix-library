from numbers import Rational
from copy import deepcopy
from fractions import Fraction
from matrixlib.exceptions import *

class Matrix:

    def __init__(self, __rows, __cols):
        self.__rows = __rows
        self.__cols = __cols
        self.__matrix = [[0 for i in range(__cols)] for j in range(__rows)]

    def __getitem__(self, row = None, col = None):
        if row != None and (row < 0 or row >= self.__rows):
            raise InvalidDimension
        if col != None and (col < 0 or col >= self.__cols):
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
        if isinstance(value, Rational):
            return any(self.__matrix[i][j] == value for i in range(self.__rows) for j in range(self.__cols))
        else:
            raise TypeError

    def __eq__(self, other):
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

    def __repr__(self):
        top = max(len(str(self.__matrix[i][j])) for i in range(self.__rows) for j in range(self.__cols))
        return "\n".join(["| " + " ".join([str(i).ljust(top) for i in self.__matrix[j]]) + " |" for j in range(self.__rows)])