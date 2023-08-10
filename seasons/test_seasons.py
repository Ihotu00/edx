from seasons import minutes
import pytest

def test_input():
    assert minutes("2022-08-10") == "Five hundred twenty-five thousand, six hundred minutes"
    pytest.raises(SystemExit)