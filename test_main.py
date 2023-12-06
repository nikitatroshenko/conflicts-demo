from main import (
    scalar_product,
    new_replicated_vector,
    new_vector,
    dot_product,
)


def test_scalar_product():
    input = [1, 2, 3, 4]
    scalar = 2
    expected = [2, 4, 6, 8]

    actual = scalar_product(input, scalar)
    assert actual == expected


def test_new_replicated_vector():
    expected = [1, 1, 1, 1]

    actual = new_replicated_vector(4, 1)
    assert actual == expected


def test_new_vector():
    expected = [1, 2, 3, 4]

    actual = new_vector(1, 2, 3, 4)
    assert actual == expected


def test_dot_product():
    lhs = [1, 2, 3, 4]
    rhs = [1, 2, 3, 4]
    expected = 30

    actual = dot_product(lhs, rhs)
    assert actual == expected
