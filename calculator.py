"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
def output_function(user_input):
    input_lst = user_input.split(" ")
    
    operand = input_lst[0]
    num1 = int(input_lst[1])
    num2 = int(input_lst[2])

    if operand == "+":
        return add(num1, num2)


def main():

    while True:
        user_input = input("> ")
        if user_input != 'q':
            output = output_function(user_input)
            print(output)
        else:
            break

main()