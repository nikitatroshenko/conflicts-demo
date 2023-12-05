from functools import reduce
import operator
from typing import List

def scalar_product(values: List[int], scalar: int) -> List[int]:
    result = []
    for value in values:
        result.append(value * scalar)
    return result


def new_replicated_vector(size: int, init_value: int) -> List[int]:
    return [init_value] * size


def new_vector(*values: str) -> List[int]:
    return [int(v) for v in values]


def dot_product(lhs: List[int], rhs: List[int]) -> int:
    assert len(lhs) == len(rhs)
    return reduce(operator.add, [a * b for a, b in zip(lhs, rhs)])


def get_long_int_arg(argv: List[str], argname: str) -> int:
    i = argv.index(argname)
    value = argv[i + 1]
    argv.pop(i + 1)
    argv.pop(i)
    return int(value)


def get_scalar(argv: List[str]) -> int:
    return get_long_int_arg("--scalar")


def get_size(argv: List[str]) -> int:
    return get_long_int_arg("--size")


def get_init_value(argv: List[str]) -> int:
    return get_long_int_arg("--init-value")


if __name__ == "__main__":
    import sys

    _size = get_size(sys.argv)
    _init_value = get_init_value(sys.argv)
    _scalar = get_scalar(sys.argv)
    _vector = new_vector(*sys.argv[1:])

    vect_1 = new_replicated_vector(_size, _init_value)
    vect_2 = scalar_product(_vector, _scalar)
    print(dot_product(vect_1, vect_2))
