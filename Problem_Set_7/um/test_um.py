from um import count
import pytest


def test_basic_valid_cases():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("UM") == 1
    assert count("um um") == 2
    assert count("um, um, um, um, um") == 5


def test_inside_other_words():
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("umbrella") == 0
    assert count("humble") == 0
    assert count("assume") == 0


def test_punctuation_boundaries():
    assert count("um?") == 1
    assert count("um.") == 1
    assert count("um,") == 1
    assert count("(um)") == 1
    assert count("um!") == 1


def test_mixed_sentences():
    assert count("hello, um, world") == 1
    assert count("Um... I think um this works") == 2
    assert count("Um, um, um!") == 3
    assert count("Um... Hi!") == 1
    assert count("um, um, um, Hi") == 3


def test_edge_positions():
    assert count("um hello") == 1
    assert count("hello um") == 1
    assert count("um") == 1
    assert count("UM, uM, Um") == 3
    assert count("UmUmuMuMmmU") == 0
    assert count("um...um") == 2
    assert count(" um ") == 1
