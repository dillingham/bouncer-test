from slugkit import slugify


def test_basic():
    assert slugify("Héllo World") == "hello-world"


def test_custom_separator():
    assert slugify("a b c", sep="_") == "a_b_c"


def test_max_length():
    assert slugify("abcdef", max_length=3) == "abc"
