# 9、编写一个程序，模拟实现用户注册功能。
# （1）一个网站的用户注册页面中包含用户名、密码、手机号等信息；
# （2）用户名规则为：长度为6~10个字符、以字母或下划线开头；
# （3）密码规则为：长度为6~10个字符、必须以字母开头、包含字母、数字、下划线；
# （3）手机号规则为：中国大陆手机号码；
# （4）若用户输入的注册信息格式有误，系统会对用户进行提示。


import re
def user_registration():
    print("注册提示：")
    print("账号长度为6~10个字符，可使用汉字、字母、数字、下滑线开头\n"
          "密码长度为6~10个字符，包含大小写字母及下划线，需以字母开头\n"
          "手机号为中国大陆手机号")
    user_name = input("请输入账号：")
    user_pwd = input("请输入密码：")
    user_phone_num = input("请输手机号：")
    while True:
        # 账号长度为6~10个字符包含汉字、大小写字母、和下划线
        reg_user = re.compile(r"^[\u4E00-\u9FA5A-Za-z0-9_]{6,10}$")
        # 密码长度为6~10个字符必须以字母开头，包含字母数字下划线
        reg_pwd = re.compile(r"^[a-zA-Z]\w{5,9}$")
        # 手机号码匹配规则
        reg_phone = re.compile(r'^1[03456789]\d{9}$')
        if re.findall(reg_user, user_name):
            if re.findall(reg_pwd, user_pwd):
                if re.findall(reg_phone, user_phone_num):
                    print("注册成功")
                    break
                else:
                    print("手机号码格式不正确")
                    user_phone_num = input("请重新输入手机号：")
            else:
                user_pwd = input("请重新输入密码：")
        else:
            user_name = input("请重新输入账号：")
if __name__ == '__main__':
    user_registration()
