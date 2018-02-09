
__author__ = "Shay Brynes"
__license__ = "Apache License 2.0"


def calc_trans(a):
    """""
    Find the transpose of the matrix by creating a new.
    
    :param list a: The first Matrix whose determinant will be found.
    :return: The transpose of the matrix.
    :rtype: list
    """""

    # Find the height and width of the matrix to transpose.
    m = len(a)
    n = len(a[0])

    solution = []

    # Iterate over all the columns of the matrix.
    for i in range(0, n):

        row = []

        # Iterate over all the rows.
        for j in range(0, m):

            # Transpose the column (i.e set the row of the solution to the column of the input).
            row.append(a[j][i])

        # Append the row to the solution.
        solution.append(row)

    # Return the solution.
    return solution
