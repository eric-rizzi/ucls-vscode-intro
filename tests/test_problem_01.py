from problems.problem_01 import add_length_of_strings


def test_add_two_integers_1() -> None:
    assert add_length_of_strings("hi", "there") == 7


def test_add_two_integers_2() -> None:
    assert add_length_of_strings("", "") == 0


def test_add_two_integers_3() -> None:
    assert add_length_of_strings("go!", "lab!") == 7
