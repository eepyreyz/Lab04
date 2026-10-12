# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Rey Abbas
# Date: 2026/10/12
# Purpose: Create the complete calculator function using default parameters and positional parameters
# Usage: ./lab4d.py

# TODO 1: Create a function called 'compute' based on README.md and print the result

    # TODO 2: Perform the required operation based on parameters

# TODO 3: Call the 'compute' function 5 times to confirm functionality
        # 4 calls should use '+', '-', '*', and '/' as the operator parameter
        # 1 call should use the default operator parameter to confirm it works     

# TODO 4: Create the 'main' function, which reads input for two numbers from the user

    # TODO 5: Perform the compute function using the chosen numbers and operator, then print the result  


# TODO 6: Call your main function with the same condition as lab4c.py

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
    # - @function: Takes two integer numbers form the user, then calls the sum function.
    # - @param: none
    # - @return: none
    """
    num1 = input("enter a number: ")
    num1 = int(num1)
    num2 = input("enter another number: ")
    num2 = int(num2)
    operation = input("enter an operation: ")

    results = compute(num1,num2,operation)

    print(f"The results of your calculation is: {results}")

if __name__ == "__main__":
    """
    @function: Gets two integers and an operation from the user, calls compute, and prints the result.
    @param: None
    @return: None
    """
    main()
    print("\n\nAdditional Tests:")
    print(compute(13, 45, '*'))
    print(compute(13, 45, '/'))
    print(compute(13, 45, '-'))
    print(compute(13, 45, '+'))
    print(compute(13, 45))

    
