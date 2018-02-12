
__author__ = "Shay Brynes"
__license__ = "Apache License 2.0"

from MatrixPy.print_matrix import *
from MatrixPy.gen_matrix import *
from MatrixPy.operations.add import *
from MatrixPy.operations.sub import *
from MatrixPy.operations.mult import *
from MatrixPy.operations.det import *
from MatrixPy.operations.inv import *
from MatrixPy.operations.transpose import *


class Matrix:

    def __init__(self, matrix_input, *ignore, m=None, n=None):
        """""
        Creates an instance of the matrix class.
        
        :param tuple matrix_input: The first Matrix in the addition.
        :param int m: The number of rows in the Matrix.
        :param int n: The number of columns in the Matrix.
        """""

        # If the user has accidentally added more parameters than needed.
        if ignore:
            print("Unnecessary arguments submitted to class constructor.")
            # Throw a type error.
            raise TypeError

        self.matrix = matrix_input

        # If the user has preset 'm'.
        if m is None:

            # 'm' is the number of rows.
            self.m = len(matrix_input)

        else:
            self.m = m

        # If the user has preset 'n'.
        if n is None:

            # 'n' is the number of columns.
            self.n = len(matrix_input[0])

        else:
            self.n = n

    def get_tuple(self):
        """""
        Returns the tuple associated with the matrix object.
        
        :return: The elements that make up the matrix
        :rtype: tuple
        """""

        return self.matrix

    def get_list(self):
        """""
        Return the list associated with the matrix object.
        
        :return: The elements that make up the matrix object.
        :rtype: list:
        """""

        return self.to_list()

    def print(self):
        """"" 
        Prints the matrix in a pretty fashion.
        """""

        print_matrix(self.matrix)

    def to_list(self):
        """""
        This method is important for the immutability of the matrix.
        Since an operation typically requires a list, it needs to be 
        converted from a tuple before the operation can proceed.

        :return: A list that represents the matrix.
        :rtype: list
        """""

        to_list = []

        # Iterate over each element in the whole.
        for i in range(0, len(self.matrix)):

            # Convert the element to a list.
            to_list.append(list(self.matrix[i]))

        # Convert the outer tuple to a list.
        to_list = list(to_list)

        return to_list

    @staticmethod
    def to_tuple(listed):
        """""
        This method is important for the immutability of the matrix.
        Since an operation typically produces a list, it needs to be 
        converted to a tuple before it can be stored correctly.
        
        :param list listed: A list that represents the matrix.
        :return: A tuple that represents the matrix.
        :rtype: tuple
        """""

        to_tuple = []

        # Iterate over each element in the whole.
        for i in range(0, len(listed)):

            # Convert the element to a tuple.
            to_tuple.append(tuple(listed[i]))

        # Convert the outer list to a tuple.
        to_tuple = tuple(to_tuple)

        return to_tuple

    @staticmethod
    def generate(m, n, minimum, maximum, *ignore, integers=True, decimal_places=None):
        """""
        Generate a random matrix of a particular size.

        :param int m: The width of the matrix.
        :param int n: The height of the matrix.
        :param int minimum: The minimum value to appear in the matrix.
        :param int maximum: The maximum value to appear in the matrix.
        :param boolean integers: Determines whether the method returns a matrix with just integer values.
        :param int decimal_places: Determines the number of decimal places for each element.
        :return: Returns a matrix filled with random values,
        :rtype: Matrix
        """""

        # If the user has accidentally added more parameters than needed.
        if ignore:
            print("Unnecessary arguments submitted to generator method.")
            # Throw a type error.
            raise TypeError

        # If 'm' is and integer.
        if type(m) is int:

            # If 'n' is and integer.
            if type(n) is int:

                # If 'minimum' is and integer.
                if type(minimum) is int:

                    # If 'maximum' is and integer.
                    if type(maximum) is int:

                        # Produce a random matrix.
                        resultant = gen_matrix(m, n, minimum, maximum, integers, decimal_places)

                        # Produce a Matrix object from this result.
                        c = Matrix(Matrix.to_tuple(resultant), m=m, n=n)

                        return c

                    else:
                        print("ERROR: Argument 'maximum' is not of type 'int'.")
                        # Throw a TypeError
                        raise TypeError

                else:
                    print("ERROR: Argument 'minimum' is not of type 'int'.")
                    # Throw a TypeError
                    raise TypeError

            else:
                print("ERROR: Argument 'n' is not of type 'int'.")
                # Throw a TypeError
                raise TypeError

        else:
            print("ERROR: Argument 'm' is not of type 'int'.")
            # Throw a TypeError
            raise TypeError

    def ins_transpose(self):
        """""
        Finds the transpose of this instance. Replaces the value of the
        instance with its transpose.
        
        """""

        resultant = calc_trans(self.to_list())

        self.matrix = Matrix.to_tuple(resultant)

    @staticmethod
    def transpose(a):
        """""
        Finds the transpose of the matrix a.
        
        :return: The matrix that is the transpose of 'a'.
        :rtype: Matrix
        """""

        resultant = calc_trans(a.to_list())

        a.matrix = Matrix.to_tuple(resultant)

    def ins_add(self, b):
        """""
        Adds another matrix to the instance. Replacing the value of 
        this instance with the value of the sum.

        :param Matrix b: Is another instance of the Matrix class.
        """""

        # If 'b' is of the type Matrix
        if isinstance(b, Matrix):

            # Add the two matrices together.
            # Send list versions of the matrix tuples, since tuples are immutable.
            resultant = calc_add(self.to_list(), b.to_list())

            # If there was a problem with the addition.
            if type(resultant) is str:
                print(resultant)
                raise ValueError

            # Set the value of this instance to the sum.
            else:

                # Since resultant is a list, convert it back to a tuple.
                self.matrix = Matrix.to_tuple(resultant)

        else:
            print("ERROR: Argument 'b' is not of type 'Matrix'.")
            # Throw a TypeError
            raise TypeError

    @staticmethod
    def add(a, b):
        """""
        Adds two matrices together producing a new instance of the class.
        
        :param Matrix a: The first instance of the Matrix class.
        :param Matrix b: Is another instance of the Matrix class.
        :return: The addition of the two matrix objects.
        :rtype: Matrix
        """""

        # If 'a' is of the type Matrix
        if isinstance(a, Matrix):

            # If 'b' is of the type Matrix
            if isinstance(b, Matrix):

                # Add the two matrices together.
                # Send list versions of the matrix tuples, since tuples are immutable.
                resultant = calc_add(a.to_list(), b.to_list())

                # If there was a problem with the addition.
                if type(resultant) is str:
                    print(resultant)
                    raise ValueError

                # Set the value of this instance to the sum.
                else:

                    # Since resultant is a list, convert it back to a tuple.
                    c = Matrix(Matrix.to_tuple(resultant), m=a.m, n=a.n)

                    # Return the matrix 'c'.
                    return c

            else:
                print("ERROR: Argument 'b' is not of type 'Matrix'.")
                # Throw a TypeError
                raise TypeError

        else:
            print("ERROR: Argument 'a' is not of type 'Matrix'.")
            # Throw a TypeError
            raise TypeError

    def ins_subtract(self, b):
        """""
        Adds another matrix to the instance. Replacing the value of 
        this instance with the value of the negation.

        :param Matrix b: Is another instance of the Matrix class.
        """""

        # If 'b' is of the type Matrix
        if isinstance(b, Matrix):

            # Subtract the two matrices.
            # Send list versions of the matrix tuples, since tuples are immutable.
            resultant = calc_sub(self.to_list(), b.to_list())

            # If there was a problem with the subtraction.
            if type(resultant) is str:
                print(resultant)
                raise ValueError

            # Set the value of this instance to the subtraction.
            else:

                # Since resultant is a list, convert it back to a tuple.
                self.matrix = Matrix.to_tuple(resultant)

        else:
            print("ERROR: Argument 'b' is not of type 'Matrix'.")
            # Throw a TypeError
            raise TypeError

    @staticmethod
    def subtract(a, b):
        """""
        Subtracts two matrices together producing a new instance of the class.

        :param Matrix a: The first instance of the Matrix class.
        :param Matrix b: Is another instance of the Matrix class.
        :return: The subtraction of the two matrix objects.
        :rtype: Matrix
        """""

        # If 'a' is of the type Matrix
        if isinstance(a, Matrix):

            # If 'b' is of the type Matrix
            if isinstance(b, Matrix):

                # Subtract the two matrices.
                # Send list versions of the matrix tuples, since tuples are immutable.
                resultant = calc_sub(a.to_list(), b.to_list())

                # If there was a problem with the subtraction.
                if type(resultant) is str:
                    print(resultant)
                    raise ValueError

                # Set the value of this instance to the subtraction.
                else:

                    # Since resultant is a list, convert it back to a tuple.
                    c = Matrix(Matrix.to_tuple(resultant), m=a.m, n=a.n)

                    # Return the matrix 'c'.
                    return c

            else:
                print("ERROR: Argument 'b' is not of type 'Matrix'.")
                # Throw a TypeError
                raise TypeError

        else:
            print("ERROR: Argument 'a' is not of type 'Matrix'.")
            # Throw a TypeError
            raise TypeError

    def ins_multiply(self, b):
        """""
        Multiplies another matrix to the instance. Replacing the value of 
        this instance with the value of the product.

        :param Matrix b: Is another instance of the Matrix class.
        """""

        # If 'b' is of the type Matrix
        if isinstance(b, Matrix):

            # Multiply the two matrices.
            # Send list versions of the matrix tuples, since tuples are immutable.
            resultant = calc_mult(self.to_list(), b.to_list())

            # If there was a problem with the product.
            if type(resultant) is str:
                print(resultant)
                raise ValueError

            # Set the value of this instance to the product.
            else:

                # Since resultant is a list, convert it back to a tuple.
                self.matrix = Matrix.to_tuple(resultant)

        else:
            print("ERROR: Argument 'b' is not of type 'Matrix'.")
            # Throw a TypeError
            raise TypeError

    @staticmethod
    def multiply(a, b):
        """""
        Multiplies two matrices together producing a new instance of the class.

        :param Matrix a: The first instance of the Matrix class.
        :param Matrix b: Is another instance of the Matrix class.
        :return: The product of the two matrix objects.
        :rtype: Matrix
        """""

        # If 'a' is of the type Matrix
        if isinstance(a, Matrix):

            # If 'b' is of the type Matrix
            if isinstance(b, Matrix):

                # Multiply the two matrices together.
                # Send list versions of the matrix tuples, since tuples are immutable.
                resultant = calc_mult(a.to_list(), b.to_list())

                # If there was a problem with the product.
                if type(resultant) is str:
                    print(resultant)
                    raise ValueError

                # Set the value of this instance to the product.
                else:

                    # Since resultant is a list, convert it back to a tuple.
                    c = Matrix(Matrix.to_tuple(resultant), m=a.m, n=b.n)

                    # Return the matrix 'c'.
                    return c

            else:
                print("ERROR: Argument 'b' is not of type 'Matrix'.")
                # Throw a TypeError
                raise TypeError

        else:
            print("ERROR: Argument 'a' is not of type 'Matrix'.")
            # Throw a TypeError
            raise TypeError

    def determinant(self):
        """""
        Finds the determinant of the instance matrix.

        :return: The determinant of the instance.
        :rtype: float
        """""

        # Send a list version of the matrix tuple, since tuples are immutable.
        resultant = calc_det(self.to_list())

        # If there was a problem with the determinant.
        if type(resultant) is str:
            print(resultant)
            raise ValueError

        # Determinant found successfully.
        else:

            # Return the determinant of the instance.
            return resultant

    def ins_inverse(self):
        """""
        Finds the inverse of the instance matrix.
        """""

        # If the Matrix is not singular.
        # Send a list version of the matrix tuple.
        if Matrix.determinant(self) != 0:

            # Send a list version of the matrix tuple, since tuples are immutable.
            resultant = calc_inv(self.to_list())

            # If there was a problem with the inverse.
            if type(resultant) is str:
                print(resultant)
                raise ValueError

            # Set the instance matrix to the result.
            else:

                # Since resultant is a list, convert it back to a tuple.
                self.matrix = Matrix.to_tuple(resultant)

        # There will be no inverse if it is.
        else:
            print("INVERSE: Matrix has no inverse, determinant is 0")
            raise ZeroDivisionError

    @staticmethod
    def inverse(a):
        """""
        Finds the inverse of the instance matrix.

        :return: The inverse of the instance.
        :rtype: Matrix
        """""

        # If the Matrix is not singular.
        # Send a list version of the matrix tuple.
        if Matrix.determinant(a) != 0:

            # Send a list version of the matrix tuple, since tuples are immutable.
            resultant = calc_inv(a.to_list())

            # If there was a problem with the inverse.
            if type(resultant) is str:
                raise ValueError

            # Create a new Matrix object to be returned.
            else:

                # Since resultant is a list, convert it back to a tuple.
                c = Matrix(Matrix.to_tuple(resultant), m=a.m, n=a.n)

                # Return the inverse of 'a'.
                return c

        # There will be no inverse if it is.
        else:
            print("INVERSE: Matrix has no inverse, determinant is 0")
            raise ZeroDivisionError
