from fuel import convert, gauge
import pytest


def test_valid_fractions():
    assert convert("4/4") == 100
    assert convert("3/4") == 75
    assert convert("2/4") == 50
    assert convert("1/4") == 25
    assert convert("3/3") == 100
    assert convert("2/3") == 67
    assert convert("1/3") == 33


def test_invalid_fractions():
    with pytest.raises(ValueError):
        convert("10/4")
    with pytest.raises(ValueError):
        convert("a/b")
    with pytest.raises(ValueError):
        convert("3/x")
    with pytest.raises(ValueError):
        convert("x")
    with pytest.raises(ValueError):
        convert("-5/5")


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")
    with pytest.raises(ZeroDivisionError):
        convert("2/0")
    with pytest.raises(ZeroDivisionError):
        convert("0/0")


def test_gauge_E():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_F():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_percentage():
    assert gauge(50) == "50%"
    assert gauge(60) == "60%"
