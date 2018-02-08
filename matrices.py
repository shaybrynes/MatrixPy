
__author__ = "Shay Brynes"
__license__ = "Apache License 2.0"

from src.print_matrix import *
from src.operations.add import *
from src.operations.sub import *
from src.operations.mult import *


class Matrix:

    def __init__(self, matrix_input, *ignore, m=None, n=None):
        """""
        Creates an instance of the matrix class.
        
        :param matrix_input: The first Matrix in the addition.
        :param m: The number of rows in the Matrix.
        :param n: The number of columns in the Matrix.
        :return: No return value, constructs the instance.
        """""

        # If the user has accidentally added more parameters than needed.
        if ignore:
            print("Unnecessary arguments submitted to class constructor.")
            # Throw a type error.
            raise TypeError

        self.matrix = matrix_input

        if m is None:

            # 'm' is the number of rows.
            self.m = len(matrix_input)

        else:
            self.m = m

        if n is None:

            # 'n' is the number of columns
            self.n = len(matrix_input[0])

        else:
            self.n = n

    def print(self):
        """"" 
        Prints the matrix in a pretty fashion.
        """""

        print_matrix(self.matrix)

    @staticmethod
    def print_stc(matrix):
        """"" 
        Prints the matrix in a pretty fashion.
        """""

        print_matrix(matrix)

    def add(self, b):
        """""
        Adds another matrix to the instance. Replacing the value of 
        this instance with the value of the sum.

        :param b: Is another instance of the Matrix class.
        """""

        # If 'b' is of the type Matrix
        if isinstance(b, Matrix):

            # Add the two matrices together.
            resultant = add(self.matrix, b.matrix)

            # If there was a problem with the addition.
            if type(resultant) is str:
                print(resultant)

            # Set the value of this instance to the sum.
            else:
                self.matrix = resultant

        else:
            print("ERROR: Argument 'b' is not of type 'Matrix'.")
            # Throw a TypeError
            raise TypeError

    @staticmethod
    def add_stc(a, b):
        """""
        Adds two matrices together producing a new instance of the class.
        
        :param a: The first instance of the Matrix class.
        :param b: Is another instance of the Matrix class.
        :return: The addition of the two matrix objects.
        :rtype: Matrix
        """""

        # If 'a' is of the type Matrix
        if isinstance(a, Matrix):

            # If 'b' is of the type Matrix
            if isinstance(b, Matrix):

                # Add the two matrices together.
                resultant = add(a.matrix, b.matrix)

                # If there was a problem with the addition.
                if type(resultant) is str:
                    print(resultant)

                # Set the value of this instance to the sum.
                else:
                    c = Matrix(resultant, m=a.m, n=a.n)

            else:
                print("ERROR: Argument 'b' is not of type 'Matrix'.")
                # Throw a TypeError
                raise TypeError

        else:
            print("ERROR: Argument 'a' is not of type 'Matrix'.")
            # Throw a TypeError
            raise TypeError

        return c

    def subtract(self, b):
        """""
        Adds another matrix to the instance. Replacing the value of 
        this instance with the value of the negation.

        :param b: Is another instance of the Matrix class.
        """""

        # If 'b' is of the type Matrix
        if isinstance(b, Matrix):

            # Subtract the two matrices.
            resultant = sub(self.matrix, b.matrix)

            # If there was a problem with the addition.
            if type(resultant) is str:
                print(resultant)

            # Set the value of this instance to the sum.
            else:
                self.matrix = resultant

        else:
            print("ERROR: Argument 'b' is not of type 'Matrix'.")
            # Throw a TypeError
            raise TypeError

    @staticmethod
    def subtract_stc(a, b):
        """""
        Subtracts two matrices together producing a new instance of the class.

        :param a: The first instance of the Matrix class.
        :param b: Is another instance of the Matrix class.
        :return: The subtraction of the two matrix objects.
        :rtype: Matrix
        """""

        # If 'a' is of the type Matrix
        if isinstance(a, Matrix):

            # If 'b' is of the type Matrix
            if isinstance(b, Matrix):

                # Add the two matrices together.
                resultant = sub(a.matrix, b.matrix)

                # If there was a problem with the addition.
                if type(resultant) is str:
                    print(resultant)

                # Set the value of this instance to the sum.
                else:
                    c = Matrix(resultant, m=a.m, n=a.n)

            else:
                print("ERROR: Argument 'b' is not of type 'Matrix'.")
                # Throw a TypeError
                raise TypeError

        else:
            print("ERROR: Argument 'a' is not of type 'Matrix'.")
            # Throw a TypeError
            raise TypeError

        return c

    def multiply(self, b):
        """""
        Multiplies another matrix to the instance. Replacing the value of 
        this instance with the value of the product.

        :param b: Is another instance of the Matrix class.
        """""

        # If 'b' is of the type Matrix
        if isinstance(b, Matrix):

            # Subtract the two matrices.
            resultant = mult(self.matrix, b.matrix)

            # If there was a problem with the addition.
            if type(resultant) is str:
                print(resultant)

            # Set the value of this instance to the sum.
            else:
                self.matrix = resultant

        else:
            print("ERROR: Argument 'b' is not of type 'Matrix'.")
            # Throw a TypeError
            raise TypeError

    @staticmethod
    def multiply_stc(a, b):
        """""
        Multiplies two matrices together producing a new instance of the class.

        :param a: The first instance of the Matrix class.
        :param b: Is another instance of the Matrix class.
        :return: The product of the two matrix objects.
        :rtype: Matrix
        """""

        # If 'a' is of the type Matrix
        if isinstance(a, Matrix):

            # If 'b' is of the type Matrix
            if isinstance(b, Matrix):

                # Add the two matrices together.
                resultant = mult(a.matrix, b.matrix)

                # If there was a problem with the addition.
                if type(resultant) is str:
                    print(resultant)

                # Set the value of this instance to the sum.
                else:
                    c = Matrix(resultant, m=a.m, n=a.n)

            else:
                print("ERROR: Argument 'b' is not of type 'Matrix'.")
                # Throw a TypeError
                raise TypeError

        else:
            print("ERROR: Argument 'a' is not of type 'Matrix'.")
            # Throw a TypeError
            raise TypeError

        return c


