from numbers import Real
from matrixlib.exceptions import *

class Matrix:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0 for i in range(cols)] for j in range(rows)]

    def get_item(self, row = None, col = None):
        if row != None and (row < 0 or row >= self.rows):
            raise InvalidDimension
        if col != None and (col < 0 or col >= self.cols):
            raise InvalidDimension
        if row != None and col != None:
            return self.matrix[row][col]
        elif row != None:
            return self.matrix[row]
        elif col != None:
            return [self.matrix[i][col] for i in range(self.rows)]
        else:
            return self.matrix

    def set_item(self, value, row = None, col = None):
        if row != None and (row < 0 or row >= self.rows):
            raise InvalidDimension
        if col != None and (col < 0 or col >= self.cols):
            raise InvalidDimension
        if row != None and col != None:
            if isinstance(value, Real):
                self.matrix[row][col] = value
                return
            else:
                raise TypeError
        if not isinstance(value, list):
            raise TypeError
        if row != None:
            if len(value) == self.cols:
                self.matrix[row] = value
                return
            else:
                raise InvalidDimension
        elif col != None:
            if len(value) == self.rows:
                for i in range(len(value)):
                    self.matrix[i][col] = value[i]
                return
            else:
                raise InvalidDimension
        else:
            if len(value) == self.rows and len(value[0]) == self.cols:
                if all(isinstance(value[i][j], Real) for i in range(self.rows) for j in range(self.cols)):
                    self.matrix = value
                    return
                else:
                    raise TypeError
            else:
                raise InvalidDimension

    def del_item(self, row = None, col = None):
        if row != None and (row < 0 or row >= self.rows):
            raise InvalidDimension
        if col != None and (col < 0 or col >= self.cols):
            raise InvalidDimension
        if row != None and col != None:
            raise ValueError
        if row != None:
            self.rows -= 1
            del(self.matrix[row])
        elif col != None:
            self.cols -= 1
            for i in range(self.rows):
                del self.matrix[i][col]
        else:
            del(self.matrix)

    def cont_item(self, value):
        if isinstance(value, Real):
            return any([self.matrix[i][j] == value for i in range(self.rows) for j in range(self.cols)])
        else:
            raise TypeError

    def eq_item(self, other):
        if isinstance(other, Matrix) and self.rows == other.rows and self.cols == other.cols:
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.matrix[i][j] != other[i][j]:
                        return False
            return True
        else:
            return False

    def repr_mat(self):
        return str("\n".join(["| " + str(i)[1:-1].replace(",","") + " |" for i in self.matrix]))

    def print_mat(self):
        print(self.repr_mat())