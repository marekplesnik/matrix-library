from .matrix import *
from .operations import *
from .exceptions import *


def validate(a): return Operations.validate(a)
def neg(a, out = False): return Operations.negation(a, out)
def add(a, b, out = False): return Operations.addition(a, b, out)
def sub(a, b, out = False): return Operations.subtraction(a, b, out)
def tpose(a, out = False): return Operations.transposition(a, out)
def mul(a, b, out = False): return Operations.multiplication(a, b, out)
def lin_sol(a, b, out = False): return Operations.linear_solve(a, b, out)
def det(a): return Operations.determinant(a)
def inverse(a, out = False): return Operations.inverse_matrix(a, out)
def sc_mul(a, x, out = False): return Operations.scalar_multiplication(a, x, out)
def dot(a, b): return Operations.dot_product(a, b)
def least_squares(a, b, out = False): return Operations.least_squares(a, b, out)