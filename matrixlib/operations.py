from matrixlib.matrix import *
from fractions import Fraction
from copy import deepcopy
from numbers import Rational

class Operations(Matrix):

    @classmethod
    def validate(cls, a):
        if isinstance(a, Matrix):
            return a
        if not isinstance(a, list):
            raise TypeError
        if not all(isinstance(a[i], list) for i in range(len(a))):
            raise TypeError
        for i in range(len(a)):
            if len(a[i]) != len(a[0]):
                raise InvalidDimension
        if not all(isinstance(a[i][j], Rational) for i in range(len(a)) for j in range(len(a[0]))):
            raise TypeError
        b = Matrix(len(a), len(a[0]))
        b._Matrix__matrix = a
        return b

    @classmethod
    def negative(cls, a, out = False):
        a = Operations.validate(a)
        for i in range(a._Matrix__rows):
            for j in range(a._Matrix__cols):
                a._Matrix__matrix[i][j] *= (-1)
        return a._Matrix__matrix if not out else a

    @classmethod
    def addition(cls, a, b, out = False):
        a = Operations.validate(a)
        b = Operations.validate(b)
        if a._Matrix__rows != b._Matrix__rows or a._Matrix__cols != b._Matrix__cols:
            raise InvalidDimension
        c = cls(a._Matrix__rows, a._Matrix__cols)
        for i in range(a._Matrix__rows):
            for j in range(a._Matrix__cols):
                c._Matrix__matrix[i][j] = a._Matrix__matrix[i][j] + b._Matrix__matrix[i][j]
        return c._Matrix__matrix if not out else c

    @classmethod
    def subtraction(cls, a, b, out = False):
        a = Operations.validate(a)
        b = Operations.validate(b)
        if a._Matrix__rows != b._Matrix__rows or a._Matrix__cols != b._Matrix__cols:
            raise InvalidDimension
        c = cls(a._Matrix__rows, a._Matrix__cols)
        for i in range(a._Matrix__rows):
            for j in range(a._Matrix__cols):
                c._Matrix__matrix[i][j] = a._Matrix__matrix[i][j] - b._Matrix__matrix[i][j]
        return c._Matrix__matrix if not out else c

    @classmethod
    def transposition(cls, a, out=False):
        a = Operations.validate(a)
        b = Matrix(a._Matrix__cols, a._Matrix__rows)
        for i in range(a._Matrix__rows):
            for j in range(a._Matrix__cols):
                b._Matrix__matrix[j][i] = a._Matrix__matrix[i][j]
        return b._Matrix__matrix if not out else b

    @classmethod
    def multiplication(cls, a, b, out=False):
        a = Operations.validate(a)
        b = Operations.validate(b)
        if a._Matrix__cols != b._Matrix__rows:
            raise Undefined
        c = cls(a._Matrix__rows, b._Matrix__cols)
        for i in range(a._Matrix__rows):
            for j in range(b._Matrix__cols):
                for k in range(a._Matrix__cols):
                    c._Matrix__matrix[i][j] += a._Matrix__matrix[i][k] * b._Matrix__matrix[k][j]
        return c._Matrix__matrix if not out else c

    @classmethod
    def linear_solve(cls, a, b, out=False):
        a = Operations.validate(a)
        b = Operations.validate(b)
        if a._Matrix__rows != b._Matrix__rows or b._Matrix__cols != 1 or a._Matrix__rows != a._Matrix__cols:
            raise InvalidDimension
        t = 0
        for i in range(a._Matrix__rows):
            if a._Matrix__matrix[i][i] == 0:
                for j in range(i + 1, a._Matrix__rows):
                    if a._Matrix__matrix[j][i] != 0:
                        a._Matrix__matrix[j], a._Matrix__matrix[i] = a._Matrix__matrix[i], a._Matrix__matrix[j]
                        b._Matrix__matrix[j][0], b._Matrix__matrix[i][0] = b._Matrix__matrix[i][0], \
                            b._Matrix__matrix[j][0]
                        break
            pivot = a._Matrix__matrix[i][i]
            if not pivot:
                raise NoSolution
            for j in range(i, a._Matrix__rows):
                a._Matrix__matrix[i][j] = Fraction(a._Matrix__matrix[i][j], pivot)
            b._Matrix__matrix[i][0] = Fraction(b._Matrix__matrix[i][0], pivot)
            for j in range(a._Matrix__rows):
                if i == j or a._Matrix__matrix[j][i] == 0:
                    continue
                k = a._Matrix__matrix[j][i]
                for l in range(t, a._Matrix__rows):
                    a._Matrix__matrix[j][l] -= k * a._Matrix__matrix[i][l]
                b._Matrix__matrix[j][0] -= k * b._Matrix__matrix[i][0]
            t += 1
        return b._Matrix__matrix if not out else b

    @classmethod
    def determinant(cls, a):
        a = Operations.validate(a)
        if a._Matrix__rows != a._Matrix__cols:
            raise Undefined
        d, t = 1, 1
        for i in range(a._Matrix__rows):
            if a._Matrix__matrix[i][i] == 0:
                for j in range(i + 1, a._Matrix__rows):
                    if a._Matrix__matrix[j][i] != 0:
                        a._Matrix__matrix[j], a._Matrix__matrix[i] = a._Matrix__matrix[i], a._Matrix__matrix[j]
                        t *= (-1)
                        break
            pivot = a._Matrix__matrix[i][i]
            if not pivot:
                return 0
            for j in range(i + 1, a._Matrix__rows):
                k = Fraction(a._Matrix__matrix[j][i], pivot)
                for l in range(i, a._Matrix__rows):
                    a._Matrix__matrix[j][l] -= k * a._Matrix__matrix[i][l]
        for i in range(a._Matrix__rows):
            d *= a._Matrix__matrix[i][i]
        return d

    @classmethod
    def inverse(cls, a, out = False):
        a = Operations.validate(a)
        if a._Matrix__rows != a._Matrix__cols:
            raise InvalidDimension
        if Operations.determinant(deepcopy(a)) == 0:
            raise ZeroDeterminant
        b = Matrix(a._Matrix__rows, a._Matrix__rows)
        for i in range(a._Matrix__rows):
            b.__setitem__(Operations.linear_solve(deepcopy(a), [[1] if j==i else [0] for j in range(a._Matrix__rows)]), None, i)
        return b._Matrix__matrix if not out else b

    @classmethod
    def scalar_multiplication(cls, a, x, out = False):
        a = Operations.validate(a)
        if not isinstance(x, Rational):
            raise TypeError
        for i in range(a._Matrix__rows):
            for j in range(a._Matrix__cols):
                a._Matrix__matrix[i][j] *= x
        return a._Matrix__matrix if not out else a

    @classmethod
    def dot_product(cls, a, b):
        a = Operations.validate(a)
        b = Operations.validate(b)
        d = 0
        if a._Matrix__rows != b._Matrix__rows or a._Matrix__cols != 1 or b._Matrix__cols != 1:
            raise InvalidDimension
        for i in range(a._Matrix__rows):
            d += a._Matrix__matrix[i][0]*b._Matrix__matrix[i][0]
        return Fraction(d)

    @classmethod
    def least_squares(cls, a, b, out = False):
        a = Operations.validate(a)
        b = Operations.validate(b)
        if a._Matrix__rows != b._Matrix__rows or b._Matrix__cols != 1:
            raise InvalidDimension
        c = Operations.transposition(deepcopy(a), True)
        d = Operations.multiplication(c,a,True)
        print(d._Matrix__matrix)
        e = Operations.multiplication(c,b,True)
        print(e._Matrix__matrix)
        f = Operations.linear_solve(d._Matrix__matrix,e._Matrix__matrix)
        return f._Matrix__matrix if not out else f