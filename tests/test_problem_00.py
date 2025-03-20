from problems.problem_00 import add_two_integers


def test_add_two_integers_1() -> None:
    assert add_two_integers(5, 0) == 5


def test_add_two_integers_2() -> None:
    assert add_two_integers(5, 4) == 9


def test_add_two_integers_3() -> None:
    assert add_two_integers(-1, 8) == 7
