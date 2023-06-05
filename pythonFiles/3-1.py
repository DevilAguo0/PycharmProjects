# 3、编写程序实现以下功能：
# （1）完成学生信息的输入，要求记录不少于5条，每个学生信息包括姓名和3门课程的成绩。
# （2）将学生信息写入当前工作目录下名为score.txt的文本文件，要求每个学生记录一行，每列数据用制表符（\t）分隔。
# （3）分别求学生3门课程成绩的平均分（保留一位小数）并输出。
# （4）找出3门课程都不及格的学生，输出他们的姓名和各科成绩。
stu_info_list = []


def stu_info_input(name, chinese, math, english):
    stu_info = {'Name': name, 'Chinese': chinese, 'Math': math, 'English': english}
    return stu_info


def average(stu):
    result = (stu["Chinese"] + stu["Math"] + stu["English"]) / 3
    return result


stu1 = stu_info_input('xiaoming', 89, 86, 90)
stu2 = stu_info_input('xiaohong', 90, 89, 87)
stu3 = stu_info_input('xiaohong', 89, 80, 95)
stu4 = stu_info_input('helo', 34, 56, 24)
stu5 = stu_info_input('kloie', 90, 58, 99)

stu_info_list.append(stu1)
stu_info_list.append(stu2)
stu_info_list.append(stu3)
stu_info_list.append(stu4)
stu_info_list.append(stu5)

with open("score.txt", "w+") as file:
    for i in stu_info_list:
        filer = file.write(str(i) + "\n")

for i in stu_info_list:
    print("{:.1f}".format(average(i)))

for i in stu_info_list:
    if i["Chinese"] < 60 and i["Math"] < 60 and i["English"]:
        print(i)
