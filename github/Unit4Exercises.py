# Unit 4 -- Python Tuples, Dictionaries and Sets

        # Lesson 1 -- Mutability

        # Question 1

        # Which of the following types in Python is mutable?
        # int
        # float
        # str
        # list XXXXXXXXXXXXXXXXX

        # Question 2

        # Consider the list my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # What will my_list look like after running the following code:
        # my_list[4] = 200

        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        my_list[4] = 200

        print(my_list)

        # Answer: [1, 2, 3, 4, 200, 6, 7, 8, 9, 10]

        # Question 3

        # Once again, consider my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # What will my_list look like after running the following code:
        # my_list.append(9)

        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        my_list.append(9)

        print(my_list)

        # Answer: [1, 2, 3, 4, 200, 6, 7, 8, 9, 10, 9]

        # Question 3

        # Assuming you have completed both operations described in the previous
        # questions. What would be the output of running my_list.sort()

        # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # None XXXXXXXXXXXXXXXXXXXXXXX
        # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 200]
        # [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 10, 200]

        # Question 4

        # After the following code is run, what will the output be?

        my_list = list(range(1, 11))
        my_list[4] = 200
        my_list.append(9)
        my_list.sort()
        print(my_list)

        # Answer: [1, 2, 3, 4, 6, 7, 8, 9, 9, 10, 200]

# Lesson 2 -- Tuples

        # Challenge 1

        # Consider the following code:

        suit_tup = ('diamond', 'club', 'spade', 'heart')

        # Is using a tuple to represent the four suites of a standard
        # deck of playing cards appropriate?

        # Answer: Yes -- because the suits in a deck of cards does not change

        # Challenge 2

        # Copy the following code into a Python session to see what it prints
        # Then, change the print statement in this challenge to print out the
        # first element in the tuple

        # Original Code

        suit_tup = ('diamond', 'club', 'spade', 'heart')
        print(suit_tup[::2])

        # Submitted code

        suit_tup = ('diamond', 'club', 'spade', 'heart')
        print(suit_tup[0])

        # Challenge 3

        # Now, change the print statement in this challenge to print out the second
        # and fourth elements in the tuple

        # Original Code

        suit_tup = ('diamond', 'club', 'spade', 'heart')
        print(suit_tup[::2])

        # Submitted Code

        suit_tup = ('diamond', 'club', 'spade', 'heart')
        print(suit_tup[1:4:2])
