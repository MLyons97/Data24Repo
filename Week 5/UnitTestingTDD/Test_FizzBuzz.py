from FizzBuzz import *


def test_div_check():
    assert div_check(10, 5)
    assert not div_check(11, 5)


def test_number_check():
    assert number_check(15, "FizzBuzz")
