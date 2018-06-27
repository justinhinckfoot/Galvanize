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
