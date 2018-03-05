
__author__ = "Shay Brynes"
__license__ = "Apache License 2.0"

from decimal import Decimal


def calc_det(a):
    """""
    Finds the determinant of the matrix 'a' using row operations
    to achieve triangulation. The determinant is the product of 
    the diagonal elements.
    
    :param float a: The first Matrix whose determinant will be found
    :return: The determinant of the matrix
    :rtype: float
    """""

    # Only square matrices have a determinant.
    if len(a) == len(a[0]):

        # Start from the first column.
        n = 0
        # Start in the first row.
        m = 0

        # Iterate over every column of the Matrix.
        while n < len(a):

            # Go down to the next row.
            m = m + 1

            # If all the elements in the column have been zeroed, move to the next column.
            if m == len(a):

                # Go to the next column.
                n = n + 1
                # Starting row is on the diagonal.
                m = n
                # Skip to the next iteration.
                continue

            # Try to prevent a divide by zero error by adding the row below to this row.
            if a[n][n] == 0:

                # Iterate over the row.
                for i in range(0, len(a[0])):

                    # Add the element below to the element in the row.
                    a[n][i] = a[n][i] + a[n + 1][i]

            # Skip if the term to be zeroed is already zero.
            if a[m][n] == 0:
                continue

            # To reduce the element to zero all elements in the row need to be multiplied by a modifier.
            # This modifier is the inverse of the diagonal element, times the element to be zeroed.
            row_mod = Decimal(a[m][n]) * (Decimal(a[n][n]) ** Decimal("-1"))

            # Perform the row addition.
            for j in range(0, len(a[1])):

                # The subtraction of the column element times the modifier from the row to be given a leading zero
                # produces a leading zero.
                a[m][j] = a[m][j] - (a[n][j] * row_mod)

        # Once the determinant has been transformed to an upper triangular matrix
        # the determinant can be found as the product of the major diagonal.
        determinant = 1

        # Iterate over all the diagonals.
        for i in range(0, len(a)):

            # Calculate the determinant.
            determinant *= a[i][i]

        # Return the determinant.
        return determinant

    else:
        # Return an error string.
        return "DETERMINANT: The Matrix is not square."
