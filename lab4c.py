# Add comments before you do anything else.
#!/usr/bin/env python3
# Author: Rey abbas
# Date: 2026/10/12
# Purpose: use the main Function as entry point.
# Usage: ./lab4c.py

# TODO 1: Create a function called 'sum' which takes two numbers as parameters and returns the sum

# TODO 2: Create the 'main' function, which reads input for two numbers from the user, then calls the sum function

# TODO 3: Call your main function with the specific condition presented in README.md




def sum (a,b):
    """
    # - @function: Takes two numbers and adds them together
    # - @param: Two integer numbers
    # - @return: The sum of both numbers
    """
    sum = a + b
    return sum

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

    valuesSum = sum(num1,num2)
    print(f"The sum of the two numbers is: {valuesSum}")

if __name__ == "__main__":
  main()
