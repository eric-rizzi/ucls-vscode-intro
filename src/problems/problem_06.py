#!/usr/bin/env python3


def count_vowels(sentence):
    """
    This function counts the number of vowels in a sentence (upper or lower
    case) and returns the result.

    > Note: In this case, "y" is not considered a vowel

    :param sentence: The sentence to count vowels in
    """
    # Replace the code below with your own code
    return 0


# ------------------------------------------------------------------------------
# Tests: Do not make changes below this line
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    total_wrong = 0

    # Test 1
    ret = count_vowels("LAB!")
    if ret != 1:
        print(f'Test 1: Uh oh, "LAB!" returned {ret}')
        total_wrong = total_wrong + 1


    # Test 2
    ret = count_vowels("Best of FRIENDS!")
    if ret != 4:
        print(f'Test 2: Uh oh, "Best of FRIENDS!" returned {ret}')
        total_wrong = total_wrong + 1


    # Test 3
    ret = count_vowels("A, E, I, O, U, and sometimes Y")
    if ret != 10:
        print(f'Test 3: Uh oh, "A, E, I, O, U, and sometimes Y" returned {ret}')
        total_wrong = total_wrong + 1


    # Test 4
    ret = count_vowels("")
    if ret != 0:
        print(f'Test 4: Uh oh, "" returned {ret}')
        total_wrong = total_wrong + 1


    # Test 5
    ret = count_vowels("Hmmmm AaEeIiOoUu Hmmmm")
    if ret != 10:
        print(f'Test 5: Uh oh, "Hmmmm AaEeIiOoUu Hmmmm" returned {ret}')
        total_wrong = total_wrong + 1


    if total_wrong == 0:
        print("Overall: Woohoo! All tests have been passed for Problem 6!")
    else:
        print("Overall: There's still work to do!")
