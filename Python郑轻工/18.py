# n=int(input())
# num=input().split(",")
# num=list(num)
# print(num)
# num=num.remove(num[0])
# print(type(num))
# num_list=[]
# num_list_ji=[]
# k=1
# for i in num:
#     i = int(i)
#     num_list.append(i)
# for i in num_list:
#     if i % 2!=0:
#         num_list_ji.append(i)
# print(num_list_ji)
# for i in num_list_ji:
#     k=i*k
# print(k)

num = input().split()
num_list=[]
result=1
for i in num:
    num_list.append(int(i))
num_list.remove(num_list[0])
for i in num_list:
    if i%2!=0:
        result=result*i
print(result)
