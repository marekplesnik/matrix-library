import unittest
from copy import deepcopy
from random import randrange, randint
from math import isclose
import numpy as np
import matrixlib as ml

class NumpyAndMatrixlib(unittest.TestCase):

    def test_negation(self):
        m, n = randint(1,50), randint(1,50)
        x = ml.Matrix(m,n)
        x.__rand__()
        a, b = ml.neg((deepcopy(x))), np.negative(x._Matrix__matrix)
        self.assertTrue(all([a[i][j] == b[i][j]  for i in range(x._Matrix__rows) for j in range(x._Matrix__cols)]))

    def test_addition(self):
        m, n = randint(1,50), randint(1,50)
        x, y = ml.Matrix(m,n), ml.Matrix(m,n)
        x.__rand__(), y.__rand__()
        a, b = ml.add(deepcopy(x), deepcopy(y)), np.add(x._Matrix__matrix, y._Matrix__matrix)
        self.assertTrue(all([a[i][j] == b[i][j] for i in range(x._Matrix__rows) for j in range(x._Matrix__cols)]))

    def test_subtraction(self):
        m, n = randint(1, 50), randint(1, 50)
        x, y = ml.Matrix(m,n), ml.Matrix(m,n)
        x.__rand__(), y.__rand__()
        a, b = ml.sub(deepcopy(x), deepcopy(y)), np.subtract(x._Matrix__matrix, y._Matrix__matrix)
        self.assertTrue(all([a[i][j] == b[i][j] for i in range(x._Matrix__rows) for j in range(x._Matrix__cols)]))

    def test_transposition(self):
        m, n = randint(1,50), randint(1,50)
        x = ml.Matrix(m,n)
        x.__rand__()
        a, b = ml.tpose(deepcopy(x)), np.transpose(x._Matrix__matrix)
        self.assertTrue(all([a[i][j] == b[i][j] for i in range(x._Matrix__cols) for j in range(x._Matrix__rows)]))

    def test_multiplication(self):
        m, n, p = randint(1,20), randint(1,20), randint(1,20)
        x, y = ml.Matrix(m,n), ml.Matrix(n,p)
        x.__rand__(), y.__rand__()
        a, b = ml.mul(deepcopy(x), deepcopy(y)), np.matmul(x._Matrix__matrix, y._Matrix__matrix)
        self.assertTrue(all([a[i][j] == b[i][j] for i in range(m) for j in range(p)]))

    def test_linearsolve(self):
        n = randint(2,10)
        x, y = ml.Matrix(n,n), ml.Matrix(n,1)
        x.__rand__(), y.__rand__()
        while ml.det(x) == 0:
            x.__rand__()
        a = ml.lin_sol(deepcopy(x),deepcopy(y))
        b = np.linalg.solve(np.array(x._Matrix__matrix,dtype = 'float64'),np.array([y._Matrix__matrix[i][0] for i in range(n)],dtype = 'float64'))
        self.assertTrue(all([isclose(a[i][0], b[i]) for i in range(n)]))

    def test_determinant(self):
        n = randint(1,50)
        x = ml.Matrix(n,n)
        x.__rand__()
        a, b = ml.det(deepcopy(x)), np.linalg.det(np.array(x._Matrix__matrix,dtype='float64'))
        self.assertTrue(isclose(a,b))

    def test_inverse(self):
        n = randint(1,10)
        x = ml.Matrix(n,n)
        x.__rand__()
        a, b = ml.inverse((deepcopy(x))), np.linalg.inv(np.array(x._Matrix__matrix,dtype='float64'))
        self.assertTrue(all([isclose(a[i][j],b[i][j])  for i in range(x._Matrix__rows) for j in range(x._Matrix__cols)]))

    def test_scalarmultiplication(self):
        m, n, y = randint(1,50), randint(1,50), randrange(-100,100)
        x = ml.Matrix(m,n)
        x.__rand__()
        a, b = ml.sc_mul(deepcopy(x),y), np.array(x._Matrix__matrix) * y
        self.assertTrue(all([isclose(a[i][j], b[i][j]) for i in range(x._Matrix__rows) for j in range(x._Matrix__cols)]))

    def test_dotproduct(self):
        n = randint(1,20)
        x, y = ml.Matrix(n,1), ml.Matrix(n,1)
        x.__rand__(), y.__rand__()
        a = ml.dot(deepcopy(x),deepcopy(y))
        b = np.dot([x._Matrix__matrix[i][0] for i in range(n)], [y._Matrix__matrix[i][0] for i in range(n)])
        self.assertTrue(isclose(a,b))

    def test_leastsquares(self):
        m, n = randint(1,10), randint(1,10)
        x, y = ml.Matrix(m,n), ml.Matrix(m,1)
        x.__rand__(), y.__rand__()
        a = ml.least_squares(deepcopy(x),deepcopy(y))
        b = np.linalg.lstsq(np.array(x._Matrix__matrix,dtype = 'float64'), np.array([y._Matrix__matrix[i][0] for i in range(m)],dtype = 'float64'),rcond=1)[0]
        self.assertTrue(all([isclose(a[i][0],b[i]) for i in range(n)]))

if __name__ == '__main__':
    unittest.main()
