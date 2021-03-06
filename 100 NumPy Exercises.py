########################################
# 100 NumPy Exercises
########################################

########################################
# http://www.labri.fr/perso/nrougier/teaching/numpy.100/
########################################



# Exercise 1
    # Import the NumPy package under the name np
    import NumPy as np

# Exercise 2
    # Print the NumPy version and the configuration
    print(np.__version__)
    np.show_config()

# Exercise 3
    # Create a null vector of size 10
    Z = np.zeros(10)
    print(Z)

# Exercise 4
    # How to get the documentation of the numpy add function
    # from the command line
    python -c "import numpy; numpy.info(numpy.add)"

# Exercise 5
    # Create a null vector of size 10 but the fifth value which is 1
    Z = np.zeros(10)
    Z[4]=1
    print(Z)

# Exercise 6
    # Create a vector with values ranging from 10 to 49
    Z = np.arange(10, 50)
    print(Z)

# Exercise 7
    # Reverse a vector (first element becomes last)
    Z = np.arange(0,10)
    Z[::-1]

# Exercise 8
    # Create a 3 x 3 matrix with values ranging from 0 to 8
    Z = np.arange(9)
    Z.reshape(3,3)
        # or
    Z = np.arange(9).reshape(3,3)
    print(Z)

# Exercise 9
    # Find indices of non-zero elements from [1,2,0,0,4,0]
    nz = np.nonzero([1,2,0,0,4,0])
    print(nz)

# Exercise 10
    # Create a 3 x 3 identity matrix
    Z  = np.identity(3)
    print(Z)
        # or
    Z = np.eye(3)
    print(Z)

# Exercise 11
    # Create a 3 x 3 x 3 array with random values
    Z = np.random.rand(3,3,3)
    print(Z)

# Exercise 12
    # Create a 10 x 10 array with random values
        # and find the minimum and maximum values
    Z = np.random.rand(10,10)
    print(np.amin(Z),np.amax(Z))

# Exercise 13
    # Create a random vector of size 30 and find the mean value
    Z = np.random.randint(0,100,30).mean()
    print(Z)

# Exercise 14
    # Create a 2D array with 1 on the border and 0 inside
    Z = np.ones((10,10))
    Z[1:-1,1:-1] = 0

# Exercise 15
    # What is the result of the following expression?
    0 * np.nan
    np.nan == np.nan
    np.inf > np.nan
    np.nan - np.nan
    0.3 == 3 * 0.1

# Exercise 16
    # Create a 5 x 5 matrix with values 1,2,3,4 just below the diagonal
    Z = np.diag(1+np.arange(4),k=-1)
    print(Z)

# Exercise 17
    # Create an 8 x 8 matrix and fill it with a checkboard pattern
    Z = np.zeros((8,8),dtype=int)
    Z[1::2,::2] = 1
    Z[::2,1::2] = 1
    print(Z)

# Exercise 18
    # Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element
    np.unravel_index(100, (6,7,8))

# Exercise 19
    # Create a checkerboard 8 x 8 matrix using the tile function
    Z = np.tile(np.array([[0,1],[1,0]),(4,4))
    print(Z)

# Exercise 20
    # Normalize a 5 x 5 random matrix
    Z = np.random.random((5,5))
    maxZ, minZ = Z.max(), Z.min()
    Z = (Z - minZ) / (maxZ - minZ)
    print(Z)

# Exercise 21
    # Create a custom dtype that describes a color as four unassigned bytes (RGBA)
    color = np.dtype([("r", np.ubyte, 1]),
                        ("g", np.ubyte, 1),
                        ("b", np.byte, 1),
                        ("a", np.byte, 1)])

# Exercise 22
    # Multiply a 5 x 3 matrix by a 3 x 2 matrix (real matrix product)
    Z = np.dot(np.one((5,3)), np.ones((3,2)))
    print(Z)

# Exercise 23
    # Given a 1D array, negate all elements which are between 3 and 8, in place
    Z = arange(11)
    Z[(Z > 3) & (Z < 8)] *= -1
    print(Z)

# Exercise 24
    # What is the output of the following script?
    print(sum(range(5),-1))
    from numpy import *
    print(sum(range(5),-1))

# Exercise 25
    # Consider an integer vector Z, which of these expressions are legal?
    Z ** Z XXXXXXXXXXXXXXXXXXXX
    2 << Z >> 2 XXXXXXXXXXXXXXXXXXXX
    Z <- Z XXXXXXXXXXXXXXXXXXXX
    1j * Z XXXXXXXXXXXXXXXXXXXX
    Z / 1 / 1 XXXXXXXXXXXXXXXXXXXX
    Z <Z> Z

# Question 26
    # What are the results of the following expressions?
    np.array(0) // np.array(0) -- an integer
    np.array(0) // np.aray(0.) -- a floating point number
    np.array(0) / np.array(0) -- a floating point number
    np.array(0) / np.array(0.) -- a floating point number

# Question 27
    # How to round away from zero in a float array?
    Z = np.random.uniform(-10,+10,10)
    print(np.trunc(Z + np.copysign(0.5,Z)))

# Question 28
    # Extract the integer part of a random array using 5 different methods
    Z = np.random.uniform(0,10,10)

    print(Z - Z%1)
    print(np.floor(Z))
    print(np.ceil(Z)-1)
    print(Z.astype(int))
    print(np.trunc(Z))

# Question 29
    # Create a 5 x 5 matrix with row values ranging from 0 to 4
    Z = np.zeros((5,5))
    Z += np.arange(5)
    print(Z)
