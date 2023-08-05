"""
https://stackoverflow.com/questions/2104782/returning-the-product-of-a-list

https://stackoverflow.com/a/55297341/3057377

"""

import math
import sys
from functools import reduce
from itertools import accumulate
from operator import mul

import numpy as np
import perfplot


def sanity_checks(lst):
    """___"""
    _l = len(lst)
    if _l == 0:
        ans = None
        return ans
    elif _l == 1:
        ans = lst[0]
        return ans
    ans = False
    return ans


def mathexp_prod(lst):
    """Return 1 if list is empty."""
    if not (ans := sanity_checks(lst)) is False:
        return ans
    ans = math.exp(sum(map(math.log, lst)))
    return ans


def reduce_lambda_prod(lst):
    """Return 1 if list is empty."""
    if not (ans := sanity_checks(lst)) is False:
        return ans
    ans = reduce(lambda x, y: x * y, lst, 1)
    return ans


def reduce_mul_prod(lst):
    """Return 1 if list is empty."""
    if not (ans := sanity_checks(lst)) is False:
        return ans
    ans = reduce(mul, lst, 1)
    return ans


def forloop_prod(lst):
    """Return None if list is empty."""
    if not (ans := sanity_checks(lst)) is False:
        return ans
    ans = lst[0]
    for elem in lst[1:]:
        ans *= elem
    return ans


def numpy_prod(lst):
    """Return 1 if list is empty."""
    if not (ans := sanity_checks(lst)) is False:
        return ans
    ans = np.prod(lst)
    return ans


def math_prod(lst):
    """Return 1 if list is empty."""
    if not (ans := sanity_checks(lst)) is False:
        return ans
    ans = math.prod(lst)
    return ans


def itertools_accumulate_prod_1(lst):
    """Fail if list is empty."""
    if not (ans := sanity_checks(lst)) is False:
        return ans
    for ans in accumulate(lst, mul):
        pass
    return ans


def itertools_accumulate_prod_2(lst):
    """Fail if list is empty."""
    if not (ans := sanity_checks(lst)) is False:
        return ans
    *_, ans = accumulate(lst, mul)
    return ans


def while_prod(lst):
    """Return None if list is empty."""
    ans = lst[0] if len(lst) else None
    i = 1
    while i < len(lst):
        ans *= lst[i]
        i += 1
    return ans


def lambda_prod_0(lst):
    """Fail if list is empty."""
    if not (ans := sanity_checks(lst)) is False:
        return ans
    prod = lambda l: l[0] if len(l) == 1 else l[0] * prod(l[1:])
    ans = prod(lst)
    return ans


def lambda_prod_1(lst):
    """Fail if list is empty."""
    if not (ans := sanity_checks(lst)) is False:
        return ans
    ans = [j := (lambda c, i: i * j if c else i)(c, i) for c, i in enumerate(lst)][-1]
    return ans


def lambda_prod_2(lst):
    """Fail if list is empty."""
    if not (ans := sanity_checks(lst)) is False:
        return ans
    ans = (lambda lst, j=1: [j := (lambda i: i * j)(i) for i in lst][-1])(lst)
    return ans


def eval_prod(lst):
    """Fail if list is empty."""
    if not (ans := sanity_checks(lst)) is False:
        return ans
    ans = eval("*".join(str(item) for item in lst))
    return ans


if __name__ == "__main__":
    exp_max = 4
    # Increase recursion limit for `eval_prod()` and `lambda_prod_0()` to work.
    sys.setrecursionlimit(2 * 10**exp_max)
    b = perfplot.bench(
        setup=np.random.rand,
        kernels=[
            lambda_prod_0,
            lambda_prod_1,
            lambda_prod_2,
            while_prod,
            reduce_lambda_prod,
            itertools_accumulate_prod_1,
            itertools_accumulate_prod_2,
            mathexp_prod,
            forloop_prod,
            reduce_mul_prod,
            math_prod,
            numpy_prod,
            eval_prod,
        ],
        n_range=[10**k for k in range(0, exp_max + 1)],
        xlabel="len(a)",
    )
    b.save("out.png")
    # b.show()
