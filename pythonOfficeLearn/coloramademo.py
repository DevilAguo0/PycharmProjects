# #!/usr/bin/env python
# # encoding: utf-8
#
# from colorama import init, Fore, Back, Style
#
# if __name__ == "__main__":
#     init(autoreset=True)  # 初始化，并且设置颜色设置自动恢复
#     print(Fore.RED + 'some red text')
#     print(Back.GREEN + 'and with a green background')
#     print(Style.DIM + 'and in dim text')
#     # 如果未设置autoreset=True，需要使用如下代码重置终端颜色为初始设置
#     # print(Fore.RESET + Back.RESET + Style.RESET_ALL)  autoreset=True
#     print('back to normal now')


# ==============================================================================


import sys
import os
import random
import string
from colorama import Fore, Style, init
import platform


def print_arg(arg):
    """
    打印参数
    :param arg:
    :return:
    """

    for ind, val in enumerate(arg):
        if ind == 0:

            print_color(Fore.YELLOW, r"------执行%s输入参数为--------" % val)
        else:
            print(val, end=",")


def print_color(color, mes=""):
    """
     获得系统平台
     windows终端需要设置
     init(wrap=True)
    :param color:
    :param mes:
    :return:
    """
    v_system = platform.system()
    if v_system != 'Windows':
        print(color + mes)
    else:
        # init(wrap=True)
        print(color + mes)


# 获得系统参数
v_arg = sys.argv
init(autoreset=True)  # 初始化，并且设置颜色设置自动恢复
# print_color(Fore.YELLOW+platform.system())
if len(v_arg) != 4:
    # print(platform.system())
    print_arg(v_arg)
    print_color(Fore.RED, "---参数输入错误--")
    print_color(Fore.RED, "fileStrReplace.py 文件名 旧字符串 新字符串")
else:
    f_name = v_arg[1].strip()
    old_str = v_arg[2].strip()  # 旧字符
    new_str = v_arg[3].strip()  # 替换的新字符
    f_new_name = "%s.new" % f_name
    replace_count = 0  # 字符替换次数
    if not os.path.exists(f_name):
        print_color(Fore.YELLOW, "%s文件不存在" % f_name)
    else:
        f_new = open(f_new_name, 'w')
        f = open(f_name, "r", )
        for line in f:  # 读取大文件
            if old_str in line:
                new_line = line.replace(old_str, new_str)  # 字符替换
                replace_count += 1
            else:
                new_line = line

            f_new.write(new_line)  # 内容写新文件

        f.close()
        f_new.close()

        if replace_count == 0:
            print_color(Fore.YELLOW, "字符%s不存在" % (old_str))
        else:
            bak_f = f_name + ''.join(random.sample(string.digits, 6))
            os.rename(f_name, bak_f)  # 备份旧文件
            os.rename(f_new_name, f_name)  # 把新文件名字改成原文件的名字，就把之前的覆盖掉了
            print_color(Fore.GREEN, "文件替换成功,[字符%s替换%s]共%s次，源文件备份[%s]" % (old_str, new_str, replace_count, bak_f))

# print_color(Style.RESET_ALL)  # 还原默认颜色