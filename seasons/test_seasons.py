from seasons import minutes
import pytest

def test_input():
    with pytest.raises(SystemExit):
        minutes("Feb 12 1999")

