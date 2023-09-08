from jar import Jar
import pytest

def test_init():
    with pytest.raises(ValueError):
        init(Jar(-10))

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(7)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert 