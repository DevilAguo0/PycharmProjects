
#  匹配目标文本的开始位置

import re
data_one="Today is March 28,2022"
data_two="28,March 2019"
print(re.match(r"\d",data_one))
print(re.match(r"\d",data_two))