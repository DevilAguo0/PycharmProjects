import requests

url = "https://baidu.com"
headers = {"User-Agent": "python"}
r1 = requests.get(url)
r2 = requests.post(url)
print(r2.request.headers)
print(r1.request.headers)
r = requests.get(url, headers=headers)
print(r.request.headers)
