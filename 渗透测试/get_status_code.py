import requests

url = "https://baidu.com"
r = requests.get(url)
print(r.status_code)
print(url)
print(r.text)

# print(r.cookies)
# print(r.headers)
# print(r.history)
# print(r.cookies)
