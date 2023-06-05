#  4、有一个数列，其前3项分别为1、2、3，从第四项开始，每项均为其相邻的前三项之和的1/2
#  ，问：该数列从第几项开始，其数值超过1200？

num_list = [1, 2, 3]
i = 0
while i < 100:
    numadd = (num_list[-1] + num_list[-2] + num_list[-3]) * 0.5
    num_list.append(numadd)
    if numadd > 1200:
        break
    # print(num_list)
    i += 1
    # if numadd > 1200:
    #     print(i)

print("该数列是从第{}项开始，其数值开始超过1200的".format(num_list.index(numadd)))

