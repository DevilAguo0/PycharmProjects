import re
words = 'And slowly read，and dream of the soft look'
result_one = re.sub(r'\s','-',words)
print(result_one)
result_two = re.subn(r'\s','-',words)
print(result_two)
