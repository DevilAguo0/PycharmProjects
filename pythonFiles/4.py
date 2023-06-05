# 有两个文本文件a.txt和b.txt，各存放一行字符，要求把这两个文件中的信息合并
# 并按字母顺序排列，写到一个新文件c.txt中
with open("a.txt", "r+") as file_a:
    file_a_r = file_a.read()
    with open("b.txt", "r+") as file_b:
        file_b_r = file_b.read()
        with open("c.txt", "w+") as file_c:
            file = file_a_r + file_b_r
            file_s = ''.join(sorted(list(file)))
            file_c.write(file_s)
