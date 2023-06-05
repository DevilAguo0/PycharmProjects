def demo(num):
    print(num)
    if num == 1:
        return
    demo(num - 1)


demo(3)
