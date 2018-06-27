# Unit 5 -- Python Functions

# Lesson 1 -- Introduction to Python Functions

    # Question 1 -- Function Outputs

        # If you were to copy the following code for get_evens
        # into your interpreter, and then run it three times, will the
        # output be the same every time you run it?

        # Provided Code

        def get_evens():
            evens = []
            for element in range(10):
                if element % 2 == 0:
                    evens.append(element)

            return evens

        # Yes XXXXXXXXXXXXXXXXXXX
        # No

    # Question 2 -- Modify get_evens Function

        # Modify the get_evens function below so it will output
        # the evens from 0 to 18 instead of from 0 to 8

        # Provided Code

        def get_evens():
            evens = []
            for element in range(10):
                if element % 2 == 0:
                    evens.append(element)
            return evens

        # Submitted Code

        def get_evens():
            evens = []
            for element in range(19):
                if element % 2 == 0:
                    evens.append(element)
            return evens

    # Question 3 -- Modify get_evens Function Again

        # Modify the get_evens function below so it will output the
        # multiples of 3 instead of 2 from 0 to 18

        # Provided Code

        def get_evens():
            evens = []
            for element in range(10):
                if element % 2 == 0:
                    evens.append(element)
            return evens

        # Submitted Code

        def get_evens():
            evens = []
            for element in range(19):
                if element % 3 == 0:
                    evens.append(element)
            return evens

# Lesson 2 -- Functions with Parameters and Arguments

    # Question 1 -- Python Function Declarations

        # Which of the following function definitions are invalid?

            # A. XXXXXXXXXXXXXXXXXXXXXXXXXXX
                def my_func1(var1='Hello', var2):
                    pass
            # B.
                def my_func1(var1, var2='Hello'):
                    pass
            # C.
                def my_func1(var1, var2=35):
                    pass
            # D. XXXXXXXXXXXXXXXXXXXXXXXXXXX
                def my_func1(var1=35, var2):
                    pass
            # E.
                def my_func1(var1=35, var2='Hello'):
                    pass
            # F.
                def my_func1(var1, var2):
                    pass

                # variables with defaults need to be made after variables w/o defaults

    # Question 2 -- Parameter versus Argument

        # Which of the following is a parameter and which is an argument?

        # A. A value passed in to a function
        # B. The name of a variable in a function definition

        # A = argument
        # B = parameter

# Lesson 3 -- Function Arguments and Variable Scope

    # Question 1 -- Function Calls

        # Consider the following function call:

            get_multiples(divisor=7, n=42)

        # Does it pass arguments by position or by keyword?

            # By position

            # By keyword XXXXXXXXXXXXXXXXXXX

    # Question 2 -- Call a Function

        # Given the following function:

            def lcm(a, b):
                """
                Find the least common multiple of two numbers

                Parameters
                ----------
                a: {int} the first number
                b: {int} the second number

                Returns
                -------
                n: {int} the least common mulitple of a and b
                """
                return abs(a * b) / gcd(a, b)

        # Write a valid call to the function

            lcm(4, 12)


    # Quetion 3 -- Variable Scope

        # Will the following code throw an error due to the variable scope issues?

        x = 7

        def some_function(z):
            for index in range(z):
                if index == x:
                    return True
            return False

        some_function(7)

        # Yes
        # No XXXXXXXXXXXXXXXXXXX

    # Question 4 -- Fix This Code

    # The function below throws an error due to variable cope issues
    # Fit it so that it does not do this

    # Original Code

    def calculate_series(n):
    '''
    calculate the nth value in the series:
    a_i = 2 * a_(i-1) + 1
    and where the initial value of the series, a_0, is initialized to 1.

    Parameters
    ----------
    n: {int}

    Returns
    -------
    a_n: {int} the nth series value

    '''
    for _ in range(n):
        a = 2 * a + 1
    return a

    # Submitted Code

    def calculate_series(n):
        '''
        calculate the nth value in the series:
        a_i = 2 * a_(i-1) + 1
        and where the initial value of the series, a_0, is initialized to 1.

        Parameters
        ----------
        n: {int}

        Returns
        -------
        a_n: {int} the nth series value

        '''
        a = 1

        for _ in range(n):
            a = 2 * a + 1
        return a

# Exercise 1 -- Checkpoint

# Question 1 -- Practice with Functions 1

    # Fill in the following function according to the docstring

    # Provided Code

    def get_divisors(n):
        '''
        This function calculates and returns all of the divisors of n, between 1 and
        n, inclusive.

        Parameters
        ----------
        n: {int}

        Returns
        -------
        divisors: {list} all divisors of n in order from smallest to largest
        '''
        pass

    # Submitted Code

    def get_divisors(n):
        '''
        This function calculates and returns all of the divisors of n, between 1 and
        n, inclusive.

        Parameters
        ----------
        n: {int}

        Returns
        -------
        divisors: {list} all divisors of n in order from smallest to largest
        '''
        divisors = []
        max = n+1
        for i in range(1,max):
            if n % i == 0:
                divisors.append(i)
        return(divisors)
