import requests
url = "https://baidu.com"
r = requests.post(url)
print(r.text)
print(r.status_code)
print(r.url)
if r.text.find("OK"):
    print("nb")