# MatrixPy
_*A simple handler for for matrix objects in Python 3.*_

## Contents:

* [Installation](https://github.com/shaybrynes/MatrixPy#installation)
* [Usage](https://github.com/shaybrynes/MatrixPy#usage)
    * [Printing the Matrices](https://github.com/shaybrynes/MatrixPy#printing-the-matrices)
    * [Adding, Subtracting and Multiplying Matrices](https://github.com/shaybrynes/MatrixPy#adding-subtracting-and-multiplying-matrices)
    * [Finding the Determinant of Matrices](https://github.com/shaybrynes/MatrixPy#finding-the-determinant-of-matrices)
    * [Finding the Inverse of Matrices](https://github.com/shaybrynes/MatrixPy#finding-the-inverse-of-matrices)
* [Support](https://github.com/shaybrynes/MatrixPy#support)
* [Future Additions](https://github.com/shaybrynes/MatrixPy#future-additions)

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
a = Matrix(identity)
```
It is important to note that the matrix inputted *must* be of the type tuple, his important for immutability.
The above code specifically makes the value of the matrix object the below matrix,

![Identity](http://latex.codecogs.com/gif.latex?%5Cbegin%7Bpmatrix%7D%201%20%26%200%20%26%200%20%5C%5C%200%20%26%201%20%26%200%20%5C%5C%200%20%26%200%20%26%201%5C%5C%20%5Cend%7Bpmatrix%7D)

Say, instead you wanted a 3x5 matrix.
```python
three_by_five = ((2, 0, -3, 4, 5), (7, 2, -1, -4, 0), (-9, 4, 5, 3, 6))
a = Matrix(three_by_five, m=3, n=5) # m=int() and n=int() are non-essential parameters 
```
This would produce a matrix object equivalent to to below,

![FiveByFive](http://latex.codecogs.com/gif.latex?%5Cbegin%7Bpmatrix%7D%202%20%26%200%20%26%20-3%20%26%204%20%26%205%5C%5C%207%20%26%202%20%26%20-1%20%26%20-4%20%26%200%5C%5C%20-9%20%26%204%20%26%205%20%26%203%20%26%206%5C%5C%20%5Cend%7Bpmatrix%7D)

In fact when using this object the only limit to the size of the matrices you use is the memory on your device

### Printing the Matrices:

MatrixPy can handle the printing of your matrices to the screen, it can be achieved using this method.
```python
identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
identity.print()
```

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
This section of code will output the two matrices. Which in this case will have the same value.
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
The rows in _a_ needs to match the number of columns in matrix _b_.

### Finding the Determinant of Matrices:

In MatrixPy determinants are found using the method found on [here](https://en.wikipedia.org/wiki/Gaussian_elimination#Computing_determinants),
on wikipedia. This method can be applied to an matrix of any size, hence the determinant of any _m_ x _m_ matrix can be found using MatrixPy.

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
Make sure to give as much detail as possible,fully submitting all errors and how you achieved this error. 
If I can not replicate an issue I will assume that it is down to user error (which I will also provide support for).

If you are consistently having issues setting up and using the project, do not hesitate to send me a private message.

## Future Additions:

- [x] Ability to calculate the inverse and determinant.
- [ ] Calculation of transpose.
- [ ] Installation via PIP.
- [ ] (Much later) eigenvalues. 
