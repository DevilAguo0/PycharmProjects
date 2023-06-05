# assert 表达式[,参数]
try:
    age= int(input("请输入年龄："))
    assert age>=18,"年龄必须大于18岁"
except Exception as Error:
    print(f"异常处理：{Error}")
    