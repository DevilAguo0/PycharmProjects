#! /Library/Frameworks/Python.framework/Versions/3.9/bin/python3
#  框架搭建
#  无限循环
import cards_tools
while True:
    #   (Adonis email:clarenceguo2060@gmail.com) 显示功能菜单
    cards_tools.show_menu()
    action_str = input("请输入你选择的操作: ")
    print("您选择的操作是{}".format(action_str))
    #  1，2，3针对名片的操作
    if action_str in ["1", "2", "3"]:
        #  新增名片
        if action_str == "1":
            cards_tools.new_card()
        #  显示名片
        elif action_str == "2":
            cards_tools.show_card()
        #  查询名片
        elif action_str == "3":
            cards_tools.search_card()
    #  输入0的时候退出系统
    elif action_str == "0":
        print("欢迎再次使用【名片管理】系统")
        break
    #  输入其他的提示输入错误，并重新输入
    else:
        print("输入错误，并重新输入")
