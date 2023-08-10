from seasons import minutes

def test_input():
    assert minutes("2022-08-10") == "Five hundred twenty-five thousand, six hundred minutes"
    assert minutes("")