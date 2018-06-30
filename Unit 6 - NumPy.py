# Unit 6 - NumPy

# Lesson 1 -- Create and Modify Arrays in NumPy

    # Question 1 -- NumPy Practice 1

        # Use the NumPy method arange to create the following NumPy arrays

        # Provided Code

        import numpy as np

        # row vector of the integers 1 to 6, inclusive
        row_vector = None

        # column vector of the integers 11 to 14, inclusive
        column_vector = None

        # Submitted Code

        import numpy as np

        row_vector = np.arange((1,7))

        column_vector = np.arange((11,15))

# Lesson 2 -- Use Boolean Indexing to Inspect and Modify NumPy Arrays

    # Question 1 -- NumPy Practice 2

    # Fill in the following function stubs

    # Provided Code

    import numpy as np

    def elements_greater_than_mean(arr):
        '''
        Return a new array with the elements of the array
        arr that are greater than its mean.

        >>> elements_greater_than_mean(np.array([0.2, 0.8, 0.3, 0.6]))
        array([0.8, 0.6])
        '''
        pass

    # Submitted Code

    import numpy as py

    def elements_greater_than_mean(arr):
        """
        Return a new array with the elements of the array
        arr that are greater than its mean.

        >>> elements_greater_than_mean(np.array([0.2, 0.8, 0.3, 0.6]))
        array([0.8, 0.6])
        """
        list = py.array(arr)

        output = list[list > py.mean(list)]

        return output

# Lesson 3 --


# Exercise 1 -- Checkpoint

# Question 1 -- NumPy Checkpoint Q1

# Use boolean indexing to return the elements of an array that are greater
# than or equal to two times the minimum element of the array

# Provided Code

import numpy as np

def elements_twice_min(arr):
    """
    Return all elements of array arr that are greater than or equal to 2 times
    the minimum element of arr.

    Parameters
    ----------
    arr: NumPy array (n, m)

    Returns
    -------
    NumPy Array, a vector of size between: 0 and (n * m) - 1
    """
    pass

# Submitted Code
import numpy as np

def elements_twice_min(arr):
    """
    Return all elements of array arr that are greater than or equal to 2 times
    the minimum element of arr.

    Parameters
    ----------
    arr: NumPy array (n, m)

    Returns
    -------
    NumPy Array, a vector of size between: 0 and (n * m) - 1
    """
    list = np.array(arr)

    output = list[list >= (np.min(list) * 2)]

    return output

# Question 2 - NumPy Checkpoint Q2

# Add two NumPy vectors or matrices together, if possible.
# If it is not possible to add the two vectors (due to size differences) return False

# Provided Code

import numpy as np

def mat_addition(A, B):
    """
    Add vector/matrix arrays A and B together. If they cannot be added
    return False.

    Parameters
    ----------
    A: NumPy array size of (n,) or (n, m)
    B: NumPy array size of (p,) or (p, q)

    Returns
    -------
    NumPy Array of same size as A and B, or False if their sizes differ.
    """
    pass

# Submitted Code

import numpy as np

def mat_addition(A, B):
    """
    Add vector/matrix arrays A and B together. If they cannot be added
    return False.

    Parameters
    ----------
    A: NumPy array size of (n,) or (n, m)
    B: NumPy array size of (p,) or (p, q)

    Returns
    -------
    NumPy Array of same size as A and B, or False if their sizes differ.
    """
    arrayA = np.array(A)
    arrayB = np.array(B)

    if np.size(A) != np.size(B):
        return False
    else:
        return arrayA + arrayB
