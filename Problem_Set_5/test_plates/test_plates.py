from plates import is_valid


def test_valid_simple():
    assert is_valid("CS50")


def test_invalid_length():
    assert not is_valid("A")
    assert not is_valid("ABCDEFG")


def test_first_two_n():
    assert not is_valid("1ABC")
    assert not is_valid("A1")


def test_first_n_not_zero():
    assert not is_valid("CS05")


def test_no_letter_after_n():
    assert not is_valid("CS50A")


def test_no_special_characters():
    assert not is_valid("CS50!")
    assert not is_valid("CS 50")


def test_valid_edge_cases():
    assert is_valid("AA123")
    assert is_valid("ABCDEF")


def test_single_valid_min_length():
    assert is_valid("AB")


def test_n_end():
    assert is_valid("AB1")


def test_multiple_n():
    assert is_valid("AB123")
