"""
https://stackoverflow.com/questions/2104782/returning-the-product-of-a-list

https://stackoverflow.com/a/55297341/3057377

"""

import math
from functools import reduce
from itertools import accumulate
from operator import mul

import numpy
import perfplot


def reduce_lambda_prod(lst):
    ans = reduce(lambda x, y: x * y, lst)
    return ans


def reduce_mul_prod(lst):
    ans = reduce(mul, lst)
    return ans


def forloop_prod(lst):
    ans = 1
    for elem in lst:
        ans *= elem
    return ans


def numpy_prod(lst):
    ans = numpy.prod(lst)
    return ans


def math_prod(lst):
    ans = math.prod(lst)
    return ans


def itertools_accumulate_1_prod(lst):
    for ans in accumulate(lst, mul):
        pass
    return ans


def itertools_accumulate_2_prod(lst):
    ans = list(accumulate(lst, lambda x, y: x * y))[-1]
    return ans


def while_prod(lst):
    ans = 1
    i = 0
    while i < len(lst):
        ans *= lst[i]
        i += 1
    return ans


def lambda_prod(lst):
    ans = [j := (lambda c, i: i * j if c else i)(c, i) for c, i in enumerate(lst)][-1]
    return ans


b = perfplot.bench(
    setup=numpy.random.rand,
    kernels=[
        lambda_prod,
        while_prod,
        itertools_accumulate_2_prod,
        reduce_lambda_prod,
        itertools_accumulate_1_prod,
        forloop_prod,
        reduce_mul_prod,
        math_prod,
        numpy_prod,
    ],
    n_range=[10**k for k in range(0, 5)],
    xlabel="len(a)",
)
b.save("out.png")
# b.show()
