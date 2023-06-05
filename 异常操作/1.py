try:
    for i in 2:
        print(i)
except TypeError as e:
    print(f'异常原因:{e}')