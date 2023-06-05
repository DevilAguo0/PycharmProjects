card_list = []


def show_menu():
    #  显示菜单
    print("*" * 50)
    print("欢迎使用【名片管理系统】v1.0")
    print("")
    print("1.新增名片")
    print("2.显示名片")
    print("3.搜索名片")
    print("")
    print("输入0，退出系统")
    print("*" * 50)


#  新增名片
def new_card():
    print("*" * 50)
    print("新增名片")

    #  提示用户输入详细信息
    print("请输入您的详细信息")
    name_str = input("请输入名字：")
    iphone_str = input("请输入电话：")
    qq_str = input("请输入QQ：")
    email_str = input("请输入邮箱：")

    #  建立一个字典
    card_dict = {"name": name_str,
                 "iphone": iphone_str,
                 "qq": qq_str,
                 "email": email_str
                 }
    #  把字典追加到列表中
    card_list.append(card_dict)
    print(card_list)
    #  提示用户输入信息成功
    print("{}已经输入成功！".format(card_dict["name"]))


#  显示名片
def show_card():
    print("*" * 50)
    print("显示所有名片")

    #  判断是否存在名片记录，如果没有提示用户返回
    if len(card_list) == 0:
        print("当前没有任何名片记录，请使用新增功能添加名片！")

        return
    #  打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t")

    print("")

    #  打印分割线
    print("=" * 30)

    #  遍历名片列表依次输入列表信息
    for card_dict in card_list:
        #  TODO 上下行无法对齐
        # print("{}\t\t{}\t\t{}\t\t{}".format(card_dict["name"],
        #                                     card_dict["iphone"],
        #                                     card_dict["qq"],
        #                                     card_dict["email"]))
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["iphone"],
                                        card_dict["qq"],
                                        card_dict["email"]))


#  查询名片
def search_card():
    print("*" * 50)
    #  注释部分是我自己写的
    # card_name = input("请输入您所查询的名字：")
    # for cards in card_list:
    #     if cards["name"] == card_name:
    #         print("您所查询的名片信息为{}".format(cards))
    #     else:
    #         print("您所查询的用户不存在，请重新输入！")
    find_name = input("请输入你查询的名字：")
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("=" * 30)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["iphone"],
                                            card_dict["qq"],
                                            card_dict["email"]))
            # 对名片进行修改删除
            deal_card(card_dict)
            break
    else:
        print("没有你所查询的名片")


# 处理名片
def deal_card(find_dict):
    """
处理查找到的名片
    :param find_dict: 查找到的的名片
    """
    print(find_dict)
    action_str = input("请输入对名片的操作(【1】修改【2】删除 【0】)返回系统：")
    # 修改名片
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "姓名：")
        find_dict["iphone"] = input_card_info(find_dict["iphone"], "号码：")
        find_dict["qq"] = input_card_info(find_dict["qq"], "QQ：")
        find_dict["email"] = input_card_info(find_dict["email"], "邮箱：")
        print(find_dict)
        print("已成功修改名片！")
    # 删除名片
    if action_str == "2":
        card_list.remove(find_dict)
        print("已成功删除该名片！")


# 针对用户的输入
def input_card_info(dict_value, tip_message):
    """
输入名片信息
    :param dict_value:字典中原有的值
    :param tip_message:输入的提示文字
    :return:如果用户输入了内容，就返回内容，否则返回字典中原有的值
    """
    #  提示用户输入内容
    result_str = input(tip_message)
    #  针对用户的输入进行判断
    if len(result_str) > 0:
        return result_str
    #  如果用户没有输入内容，返回字典中原有的值
    else:
        return dict_value
