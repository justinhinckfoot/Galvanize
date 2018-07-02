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
