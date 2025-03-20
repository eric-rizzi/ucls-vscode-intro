#!/usr/bin/env python3


def add_two_integers(int_1, int_2):
    """
    This function adds two integers together and returns the result.

    :param int_1: The first number
    :param int_2: The second number
    """
    # Replace the code below with your own code
    return int_1 + int_2


# ------------------------------------------------------------------------------
# Tests: Do not make changes below this line
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    total_wrong = 0

    # Test 1
    ret = add_two_integers(5, 0)
    if ret != 5:
        print(f"Test 1: Uh oh, 5 + 0 returned {ret}")
        total_wrong = total_wrong + 1


    # Test 2
    ret = add_two_integers(5, 4)
    if ret != 9:
        print(f"Test 2: Uh oh, 5 + 4 returned {ret}")
        total_wrong = total_wrong + 1


    # Test 3
    ret = add_two_integers(-1, 8)
    if ret != 7:
        print(f"Test 3: Uh oh, -1 + 8 returned {ret}")
        total_wrong = total_wrong + 1


    if total_wrong == 0:
        print("Overall: Woohoo! All tests have been passed for Problem 1!")
    else:
        print("Overall: There's still work to do!")
