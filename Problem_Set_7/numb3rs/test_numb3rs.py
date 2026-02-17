from numb3rs import validate


def test_clearly_valid_addresses():
    assert validate("192.168.1.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.4") == True


def test_numeric_range_violations():
    assert validate("256.100.100.100") == False
    assert validate("999.999.999.999") == False
    assert validate("300.1.1.1") == False
    assert validate("192.168.1.256") == False


def test_leading_zero_violations():
    assert validate("01.2.3.4") == False
    assert validate("192.168.01.1") == False
    assert validate("00.10.20.30") == False
    assert validate("00.02.023.05") == False


def test_structural_errors():
    assert validate("192.168.1") == False
    assert validate("192.168.1.1.5") == False
    assert validate("192..1.1") == False
    assert validate(".") == False
    assert validate("") == False


def test_non_numeric_content():
    assert validate("abc.def.ghi.jkl") == False
    assert validate("192.168.one.1") == False
    assert validate("192.168.-1.1") == False
    assert validate("192.168.1.a") == False
