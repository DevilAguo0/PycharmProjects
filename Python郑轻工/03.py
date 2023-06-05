n = int(input())
num=[]
for i in range(n+1):
    for k in range(n+1):
        if i*k==n:


            num.append(k)
            num.append(i)
print(max(num))

