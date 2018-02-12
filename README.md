
# MatrixPy
_*A simple handler for matrix objects in Python 3.*_

## Contents:

* [Installation](https://github.com/shaybrynes/MatrixPy#installation)
* [License](https://github.com/shaybrynes/MatrixPy#license)
* [Usage](https://github.com/shaybrynes/MatrixPy#usage)
    * [Printing the Matrices](https://github.com/shaybrynes/MatrixPy#printing-the-matrices)
    * [Generate a Matrix](https://github.com/shaybrynes/MatrixPy#generate-a-matrix)
    * [Adding, Subtracting and Multiplying Matrices](https://github.com/shaybrynes/MatrixPy#adding-subtracting-and-multiplying-matrices)
    * [Finding the Transpose of a Matrix](https://github.com/shaybrynes/MatrixPy#finding-the-transpose-of-a-matrix)
    * [Finding the Determinant of Matrices](https://github.com/shaybrynes/MatrixPy#finding-the-determinant-of-matrices)
    * [Finding the Inverse of Matrices](https://github.com/shaybrynes/MatrixPy#finding-the-inverse-of-matrices)
* [Support](https://github.com/shaybrynes/MatrixPy#support)
* [Future Additions](https://github.com/shaybrynes/MatrixPy#future-additions)

## License:

This project uses a license, the license is automatically included in the project files.

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Installation:

Just clone the MatrixPy repository and place the folder in your project directory. Then add the following to the top
of your code to to use the module.

```python
from MatrixPy.matrix import Matrix
```

You are now ready to start using matrix objects in your project.

## Usage:

To instantiate a matrix object in MatrixPy use the Matrix() method.
```python
identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1)) # The 3x3 identity matrix
a_matrix = Matrix(identity)
```
It is important to note that the matrix inputted *must* be of the type tuple, this important for immutability.
The above code specifically makes the value of the matrix object the below matrix,

![Identity](http://latex.codecogs.com/gif.latex?%5Cbegin%7Bpmatrix%7D%201%20%26%200%20%26%200%20%5C%5C%200%20%26%201%20%26%200%20%5C%5C%200%20%26%200%20%26%201%5C%5C%20%5Cend%7Bpmatrix%7D)

Say, instead you wanted a 3x5 matrix.
```python
three_by_five = ((2, 0, -3, 4, 5), (7, 2, -1, -4, 0), (-9, 4, 5, 3, 6))
a_matrix = Matrix(three_by_five, m=3, n=5) # m=int() and n=int() are non-essential parameters 
```
This would produce a matrix object equivalent to the matrix below,

![ThreeByFive](http://latex.codecogs.com/gif.latex?%5Cbegin%7Bpmatrix%7D%202%20%26%200%20%26%20-3%20%26%204%20%26%205%5C%5C%207%20%26%202%20%26%20-1%20%26%20-4%20%26%200%5C%5C%20-9%20%26%204%20%26%205%20%26%203%20%26%206%5C%5C%20%5Cend%7Bpmatrix%7D)

In fact when using this object the only limit to the size of the matrices available is the memory available to python.

Once the Matrix Object has been instantiated the data used to make the object can be retrieved. To retrieve the data use
any of the following commands;

```python
a_tuple = a_matrix.matrix # Returns the tuple that stores all the matrix elements.
a_tuple = a_matrix.get_tuple() # Also returns the tuple.
a_list = a_matrix.get_list() # Returns a list that contains the same information as the tuple.
```

### Printing the Matrices:

MatrixPy can handle the printing of your matrices to the screen, it can be achieved using this method.
```python
identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
identity.print()
```

### Generate a Matrix:

This module also allows the generation of matrices of any size. The method to call is:

```python
a_matrix = Matrix.generate(m, n, minimum, maximum, integers=True, decimal_places=None) 
# The last two arguments are non-essential.
```

This will generate a matrix of size _'m'_ x _'n'_ with elements that range in value from _'minimum'_ to _'maximum'_
these values must all be integers, however a future goal is to allow floating point values for the minimum
and maximum value. _'integers'_ and _'decimal\_places'_ are optional arguments that allow the generation of 
floating point values to fill the elements on th matrix. _'integers'_ set to false produces floating point
values and _'decimal\_places'_ sets the number of decimal places each of the elements should be rounded to.

### Adding, Subtracting and Multiplying Matrices:

MatrixPy handles the addition of two Matrices. It has two methods, each of which produces a different result.
```python
a_matrix = ((1, 1, 1), (1, 1, 1), (1, 1, 1))
identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))

b_matrix = Matrix.add(a_matrix, identity) # Adds the two matrices, puts answer in new Matrix object.
a_matrix.ins_add(identity) # Adds the two matrices, changes the value of a_matrix to the sum.

a_matrix.print()
b_matrix.print()
```
This section of code will output two matrices. Which in this case will have the same value.
Using the _ins\__ prefix tells MatrixPy that the modifier should be applied to the instance.

Subtraction of the matrices works in the same way, but the call to be made is as follows;
```python
b_matrix = Matrix.subtract(a_matrix, identity)
a_matrix.ins_subtract(identity)
```

Similarily for multiplying matrices;
```python
b_matrix = Matrix.multiply(a_matrix, identity)
a_matrix.ins_multiply(identity)
```
However, it should be noted that the normal rules for multiplying matrices applies. 
The rows in _'a'_ needs to match the number of columns in matrix _'b'_.

### Finding the Transpose of a Matrix:

MatrixPy also allows the user to calculate the transpose of a given Matrix. The transpose is a 
flipping of the matrix across its diagonal axis from the upper-left most corner. The transpose
is found as follows:

```python
b_matrix = Matrix.transpose(a_matrix) # or
a_matrix.ins_transpose()
``` 

Both of these methods produce the same result, but as before _ins\__ changes the value of the instance.

### Finding the Determinant of Matrices:

In MatrixPy determinants are found using the algorithm found [here](https://en.wikipedia.org/wiki/Gaussian_elimination#Computing_determinants),
on wikipedia. This method can be applied to an matrix of any size, hence the determinant of any _'m'_ x _'m'_ matrix can be found using MatrixPy.

The determinant in MatrixPy is calculated using the method below, it returns a float.
```python
a_matrix = ((2, 1, -1), (4, 1, 7), (8, -1, 3))
determinant = a_matrix.determinant()
print(determinant)
```

### Finding the Inverse of Matrices:

MatrixPy uses a similar algorithm to find the inverse of a matrix, it can be found [here](https://en.wikipedia.org/wiki/Gaussian_elimination#Finding_the_inverse_of_a_matrix),
again on wikipedia. As with the determinant this can be applied to a matrix of any size.

The determinant in MatrixPy is calculated using the method below,
```python
a_matrix = ((2, 1, -1), (4, 1, 7), (8, -1, 3))

b_matrix = Matrix.inverse(a_matrix) # Inverses the matrix, returns a new Matrix object.
a_matrix.ins_inverse() # Inverses the matrix, sets its value as its own inverse.

a_matrix.print()
b_matrix.print()
```

The two print statements will return the same value.

## Support:

The best way to show me that there is a problem with this project is to submit an issue report [here](https://github.com/shaybrynes/MatrixPy/issues). 
Make sure to give as much detail as possible, fully submitting all errors and how you achieved this error. 
If I can not replicate an issue I will assume that it is down to user error (which I will also provide support for).

If you are consistently having issues setting up and using the project, do not hesitate to send me a private message.

## Future Additions:

- [x] Ability to calculate the inverse and determinant.
- [x] Calculation of transpose.
- [ ] Installation via PIP.
- [ ] (Much later) eigenvalues. 
