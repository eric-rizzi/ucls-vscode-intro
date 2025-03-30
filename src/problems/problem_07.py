#!/usr/bin/env python3


def count_nums_between(int_list, min_num, max_num):
    """
    This function counts the number of integers in a list that are between
    `min_num` and `max_num` (inclusive).

    :param int_list: The list of numbers
    :param min_num: The minimum number to look for numbers "between"
    :param max_num: The maximum number to look for numbers "between"
    """
    # Replace the code below with your own code
    ret = 0
    for i in int_list:
        if min_num <= i <= max_num:
            ret += 1
    return ret


# ------------------------------------------------------------------------------
# Tests: Do not make changes below this line
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    total_wrong = 0

    # Test 1
    ret = count_nums_between([1, 2, 3, 4], 0, 5)
    if ret != 4:
        print(f"Test 1: Uh oh, [1, 2, 3, 4] returned {ret}")
        total_wrong = total_wrong + 1


    # Test 2
    ret = count_nums_between([1, 2, -4, -6, 3, 4], 3, 4)
    if ret != 2:
        print(f"Test 2: Uh oh, [1, 2, -4, -6, 3, 4] returned {ret}")
        total_wrong = total_wrong + 1


    # Test 3
    ret = count_nums_between([-5, -1, -2], 10, 12)
    if ret != 0:
        print(f"Test 3: Uh oh, [-5, -1, -2] returned {ret}")
        total_wrong = total_wrong + 1


    # Test 4
    ret = count_nums_between([], 8, 10)
    if ret != 0:
        print(f"Test 4: Uh oh, [] returned {ret}")
        total_wrong = total_wrong + 1


    # Test 5
    ret = count_nums_between([1, 1, 1, 1, 1, 1, 1], 0, 2)
    if ret != 7:
        print(f"Test 5: Uh oh, [1, 1, 1, 1, 1, 1, 1] returned {ret}")
        total_wrong = total_wrong + 1


    # Test 6
    ret = count_nums_between([1, 1, 1, 1, 1, 1, 1], 0, 1)
    if ret != 7:
        print(f"Test 6: Uh oh, [1, 1, 1, 1, 1, 1, 1] returned {ret}")
        total_wrong = total_wrong + 1


    # Test 7
    ret = count_nums_between([1, 1, 1, 1, 1, 1, 1], 1, 1)
    if ret != 7:
        print(f"Test 7: Uh oh, [1, 1, 1, 1, 1, 1, 1] returned {ret}")
        total_wrong = total_wrong + 1


    # Test 8
    ret = count_nums_between([1, 1, 1, 1, 1, 1, 1], 1, 2)
    if ret != 7:
        print(f"Test 8: Uh oh, [1, 1, 1, 1, 1, 1, 1] returned {ret}")
        total_wrong = total_wrong + 1


    # Test 9
    ret = count_nums_between([1, 1, 1, 1, 1, 1, 1], 0, 0)
    if ret != 0:
        print(f"Test 9: Uh oh, [1, 1, 1, 1, 1, 1, 1] returned {ret}")
        total_wrong = total_wrong + 1


    # Test 10
    ret = count_nums_between([1, 1, 1, 1, 1, 1, 1], 2, 2)
    if ret != 0:
        print(f"Test 10: Uh oh, [1, 1, 1, 1, 1, 1, 1] returned {ret}")
        total_wrong = total_wrong + 1


    if total_wrong == 0:
        print("Overall: Woohoo! All tests have been passed for Problem 7!")
    else:
        print("Overall: There's still work to do!")
