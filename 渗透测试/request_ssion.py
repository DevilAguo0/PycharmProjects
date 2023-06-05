import requests
url = "https://www.baidu.com"
s = requests.Session()
r = s.get(url)
print(r.cookies)
print(r.request.headers)

