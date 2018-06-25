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
