
__author__ = "Shay Brynes"
__license__ = "Apache License 2.0"


def print_matrix(matrix):

    for n in range(0, len(matrix)):

        for m in range(0, len(matrix[n])):

            if m == 0:
                print("(", end="")

            print(matrix[n][m], end="")

            if m == len(matrix[n])-1:
                print(")")
            else:
                print(", ", end="")
