num = 10


def demo1():
    global num
    num = 99
    print(num)


def demo2():
    print(num)


demo1()
demo2()
