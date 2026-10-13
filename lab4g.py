# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:Rey Abbas
# Date: 2026/10/12
# Purpose: Practice map, filter and lambda expressions.
# Usage: ./lab4g.py

# TODO 1: Create a variable list called 'numbers' containing the values 2 to 10
# TODO 2: Square all elements in the list using map and lambda functions
# TODO 3: Print the numbers list
# TODO 4: Make a new variable called 'divisible_by_2'
# TODO 5: Filter out all numbers from th e numbers list that are divisible by 2, using filter and lamba function
        # Store them in the 'divisible_by_2' variable
# TODO 6: Print the 'divisible_by_2' variable

numbers = [2,3,4,5,6,7,8,9,10]
numbers = list(map(lambda x: x ** 2, numbers))
print(numbers)


divisible_by_2 = list(filter(lambda x: x % 2 == 0, numbers))
print(divisible_by_2)
