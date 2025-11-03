from algo import edit_distance


def test_edit_distance_example():
    word1 = "kitten"
    word2 = "sitting"
    assert edit_distance(word1, word2) == 3

def test_same_word():
    word1 = "hello"
    word2 = "hello"
    assert edit_distance(word1, word2) == 0

def test_single_char():
    word1 = "a"
    word2 = "a"
    assert edit_distance(word1, word2) == 0

def test_diff_char():
    word1 = "a"
    word2 = "b"
    assert edit_distance(word1, word2) == 1

def test_diff_start_char():
    word1 = "accc"
    word2 = "bccc"
    assert edit_distance(word1, word2) == 1

def test_empty_string():
    word1 = ""
    word2 = "cat"
    assert edit_distance(word1, word2) == 3