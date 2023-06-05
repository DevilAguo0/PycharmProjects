# def demo(num, *swe, **person):
#     print(num)
#     print(swe)
#     print(person)
#


#
# demo(12, 3, 5, 5, 6, name="xiaomi", age=15)

#  args 演练
def sums(*args):
    num = 0
    for n in args:
        num += n
    return num


print(sums(1, 3, 4, 5, 6, 7))


#  元素的拆包


def dev(*args, **kwargs):
    print(args)
    print(kwargs)


# dev(1, 2, 3, name="xiaomi", age=18)
lists = [1, 3, 5, 5]
dicts = {"name": "xiaomi", "age": 18}
dev(*lists, **dicts)
