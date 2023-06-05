a1, a2, n = input("").split()
a1 = int(a1)
a2 = int(a2)
n = int(n)
d = a2-a1
# an = d * (n - 1) + a1
# s = int((an + a1) * n / 2)
Sn = n * a1 + n * (n - 1) * d / 2
Sn = int(Sn)
print(Sn)
