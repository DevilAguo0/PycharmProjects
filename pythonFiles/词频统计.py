import jieba
with open("/Users/wevilaguo/Desktop/python.txt", "r") as file:
    file = file.read()
file = file.replace(".", "").replace("!", "").replace("--", "").replace("*", "").replace(",", "")
content_list = file.split()
counts = {}
for word in content_list:
    counts[word] = counts.get(word, 0) + 1
keyvalist = list(counts.items())
keyvalist.sort(key=lambda x: x[1], reverse=True)
for i in keyvalist:
    print(str(i).replace("(", "").replace(")", "").replace("'", "").replace("'", "").replace(",", "").replace("'","").replace("", ""))
