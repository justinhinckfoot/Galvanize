# Unit 1 Checkpoint

# Challenge 1
# Write a script that takes two user inputted numbers
# and prints "The first number is larger." or
# "The second number is larger." depending on which is larger.
# If the numbers are equal print "The two numbers are equal."

first = int(input('Enter first test value: '))
second = int(input('Enter second test value: '))

if first > second:
    print('The first number is larger.')
elif first < second:
    print('The second number is larger.')
else:
    print('The two numbers are equal.')

# Challenge 2
# Write a script that computes the factorial
# of a user inputted positive numbers
# and prints the result.

user_input = int(input('Enter a value to compute its factorial: '))
total = 1

while user_input > 0:
    total *= user_input
    user_input -= 1
print(total)

# Challenge 3
# Write a script that computes and prints
# all of the positive divisors of a user inputted
# positive number from lowest to highest.

user_input = int(input('Enter a value to view all positive divisors: '))
x = 1

while user_input >= x:
    if user_input % x == 0:
        print(x)
        x += 1
    else:
        x += 1

# Challenge 4
# Write a script that copmutes the greatest common divisor
# between two user inputted positive numbers and prints the result.

user_input = int(input('Please enter the first test value: '))
second_user_input = int(input('Please enter the second test value: '))
divisor = 1
gcd = 1

while divisor <= user_input or divisor <= second_user_input:
    if user_input % divisor == 0 and second_user_input % divisor == 0:
        gcd = divisor
        divisor += 1
    else:
        divisor += 1
print(gcd)
