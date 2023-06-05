import random

while True:
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    a = random.sample(num_list, 3)
    del num_list[num_list.index(a[0])], num_list[num_list.index(a[1])], \
        num_list[num_list.index(a[2])]
    b = random.sample(num_list, 3)
    del num_list[num_list.index(b[0])], num_list[num_list.index(b[1])], \
        num_list[num_list.index(b[2])]
    c = num_list
    a1 = random.choice(a)
    a.remove(a1)
    a2 = random.choice(a)
    a.remove(a2)
    a3 = a[0]
    a = a1 * 100 + a2 * 10 + a3
    b1 = random.choice(b)
    b.remove(b1)
    b2 = random.choice(b)
    b.remove(b2)
    b3 = b[0]
    b = b1 * 100 + b2 * 10 + b3
    c1 = random.choice(c)
    c.remove(c1)
    c2 = random.choice(c)
    c.remove(c2)
    c3 = c[0]
    c = c1 * 100 + c2 * 10 + c1
    if a / b / c == 1 / 2 / 3:
        print(a, b, c)
    else:
        continue

# i = 0
# while i < 3:
#     random_num = random.randint(1, 3)
#     if random_num == 1:
#         a1 = int(a[0]) * 100
#         b1 = int(b[0]) * 100
#         c1 = int(c[0]) * 100
#     elif random_num == 2:
#         a2 = int(a[1]) * 10
#         b2 = int(b[1]) * 10
#         c2 = int(c[1]) * 10
#     else:
#         a3 = int(a[2])
#         b3 = int(b[2])
#         c3 = int(c[2])
#         i += 1
#         print(a1)
#         print(a2)
#         print(a3)
# a = a1 + a2 + a3
# b = b1 + b2 + b3
# c = c1 + c2 + c3
# if a / b / c == 1 / 2 / 3:
#     print(a, b, c)

# b = random.sample(, 3)
# c = num_list - a - b
# print(a)
# print(b)
# print(c)


