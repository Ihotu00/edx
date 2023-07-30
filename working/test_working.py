from working import convert
import pytest

def test_format():
    with pytest.raises(ValueError):
        convert("12 - 14")

def test_time():
    with pytest.raises(ValueError):
        convert("12:60 AM to 13:00 PM")

def test_minutes():
    assert convert("9:00 AM to 9:30 PM") == "09:00 to 21:30"
    assert convert("10 PM to 9 AM") == "22:00 to 09:00"