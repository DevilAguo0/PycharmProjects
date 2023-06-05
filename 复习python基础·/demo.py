# import random
# random.randint
# from random import randint(1,100)
def fun(n):
    if n == 1 or n == 2:
        return n
    else:
        return fun(n - 1) + fun(n - 2)


print(fun(4))
