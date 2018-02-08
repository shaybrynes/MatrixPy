
__author__ = "Shay Brynes"
__license__ = "Apache License 2.0"

from MatrixPy.print_matrix import *
from MatrixPy.operations.add import *
from MatrixPy.operations.sub import *
from MatrixPy.operations.mult import *
from MatrixPy.operations.det import *


class Matrix:

    def __init__(self, matrix_input, *ignore, m=None, n=None, det=False, inv=False):
        """""
        Creates an instance of the matrix class.
        
        :param list matrix_input: The first Matrix in the addition.
        :param int m: The number of rows in the Matrix.
        :param int n: The number of columns in the Matrix.
        :param boolean determinant: If true the determinant will be pre-calculated, callable as obj.determinant
        :param boolean inverse: If true the inverse will be pre-calculated, callable as obj.inverse
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

        # If the user does not want the determinant pre-calculated.
        if det is False:

            # Set the determinant to None.
            self.det = None

        else:
            self.det = self.ins_determinant()

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

    def ins_add(self, b):
        """""
        Adds another matrix to the instance. Replacing the value of 
        this instance with the value of the sum.

        :param b: Is another instance of the Matrix class.
        """""

        # If 'b' is of the type Matrix
        if isinstance(b, Matrix):

            # Add the two matrices together.
            resultant = calc_add(self.matrix, b.matrix)

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
    def add(a, b):
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
                resultant = calc_add(a.matrix, b.matrix)

                # If there was a problem with the addition.
                if type(resultant) is str:
                    print(resultant)

                # Set the value of this instance to the sum.
                else:
                    c = Matrix(resultant, m=a.m, n=a.n)

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

        :param b: Is another instance of the Matrix class.
        """""

        # If 'b' is of the type Matrix
        if isinstance(b, Matrix):

            # Subtract the two matrices.
            resultant = calc_sub(self.matrix, b.matrix)

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
    def subtract(a, b):
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

                # Subtract the two matrices together.
                resultant = calc_sub(a.matrix, b.matrix)

                # If there was a problem with the addition.
                if type(resultant) is str:
                    print(resultant)

                # Set the value of this instance to the sum.
                else:
                    c = Matrix(resultant, m=a.m, n=a.n)

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

        :param b: Is another instance of the Matrix class.
        """""

        # If 'b' is of the type Matrix
        if isinstance(b, Matrix):

            # Multiply the two matrices.
            resultant = calc_mult(self.matrix, b.matrix)

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
    def multiply(a, b):
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

                # Multiply the two matrices together.
                resultant = calc_mult(a.matrix, b.matrix)

                # If there was a problem with the addition.
                if type(resultant) is str:
                    print(resultant)

                # Set the value of this instance to the sum.
                else:
                    c = Matrix(resultant, m=a.m, n=b.n)

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

    def ins_determinant(self):
        """""
        Finds the determinant of the instance matrix.

        :return: The determinant of the instance.
        :rtype: Float
        """""

        resultant = calc_det(self.matrix)

        # If there was a problem with the determinant.
        if type(resultant) is str:
            print(resultant)

        # Set the value of this instance to the sum.
        else:
            self.det = resultant

        # Return the determinant of the instance.
        return resultant

    @staticmethod
    def determinant(a):
        """""
                Finds the determinant of the instance matrix.

                :return: The determinant of the instance.
                :rtype: Float
                """""

        resultant = calc_det(a)

        # If there was a problem with the determinant.
        if type(resultant) is str:
            print(resultant)

        # Set the value of this instance to the sum.
        else:
            a.det = resultant

        # Return the determinant of 'a'.
        return resultant

