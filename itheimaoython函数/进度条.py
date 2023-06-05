def print_line(char, times):
    """
打印单行分割线
    :param char: 分割字符
    :param times: 分割次数
    """
    print(char * times)


# print_line("*", 60)


def print_lines(char, times, much):
    """
打印多行分割线
    :param char: 分割线使用的字符
    :param times: 分割线的行数
    :param much: 每行分割线字符所使用的次数
    """
    row = 0
    while row < much:
        print_line(char, times)
        row += 1


print_lines("0", 23, 20)
