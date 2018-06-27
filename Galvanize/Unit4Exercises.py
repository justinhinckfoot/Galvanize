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

        # Challenge 4

        # Say that you want to add a new suit to the card deck
        # Call it gorilla
        # Which of the following options can be used to add gorilla to your deck

        # suit_tup.append('gorilla')
        # suit_tup. += ('gorilla')
        # suit_tup += tuple('gorilla')
        # suit_tup = ('diamond, 'club', 'spade', 'heart', 'gorilla') XXXXXXXXXXXXXXXXX

# Lesson 3 -- Dictionaries

        # Challenge 1

        # Consider the following code:

        my_dct = {'Texas': 'Austin', 'Indiana': 'Indianapolis', 'Illinois': 'Chicago', 'New York': 'New York City'}
        for element in my_dct:
            print(element)

        # Which of the following could be one of the lines printed by this code?

        # Texas XXXXXXXXXXXXXXXXXXXXXXX -- when iterating through a dictionary, each
                # key is accessed so the code prints the states, not the capitals
        # Austin
        # Texas, Austin
        # {Texas: Austin}

        # Challenge 2

        # Modify the code below so that it takes the user inputted state,
        # and if it is in my_dct, print out its capital
        # If it's not, then print out 'Capital not found!'

        # Original code

        # Example input() statement
        state = input('Please enter a State: ')

        my_dct = {'Texas': 'Austin', 'Indiana': 'Indianapolis', 'Illinois': 'Chicago', 'New York': 'Albany'}

        print(my_dct)

        # Submitted Code

        state = str(input('Enter a state to view its capital: '))

        my_dct = {'Texas': 'Austin', 'Indiana': 'Indianapolis', 'Illinois': 'Chicago', 'New York': 'Albany'}

        print(my_dct.get(state,'Capital not found!'))

# Lesson 4 -- Getting More Out of Dependencies

        # Challenge 1

        # Change the loop so that it not only prints the key at every iteration,
        # but both the key and value
        # These key-value pairs should be printed as tuples

        # Original Code

        my_dct = {'Texas': 'Austin', 'Indiana': 'Indianapolis', 'Illinois': 'Chicago', 'New York': 'Albany'}
        for state in my_dct:
            print(state)

        # Submitted Code

        my_dct = {'Texas': 'Austin', 'Indiana': 'Indianapolis', 'Illinois': 'Chicago', 'New York': 'Albany'}
        for thing in my_dct.items():
            print(thing)

        # Challenge 2

        # Modify the code below to print the capitals that start with an s

        # Original Code

        my_dct = {'Texas': 'Austin', 'Indiana': 'Indianapolis', 'Illinois': 'Chicago',
                  'New York': 'Albany', 'Iowa': 'Des Moines',
                  'California': 'Sacramento', 'Utah': 'Salt Lake City',
                  'Ohio': 'Columbus'}
        for state in my_dct:
            print(my_dct[state])

        # Submitted Code

        my_dct = {'Texas': 'Austin', 'Indiana': 'Indianapolis', 'Illinois': 'Chicago',
                  'New York': 'Albany', 'Iowa': 'Des Moines',
                  'California': 'Sacramento', 'Utah': 'Salt Lake City',
                  'Ohio': 'Columbus'}
        for capital in my_dct.values():
            if capital.startswith('S'):
                print(capital)

# Lesson 5 -- Sets

        # Challenge 1

        # Use a for loop to iterate over and print each element in my_set

        # Original Code

        my_set = {2, 3, 5, 7, 11}

        # Submitted Code

        my_set = {2, 3, 5, 7, 11}

        for element in my_set:
            print(element)

        # Challenge 2

        # Use a for loop to print the values in my_new_set that do NOT appear in my_set

        # Original Code

        my_set = {2, 3, 5, 7, 11}
        my_new_set = {1, 3, 5, 7, 9}

        # Submitted Code

        my_set = {2, 3, 5, 7, 11}
        my_new_set = {1, 3, 5, 7, 9}

        for element in my_new_set:
            if element not in my_set:
                print(element)

# Lesson 6 - Dictionary Comprehensions

        # Challenge 1

        # Take input from the user with a list of words to capitalize
        # These words should be separated by spaces
        # Then create a dictionary that has keys that are the original word
        # and values that are the uppercase version of the word

        user_input = input('Enter a space-separated list of values: ')
        user_set = user_input.split(' ')

        user_dict = {input: input.upper() for input in user_set}

        print(user_dict)

# Challenge 2

# Create tuples that have a word of mixed case as the first element
# and an entirely lowercase string as the element element
# Take a list of space separated words for your input

user_input = input('Enter a space-separated list of values: ')
user_set = user_input.split(' ')

user_dict = {input: input.lower() for input in user_set}

user_tuple = tuple(user_dict)

for item in user_set.items():
    tuple(item)
    print(item)

print(user_dict)
print(user_tuple)
result =

# Unit 4 Checkpoint

        # Challenge 1 -- Tuplle Challenge

        # Write a script that prompts the user to input a series of numbers separated
        # by commas. Your script will then take these inputted numbers and store them
        # as a set of tuples, two at a time. Finally your script will print
        # that list of tuples to the user.
        # If the user inputs an odd number of numbers, then only make a list
        # of the largest number of pairs of two that are possible.

        user_input = input('Please enter a list of comma-separated values: ')

        user_list = [int(i) for i in user_input.split(', ')]

        tuple_list = []

        for i, j in zip(user_list[0::2],user_list[1::2]):
            tuple_list.append((i, j))
