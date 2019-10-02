"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
def output_function(user_input):
    input_lst = user_input.split(" ")
    
    if len(input_lst) == 3:
        operand = input_lst[0]
        num1 = int(input_lst[1])
        num2 = int(input_lst[2])
    else:
        operand = input_lst[0]
        num1 = int(input_lst[1])


    if operand == "+":
        return add(num1, num2)
    elif operand == "-":
        return subtract(num1, num2)
    elif operand == "*":
        return multiply(num1, num2)
    elif operand == "/":
        return divide(num1, num2)
    elif operand == "square":
        return square(num1)
    elif operand == "cube":
        return cube(num1)
    elif operand == "pow":
        return power(num1, num2)
    else: 
        return mod(num1, num2)



def main():

    while True:
        user_input = input("> ")
        if user_input != 'q':
            output = output_function(user_input)
            print(output)
        else:
            break

main()