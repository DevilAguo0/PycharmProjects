char_list = input().split()
num=[]
for i in char_list:
    num.append(ord(i))
print(chr(max(num)))