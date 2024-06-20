from um import count

def test_count():
    assert count("um happy uman um") == 2
    assert count("um happy uman") == 1
    assert count("Um um bum") == 2
