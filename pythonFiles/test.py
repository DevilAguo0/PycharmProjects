import os

conment = open("/Users/wevilaguo/Desktop/studentmanage.py","r").read()
# print(conment)
conment_copy=open("/Users/wevilaguo/Desktop/studentmanage_copy2.py","w")
print(conment_copy)
file=conment_copy.write(conment)
print(file)
# print(conment)
# print(os.getcwd())
# os.mkdirs()  # 创建多层目录
# os.mkdir()  # 创建最后一层目录
# print(os.listdir())
#
print(os.path.isabs("/Users/wevilaguo/Desktop/studentmanage_copy2.py"))    #判断是否为觉对路径
print(os.path.exists("/Users/wevilaguo/Desktop/studentmanage_copy2.py"))  #判断是否存在


