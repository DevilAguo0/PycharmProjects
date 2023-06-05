import requests

url = "https://www.baidu.com"
#  ip = 172.16.172.126
proxies = {"http": 'http://172.16.172.126:8080', "https": "https://172.16.172.126:8080"}
r = requests.get(url, proxies=proxies, verify=False)
print(r.status_code)