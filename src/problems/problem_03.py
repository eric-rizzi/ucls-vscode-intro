#!/usr/bin/env python3


def largest_input(num_1, num_2, num_3):
    """
    This function returns the largest of three integer inputs.

    > Note: assume that all the numbers are different values.

    :param num_1: The first number
    :param num_2: The second number
    :param num_3: The third number
    """
    # Replace the code below with your own code
    return num_1


# ------------------------------------------------------------------------------
# Tests: Do not make changes below this line
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    total_wrong = 0

    # Test 1
    ret = largest_input(6, 5, 4)
    if ret != 6:
        print(f"Test 1: Uh oh, (6, 5, 4) returned {ret}")
        total_wrong = total_wrong + 1


    # Test 2
    ret = largest_input(1, 2, 3)
    if ret != 3:
        print(f"Test 2: Uh oh, (1, 2, 3) returned {ret}")
        total_wrong = total_wrong + 1


    # Test 3
    ret = largest_input(10, 11, 9)
    if ret != 11:
        print(f"Test 3: Uh oh, (10, 11, 9) returned {ret}")
        total_wrong = total_wrong + 1


    # Test 4
    ret = largest_input(10, 1000, 20)
    if ret != 1000:
        print(f"Test 4: Uh oh, (10, 1000, 20) returned {ret}")
        total_wrong = total_wrong + 1


    if total_wrong == 0:
        print("Overall: Woohoo! All tests have been passed for Problem 3!")
    else:
        print("Overall: There's still work to do!")
