#  匹配目标文本的任意位置

import re

info_one = "I was born in 2000"
info_two = "2000000505"
print(re.search(r"\d", info_one))
print(re.search(r"\D", info_two))



