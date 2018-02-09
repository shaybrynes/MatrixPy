
__author__ = "Shay Brynes"
__license__ = "Apache License 2.0"


def calc_det(to_det):
    """""
    Finds the determinant of the matrix 'a' using row operations
    to achieve triangulation. The determinant is the product of 
    the diagonal elements.
    
    :param float to_det: The first Matrix whose determinant will be found
    :return: The determinant of the matrix
    :rtype: float
    """""

    # Only square matrices have a determinant.
    if len(to_det) == len(to_det[0]):

        # Start from the first column.
        n = 0
        # Start in the first row.
        m = 0

        # Iterate over every column of the Matrix.
        while n < len(to_det):

            # Go down to the next row.
            m = m + 1

            # If all the elements in the column have been zeroed, move to the next column.
            if m == len(to_det):

                # Go to the next column.
                n = n + 1
                # Starting row is on the diagonal.
                m = n
                # Skip to the next iteration.
                continue

            # Try to prevent a divide by zero error by adding the row below to this row.
            if to_det[n][n] == 0:

                # Iterate over the row.
                for i in range(0, len(to_det[0])):

                    # Add the element below to the element in the row.
                    to_det[n][i] = to_det[n][i] + to_det[n + 1][i]

            # Skip if the term to be zeroed is already zero.
            if to_det[m][n] == 0:
                continue

            # To reduce the element to zero all elements in the row need to be multiplied by a modifier.
            # This modifier is the inverse of the diagonal element, times the element to be zeroed.
            row_mod = round(to_det[m][n] * (to_det[n][n] ** (-1)), 14)

            # Perform the row addition.
            for j in range(0, len(to_det[1])):

                # The subtraction of the column element times the modifier from the row to be given a leading zero
                # produces a leading zero.
                to_det[m][j] = round(to_det[m][j] - (to_det[n][j] * row_mod), 14)

        # Once the determinant has been transformed to an upper triangular matrix
        # the determinant can be found as the product of the major diagonal.
        determinant = 1

        # Iterate over all the diagonals.
        for i in range(0, len(to_det)):

            # Calculate the determinant.
            determinant *= to_det[i][i]

        # Return the determinant.
        return determinant

    else:
        # Return an error string.
        return "DETERMINANT: The Matrix is not square."
