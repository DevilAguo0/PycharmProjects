import random
passwd = ""
for i in range(6):
    a = random.randint(1, 3)
    if a == 1:
        x = chr(random.randint(ord("a"), ord("z")))
    elif a == 2:
        x = chr(random.randint(ord("A"), ord("Z")))
    else:
        x = random.randint(1, 9)
    passwd = passwd + str(x)
print(passwd)
