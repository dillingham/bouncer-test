from slugkit import slugify


def test_basic():
    assert slugify("Héllo World") == "hello-world"


def test_custom_separator():
    assert slugify("a b c", sep="_") == "a_b_c"


def test_max_length():
    assert slugify("abcdef", max_length=3) == "abc"


def test_no_trailing_separator_from_punctuation():
    assert slugify("Hello, World!") == "hello-world"


def test_no_leading_separator():
    assert slugify("  --Hello") == "hello"


def test_truncation_does_not_end_with_separator():
    assert slugify("hello world", max_length=6) == "hello"
