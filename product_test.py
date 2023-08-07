"""
https://stackoverflow.com/questions/2104782/returning-the-product-of-a-list

https://stackoverflow.com/a/55297341/3057377

# Empty product
https://en.wikipedia.org/wiki/Empty_product

"""

import math
import sys
from functools import reduce
from itertools import accumulate
from operator import mul

import numpy as np
import perfplot


def mathexp_prod(lst):
    ans = math.exp(sum(map(math.log, lst)))
    return ans


def reduce_lambda_prod(lst):
    ans = reduce(lambda x, y: x * y, lst, 1)
    return ans


def reduce_mul_prod(lst):
    ans = reduce(mul, lst, 1)
    return ans


def forloop_prod(lst):
    ans = lst[0] if len(lst) else 1
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
    if not len(lst):
        return 1
    for ans in accumulate(lst, mul):
        pass
    return ans


def itertools_accumulate_prod_2(lst):
    if not len(lst):
        return 1
    *_, ans = accumulate(lst, mul)
    return ans


def while_prod(lst):
    ans = lst[0] if len(lst) else 1
    i = 1
    imax = len(lst)
    while i < imax:
        ans *= lst[i]
        i += 1
    return ans


def list_comprehension_prod(lst):
    ans = (lambda lst, j=1: [j := i * j for i in lst][-1])(lst) if len(lst) else 1
    return ans


def eval_prod(lst):
    if not len(lst):
        return 1
    ans = eval("*".join(str(item) for item in lst))
    return ans


if __name__ == "__main__":
    exp_max = 5
    # Increase recursion limit for `eval_prod()` to work.
    sys.setrecursionlimit(10**exp_max)
    b = perfplot.bench(
        setup=np.random.rand,
        kernels=[
            eval_prod,
            while_prod,
            reduce_lambda_prod,
            mathexp_prod,
            list_comprehension_prod,
            itertools_accumulate_prod_1,
            itertools_accumulate_prod_2,
            forloop_prod,
            reduce_mul_prod,
            math_prod,
            numpy_prod,
        ],
        n_range=[10**k for k in range(0, exp_max + 1)],
    )
    b.save(
        "out.png",
        logx=True,
        logy=True,
    )
    # b.show()
