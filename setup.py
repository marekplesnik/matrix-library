from setuptools import setup

with open("README.md","r") as RM:
    long_description = RM.read()

setup(
    name = "matrixlib",
    version = "1.0.0",
    description = "Python 3.10 package for matrices, matrix operations and methods of linear algebra",
    url = "https://github.com/marekplesnik/matrix-library",
    author = "Marek Plesník",
    long_description = long_description,
    long_description_content_type="text/markdown",
    packages = ["matrixlib"],
    classifiers = ["Programming Language :: Python :: 3.10"],
    python_requires = '>=3.10'
)