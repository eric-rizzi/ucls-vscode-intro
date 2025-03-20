#!/usr/bin/env python3


def look_smart(sentence):
    """
    This function replaces all the words in a sentence that are short (less than
    four letters) with "paradigm shifting" just to look smart.

    :param sentence: The phrase to make smarter
    """
    # Replace the code below with your own code
    smart_sentence = ""
    for word in sentence.split():
        if len(word) <= 3:
            smart_sentence += " paradigm shifting"
        else:
            smart_sentence = smart_sentence + " " + word

    return smart_sentence.strip()


# ------------------------------------------------------------------------------
# Tests: Do not make changes below this line
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    total_wrong = 0

    # Test 1
    ret = look_smart("This seems fun")
    if ret != "This seems paradigm shifting":
        print(f'Test 1: Uh oh, "This seems fun" returned {ret}')
        total_wrong = total_wrong + 1


    # Test 2
    ret = look_smart("Hi there Dan")
    if ret != "paradigm shifting there paradigm shifting":
        print(f'Test 2: Uh oh, "Hi there Dan" returned {ret}')
        total_wrong = total_wrong + 1


    # Test 3
    ret = look_smart("This sentence refuses words below length four")
    if ret != "This sentence refuses words below length four":
        print(f'Test 3: Uh oh, "This sentence refuses words below length four" returned {ret}')
        total_wrong = total_wrong + 1


    # Test 4
    ret = look_smart("yo")
    if ret != "paradigm shifting":
        print(f'Test 4: Uh oh, "yo" returned {ret}')
        total_wrong = total_wrong + 1


    # Test 5
    ret = look_smart("encyclopedia")
    if ret != "encyclopedia":
        print(f'Test 5: Uh oh, "encyclopedia" returned {ret}')
        total_wrong = total_wrong + 1


    if total_wrong == 0:
        print("Overall: Woohoo! All tests have been passed for Problem 8!")
    else:
        print("Overall: There's still work to do!")
