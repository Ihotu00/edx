from seasons import minutes
import pytest

def test_input():
    with pytest.raises(SystemExit):
        minutes("Feb 12 1999")

# def test_output():
#     assert minutes("2022-08-10") == "Five hundred twenty-five thousand, six hundred minutes"
