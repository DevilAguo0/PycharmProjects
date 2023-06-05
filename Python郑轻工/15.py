n,capital=input().split()
n=int(n)
capital=float(capital)
result=capital*1.0225**n
print("{:.6f}".format(result))