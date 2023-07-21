from fuel import convert
from fuel import gauge
import pytest

def test_exception():
    with pytest.raises(ZeroDivisionError):
        convert("9/0")
    with pytest.raises(ValueError):
        convert("9/4")

def test_convert():
    assert convert("9/10") == 90
    assert convert("1/4") == 25

def test_gauge():
    assert gauge(10) == "10%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"