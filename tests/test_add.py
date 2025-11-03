from algo import add


def test_add_example():
    a = 3
    b = 3
    assert add(a, b) == 6

def test_add_non_duplicate():
    a = 3
    b = 4
    assert add(a, b) == 7