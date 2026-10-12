# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Rey Abbas
# Date: 2026/10/12
# Purpose: Practice variable number of arguments with *args
# Usage: ./lab4f.py

# TODO 1: Create a function called 'get_initials' based on README.md
    
    # TODO 2: Extract the first letter from each name provided

    # TODO 3: Return the initials as a list of strings

# TODO 4: Create the 'main' function, which calls the 'get_initials' function

def get_initials (*args):
    """
    @function: Takes a variable number of names and extracts the first letter of each name.
    @param: *args - A variable number of names (strings).
    @return: A list containing the first letter of each name.
    """
    firstLetters = []
    for name in args:
        firstLetters.append(name[0])
        print(f"first letter: {name[0]}")

    return firstLetters

def main():
    """
    @function: Calls the get_initials function, stores the returned list, and prints it.
    @param: None
    @return: None
    """
    initials = get_initials("Alice", "Bob", "Charlie", "David")
    print(initials)

if __name__ == "__main__":
    main()



