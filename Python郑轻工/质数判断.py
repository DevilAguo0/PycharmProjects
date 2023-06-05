a = int(input())
if a != 1:

    for i in range(a + 1):
        for k in range(i+1):

            if i % k == 0:
                print("是质数")
            else:
                print("不是质数")
    else:
        print("不是质数")
