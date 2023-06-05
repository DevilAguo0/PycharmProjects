import re
word = 'hello itheima'
match_result = re.search(r'\whe\w',word)
print(match_result)
print(match_result.group())
print(match_result.span())
print(match_result.start())
print(match_result.end())

