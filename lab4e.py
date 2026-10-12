# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Modify the calcualtor program to use keyword parameters.
# Usage: ./lab4e.py

# TODO 1: Copy the code from lab4d.py

# TODO 2: Modify the 'compute' function to use keyword parameters for the operator and numbers
# Refer to lesson slides to review the difference between keyword and positional parameters


def compute (num1, num2, operation = "+"):
    """
    @function: Performs a calculation using two numbers and an operation.
    @param: num1, num2, and an operation
    @param: operation - The operation (+, -, *, /), default is +.
    @return: The result of the calculation.
    """
    results = None

    if operation == "+":
        results = num1 + num2
    elif operation == "-":
        results = num1 - num2
    elif operation == "/":
        results = num1 / num2
    elif operation == "*":
        results = num1 * num2
    else:
        print("Invalid operation")
    # print(results)
    return results
    

def main():
    """
    @function: Gets two integers and an operation from the user, calls compute, and prints the result.
    @param: None
    @return: None
    """
    num1 = input("enter a number: ")
    num1 = int(num1)
    num2 = input("enter another number: ")
    num2 = int(num2)
    operation = input("enter an operation: ")

    results = compute(num1=num1,operation=operation,num2=num2)

    print(f"The results of your calculation is: {results}")

if __name__ == "__main__":

    main()
    print("\n\nAdditional Tests:")
    print(compute(operation='*', num2=45, num1=13))
    print(compute(num2=45, operation='/', num1=13))
    print(compute(num1=13, operation='-', num2=45))
    print(compute(operation='+', num1=13, num2=45))
    print(compute(num2=45, num1=13))

