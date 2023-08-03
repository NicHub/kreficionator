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
prod = lambda l: l[0] if len(l) == 1 else l[0] * prod(l[1:])
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
        lambda y: lambda l: l[0] if len(l) == 1 else l[0] * y(y)(l[1:])
    )
)(None)
prod = lambda l: [(lambda l0, ln, i: print(i))(l[0], l[1:], i) for i in l]
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




def fibo (n):
    return n if n <=1 else (fibo(n-1) + fibo(n-2))

nums = [1, 2, 3, 4, 5, 6]
res = [fibo(x) for x in nums]
print(res)
# [1, 1, 2, 3, 5,

[y for x in nums if (y:=fibo(x)) % 2 == 0]
# [2, 8]




from itertools import accumulate
from operator import mul

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
