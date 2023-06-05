a, b, c, d = input().split()
a = float(a)
b = float(b)
c = float(c)
d = float(d)
distance = ((c-a)**2+(d-b)**2)**0.5
print('{:.2f}'.format(distance))