#!/usr/bin/env python3


def roller_coaster_rules(height_ft, height_in):
    """
    This function is in charge of determining whether someone is allowed onto a
    roller coaster. If they are greater than 5'6", then the value "allowed"
    should be returned. Otherwise, "nope" should be returned.

    Hints:
    - If they're 4 feet tall (or shorter), inches don't matter: they're too short.
    - If they're 6 feet tall (or taller), inches don't matter: they're allowed.
    - Only when they're 5 feet tall do we actually have to check the inches part

    :param height_ft: The height of the patron in feet
    :param height_in: The remaining inches of the patron's height
    """
    if height_ft >= 6:
        return "allowed"
    elif height_ft <= 4:
        return "nope"
    elif height_in >= 6:
        return "allowed"
    else:
        return "nope"


# ------------------------------------------------------------------------------
# Tests: Do not make changes below this line
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    total_wrong = 0

    # Test 1
    ret = roller_coaster_rules(4, 1)
    if ret != "nope":
        print(f"Test 1: Uh oh, (4, 1) returned {ret}")
        total_wrong = total_wrong + 1


    # Test 2
    ret = roller_coaster_rules(4, 11)
    if ret != "nope":
        print(f"Test 2: Uh oh, (4, 11) returned {ret}")
        total_wrong = total_wrong + 1


    # Test 3
    ret = roller_coaster_rules(5, 2)
    if ret != "nope":
        print(f"Test 3: Uh oh, (5, 2) returned {ret}")
        total_wrong = total_wrong + 1


    # Test 4
    ret = roller_coaster_rules(5, 5)
    if ret != "nope":
        print(f"Test 4: Uh oh, (5, 5) returned {ret}")
        total_wrong = total_wrong + 1


    # Test 5
    ret = roller_coaster_rules(5, 6)
    if ret != "allowed":
        print(f"Test 5: Uh oh, (5, 6) returned {ret}")
        total_wrong = total_wrong + 1


    # Test 6
    ret = roller_coaster_rules(5, 7)
    if ret != "allowed":
        print(f"Test 6: Uh oh, (5, 7) returned {ret}")
        total_wrong = total_wrong + 1


    # Test 7
    ret = roller_coaster_rules(6, 1)
    if ret != "allowed":
        print(f"Test 7: Uh oh, (6, 1) returned {ret}")
        total_wrong = total_wrong + 1


    # Test 8
    ret = roller_coaster_rules(6, 11)
    if ret != "allowed":
        print(f"Test 8: Uh oh, (6, 11) returned {ret}")
        total_wrong = total_wrong + 1


    if total_wrong == 0:
        print("Overall: Woohoo! All tests have been passed for Problem 4!")
    else:
        print("Overall: There's still work to do!")
