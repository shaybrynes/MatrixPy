
__author__ = "Shay Brynes"
__license__ = "Apache License 2.0"


def calc_add(a, b):
    """""
    Adds two matrices together.
    :param a: The first Matrix in the addition
    :param b: The second Matrix in the addition
    :return: The result of the addition of the two matrices 
    """""

    # If the number of rows in each of the Matrices is the same.
    if len(a) == len(b):

        # If the number of columns is the same in each of the Matrices
        if len(a[0]) == len(b[0]):

            solution = []

            # Iterate over each of the rows
            for m in range(0, len(a)):
                row = []

                # Iterate over each or the columns in each row.
                for n in range(0, len(a[0])):

                    # Add terms in the same position together.
                    term = a[m][n] + b[m][n]
                    # Append this term to the row.
                    row.append(term)

                # Append the row to the solution.
                solution.append(row)

            # Return the resultant matrix.
            return solution

        else:
            # Return an error string.
            return "ADD: Number of columns does not match."

    else:
        # Return an error string.
        return "ADD: Number of rows does not match."
