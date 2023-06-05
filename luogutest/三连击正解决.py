for i in range(122, 333):
    j = str(2 * i)
    k = str(3 * i)
    i = str(i)
    a = {i[0], i[1], i[2], j[0], j[1], j[2], k[0], k[1], k[2]}
    if len(a) == 9 and ("0" not in a):
        print(int(i), int(j), int(k))
