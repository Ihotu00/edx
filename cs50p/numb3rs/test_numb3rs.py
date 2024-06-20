from numb3rs import validate

def test_format():
    assert validate("1.2.3.4.5") == False
    assert validate("1.2.3.4") == True

def test_range():
    assert validate("5.300.277.313") == False
    assert validate("500.3.277.313") == False
    assert validate("500.300.2.313") == False
    assert validate("500.300.277.3") == False
    assert validate("255.190.2.3") == True