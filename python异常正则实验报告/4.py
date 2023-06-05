# 4、录入一个学生的成绩，把该学生的成绩转换为A优秀、B良好、C合格、D不及格的形式，最后将该学生的成绩打印出来。
# 要求使用assert断言处理分数不合理的情况。

try:
    score = int(input("请输入分数："))
    assert 0 <= score <= 100, "分数必须在0到100之间"

    if 90 < score < 100:
        print("优秀")
    elif 80 < score < 89:
        print("良好")
    elif 60 < score < 79:
        print("合格")
    elif 0 < score < 59:
        print("不合格")
except Exception as Error:
    print(Error)
