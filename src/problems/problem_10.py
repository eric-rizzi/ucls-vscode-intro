#!/usr/bin/env python3


def primes(max_num):
    """
    This function takes a single input: an integer. It then returns all the
    prime numbers less than **or equal to** that number.

    :param max_num: The maximum to check for whether it's prime or not
    """
    # Replace the code below with your own code
    return [-1]


# ------------------------------------------------------------------------------
# Tests: Do not make changes below this line
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    total_wrong = 0

    # Test 1
    ret = primes(0)
    if ret != []:
        print(f"Test 1: Uh oh, 0 returned {ret}")
        total_wrong = total_wrong + 1


    # Test 2
    ret = primes(1)
    if ret != []:
        print(f"Test 2: Uh oh, 1 returned {ret}")
        total_wrong = total_wrong + 1


    # Test 3
    ret = primes(-10)
    if ret != []:
        print(f"Test 3: Uh oh, 10 returned {ret}")
        total_wrong = total_wrong + 1


    # Test 4
    ret = primes(10)
    if ret != [2, 3, 5, 7]:
        print(f"Test 4: Uh oh, 10 returned {ret}")
        total_wrong = total_wrong + 1


    # Test 5
    ret = primes(13)
    if ret != [2, 3, 5, 7, 11, 13]:
        print(f"Test 5: Uh oh, 13 returned {ret}")
        total_wrong = total_wrong + 1


    if total_wrong == 0:
        print("Overall: Woohoo! All tests have been passed for Problem 10!")
    else:
        print("Overall: There's still work to do!")
