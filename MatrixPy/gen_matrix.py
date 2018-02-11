
_author_ = "Shay Brynes"
__license__ = "Apache License 2.0"

from random import randint, random


def gen_matrix(m, n, min , max, integers, decimal_places):
    """""
    A module for generating random integer element matrices.

    :param int m: The number of rows.
    :param int n: The number of columns.
    :param int min: The minimum number that will appear in the matrix.
    :param int max: The maximum number that will appear in the matrix.
    :param boolean integers: Whether or not all the elements in the matrix are integers.
    :param int decimal_places: The number of decimal places if floating points make up the elements.
    :return: A random matrix of size m x n
    :rtype: list
    """""

    solution = []

    for i in range(0, m):

        row = []

        for j in range(0, n):

            # Generate a random element
            if integers is True:

                # If the element should be an integer.
                element = randint(min - 1, max)

            else:
                # If it should be a float.
                element = randint(min - 1, max) * random()

                # If wanted, the element should be rounded.
                if decimal_places is not None:
                    element = round(element, decimal_places)

            # Append the element to the row.
            row.append(element)

        # Append the row to the solution.
        solution.append(row)

    # Return the solution to the user.
    return solution