"""
Assignment Question 3: Case study, to develop a simple calculator program that can perform various mathematical operations.

Task 1. Basic Operations:

Implement functions for addition, subtraction, multiplication, and division.
Task 2. Variable Number of Arguments:

Allow the addition and multiplication functions to accept a variable number of arguments.
Task 3. Scope:

Implement a function to calculate the factorial of a number and demonstrate variable scope.
Task 4. Passing Functions to a Function:

Create a function that takes two numbers and a function as parameters and applies the function to the numbers.

The program should satisfy the following logic

The add, subtract, multiply, and divide functions must handle basic mathematical operations.
The multiply function accepts a variable number of arguments using the *args syntax.
The factorial function calculates the factorial of a number, demonstrating variable scope.
The apply_operation function takes two numbers and a function as parameters and applies the function to the numbers.
The main program utilizes a loop to repeatedly present the user with a menu for different operations.
"""


# Task 1. Basic Operations:
# Implement functions for addition, subtraction, multiplication, and division.

# Task 2. Variable Number of Arguments:
# Allow the addition and multiplication functions to accept a variable number of arguments.

"""

def fact():
    # Task 3. Scope:
    global num
    num = int(input("Please enter a number: "))
    for n in range(1, num):
        num = num * n
    print("The factorial is:", num)
    print("\n")


def add(*numbers):
    result = num1 + num2
    print("The answer is:", result)
    print("\n")


def subtract(x, y):
    return x - y


def multiply(*args):
    result = num1 * num2
    print("The answer is", result)
    print("\n")


def divide(x, y):
    if y == 0:
        return "Can not divide by zero"
    return x / y


# -----------------------------------------------Main Program------------------------------


while True:
    print("1. Addition \n2. Subtraction \n3. Multiply \n4. Divide \n5. Factorial \n6. Exit")
    print("Please enter the number of which calculation you want to use")
    x = float(input())
    if x == 6:
        print("You have exited the code")
        break
    elif x == 1:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        add(num1, num2)
    elif x == 2:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("The answer is:", subtract(num1, num2))
        print("\n")
    elif x == 3:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        multiply(num1, num2)
    elif x == 4:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("The answer is:", divide(num1, num2))
        print("\n")
    elif x == 5:
        fact()
    elif x > 6:
        print("Invalid Input")
        break
"""
# Task 4. Passing Functions to a Function:

# Create a function that takes two numbers and a function as parameters and applies the function to the numbers.

def func_func(num1, num2, math):
    return math(num1, num2)


# Functions for the different operations
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"


# Example usage
addi = func_func(5, 3, add)
print(f"Addition Result: {addi}")

subt = func_func(10, 4, subtract)
print(f"Subtraction Result: {subt}")

mul = func_func(7, 2, multiply)
print(f"Multiplication Result: {mul}")

div = func_func(8, 4, divide)
print(f"Division Result: {div}")
