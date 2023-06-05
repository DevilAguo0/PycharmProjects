# 找出1与100之间的全部“同构数”。“同构数”是这样一种数，它出现在它的平方数的右端。
# 例如，5的平方是25,5是25中右端的数，5就是同构数，25也是一个同构数，它的平方是625。
#
for i in range(1, 101):
    a = str(i ** 2)
    j = str(i)
    b = len(j)
    flag = True
    for c in range(-1, -b - 1, -1):
        if a[c] != j[c]:
            flag = False
            break
    if flag is True:
        print(i, a)
