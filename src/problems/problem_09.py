#!/usr/bin/env python3


def fibonacci(desired_len):
    """
    This function takes a single input: an integer. It then returns a list of
    integers of the given length filled with the Fibonacci numbers.

    :param desired_len: The number of fibonacci numbers to produce
    """
    # Replace the code below with your own code
    if desired_len <= 0:
        return []
    elif desired_len == 1:
        return [1]
    elif desired_len == 2:
        return [1, 1]
    else:
        ret = [1, 1]
        for i in range(2, desired_len):
            ret.append(ret[-1] + ret[-2])
        return ret


# ------------------------------------------------------------------------------
# Tests: Do not make changes below this line
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    total_wrong = 0

    # Test 1
    ret = fibonacci(0)
    if ret != []:
        print("Test 1: Uh oh, 0 returned", ret)
        total_wrong = total_wrong + 1


    # Test 2
    ret = fibonacci(-10)
    if ret != []:
        print("Test 2: Uh oh, -10 returned", ret)
        total_wrong = total_wrong + 1


    # Test 3
    ret = fibonacci(1)
    if ret != [1]:
        print("Test 3: Uh oh, 1 returned", ret)
        total_wrong = total_wrong + 1


    # Test 4
    ret = fibonacci(5)
    if ret != [1, 1, 2, 3, 5]:
        print("Test 4: Uh oh, 5 returned", ret)
        total_wrong = total_wrong + 1


    # Test 5
    ret = fibonacci(8)
    if ret != [1, 1, 2, 3, 5, 8, 13, 21]:
        print("Test 5: Uh oh, 8 returned", ret)
        total_wrong = total_wrong + 1


    if total_wrong == 0:
        print("Overall: Woohoo! All tests have been passed for Problem 9!")
    else:
        print("Overall: There's still work to do!")
