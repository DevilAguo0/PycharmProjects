import requests

url = "https://aws.amazon.com"
r = requests.get(url)
# print(r.headers)  # 响应头
# print("*" * 100)
# print(r.request.headers)  # 获取请求头
# # print("*" * 100)
# print(r.text.)  # 获取的是网页源代码
# print("*" * 100)
# print(r.content) # 获取的是二进制代码
#输出 url
# print(r.url)
print(r.cookies)
