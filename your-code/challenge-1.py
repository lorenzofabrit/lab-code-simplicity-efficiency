"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""



# this process can be made easier by using a function instead of the If condition

def calculator():
    print('Welcome to this calculator!')
    print('It can add and subtract whole numbers')
    a = int(input('Please choose your first number: '))
    operation = input('Please type in the operation you would like to complete (+ or -): ')
    b = int(input('Please choose your second number: '))

    # Addition
    if operation == '+':
        print('{} + {} = '.format(a, b))
        print(a + b)

    # Subtraction
    if operation == '-':
        print('{} - {} = '.format(a, b))
        print(a - b)
