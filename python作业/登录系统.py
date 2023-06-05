# 。6、要求编写程序，模拟登录系统账号密码检测功能，并限制账号或密码输错的次数至多3次。
# 登录系统一般具有账号密码检测功能，即检测用户输入的账号密码是否正确。若用户输入的账号
# 或密码不正确，提示 “用户名或密码错误”和“您还有*次机会”；若用户输入的账号和密码正确，
# 提示“登录成功”；若输入的账号密码错误次数超过3次，提示“输入错误次数过多，请稍后再试”
right_username = "xiaoming"
right_passwd = 123456
username = input("请输入用户名：")
passwd = int(input("请输入密码："))

i = 1
while i < 4:
    if username == right_username and passwd == right_passwd:
        print("登录成功！")
        break
    elif username != right_username or passwd != right_passwd:
        left_times = 3 - i
        print("密码输入错误，您还有{}次机会".format(left_times))
        # inputnamepasswd()
        username = input("请输入用户名：")
        passwd = int(input("请输入密码："))
    i += 1
    if i > 3:
        print("输入错误次数过多，请稍后再试!")
