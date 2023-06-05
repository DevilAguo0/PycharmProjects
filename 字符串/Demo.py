# # str1 = '我的外号是"大西瓜"'
# # print(str1)
# # for char in str1:
# #     print(char)
# # print(len(str1))
# # # print(str1.count("haha"))
# # # print(str1.index("haha"))
# # str = "123"
# # # print(str.find("llo"))
# # # print(str.find("abc"))
# # # #print(str.index("llo"))
# # # # print(str.index("abc"))
# # # print(str.startswith("he"))
# # # print(str.endswith("a"))
# # # print(str)
# # # print(str.replace("python", "world"))
# # print(str.isdecimal())
# poem = ["将进酒",
#         "\t\n天生我材必有用",
#         "千金散盡還復來\t\n",
#         "烹羊宰牛且為樂",
#         "會須一飲三百杯"]
# for poem_str in poem:
#     # print("|{}|".format(poem_str.center(10, " ")))
#     print("|%s|" % poem_str.strip().center(10, " "))
# #  这段代码有问题

poem2_str = "将进酒天生我 材必有 用千金散 盡 還復來   烹羊  宰牛且為  樂會須一 飲 三 百杯"
# print(poem2_str.split())
result = " ".join(poem2_str.split())
print(result)
