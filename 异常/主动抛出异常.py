def input_pwd():
    # 提示用户输入密码
    pwd = input("请输入密码：")
    #  判断密码长度 >= 8,返回用户输入的密码
    if len(pwd) >= 8:
        return pwd
    # 创建异常对象-可以使用错误信息字符串
    ex = Exception("密码长度不够")
    # 主动抛出异常
    raise ex


try:
    print(input_pwd())
except Exception as result:
    print("错误:{}".format(result))
