
__author__ = "Shay Brynes"
__license__ = "Apache License 2.0"

from decimal import Decimal


def calc_inv(a):
    """""
    Finds the inverse of the matrix 'a' using row operations
    to achieve the identity matrix after an augmentation. 
    
    :param list a: The matrix to invert.
    :return: The inverse of the matrix.
    :rtype: list
    """""

    # Only square matrices have an inverse.
    if len(a) == len(a[0]):

        # If the matrix is 2x2 then the inverse is easy to solve.
        if len(a) == 2:

            # Calculate the inverse.
            inverse = calc_two_inv(a)

            # Return the inverse.
            return inverse

        identity = []

        # Generate the Identity matrix for the size of the inputted matrix.
        # That has 'i' rows.
        for i in range(0, len(a)):

            row = []

            # And 'j' columns.
            for j in range(0, len(a[i])):

                # Identity matrix has 1 on the diagonal, and zero everywhere else.
                if i == j:
                    row.append(1)

                else:
                    row.append(0)

            # Append the row to the identity matrix.
            identity.append(row)

        # Augment the matrix to inverse with the identity matrix generated.
        inv = [a, identity]

        inverse = calc_n_inv(a, inv)

        # Return the inverse.
        return inverse

    else:
        # Return an error string.
        return "INVERSE: The Matrix is not square."


def calc_n_inv(a, inv):
    """""
    Finds the inverse of the matrix 'a' using row operations
    to achieve the identity matrix after an augmentation. 

    :param list a: The first Matrix in the multiplication.
    :param list inv: The augmented version of the matrix.
    :return: The inverse of the matrix.
    :rtype: list
    """""

    # Start in the first column.
    n = 0
    # Start in an imaginary row above the augmented matrix, since the iterator is added at the start of the iteration.
    m = -1

    # Iterate over every column of the Matrix.
    while n < len(a):

        # Go down to the next row.
        m = m + 1

        # If all rows of the left hand side have been iterated.
        if m == len(inv[0]):

            # Go to the next column
            n = n + 1

            # Go back to the first row
            m = 0

            # If we finished the final column then break the iteration.
            if n == len(a):
                break

        # Try to prevent a divide by zero error by adding the row below to this row.
        # Applies to both sides of the augmentation.
        if inv[0][n][n] == 0 or inv[1][n][n] == 0:

            # Iterate over the row.
            for i in range(0, len(a[0])):

                # Add the element below to the element in the row.
                # Applies to both sides of the augmentation.
                inv[0][n][i] = inv[0][n][i] + inv[0][n + 1][i]
                inv[1][n][i] = inv[1][n][i] + inv[1][n + 1][i]

        # If the element to be reduced needs to be 0, i.e does not lie on the diagonal.
        if n != m:

            # To reduce the element to zero all elements in the row need to be multiplied by a modifier.
            # This modifier is the inverse of the diagonal element, times the element to be zeroed.
            row_mod = Decimal(inv[0][m][n]) * Decimal(str(inv[0][n][n])) ** Decimal("-1")

            # Perform the row addition.
            for j in range(0, len(a[1])):

                # The subtraction of the column element times the modifier from the row to be given a leading zero
                # produces a leading zero. Applies to both sides of the augmentation.
                inv[0][m][j] = inv[0][m][j] - (inv[0][n][j] * row_mod)
                inv[1][m][j] = inv[1][m][j] - (inv[1][n][j] * row_mod)

        # If the element to be reduced needs to be 1, i.e does lie on the diagonal.
        elif n == m:

            # To reduce the element to one all elements in the row need to be multiplied by a modifier.
            # This modifier is the inverse of the diagonal element.
            row_mod = Decimal(str(inv[0][n][n])) ** Decimal("-1")

            # Perform the row addition.
            for i in range(0, len(a[0])):

                # Multiplying the whole row by the modification factor will keep leading zeroes as zeroes, and
                # reduce the diagonal part to 1. Applies to both sides of the augmentation.
                inv[0][m][i] = inv[0][m][i] * row_mod
                inv[1][m][i] = inv[1][m][i] * row_mod

    return inv[1]


# Calculates inverse of 2x2 matrices
def calc_two_inv(a):
    """""
    Returns the inverse of a 2x2 matrix.

    :param list a: The matrix of size 2x2 to invert.
    :return: The inverse of the matrix.
    :rtype: list
    """""

    # Set up the initial conditions.
    inv = [[], []]
    # Calculate the determinant.
    determinant = ((a[0][0]*a[1][1]) - (a[0][1]*a[1][0]))

    # Find the inverse of the matrix.
    inv[0].append(round(a[1][1]/determinant, 12))
    inv[0].append(round(-a[0][1]/determinant, 12))
    inv[1].append(round(-a[1][0]/determinant, 12))
    inv[1].append(round(a[0][0]/determinant, 12))

    # Return the inverse of the matrix.
    return inv


