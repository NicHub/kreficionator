from itertools import accumulate
from operator import mul

phonemes = (
    ("k", "c", "ch"),
    ("r"),
    ("ai", "è"),
    ("f", "ff", "ph"),
    ("i", "y"),
    ("ss", "c", "t", "sc"),
    ("i"),
    ("on", "ond", "ont"),
)


list2 = [1, 2, 3]
prod = lambda _l: _l[0] if len(_l) == 1 else _l[0] * prod(_l[1:])  # noqa: E731
p = prod(list2)
print(p)


def product(lst):
    p = 1
    for i in lst:
        p *= i
    return p


product(list2)


# Exemple d'utilisation :
my_list = [1, 2, 3, 4, 5]
result = prod(my_list)
print(result)


list1 = [len(row) for row in phonemes]
prod = (
    lambda f: (lambda x: x(x))(
        lambda y: lambda _l: _l[0] if len(_l) == 1 else _l[0] * y(y)(_l[1:])
    )
)(None)
prod = lambda _l: [  # noqa: E731
    (lambda l0, ln, i: print(i))(_l[0], _l[1:], i) for i in _l
]
p = prod(list1)
print(p)


# Return double of n
def addition(n):
    return n + n


# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
result = map(addition, numbers)
print(list(result))


def fibo(n):
    return n if n <= 1 else (fibo(n - 1) + fibo(n - 2))


nums = [1, 2, 3, 4, 5, 6]
res = [fibo(x) for x in nums]
print(res)
# [1, 1, 2, 3, 5,

[y for x in nums if (y := fibo(x)) % 2 == 0]
# [2, 8]


def itertools_accumulate_0(lst):
    for value in accumulate(lst, mul):
        pass
    return value


def itertools_accumulate_1(lst):
    for value in accumulate(lst, lambda x, y: x * y):
        pass
    return value


def itertools_accumulate_2(lst):
    return list(accumulate(lst, lambda x, y: x * y))[-1]


itertools_accumulate_2(list1)
