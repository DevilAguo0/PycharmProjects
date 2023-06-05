namelist = ["zhangsan", "lisi", "wangwu", "zhaoyun"]
numberlist = [1, 2, 3, 5, 6, 7, 70]
tem_list = ["猴哥", "八届", "沙湿地"]
namelist.append("lixiaoer")
print(namelist.index("zhangsan"))
namelist[0] = "wangsan"
namelist.insert(2, "lihuo")
namelist.extend(tem_list)
namelist.remove("wangsan")
# namelist.clear()
# namelist.pop(3)
namelist.pop()
del namelist[0]

print(namelist)
# print(len(namelist))
# count = namelist.count("猴哥")
# print(count)
#namelist.sort()
#namelist.sort(reverse=True)
# namelist.reverse()
# numberlist.sort(reverse=True)
#
for my_name in namelist:
    print("我的名字是{}".format(my_name))
