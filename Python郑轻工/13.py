# 输入一个字母，若是小写字母，则变为大写输出，否则，原样输出。
# word = input()
#
# adress = ord(word)
# if adress in range(97, 123):
#     print(chr(adress - 32))
# else:
#     print(word)
# s = input('请输入一个字符：')
#  if 'a' <= s <= 'z':
#      print(chr(ord(s) - 32))
#  # elif 'A' <= s <= 'Z':
#  #    print(chr(ord(s) + 32))
# else:
# 　　print('s')
# s = input("")
# if 'a' <= s <= 'z':
#     print(chr(ord(s) - 32))
# else:
#     print(s)

s=input()
# if s>= 'a' and s<= 'z':
if 'a'<= s <='z':
    print(s.swapcase())
else:
    print(s)












