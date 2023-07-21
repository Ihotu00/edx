from bank import value

def test_hello():
    assert value("Hello James") == 0

def test_h():
    assert value("How are you") == 20

def test_other():
    assert value("What's up?") == 100