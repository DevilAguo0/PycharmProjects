import copy
dirctdemo = {"name":"xiaoming","age":18,"grade": 6}
dirctdemo["append"] = {1:2,3:4}
print(dirctdemo["name"])
print(dirctdemo.fromkeys("ahdebive"))
print(dirctdemo)
print(dirctdemo.items())
print(dirctdemo.popitem())
print(dirctdemo)
print(dirctdemo.get("key","不存在"))
print(dirctdemo)
print(dirctdemo.copy())
print(copy.deepcopy(dirctdemo))