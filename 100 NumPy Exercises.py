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
