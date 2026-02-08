from bank import value


def test_hello_cases():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0


def test_h_cases():
    assert value("hi") == 20
    assert value("Hey") == 20
    assert value("How are you?") == 20


def test_other_cases():
    assert value("are you good?") == 100
    assert value("ARE YOU FINE?") == 100
    assert value("Are You Well?") == 100
