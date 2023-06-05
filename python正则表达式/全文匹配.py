# import re
# string = "狗的英文：Dog，猫的英文：Cat。"
# reg_zhn = re.compile(r"[\u4e00-\u9fa5]+")
# print(re.findall(reg_zhn,string))
import re
string ="狗的英文：Dog，猫的英文：Cat。"
re_eng = re.compile(r"[a-zA-Z]+")
result_info=re.finditer(re_eng,string)
print(result_info)
print(type(result_info))
print(result_info.__next__())