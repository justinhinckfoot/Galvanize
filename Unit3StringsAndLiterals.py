# Unit 3 -- Strings and Lists

# Lesson 1 -- Introduction to Strings

        # Challenge 1

        # The following code contains a syntax error in the way that
        # the string is specified. Fix the error.
        # The output of the program should be "This won't work."

        # Original Code

        # A poorly-specified string
        s = 'This won't work.'

        # Print the string after you fix it
        print(s)

        # Answer

        # A poorly-specified string
        s = "This won't work."

        # Print the string after you fix it
        print(s)

        # Challenge 2

        # Write a program that takes a user-inputted non-negative integer
        # and generates an arrow whose tail is the length of the number.

        n = int(input('Enter the length of the tail: '))

        length = str('-') * n

        print(length + str('>'))

        # Challenge 3

        # Write a program that takes a user-inputted string, converts it
        # to all caps and prints it outself.

        string = str(input('Enter a string to covert: '))

        print(string.upper())

        # Challenge 4

        # Write a program that takes a user-inputted string and does the following:
            # if the string is in all caps, convert it to lower case
            # if the string is not in all caps, covert it to all caps and append
                # 3 exclamation marks to the entered
        # your program should then print out the converted stringself.

        string = str(input('Enter a string to convert: '))

        if string.isupper() == True:
            print(string.lower())
        else:
            print(string.upper() + '!!!')

        # Challenge 5

        # Write a program that takes a user-inputted string and tests to see
        # if it ends with three exclamation points. If it does, replace the "!!!"
        # with a period ("."). Your program should then print out the stringself.

        string = str(input('Enter a string to convert: '))

        if string.endswith("!!!"):
            print(string.replace("!!!","."))
        else:
            print(string)

# Lesson 2 -- Strings Indexing and Iterations

        # Challenge 1

        # Write a program that takes a user-inputted string and prints out
        # the character at index 5. If the string has less than 6 characters,
        # your program should print 'String too short.'

        string = str(input('Enter a string to test: '))

        if len(string) < 6:
            print('String too short.')
        else:
            print(string[5])

        # Challenge 2

        # Write a program that takes a user-inputted string and prints out
        # the substring of characters at the 2nd, 3rd, and 4th index
        # positions. If the string has less than 5 characters, your program
        # should print 'String too short.'

        string = str(input('Enter a string to test: '))

        if len(string) < 5:
            print('String too short.')
        else:
            print(string[2:5])

        # Challenge 3

        # Write a program that takes a user-inputted string and prints
        # out every other character from that string, beginning at index 1.
        # If the string has less than 2 characters, your program should
        # print 'String too short.'

        string = str(input('Enter a string to test: '))

        if len(string) < 2:
            print('String too short.')
        else:
            print(string[1::2])

        # Challenge 4

        # Write a program that takes a user-inputted string and prints
        # out the next-to-last character from that string. If the stringself
        # has less than 2 characters, your program should print 'String too short.'

        string = str(input('Enter a string to test: '))

        if len(string) < 2:
            print('String too short.')
        else:
            print(string[-2])

        # Challenge 5

        # The sample below uses a while loop to print out every other character
        # (starting at index 0) from a user-inputted string in uppercase.
        # Rewrite the code to use a for loop instead; your program's output
        # should be the same as before.

        # Original Code

        # Example input() statement
        s = input('Please enter a string: ')

        i = 0
        while i < len(s):
            print(s[i].upper())
            i += 2

        # Rewritten Code

        string = str(input('Enter a string to test: '))
        i = 0

        for i in string[::2]:
            print(i.upper())

# Lesson 3 -- String Formatting

        # Challenge 1

        # Write a program that takes a user-inputted string and prints
        # out 'Hello, <input>!' in response, where <input> is the inputted string.

        string = str(input('Enter your name: '))

        print('Hello, {}!'.format(string))

        # Challenge 2

        # Write a program that takes a user-inputted integer and prints out
        # Two times <input> is <result>, where <input> is the inputted integer
        # and <result> is twice the value.

        number = int(input('Enter a value to multiply: '))
        double = number * 2

        print('Two times {} is {}.'.format(number,double))

# Challenge 3

# Write a program that takes a user-inputted integer and prints
# out the value of pi to the number of decimal places specified
# by the integer.

from math import pi

N = int(input('Enter the number of decimal points: '))

print({pi:.10f})

# Lesson 4 -- Lists

        # Challenge 1

        # Write a program that takes in:
            # s1 -- A comma-separated string
            # s2 -- A string to be counted
        # And prints the number of occurances of the second string within
        # the string's comma-separated members.

        s1 = str(input('Enter a list of comma-separated values: '))
        s2 = str(input('Enter a value to count from list: '))
        l = s1.split(', ')

        print(l.count(s2))
        print(l.count(l[1]))

        # Challenge 2

        # Write a program that takes a series of user-inputted, comma-separated
        # strings and prints a list of those strings with the first element repeated
        # at the end.

        user_input = str(input('Enter a list of command-separated values: '))
        user_list = user_input.split(', ')

        user_list.append(user_list[0])
        print(list)

        # Challenge 3

        # Write a program that takes a series of user-inputted, comma-separated
        # strings, creates a list from it, and turns that list into a word-unit
        # palindrome; i.e., a list with the same words forward and backwardself.

        user_input = str(input('Enter a list of comma-separated values: '))
        user_list = user_input.split(', ')
        duplicate = list(user_list)

        duplicate.reverse()
        user_list.extend(duplicate)
        print(user_list)

        # Challenge 4

        # Write a program that takes a series of user-inputted,
        # comma-separated strings, creates a list from it, and turns that list
        # into a word-unit palindrome with an odd number of elements.
        # This implies that the palindrome will 'hinge' on its middle element.

        user_input = str(input('Enter a list of comma-separated values: '))
        user_list = user_input.split(', ')
        duplicate = list(user_list[:-1])

        duplicate.reverse()

        user_list.extend(duplicate)
        print(user_list)

        # Challenge 5

        # Write a program that takes a series of user-inputted, comma-separated
        # strings, and prints out a list of the odd-indexed elements.

        user_input = str(input('Enter a list of comma-separated values: '))
        user_list = user_input.split(', ')

        print(user_list[1::2])

        # Challenge 6

        # Write a program that takes a series of user-inputted, comma-separated
        # strings, creates a list from it, sorts the list, then prints the sorted list
        # with each element numbered, starting from 1

        user_input = str(input('Enter a list of comma-separated values: '))
        user_list = user_input.split(', ')

        user_list.sort()

        for count, ele in enumerate(user_list,1):
            print(count, ele)

# Lesson 5 -- String Comprehension

        # Challenge 1

        # Write a one-liner that takes in a list of words like ['SPAM','Spam','spam']
        # and outputs a list with the lowercase version of each word. Use a list
        # comprehension, do not use a for loop!

        user_input = str(input('Enter a list of comma-separated values: '))
        user_list = user_input.split(', ')

        lowercase = [print(string.lower()) for string in user_list]

# Exercise 1 -- Practice with Strings and Lists

# Part 1 -- Practice with for Loops

        # Challenge 1

        # Write a script that computes the factorial of a user-inputted positive
        # number and prints the result

        user_input = int(input('Enter a value to compute its factorial: '))
        total = 1

        while user_input > 0:
            total *= user_input
            user_input -= 1
        print(total)

        user_input = int(input('Enter a value to compute its factorial: '))
        factorial_list = list(range(1,user_input))
        total = user_input

        for num in factorial_list:
            total *= num
        print(total)
