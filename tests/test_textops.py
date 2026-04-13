from portfolio.textops import normalize_whitespace, reverse_words, word_frequencies


def test_normalize_whitespace():
    assert normalize_whitespace(" a\tb \n c ") == "a b c"


def test_reverse_words():
    assert reverse_words("one two three") == "three two one"


def test_word_frequencies():
    freq = word_frequencies("A a a b, b!")
    assert freq == {"a": 3, "b": 2}
