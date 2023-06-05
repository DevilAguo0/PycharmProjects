a = list(range(1, 11))
b = [x * x for x in range(1, 11) if x % 2 == 0]
c = [m + n for m in "xyz" for n in "abc"]
print(a)
print(b)
print(c)
import os

d = [d for d in os.listdir("/Users/wevilaguo")]
print(d)

dict1 = {"name": "guoshuaihao", "age": 18, "QQ": 23457678}
for ite, con in dict1.items():
    print(ite, ":", con)
e = [ite +":"+str(con) for ite, con in dict1.items()]
print(e)
x="xyz"
y=123
print(isinstance(x,str))
print(isinstance(y,str))














with open("/Users/wevilaguo/Desktop/python.txt") as file:
    filer = file.read()
filer.lower()
print(filer.lower())
print(filer.upper())
print(filer.capitalize())
print(filer.title())