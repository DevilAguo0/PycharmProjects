a=[[1,2],[3,4],[5,6]]
# for i in a:
#     for j in i:
#         print(j)
b=[j for i in a for j in i]#注意两个for的顺序
print(b)