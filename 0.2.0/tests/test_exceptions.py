import unittest
from random import randint
import matrixlib as ml
from matrixlib.exceptions import *

class TestMatrix(unittest.TestCase):

    def test_init(self):
        with self.assertRaises(InvalidDimension):
            x = ml.Matrix(-1,randint(1,10))
            y = ml.Matrix(randint(1,10),0)

    def test_getter(self):
        x = ml.Matrix(randint(1,10),randint(1,10))
        with self.assertRaises(InvalidDimension):
            x.__getitem__(-1)
            x.__getitem__(0,x._Matrix__cols)

    def test_setter(self):
        x = ml.Matrix(randint(1, 10), randint(1, 10))
        with self.assertRaises(InvalidDimension):
            x.__setitem__([0 for i in range(x._Matrix__cols)],-1)
            x.__setitem__([[0] for i in range(x._Matrix__rows)],None,x._Matrix__cols)
            x.__setitem__([0 for i in range(x._Matrix__cols+1)],1)
            x.__setitem__([[0] for i in range(x._Matrix__rows+1)],None,1)
        with self.assertRaises(TypeError):
            x.__setitem__("siuuu",1,1)

    def test_deleter(self):
        pass

    def test_container(self):
        pass

    def test_comparator(self):
        pass

class TestOperations(unittest.TestCase):

    def test_validate(self):
        pass

    def test_negation(self):
        pass

    def test_addition(self):
        pass

    def test_subtraction(self):
        pass

    def test_transposition(self):
        pass

    def test_multiplication(self):
        pass

    def test_linearsolve(self):
        pass

    def test_determinant(self):
        pass

    def test_inversematrix(self):
        pass

    def test_scalarmultiplication(self):
        pass

    def test_dotproduct(self):
        pass

    def test_leastsquares(self):
        pass

if __name__ == '__main__':
    unittest.main()