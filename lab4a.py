# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Rey Abbas
# Date: 2026/10/12
# Purpose: Create Simple Functions.
# Usage: ./lab4a.py

# TODO 1: Define a function with the name 'is_even' with the parameters listed in README.md


    # TODO 2: Add the following doc-strings:
    # - @function: add the definition of the function here
    # - @param: write the parameters here
    # - @return: write the return value here

    # TODO 3: Create the functionality as described in the README.md file

    # TODO 4: Do not forge to return your resulting value

# TODO 5: Call the function `is_even` to confirm it works


def is_even (anyList):
    """
    # - @function: Checks a list of numbers for atleast one even number.
    # - @param: anyList - an int list
    # - @results: returns true if an even number is present, otherwise it returns false
    """
    for element in anyList:
        if element % 2 == 0:
            results = True
            # print(results)
            break
        else:
            results = False
    return results

results = is_even([1,2,3,4,5,6])
print(results)

