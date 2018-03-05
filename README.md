
# MatrixPy
_*A simple handler for matrix objects in Python 3.*_

## Contents:

* [Installation](https://github.com/shaybrynes/MatrixPy#installation)
* [License](https://github.com/shaybrynes/MatrixPy#license)
* [Usage](https://github.com/shaybrynes/MatrixPy#usage)
    * [Printing the Matrices](https://github.com/shaybrynes/MatrixPy#printing-the-matrices)
    * [Generate a Matrix](https://github.com/shaybrynes/MatrixPy#generate-a-matrix)
    * [Round elements of a Matrix](https://github.com/shaybrynes/MatrixPy#round-elements-of-a-matrix)
    * [Adding, Subtracting and Multiplying Matrices](https://github.com/shaybrynes/MatrixPy#adding-subtracting-and-multiplying-matrices)
    * [Finding the Transpose of a Matrix](https://github.com/shaybrynes/MatrixPy#finding-the-transpose-of-a-matrix)
    * [Finding the Determinant of Matrices](https://github.com/shaybrynes/MatrixPy#finding-the-determinant-of-matrices)
    * [Finding the Inverse of Matrices](https://github.com/shaybrynes/MatrixPy#finding-the-inverse-of-matrices)
    * [Finding the solutions of a system of equations](https://github.com/shaybrynes/MatrixPy#finding-the-solutions-of-a-system-of-equations)
* [Support](https://github.com/shaybrynes/MatrixPy#support)
* [Future Additions](https://github.com/shaybrynes/MatrixPy#future-additions)

## License:

This project uses a license, the license is automatically included in the project files.

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Installation:

The installation can be completed one of two ways, either clone the MatrixPy repository and place the folder in your project directory. 
Or run the following _'pip'_ command

```DOS .bat
pip install MatrixPy
```

Then add the following to the top of your code to to use the module.

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
a_matrix = Matrix(three_by_five)
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
identity_tuple = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
identity_matrix = Matrix(identity_tuple)
identity_matrix.print()
```
This prints the matrix to the console.

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

### Round elements of a Matrix:

MatrixPy also allows you to round every element of the matrix to a specified number of decimal places.
```python
a_tuple = ((2.543, 3.55), (9.11034, 3.14159))
a_matrix = Matrix(a_tuple)

a_matrix.round(2, normalize=False)
# 'normalize' is a non-essential parameter that is true removes trailing zeroes.
a_matrix.print()
```

This produces a matrix whose elements are all rounded to 2 decimal places. These elements have kept their trailing zeroes because
normalize is set to _'False'_.



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
b_matrix = Matrix.subtract(a_matrix, identity)  # Subtracts the two matrices, puts answer in new Matrix object.
a_matrix.ins_subtract(identity) # Subtracts the two matrices, changes the value of a_matrix to the sum.
```

Similarily for multiplying matrices;
```python
b_matrix = Matrix.multiply(a_matrix, identity) # Multiplies the two matrices, puts answer in new Matrix object.
a_matrix.ins_multiply(identity) # Multiplies the two matrices, changes the value of a_matrix to the sum.
```
However, it should be noted that the normal rules for multiplying matrices applies. 
The rows in _'a'_ needs to match the number of columns in matrix _'b'_.

### Finding the Transpose of a Matrix:

MatrixPy also allows the user to calculate the transpose of a given Matrix. The transpose is a 
flipping of the matrix across its diagonal axis from the upper-left most corner. The transpose
is found as follows:

```python
a_tuple = ((2, 1, -1), (4, 1, 7), (8, -1, 3))
a_matrix = Matrix(a_tuple)

b_matrix = Matrix.transpose(a_matrix) # or
a_matrix.ins_transpose()
``` 

Both of these methods produce the same result, but as before _ins\__ changes the value of the instance.

### Finding the Determinant of Matrices:

In MatrixPy determinants are found using the algorithm found [here](https://en.wikipedia.org/wiki/Gaussian_elimination#Computing_determinants),
on wikipedia. This method can be applied to an matrix of any size, hence the determinant of any _'m'_ x _'m'_ matrix can be found using MatrixPy.

The determinant in MatrixPy is calculated using the method below, it returns a decimal object.
```python
a_tuple = ((2, 1, -1), (4, 1, 7), (8, -1, 3))
a_matrix = Matrix(a_tuple)

determinant = a_matrix.determinant()
print(determinant)
```

### Finding the Inverse of Matrices:

The algorithm for finding inverses is similar to the algorithm for finding the determinant, it can be found [here](https://en.wikipedia.org/wiki/Gaussian_elimination#Finding_the_inverse_of_a_matrix),
again on wikipedia. As with the determinant this can be applied to a matrix of any size.

The inverse in MatrixPy is calculated using the method below,
```python
a_tuple = ((2, 1, -1), (4, 1, 7), (8, -1, 3))
a_matrix = Matrix(a_tuple) # Creates a Matrix object.

b_matrix = Matrix.inverse(a_matrix) # Inverses the matrix, returns a new Matrix object.
a_matrix.ins_inverse() # Inverses the matrix, sets its value as its own inverse.

a_matrix.print()
b_matrix.print()
```

The two print statements will return the same value.

### Finding the solutions of a system of equations:

This project now also supports the calculation for solutions for a system of simultaneous equations. The algorithm is also based on row reduction and its method can be seen in action 
[here](https://en.wikipedia.org/wiki/System_of_linear_equations#Row_reduction). This can be used to find the solutions of any number of variables.

The system of equations shown below has 3 equations for 3 variables. An equation is required for each variable for a full solution to be found. In short, the tuple of equation coefficients must be square.

![system_eqs](https://latex.codecogs.com/gif.latex?%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%20x%20&plus;%203y%20&plus;%204z%20%3D%20-10%5C%5C%203x%20-%204y%20&plus;%202z%20%3D%204%5C%5C%20-x%20&plus;%20y%20-%202z%20%3D%206%20%5Cend%7Bmatrix%7D%5Cright)

The python code and method calls to find the solutions to this system of equations are as follows,
```python
a_tuple = ((1, 3, 4), (3, -4, 2), (-1, 1, -2)) # Matrix of the co-efficients of the system of equations.
b_tuple = ((-10), (4), (6)) # Matrix of the solutions to each of the equations.

a_matrix = Matrix(a_tuple)
b_matrix = Matrix(b_tuple)

c = Matrix.solve_system(a_matrix, b_matrix)
c.print()
```

This prints the solutions to the system of equations. It is important that the all the coefficients for a particular variable are in the same column. The output matrix has the solution for that
variable in the same column as you placed it in the original matrix. For the example given the solution for _'x'_ will be located in the first column, _'y'_ in the second and _'z'_ in the third.


## Support:

The best way to show me that there is a problem with this project is to submit an issue report [here](https://github.com/shaybrynes/MatrixPy/issues). 
Make sure to give as much detail as possible, fully submitting all errors and how you achieved this error. 
If I can not replicate an issue I will assume that it is down to user error (which I will also provide support for).

If you are consistently having issues setting up and using the project, do not hesitate to send me a private message.

## Future Additions:

- [x] Ability to calculate the inverse and determinant.
- [x] Calculation of transpose.
- [x] Installation via PIP.
- [ ] (Much later) eigenvalues. 
