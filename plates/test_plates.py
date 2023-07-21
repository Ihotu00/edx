from plates import is_valid

def test_length():
    assert is_valid("c") == False
    assert is_valid("cascade") == False

def test_alpha():
    assert is_valid("12345") == False
    assert is_valid("1cas") == False
    assert is_valid("c2as") == False

def test_special():
    assert is_valid("case!") == False

def test_num():
    assert is_valid("ca12s") == False
    assert is_valid("cas02") == False
