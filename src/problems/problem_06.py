#!/usr/bin/env python3


def sum_of_positive_integers_in_list(int_list):
    """
    This function adds all of the positive integers in a list and returns the
    result.

    :param int_list: The list of numbers
    """
    # Replace the code below with your own code
    s = 0
    for e in int_list:
        if e > 0:
            s = s + e
    return s


# ------------------------------------------------------------------------------
# Tests: Do not make changes below this line
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    total_wrong = 0

    # Test 1
    ret = sum_of_positive_integers_in_list([1, 2, 3, 4])
    if ret != 10:
        print("Test 1: Uh oh, [1, 2, 3, 4] returned", ret)
        total_wrong = total_wrong + 1


    # Test 2
    ret = sum_of_positive_integers_in_list([1, 2, -4, -6, 3, 4])
    if ret != 10:
        print("Test 2: Uh oh, [1, 2, -4, -6, 3, 4] returned", ret)
        total_wrong = total_wrong + 1


    # Test 3
    ret = sum_of_positive_integers_in_list([-5, -1, -2])
    if ret != 0:
        print("Test 3: Uh oh, [-5, -1, -2] returned", ret)
        total_wrong = total_wrong + 1


    # Test 4
    ret = sum_of_positive_integers_in_list([])
    if ret != 0:
        print("Test 4: Uh oh, [] returned", ret)
        total_wrong = total_wrong + 1


    # Test 5
    ret = sum_of_positive_integers_in_list([1, 1, 1, 1, 1, 1, 1])
    if ret != 7:
        print("Test 5: Uh oh, [1, 1, 1, 1, 1, 1, 1] returned", ret)
        total_wrong = total_wrong + 1


    if total_wrong == 0:
        print("Overall: Woohoo! All tests have been passed for Problem 6!")
    else:
        print("Overall: There's still work to do!")
