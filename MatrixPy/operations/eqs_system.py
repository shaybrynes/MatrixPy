
__author__ = "Shay Brynes"
__license__ = "Apache License 2.0"


from decimal import Decimal


def calc_solutions(a, b):
    """""
    Finds the solutions of the system of equations defined as 'a' = 'b'.
    Where 'a' is the Matrix of coefficients of the variables and 
    'b' is matrix of the solutions to these equations.
    
    :param list a: The matrix of the coefficients of the equations to solve.
    :param list b: The specific solutions to those equations.
    :return c: A list of the solutions for each of the variables.
    :rtype: list
    """""

    # Augment the matrix to include the co-efficients and the solutions.
    augmented = [a, b]

    # Start in the first column.
    n = 0
    # Start in an imaginary row above the augmented matrix, since the iterator is added at the start of the iteration.
    m = -1

    # Iterate over every column of the Matrix.
    while n < len(a):

        # Go down to the next row.
        m = m + 1

        # If all rows of the left hand side have been iterated.
        if m == len(augmented[0]):

            # Go to the next column
            n = n + 1

            # Go back to the first row
            m = 0

            # If we finished the final column then break the iteration.
            if n == len(a):
                break

        # Try to prevent a divide by zero error by adding the row below to this row.
        # Applies to both sides of the augmentation.
        if augmented[0][n][n] == 0 or augmented[1][n][0] == 0:

            # Iterate over the row.
            for i in range(0, len(a[0])):

                # Add the element below to the element in the row.
                # Applies to both sides of the augmentation.
                augmented[0][n][i] = augmented[0][n][i] + augmented[0][n + 1][i]
                augmented[1][n][0] = augmented[1][n][0] + augmented[1][n + 1][0]

        # If the element to be reduced needs to be 0, i.e does not lie on the diagonal.
        if n != m:

            # To reduce the element to zero all elements in the row need to be multiplied by a modifier.
            # This modifier is the inverse of the diagonal element, times the element to be zeroed.
            row_mod = Decimal(str(augmented[0][m][n])) * Decimal(str((augmented[0][n][n])))**Decimal("-1")

            # Perform the row addition.
            for j in range(0, len(a[1])):

                # The subtraction of the column element times the modifier from the row to be given a leading zero
                # produces a leading zero.
                augmented[0][m][j] = augmented[0][m][j] - (augmented[0][n][j] * row_mod)

            # Should only be applied once to the right hand side.
            augmented[1][m][0] = augmented[1][m][0] - (augmented[1][n][0] * row_mod)

        # If the element to be reduced needs to be 1, i.e does lie on the diagonal.
        elif n == m:

            # To reduce the element to one all elements in the row need to be multiplied by a modifier.
            # This modifier is the inverse of the diagonal element.
            row_mod = Decimal(str(augmented[0][n][n]))**Decimal("-1")

            # Perform the row addition.
            for i in range(0, len(a[0])):

                # Multiplying the whole row by the modification factor will keep leading zeroes as zeroes, and
                # reduce the diagonal part to 1.
                augmented[0][m][i] = augmented[0][m][i] * row_mod

            # Should only be applied once to the right hand side.
            augmented[1][m][0] = augmented[1][m][0] * row_mod

    solutions = [[]]

    # Iterate over the whole augmentation.
    for i in range(0, len(augmented[1])):

        # Append the solutions to a list
        solutions[0].append(augmented[1][i][0])

    # Returns the solutions of the system of equations.
    return solutions
