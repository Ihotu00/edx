import twttr

def test_lower():
    assert twttr.shorten("abcdeiou") == "bcd"

def test_upper():
    assert twttr.shorten("ABCDEIOU") == "BCD"

def test_punctuation():
    assert twttr.shorten("WHAT.,!? 23") == "WHT.,!? 23"
