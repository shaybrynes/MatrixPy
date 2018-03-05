
__author__ = "Shay Brynes"
__license__ = "Apache License 2.0"


def calc_mult(a, b):
    """""
    Multiplies two matrices together.
    :param list a: The first matrix in the multiplication.
    :param list b: The second matrix in the multiplication.
    :return: The result of the multiplication of the two matrices.
    :rtype: list
    """""

    # For matrix multiplication columns in 'a' must match number of rows in 'b'.
    if len(a[0]) == len(b):

        solution = []

        # Iterate over the rows of the matrix.
        for m in range(0, len(a)):

            row = []

            # Iterate over the columns of the second matrix.
            for n_b in range(0, len(b[0])):

                term = 0

                # Iterate over the columns of the first matrix.
                for n_a in range(0, len(a[0])):

                    # An element of the resultant matrix is the sum of the product of
                    # corresponding elements in the selected rows and columns.
                    term = term + (a[m][n_a] * b[n_a][n_b])

                # Once the term is found, add it to the list of elements.
                row.append(term)

            # Append the row to the solution.
            solution.append(row)

        # Return the resultant matrix.
        return solution

    else:
        # Return an error string.
        return "MULTIPLY: Number of rows in 'b' does not match the number of columns in 'a'."
