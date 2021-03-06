
__author__ = "Shay Brynes"
__license__ = "Apache License 2.0"

from decimal import *

from MatrixPy.print_matrix import *
from MatrixPy.gen_matrix import *
from MatrixPy.operations.add import *
from MatrixPy.operations.sub import *
from MatrixPy.operations.mult import *
from MatrixPy.operations.det import *
from MatrixPy.operations.inv import *
from MatrixPy.operations.transpose import *
from MatrixPy.operations.eqs_system import *


class Matrix:

    def __init__(self, matrix_input):
        """""
        Creates an instance of the matrix class.
        
        :param tuple matrix_input: The first Matrix in the addition.
        """""
        # If the matrix is rectangular create an instance.
        if Matrix.__verify_matrix__(matrix_input):

            # Force use of tuple type, immutability issues otherwise.
            if type(matrix_input) is tuple:
                self.matrix = matrix_input

            # Let the user off for inputting a list.
            elif type(matrix_input) is list:
                self.matrix = Matrix.to_tuple(matrix_input)

            else:
                print("Tuple needed for class constructor.")
                # Throw a type error.
                raise TypeError

            self.__decimalify__()

        # Inform the user of their mistake.
        else:
            print("The class constructor requires a rectangular matrix.")
            # Throw a type error.
            raise TypeError

    def __decimalify__(self):
        """""
        Sets all elements of the matrix to decimal elements,
        this improves floating point accuracy
        """""

        solution = []
        matrix_list = self.to_list()

        # Iterate over the whole height of the matrix.
        for i in range(0, len(matrix_list)):

            row = []
            # Iterate over the whole height of the list.
            for j in range(0, len(matrix_list[0])):
                # Set the element to a decimal object.
                row.append(Decimal(str(matrix_list[i][j])))

            solution.append(row)

        # Change the matrix object's value to the decimal element.
        self.matrix = Matrix.to_tuple(solution)

    @staticmethod
    def __verify_square__(a):
        """""
        Determines if the matrix is square.
        """""

        matrix_tuple = Matrix.to_tuple(a)

        # Find the number of rows in the matrix.
        num_rows = len(matrix_tuple)

        # Iterate over the rows.
        for row in matrix_tuple:

            # If the row has more elements than the number of rows, then we aren't square.
            if len(row) != num_rows:

                return False

        return True

    @staticmethod
    def __verify_matrix__(matrix_input):
        """""
        Determines if the matrix is rectangular, this is important for many
        of the operations in this module. 
        """""

        # Length of the first row.
        first_len = len(matrix_input[0])

        # Iterate over all the rows.
        for i in range(0, len(matrix_input)):

            # If the length of a row is not the same as the first then the matrix is not rectangular.
            if len(matrix_input[i]) != first_len:

                return False

        return True

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

    def round(self, decimals, *ignore, normalize=False):
        """""
        This method rounds every element in the matrix to the desired
        number of decimal places.

        :param int decimals: A the number of decimal places to round too.
        :param boolean normalize: Whether or not trailing zeroes should be removed.
        """""

        # If the user has accidentally added more parameters than needed.
        if ignore:
            print("Unnecessary arguments submitted to generator method.")
            # Throw a type error.
            raise TypeError

        else:

            solutions = []
            matrix_list = self.to_list()

            # Iterate over the whole height of the matrix.
            for i in range(0, len(matrix_list)):

                row = []
                # Iterate over the whole width of the list.
                for j in range(0, len(matrix_list[0])):
                    # Round the value to the specified number of decimal places.
                    element = matrix_list[i][j].quantize(Decimal("10")**(Decimal("-1")*Decimal(str(decimals))))

                    # Should trailing zeroes be removed?
                    if normalize:
                        element = element.normalize()

                    row.append(element)

                solutions.append(row)

            # Change the matrix object's value to the rounded element.
            self.matrix = Matrix.to_tuple(solutions)

    @staticmethod
    def generate_random(m, n, minimum, maximum, *ignore, integers=True, decimal_places=None):
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

        else:

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
                            c = Matrix(Matrix.to_tuple(resultant))

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

    @staticmethod
    def generate_identity(m):
        """""
        Generate an identity matrix of size m.
        
        :param int m: The size of the identity matrix.
        :return: Returns an identity matrix of size m.
        :rtype: Matrix
        """""

        # Create a list to represent the identity.
        matrix_list = [[Decimal(0) for i in range(m)] for j in range(m)]

        # Change the diagonal elements to 1.
        for i in range(m):
            matrix_list[i][i] = Decimal(1)

        # Create a matrix object.
        c = Matrix(matrix_list)

        return c

    @staticmethod
    def transpose(a):
        """""
        Finds the transpose of the matrix a.
        
        :return: The matrix that is the transpose of 'a'.
        :rtype: Matrix
        """""

        resultant = calc_trans(a.to_list())
        a.matrix = Matrix.to_tuple(resultant)

        return a

    def __add__(self, other):
        """""
        Adds two matrices using Python's built in addition capabilities.
        c = a + b 
        
        :return: The addition of the two matrix objects.
        :rtype: Matrix
        """""

        # Use the add() function.
        c = self.add(self, other)

        return c

    def __sub__(self, other):
        """""
        Subtract two matrices using Python's built in subtraction capabilities.
        c = a - b 

        :return: The subtraction of the two matrix objects.
        :rtype: Matrix
        """""

        # Use the subtract() function.
        c = self.subtract(self, other)

        return c

    def __mul__(self, other):
        """""
        Multiplies two matrices using Python's built in multiplication capabilities.
        c = a * b 

        :return: The multiplication of the two matrix objects.
        :rtype: Matrix
        """""

        # Use the multiply() function.
        c = self.multiply(self, other)

        return c

    def __abs__(self):
        """""
        Finds the determinant of the matrix.
        c = |a|
        
        :return: The determinant of the matrix.
        :rtype: decimal
        """""

        # Use the determinant function.
        return Matrix.determinant(self)

    def __pow__(self, power, modulo=None):
        """""
        Calculates the power of the matrix.
        c = a ** power
        
        :param int power: An integer to raise the matrix too.
        :return: Matrix which is the power of the original matrix.
        :rtype: Matrix
        """""

        # Use the power() function
        return Matrix.power(self, power)

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
                    c = Matrix(Matrix.to_tuple(resultant))

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
                    c = Matrix(Matrix.to_tuple(resultant))

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
                    c = Matrix(Matrix.to_tuple(resultant))

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

    @staticmethod
    def power(a, power):
        """""
        Calculates a to the power of power.
        
        :param Matrix a: The matrix that is being raised to the power.
        :param int power: The exponent to raise the matrix by.
        :return: The matrix raised to the power.
        :rtype: Matrix
        """""
        if type(power) is int:

            # If the power is negative find the inverse first.
            if power < 0:

                a = Matrix.inverse(a)

            if power != 0:

                # Find the power using iteration.
                for i in range(0, abs(power)-1):

                    a *= a

                return a

            else:
                # If the exponent is zero then the result is the identity matrix.
                return Matrix.generate_identity(len(Matrix.to_list(a)))

        elif type(power) is str:

            # Check to see if the user is looking for the transpose.
            if power == "T" or power == "t":

                return Matrix.transpose(a)

        else:
            print("ERROR: argument power is not of type 'Int'")
            raise TypeError

    @staticmethod
    def determinant(a):
        """""
        Finds the determinant of the parameter matrix.

        :param Matrix a: The matrix whose determinant is to be found.
        :return: The determinant of the parameter.
        :rtype: float
        """""

        # Send a list version of the matrix tuple, since tuples are immutable.
        resultant = calc_det(a.to_list())

        # If there was a problem with the determinant.
        if type(resultant) is str:
            print(resultant)
            raise ValueError

        # Determinant found successfully.
        else:

            # Return the determinant of the instance.
            return Decimal(resultant)

    @staticmethod
    def inverse(a):
        """""
        Finds the inverse of the instance matrix.

        :param Matrix a: The matrix to be inverted.
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
                c = Matrix(Matrix.to_tuple(resultant))

                # Return the inverse of 'a'.
                return c

        # There will be no inverse if it is.
        else:
            print("INVERSE: Matrix has no inverse, determinant is 0")
            raise ZeroDivisionError

    @staticmethod
    def solve_system(a, b):
        """""
        Finds the solutions to a system of simultaneous equations.
        
        :param Matrix a: The matrix of the co-efficients equations to be solved.
        :param Matrix b: The matrix of the solutions to the equations.
        :return: The solutions of the system of equations.
        :rtype: Matrix
        """""

        # Send a list version of the matrix tuple, since tuples are immutable.
        resultant = calc_solutions(a.to_list(), b.to_list())

        # If there was a problem with the inverse.
        if type(resultant) is str:
            raise ValueError

        # Create a new Matrix object to be returned.
        else:

            # Since resultant is a list, convert it back to a tuple.
            c = Matrix(Matrix.to_tuple(resultant))
            # Return the solutions of the system.
            return c
