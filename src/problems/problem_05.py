#!/usr/bin/env python3


def any_dogs(sentence):
    """
    This function checks a sentence to see if there are any instances of
    the word "dog". If there is, then the function returns "dogs seen".
    Otherwise, the function returns "no dogs".

    :param sentence: The sentence to check for the presence of dogs
    """
    if "dog" in sentence.lower():
        return "dogs seen"
    return "no dogs"


# ------------------------------------------------------------------------------
# Tests: Do not make changes below this line
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    total_wrong = 0

    # Test 1
    ret = any_dogs("llama horse dog cat")
    if ret != "dogs seen":
        print(f'Test 1: Uh oh, "llama horse dog cat" returned {ret}')
        total_wrong = total_wrong + 1


    # Test 2
    ret = any_dogs("Llama Horse Dog cat")
    if ret != "dogs seen":
        print(f'Test 2: Uh oh, "Llama Horse Dog cat" returned {ret}')
        total_wrong = total_wrong + 1


    # Test 3
    ret = any_dogs("dog")
    if ret != "dogs seen":
        print(f'Test 3: Uh oh, "dog" returned {ret}')
        total_wrong = total_wrong + 1


    # Test 4
    ret = any_dogs("Cat")
    if ret != "no dogs":
        print(f'Test 4: Uh oh, "Cat" returned {ret}')
        total_wrong = total_wrong + 1


    # Test 5
    ret = any_dogs("cat cat not sure but seems like a dog")
    if ret != "dogs seen":
        print(f'Test 5: Uh oh, "cat cat not sure but seems like a dog" returned {ret}')
        total_wrong = total_wrong + 1


    if total_wrong == 0:
        print("Overall: Woohoo! All tests have been passed for Problem 5!")
    else:
        print("Overall: There's still work to do!")
