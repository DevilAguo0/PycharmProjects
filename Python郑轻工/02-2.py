n = int(input())
num = input().split()
num_nu = []
for i in num:
    i = int(i)
    num_nu.append(i)
num_nu = set(num_nu)
num_nu = list(num_nu)
num_nu.sort()
print(len(num_nu))
for i in num_nu:
    print(i, end=" ")
