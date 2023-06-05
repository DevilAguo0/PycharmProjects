# 给定一个百分制成绩, 请根据百分制成绩输出其对应的等级。转换关系如下：
# 90分及以上为’A’，80~89为’B’， 70~79为’C’， 60~69为’D’，60分以下为’E’。


score = int(input())
if score >= 90:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:

    print("D")
else:
    print("E")