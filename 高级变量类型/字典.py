# xiaoming = {"name": "xiaoming",
#             "age": 35,
#             "gender": True,
#             "height": 175,
#             "weight": 75.5}
# print(xiaoming)
# xiaowu = {"name": "xiaowu",
#           "age": 24,
#           "gender": True,
#           "height": 183,
#           "wight": 175}
# print(xiaowu)
# xiaohong = {"name": "Xiaoping",
#             "age": 34,
#             "gender": False,
#             "weight": 89,
#             "height": 161}
# print(xiaohong)
# guoshuaihao = {"name": "guoshuiahao",
#                "age": 23,
#                "gender": True,
#                "height": 175,
#                "weight": 85}
# print(guoshuaihao)
xiaoming_dict = {"name": "xiaoming",
                 "age": 18,
                 "gender": True}
#  取值
print(xiaoming_dict["name"])
print(xiaoming_dict["age"])
print(xiaoming_dict["gender"])
#新增/修改，key不存在就新增，key存在就修改
xiaoming_dict["height"] = 185
xiaoming_dict["name"] = "xiaowang"
#  删除，不存在会报错
xiaoming_dict.pop("name")
#  统计键值对的数量
print(len(xiaoming_dict))
#  合并字典
tem_dict = {"xueli": "benke",
            "age": 45}
xiaoming_dict.update(tem_dict)

#  清空字典
xiaoming_dict.clear()
print(xiaoming_dict)