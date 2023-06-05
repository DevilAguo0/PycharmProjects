#  贪婪匹配

import re

words = "And slowly read,and dream of the soft look"
result = re.search(r'and\s.*', words)
print(result.group())

#  非贪婪匹配

import re

words = "And slowly read,and dream of the soft look"
result = re.search(r'and\s.*?', words)
print(result.group())

print(re.search(r'and\s.+', words).group())
print(re.search(r'and\s.+?', words).group())
