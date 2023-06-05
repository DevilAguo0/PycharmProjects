# 5. 编写程序制作英文学习词典，词典有3个基本功能：添加、查询和退出。程序读取源文件路径
# 下的txt格式词典文件。词典文件存储方式为“英文单词 中文释义”，每行仅有一对中英释义。程序
# 会根据用户的选择进入相应的功能模块，并显示相应的操作提示。当添加的单词已存在时，显示“该
# 单词已添加到词典库”，当查询的单词不存在时，显示“词典库中未找到这个单词”。用户输入其他选项
# 时，提示“输入有误”。

while True:
    print("""
    ==============
    欢迎使用英文学习字典：
    1.添加
    2.查询
    3.退出
    ==============

    """)

    print("加载程序。。。")

    num = int(input("请输入功能序号："))
    word_dict = {}

    if num == 1:
        word = input("英语单词：")
        word_translate = input("中文释义:")
        word_dict["英语单词"] = word
        word_dict["中文释义"] = word_translate
        # word_dict.update{"英语单词":word,"中文释义":word_translate}
        with open("vocubulary.txt", "a+") as vocubulary:
            vocubulary.write(str(word_dict) + '\n')
            print("该单词已添加到词典库")

    elif num == 2:
        words = input("请输入查询的单词：")

        with open("vocubulary.txt", "r+") as vocubulary:
            word = vocubulary.read()
            if words in word:
                print("该单词已添加到词典库")
            else:
                print("词典库中未找到这个单词")
    elif num == 3:
        quit()
    else:
        print('输入有误')
