from twttr import shorten


def test_twitter():
    assert shorten("Twitter") == "Twttr"


def test_lowercase():
    assert shorten("twitter") == "twttr"


def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"


def test_numbers_preserved():
    assert shorten("h3ll0") == "h3ll0"


def test_punctuation():
    assert shorten("hello!") == "hll!"


def test_empty_string():
    assert shorten("") == ""
