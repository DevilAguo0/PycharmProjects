#!/usr/bin/python3
# Anchor extraction from html document
from bs4 import BeautifulSoup
from urllib.request import urlopen

with urlopen('https://about.google/intl/zh-CN/products/') as response:
    soup = BeautifulSoup(response, 'html.parser')
    # 获取所有文字内容
    print(soup.get_text())
    for anchor in soup.find_all('a'):
        print(anchor.get('href', '/'))
