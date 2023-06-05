import re

ydreg = re.compile(r'^13[456789]|14[78]|15[012789]|165|178|198|18[23478]\d{9}$')
ltreg = re.compile(r'^13[012]|14[056]|15|17|18[56]|166\d{8}$')
dxreg=re.compile(r'^133|149|153|17[3471|18[019]|19[19]\d{8}$')
while True:
    phnum=input('请输入手机号：')
    if re.match(ydreg,phnum):
        print("该号码属于:中国移动")
    elif re.match(ltreg,phnum):
        print("该号码属于:中国联通")
    elif re.match(dxreg,phnum):
        print("该号码属于:中国电信")
    else:
        print("手机号非法,请重新输入！")