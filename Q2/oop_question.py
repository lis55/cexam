"""
Hint: Use map and filter from the standard Python library.

Remember that you are not allowed to use Numpy.
"""


class Tensor:
    """
    Class to represent a multidimensional Tensor.

    1. You need to implement first the __init__ method.

    2. The __str__, reduce, map, mask and filter method must be abstract.
       What is the implementation of an abstract method?
    """
    def __init__(self, xs, shape):
        """
        xs is the list of numbers stored in the Tensor and a tuple
        containing the size of each dimension.
        """
        raise NotImplementedError()

    def __str__(self):
        """
        Transforms an Tensor into a string.
        """
        raise NotImplementedError()

    def reduce(self, function, axis=0):
        """
        Using the `function` accumulate over one axis. See below the examples
        for Vector, Matrix and Array3D.
        """
        raise NotImplementedError()

    def map(self, function):
        """
        Apply a function uniformly over all the number in the Tensor.
        """
        raise NotImplementedError()

    def mask(self, predicate):
        """
        using the predicate transform all the values in the Tensor to Booleans.
        """
        raise NotImplementedError()

    def filter(self, predicate):
        """
        
        """
        raise NotImplementedError()


class Vector(Tensor):
    """
    """
    def __init__(self, xs, shape):
        raise NotImplementedError()

    def __str__(self):
        """
        example:
           v = Vector([1, 2, 3], (3))
           print(v)
           Vector [1, 2, 3]
        """
        raise NotImplementedError()

    def map(self, function):
        """
        example:
           from math import sqrt
           v = Vector([1, 2, 3], (3))
           r = v.map(sqrt)
           print(r)
           Vector [1.0, 1.41, 1.73]
        """
        raise NotImplementedError()

    def reduce(self, function, axis=0):
        """
        example:
           v = Vector([1, 2, 3], (3))
           r = v.reduce(lambda x, acc: x + acc)
           print(r)
           6
        """
        raise NotImplementedError()

    def mask(self, predicate):
        """
        example:
           v = Vector([2, 5, 1, 3], (4))
           r = v.mask(lambda x: x > 2)
           print(r)
           [False, True, False, True]
        """
        raise NotImplementedError()

    def filter(self, predicate):
        """
        This method must be implemented using mask.

        example:
           v = Vector([2, 5, 1, 3], (4))
           r = v.filter(lambda x: x > 2)
           print(r)
           Vector [5, 3]
        """
        raise NotImplementedError()


class Matrix(Tensor):
    """
    """

    def __init__(self, xs, shape):
        raise NotImplementedError()

    def __str__(self):
        """
        example:
           shape = (2, 3)
           a3 = Matrix([1, 2, 3, 4, 5, 6]], shape)
           print(a3)
           Matrix [[1, 2, 3], [4, 5, 6]])
        """
        raise NotImplementedError()

    def map(self, function):
        """
        example:
           shape = (2, 3)
           a3 = Matrix([1, 2, 3, 4, 5, 6], shape)
           r = a3.map(lambda x: x * 2)
           print(r)
           Matrix [[2, 4, 6], [8, 10, 12]]
        """
        raise NotImplementedError()

    def reduce(self, function, axis=0):
        """
        example:
           shape = (2, 3)
           m = Matrix([1, 2, 3, 4, 5, 6], shape)
           function = lambda x, acc: x * acc)
           r1 = m.reduce(function)
           r2 = m.reduce(function, axis=1)
           print(r1)
           Vector [6, 120]
           print(r2)
           Vector [4, 10, 18]
        """
        raise NotImplementedError()

    def mask(self, predicate):
        """
        example:
           shape = (2, 3)
           m = Matrix([1, 3, 2, 4, 0, 5], shape)
           r = m.mask(lambda x: x > 2)
           print(r)
           Matrix [[False, True, False], [True, False, True]]
        """
        raise NotImplementedError()

    def filter(self, predicate):
        """
        This function must be implemented using the previous mask method.

        example:
           shape = (2, 3)
           m = Matrix([1, 3, 2, 4, 0, 5], shape)
           r = m.filter(lambda x: x > 2)
           print(r)
           Vector [3, 4, 5]
        """
        raise NotImplementedError()


class Array3D(Tensor):
    """
    Creates a Tensor object representing a 3-dimensional array.
    """

    def __init__(self, xs, shape):
        """
        Initialization.
        """
        raise NotImplementedError()

    def __str__(self):
        """
        example:
           shape = (2, 2,  3)
           a3 = Array3D([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], shape)
           print(a3)
           Array3D [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
        """
        raise NotImplementedError()

    def map(self, function):
        """
        example:
           from math import (pi, sin)
           shape = (2, 2, 3)
           a3 = Array3D([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], shape)
           r = a3.map(lambda x: sin(x * pi / 2))
           print(r)
           Array3D [[[1, 0, -1], [0, 1, 0]], [[-1, 0, 1], [0, -1, 0]]]
        """
        raise NotImplementedError()

    def reduce(self, function, axis=0):
        """
        example:
           shape = (2, 2, 3)
           a3 = Array3D([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], shape)
           function = lambda x, acc: x + acc
           r1 = a3.reduce(function)
           r2 = a3.reduce(function, axis=1)
           r3 = a3.reduce(function, axis=2)
           print(r1)
           Matrix [[8, 10, 12], [14, 16, 18]]
           print(r2)
           Matrix [[5, 7, 9], [17, 19, 21]]
           print(r3)
           Matrix [[6, 15], [24, 33]]
        """
        raise NotImplementedError()

    def mask(self, predicate):
        """
        example:
           shape = (2, 2, 3)
           a3 = Array3D([1, 3, 2, 4, 0, 5, -23, 4, 12, -2, 0, 2], shape)
           r = a3.mask(lambda x: x > 2)
           print(r)
           Array3D [[[False, True, False], [True, False, True]],
                    [[False, True, True], [False, False, False]]]
        """
        raise NotImplementedError()

    def filter(self, predicate):
        """
        example:
           shape = (2, 2, 3)
           a3 = Array3D([1, 3, 2, 4, 0, 5, -23, 4, 12, -2, 0, 2], shape)
           r = m.filter(lambda x: x > 2)
           print(r)
           Vector [3, 4, 5, 4, 12]
        """
        raise NotImplementedError()
