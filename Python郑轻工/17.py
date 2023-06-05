a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
if a**2+b**2==c**2:
    print("yes")
elif a**2+c**2==b**2:
    print("yes")
elif b**2+c**2==a**2:
    print("yes")
else:
    print("no")