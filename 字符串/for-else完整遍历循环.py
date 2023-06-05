stu_list = [
    {"name": "xiaomei"},
    {"name": "xiaohong"}
]
find_name = "xiaohang"
for stu_info in stu_list:
    # print(stu_info)
    if stu_info["name"] == find_name:
        print("找到了{}".format(stu_info["name"]))
        break
else:
    print("没有找到{}".format(stu_info["name"]))
