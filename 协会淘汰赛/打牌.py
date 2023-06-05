def jie_cheng(num):
    if num==1:
        return 1
    else:
        return num*jie_cheng(num-1)


while True:

    a=int(input())
    result = jie_cheng(a)/jie_cheng(a-2)*0.5 +1
    print(result)
