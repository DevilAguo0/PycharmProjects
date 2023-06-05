num = int(input("请输入任意一个三位数："))
a = num // 100
b = (num - a * 100) // 10
c = num % 10
num_list = [a, b, c]
max_num = max(num_list)
min_num = min(num_list)
num_list.remove(max_num)
num_list.remove(min_num)
mindd_num = num_list[0]
restlt = max_num * 100 + mindd_num * 10 + min_num
print("重新排列后最大的整数是:{}".format(restlt))
