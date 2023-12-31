from typing import List

def scalar_product(values: List[int], scalar: int) -> List[int]:
    result = []
    for value in values:
        result.append(value * scalar)
    return result


def new_replicated_vector(size: int, init_value: int) -> List[int]:
    result = []
    for _ in range(size):
        result.append(init_value)
    return result


def new_vector(*values: str) -> List[int]:
    result = []
    for value in values:
        result.append(int(value))
    return result


def dot_product(lhs: List[int], rhs: List[int]) -> int:
    assert len(lhs) == len(rhs)
    result = 0
    for i in range(len(lhs)):
        for j in range(len(rhs)):
            result += lhs[i] * rhs[j]
    return result


def get_scalar(argv: List[str]) -> int:
    i = argv.index("--scalar")
    scalar = argv[i + 1]
    argv.pop(i + 1)
    argv.pop(i)
    return int(scalar)


def get_size(argv: List[str]) -> int:
    i = argv.index("--size")
    scalar = argv[i + 1]
    argv.pop(i + 1)
    argv.pop(i)
    return int(scalar)


def get_init_value(argv: List[str]) -> int:
    i = argv.index("--init-value")
    scalar = argv[i + 1]
    argv.pop(i + 1)
    argv.pop(i)
    return int(scalar)


if __name__ == "__main__":
    import sys

    _size = get_size(sys.argv)
    _init_value = get_init_value(sys.argv)
    _scalar = get_scalar(sys.argv)
    _vector = new_vector(*sys.argv[1:])

    vect_1 = new_replicated_vector(_size, _init_value)
    vect_2 = scalar_product(_vector, _scalar)
    print(dot_product(vect_1, vect_2))
