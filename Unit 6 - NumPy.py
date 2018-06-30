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
