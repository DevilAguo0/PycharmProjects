import re
regex_obj = re.compile(r'\d')
regex_obj2=re.compile(r'[a-z]+',re.I)
words='Today is March 28,2019'
print(regex_obj2.findall(words))

