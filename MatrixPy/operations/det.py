
__author__ = "Shay Brynes"
__license__ = "Apache License 2.0"


def calc_det(a):
    """""
    Finds the determinant of the matrix 'a' using row operations
    to achieve triangulation. The determinant is the product of 
    the diagonal elements.
    :param a: The first Matrix in the multiplication
    :return: The result of the multiplication of the two matrices 
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

                # Next column.
                n = n + 1
                # Starting row is on the diagonal.
                m = n
                # Skip to the next iteration.
                continue

            # Try to prevent a divide by zero error by adding the row below to this row.
            if a[n][n] == 0:

                # Iterate over the row
                for i in range(0, len(a[0])):

                    # Add the element below to the element in the row.
                    a[n][i] = a[n][i] + a[n + 1][i]

            # Skip if the term to be zeroed is already zero.
            if a[m][n] == 0:
                continue

            # To reduce the element to zero all elements in the row need to be multiplied by a modifier.
            # This modifier is the inverse of the diagonal element, times the element to be zeroed.
            rowMod = round(a[m][n] * (a[n][n]**(-1)), 14)

            # Perform the row addition.
            for j in range(0, len(a[1])):

                # The subtraction of the column element times the modifier from the row tobe given a leading zero
                # produces a leading zero.
                a[m][j] = round(a[m][j] - (a[n][j] * rowMod), 14)

        # Once the determinant has been transformed to an upper triangular matrix
        # the determinant can be found as the product of the major diagonal.
        determinant = 1

        # Iterate over all the diagonals.
        for i in range(0, len(a)):

            # Calculate the determinant.
            determinant *= a[i][i]

        # Reutrn the determinant.
        return determinant

    else:
        # Return an error string.
        return "DETERMINANT: The Matrix is not square."
