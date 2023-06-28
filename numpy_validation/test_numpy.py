import unittest
from copy import deepcopy
from random import randrange, randint
from math import isclose
import numpy as np
import matrixlib as ml


class NumpyAndMatrixlib(unittest.TestCase):

    def test_negation(self):
        m, n = randint(1, 50), randint(1, 50)
        x = ml.Matrix(m, n).rand()
        a, b = np.negative(deepcopy(x)._Matrix__matrix), (-x)._Matrix__matrix
        self.assertTrue(all([a[i][j] == b[i][j] for i in range(m) for j in range(n)]))

    def test_addition(self):
        m, n = randint(1, 50), randint(1, 50)
        x, y = ml.Matrix(m, n).rand(), ml.Matrix(m, n).rand()
        a, b = np.add(deepcopy(x)._Matrix__matrix, deepcopy(y)._Matrix__matrix), (x+y)._Matrix__matrix
        self.assertTrue(all([a[i][j] == b[i][j] for i in range(m) for j in range(n)]))

    def test_subtraction(self):
        m, n = randint(1, 50), randint(1, 50)
        x, y = ml.Matrix(m, n).rand(), ml.Matrix(m, n).rand()
        a, b = np.subtract(deepcopy(x)._Matrix__matrix, deepcopy(y)._Matrix__matrix), (x-y)._Matrix__matrix
        self.assertTrue(all([a[i][j] == b[i][j] for i in range(m) for j in range(n)]))

    def test_transposition(self):
        m, n = randint(1, 50), randint(1, 50)
        x = ml.Matrix(m, n).rand()
        a, b = np.transpose(deepcopy(x)._Matrix__matrix), (x**"t")._Matrix__matrix
        self.assertTrue(all([a[i][j] == b[i][j] for i in range(n) for j in range(m)]))

    def test_multiplication(self):
        m, n, p = randint(1, 20), randint(1, 20), randint(1, 20)
        x, y = ml.Matrix(m, n).rand(), ml.Matrix(n, p).rand()
        a, b = np.matmul(deepcopy(x)._Matrix__matrix, deepcopy(y)._Matrix__matrix), (x@y)._Matrix__matrix
        self.assertTrue(all([a[i][j] == b[i][j] for i in range(m) for j in range(p)]))

    def test_linearsolve(self):
        n = randint(2, 10)
        x, y = ml.Matrix(n, n).rand(), ml.Matrix(n, 1).rand()
        while x.det() == 0:
            x.rand()
        a, b = np.linalg.solve(np.array(deepcopy(x)._Matrix__matrix, dtype='float64'), np.array([deepcopy(y)._Matrix__matrix[i][0] for i in range(n)],dtype='float64')), x.lin_sol(y)._Matrix__matrix
        self.assertTrue(all([isclose(a[i], b[i][0]) for i in range(n)]))

    def test_determinant(self):
        n = randint(1, 50)
        x = ml.Matrix(n, n).rand()
        a, b = np.linalg.det(np.array(deepcopy(x)._Matrix__matrix,dtype='float64')), x.det()
        self.assertTrue(isclose(a, b))

    def test_inverse(self):
        n = randint(1, 10)
        x = ml.Matrix(n, n).rand()
        while x.det() == 0:
            x.rand()
        a, b = np.linalg.inv(np.array(deepcopy(x)._Matrix__matrix,dtype='float64')), (x**(-1))._Matrix__matrix

    def test_scalarmultiplication(self):
        m, n, y = randint(1,50), randint(1,50), randrange(-100,100)
        x = ml.Matrix(m, n).rand()
        a, b = np.array(deepcopy(x)._Matrix__matrix)*y, (y*x)._Matrix__matrix
        self.assertTrue(all([isclose(a[i][j], b[i][j]) for i in range(x._Matrix__rows) for j in range(x._Matrix__cols)]))

    def test_dotproduct(self):
        n = randint(1, 20)
        x, y = ml.Matrix(n,1).rand(), ml.Matrix(n,1).rand()
        a, b = np.dot([deepcopy(x)._Matrix__matrix[i][0] for i in range(n)], [deepcopy(y)._Matrix__matrix[i][0] for i in range(n)]), x*y
        self.assertTrue(isclose(a, b))

    def test_leastsquares(self):
        m, n = randint(1, 10), randint(1, 10)
        x, y = ml.Matrix(m, n).rand(), ml.Matrix(m, 1).rand()
        if ((x**"t")@x).det() == 0:
            self.assertTrue(True)
        else:
            a, b = np.linalg.lstsq(np.array(deepcopy(x)._Matrix__matrix,dtype = 'float64'), np.array([deepcopy(y)._Matrix__matrix[i][0] for i in range(m)],dtype = 'float64'),rcond=1)[0], x.least_squares(y)._Matrix__matrix
            self.assertTrue(all([isclose(a[i],b[i][0]) for i in range(n)]))


if __name__ == '__main__':
    unittest.main()