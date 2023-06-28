class Undefined(Exception):
    """
    Exception raised when an operation isn't mathematically defined
    """
    pass

class InvalidDimension(Exception):
    """
    Exception raised when dimensions differ
    """
    pass

class ZeroDeterminant(Exception):
    """
    Exception raised when a singular matrix is encountered
    """
    pass

class NoSolution(Exception):
    """
    Exception raised when a system of linear equations doesn't have a unique solution
    """
    pass