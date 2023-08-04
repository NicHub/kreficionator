"""
https://stackoverflow.com/questions/2104782/returning-the-product-of-a-list

https://stackoverflow.com/a/55297341/3057377

"""

import math
from functools import reduce
from itertools import accumulate
from operator import mul

import numpy as np
import perfplot


def mathexp_prod(lst):
    ans = math.exp(sum(map(math.log, lst)))
    return ans


def reduce_lambda_prod(lst):
    ans = reduce(lambda x, y: x * y, lst)
    return ans


def reduce_mul_prod(lst):
    ans = reduce(mul, lst)
    return ans


def forloop_prod(lst):
    ans = lst[0]
    for elem in lst[1:]:
        ans *= elem
    return ans


def numpy_prod(lst):
    ans = np.prod(lst)
    return ans


def math_prod(lst):
    ans = math.prod(lst)
    return ans


def itertools_accumulate_prod_1(lst):
    for ans in accumulate(lst, mul):
        pass
    return ans


def itertools_accumulate_prod_2(lst):
    ans = [_ for _ in accumulate(lst, mul)][-1]
    return ans


def while_prod(lst):
    ans = lst[0]
    i = 1
    while i < len(lst):
        ans *= lst[i]
        i += 1
    return ans


def lambda_prod_1(lst):
    ans = [j := (lambda c, i: i * j if c else i)(c, i) for c, i in enumerate(lst)][-1]
    return ans


def lambda_prod_2(lst):
    if len(lst) == 1:
        ans = lst[0]
    else:
        j = lst[0]
        ans = [j := (lambda i: i * j)(i) for i in lst[1:]][-1]
    return ans


if __name__ == "__main__":
    b = perfplot.bench(
        setup=np.random.rand,
        kernels=[
            lambda_prod_1,
            lambda_prod_2,
            while_prod,
            reduce_lambda_prod,
            itertools_accumulate_prod_2,
            mathexp_prod,
            itertools_accumulate_prod_1,
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
