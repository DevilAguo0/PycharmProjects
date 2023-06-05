# 0~100所有偶数相加的结果
i = 0
result = 0
while i <= 100:
    if i % 2 == 0:
        result += i
    i += 1
print(result)
