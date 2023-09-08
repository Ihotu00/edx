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
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert deposite.self.size == 1
    jar.deposit(5)
    assert deposite.self.size == 6
    with pytest.raises(ValueError):
        jar.deposit(10)

def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(3)
    assert withdraw.self.size == 7
    with pytest.raises(ValueError):
        jar.withdraw(10)
