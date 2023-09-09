# def gen():
#     x, y = 1, 2
#     yield (x, y)
#     x += 1
#     yield (x, y)


# g = gen()
# print(next(g))
# print(next(g))


# string = "Yashi"
# # printing the string in reverse order
# li = list(string[i] for i in range(len(string) - 1, -1, -1))
# print(li)


# def mul(x, y):
#     yield (x * y)


# lst = range(10)
# ans = 1
# for id in range(len(lst) - 1):
#     next()


# *_, last = (x * x for x in range(10))

# from itertools import accumulate
# from operator import mul
# lst = [1, 4, 5, 6]
# lst = []
# ans = 1 / 0 if len(lst) else 1
# print(ans)


# *_, ans = accumulate(lst, mul) if len(lst) else (None, 1)
# print(ans)

def for_loop_iter_prod_2(lst):
    it = iter(lst)
    ans = next(it, 1)
    for _ in range(len(it)):
        print(ans)
        ans *= next(it)
    return ans

lst = [1,2,3,4,6]
for_loop_iter_prod_2(lst)