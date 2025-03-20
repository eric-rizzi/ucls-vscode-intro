#!/usr/bin/env python3


def add_length_of_strings(str_1, str_2):
    """
    This function takes in two strings and adds their lengths together.

    :param str_1: The first string
    :param str_2: The second string
    """
    # Replace the code below with your own code
    return len(str_1) + len(str_2)


# ------------------------------------------------------------------------------
# Tests: Do not make changes below this line
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    total_wrong = 0

    # Test 1
    ret = add_length_of_strings("hi", "there")
    if ret != 7:
        print(f'Test 1: Uh oh, len("hi") + len("there") returned {ret}')
        total_wrong = total_wrong + 1


    # Test 2
    ret = add_length_of_strings("", "hi")
    if ret != 2:
        print(f'Test 2: Uh oh, len("") + len("hi") returned {ret}')
        total_wrong = total_wrong + 1


    # Test 3
    ret = add_length_of_strings("encyclopedia", " brown")
    if ret != 18:
        print(f'Test 3: Uh oh, len("encyclopedia") + len(" brown") returned {ret}')
        total_wrong = total_wrong + 1


    if total_wrong == 0:
        print("Overall: Woohoo! All tests have been passed for Problem 1!")
    else:
        print("Overall: There's still work to do!")
