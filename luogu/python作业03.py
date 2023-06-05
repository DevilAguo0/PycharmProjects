import random
list1 = []
i = 0
while i < 10:
    a = random.randint(1, 100)
    list1.append(a)
    i += 1
print(list1)
person = int(input("请输入任意一个数字："))
list1.append(person)
print(list1)
list2 = set(list1)
print(list2)
a = sorted(list2)
print(a)
