












def list_comprehension_prod(lst):
    ans = (lambda lst, j=1: [j := i * j for i in lst][-1])(lst) if len(lst) else 1
    return ans


lst = [2, 3, 4, 5]


def t(lst):
    ans = [elem * i for i in lst[1:] for elem in [lst[0]]][-1] if len(lst) else 1
    return ans


print(lst)
print(t(lst))
