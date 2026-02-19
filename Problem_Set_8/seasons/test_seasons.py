from seasons import calculate_minutes
from seasons import convert_to_words
import pytest


def test_valid_cases():
    assert convert_to_words(0) == "Zero minutes"
    assert convert_to_words(1) == "One minutes"
    assert convert_to_words(1440) == "One thousand, four hundred forty minutes"
    assert convert_to_words(1000) == "One thousand minutes"
    assert convert_to_words(1000000) == "One million minutes"


def test_small_numbers():
    assert convert_to_words(0) == "Zero minutes"
    assert convert_to_words(1) == "One minutes"
    assert convert_to_words(2) == "Two minutes"
    assert convert_to_words(59) == "Fifty-nine minutes"
    assert convert_to_words(60) == "Sixty minutes"


def test_large_numbers():
    assert convert_to_words(1440) == "One thousand, four hundred forty minutes"
    assert (
        convert_to_words(525600)
        == "Five hundred twenty-five thousand, six hundred minutes"
    )
    assert convert_to_words(1000000) == "One million minutes"
    assert (
        convert_to_words(999999)
        == "Nine hundred ninety-nine thousand, nine hundred ninety-nine minutes"
    )
    assert (
        convert_to_words(777777)
        == "Seven hundred seventy-seven thousand, seven hundred seventy-seven minutes"
    )


def test_no_and():
    assert " and " not in convert_to_words(111).lower()
    assert " and " not in convert_to_words(222).lower()
    assert " and " not in convert_to_words(333).lower()
    assert " and " not in convert_to_words(141253).lower()
    assert " and " not in convert_to_words(4263754).lower()


def test_capitalization():
    assert convert_to_words(111)[0].isupper()
    assert convert_to_words(222)[0].isupper()
    assert convert_to_words(333)[0].isupper()
    assert convert_to_words(10043859351)[0].isupper()
    assert convert_to_words(99999999)[0].isupper()


def test_suffix():
    assert convert_to_words(3256).endswith(" minutes")
    assert convert_to_words(5446).endswith(" minutes")
    assert convert_to_words(87659).endswith(" minutes")
    assert convert_to_words(34637).endswith(" minutes")
    assert convert_to_words(1242136658).endswith(" minutes")
