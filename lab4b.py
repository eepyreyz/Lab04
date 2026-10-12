# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Rey Abbas
# Date: 2026/10/12
# Purpose: Create Some Complex Functions.
# Usage: ./lab4b.py

# TODO 1: Create a function called 'even_numbers' with the parameters listed in README.md

    # TODO 2: Add the following doc-strings:
        # - @function: add the definition of the function here
        # - @param: write the parameters here
        # - @return: write the return value here

    # TODO 3: Complete the functionality of the function based on README.md instructions

    # TODO 4: Do not forge to return your resulting value

# TODO 5: Call the function `even_numbers` to confirm it works

def even_numbers (anyList):
    """
    # - @function: Takes a list of integers and creates another list of just the even numbers.
    # - @param: A list of integers.
    # - @return: contains the even number from the list entered in the parameters.
    """
    evenList = []
    for element in anyList:
        if element % 2 == 0:
            evenList.append(element)
    return evenList # we need to return the list because we created it inside the function


anyList = [1,2,3,4,5,6,7,8]

evenList = even_numbers(anyList) # recive the results in a variable

# print(anyList)
print(evenList)

