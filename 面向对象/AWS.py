# coding=utf-8
# pip3 install pySocket
# pip3 install twocaptcha
# pip3 install 2captcha-python
import base64
import json
import socket
import sys
from random import random, choice
from time import sleep
import time
import os
from urllib import parse
from twocaptcha import TwoCaptcha
from bs4 import BeautifulSoup
import requests
import socks
from faker import Faker
import traceback

items = []


def read_cookies_and_token():
    with open('abck.txt', 'r') as f:
        content = list(f)
        print(content)
        for c in content:
            obj = {
                'aws-session-id-fallback': '',
                'aws-session-id': '',
                'JSESSIONID': '',
                'xsrftoken': ''
            }
            obj['aws-session-id-fallback'] = json.loads(c)['aws-session-id-fallback']
            obj['aws-session-id'] = json.loads(c)['aws-session-id']
            obj['JSESSIONID'] = json.loads(c)['JSESSIONID']
            obj['xsrftoken'] = json.loads(c)['xsrftoken']
            items.append(obj)
        print(items)


class AwsAuto():
    def fakeAddress(self):
        fake = Faker()
        ad = ""
        # print(ad)
        while ad == "" or (len(ad) >= 20) or "," in ad:
            ad = fake.address().split('\n')[0]
        print("------------输出地址")
        print(ad)
        return ad

    def fakeAddress_GB(self):
        fake = Faker('en_GB')
        ad = ""
        lens = 4
        # print(ad)
        while lens == 4:
            ad = fake.address().split('\n')
            lens = len(ad)
        # print(ad)
        self.add1 = self.fakeAddress_GB()[0]
        # self.item = item
        self.city = self.fakeAddress_GB()[1]
        self.state = 'ENG'
        self.postalCode = self.fakeAddress_GB()[2]
        self.fullName = fake.name()

    def fakeAddress_US(self):
        fake = Faker('en_GB')
        ad = ""
        lens = 4
        # print(ad)
        while lens == 4:
            ad = fake.address().split('\n')
            lens = len(ad)
        # print(ad)
        self.fullName = fake.name()
        self.add1 = ad[0]

    def __init__(self, email, pwd, card_code, card_year, card_month):
        print("初始化姓名,邮箱,密码,地址1，5sim的api")
        self.sess = requests.Session()
        # fake = Faker()
        self.item_ua = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
            # "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
        ]

        self.ua = choice(self.item_ua)
        print("输出ua值.......")
        print(self.ua)
        # self.language = "en-GB,en;q=0.9"
        self.language = "en-US,en;q=0.9"
        self.times = 42
        self.ip = '127.0.0.1'
        self.port = 5002
        self.countryCode = "US"  # GB
        self.languageSettings = "en_US"
        self.i = 0

        self.m1 = ''

        self.fullName = ''
        self.startSMS_inx = 0

        self.email = email
        self.pwd = pwd
        # self.form1_awsName = self.form1_name

        # self.add1 = self.fakeAddress_GB()[0]
        # self.item = item
        self.add1 = ''
        self.city = ''
        self.state = ''
        self.postalCode = ''
        # self.fakeAddress_US()
        # self.state = ''
        # self.postalCode = ''
        self.phoneNumber = ''
        self.api_key = '5faf4e021d574c0b874590a9d3cccd99'
        self.id = ''
        self.number = ''
        self.cookie = None

        self.xToken = ''

        self.image_url = ''
        self.base64_image = ''

        self.b64 = ''
        self.Cap_guss = ''
        self.Cap_ces = ''
        self.Cap_url = ''
        self.level = 'hard'

        self.card_code = card_code
        self.card_month = card_month
        self.card_year = card_year

        self.smsPin = ''
        self.divaImgCaptchaLevel = 'ImgHardCaptcha'

        self.wait = 5
        self.ip_check = ''

        # print(self.item)
        print(self.add1)

    '''
    def fff1(self):
        fake = Faker()
        f_address = fake.address().split('\n')[0]
        if len(f_address) <= 20:
            print(f_address)
            return f_address
        else:
            return "0067 Scott Landing"
    def fff2(self):
            return "531 Gerald Pass"
    '''

    # http://api1.5sim.net/stubs/handler_api.php?api_key=$api_key&action=getNumber&service=$service&forward=$forward&operator=$operator&country=$country

    def get_number(self, country_id=36, service='am'):
        # USA =12
        # Canada = 36
        country = country_id
        service = service
        params = (
            ('api_key', self.api_key),
            ('country', country),
            ('action', 'getNumber'),
            ('service', service),
        )
        # 测试关闭
        response = requests.get('http://api1.5sim.net/stubs/handler_api.php', params=params)
        print(response.text)
        self.id = response.text.split(':')[1]
        self.number = response.text.split(':')[2]
        print("订单id号：" + self.id)
        print("电话号：" + self.number)
        ##ACCESS_NUMBER:113585846:14504260130
        # self.number = "+15486660391"

    def get_number_test(self, country_id=36, service='am'):
        country_id = 1
        service = '33'
        self.id = "116127435"
        self.number = "15792646801"

    def get_code(self):
        # 等待30秒
        time = 30
        params = (
            ('api_key', self.api_key),
            ('id', self.id),
            ('action', 'getStatus')
        )
        text = "STATUS_WAIT_CODE"
        while (text == "STATUS_WAIT_CODE"):
            print("获取验证码状态,等待30秒.....")
            sleep(time)
            response = requests.get('http://api1.5sim.net/stubs/handler_api.php', params=params)
            text = response.text
            print(response.text)
        if "STATUS_OK" in response.text:
            self.smsPin = response.text.split(':')[1]
            print("获取验证码成功" + self.smsPin + "......")
            return True;
        else:
            print("获取验证码失败，错误状态码为:" + response.text + "......")
            return False;

    def get_m1(self):
        print("获取m1......")
        url = "http://www.metadata1.com/api/metadata_api/metadata1"
        payload = {
            'username': self.email,
            'uuid': 'M-000312',
            'api_key': '3eecb1c9148061897cac462126ce03c2',
            'pro_no': '10001',
            # 'timeZone' : 8,
            # "login_href": "https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation",
            'userAgent': self.ua
        }
        files = [
        ]
        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': self.ua,
        }
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        # print(response.json()['data'])
        self.m1 = response.json()['data']
        print("输出m1长度...")
        print(len(self.m1))

    def get_proxy(self):
        print("进入get_proxy...")
        # s = requests.Session();
        url = "http://dvapi.doveip.com/cmapi.php?rq=distribute&user=Devilaguo&token=ekI5QytjbWxjWGhBY3lDZElJM21xQT09&geo=us"
        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': self.ua,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': self.language,
            # 'Cookie': '__cfduid=de56e8fce05263f13e238c71fd2478b4e1617797412; _ga=GA1.1.1352837125.1617797415; _ga_TQT1FMTQJ0=GS1.1.1617804324.2.1.1617804547.0'
        }
        # response = requests.request("GET", url, headers=headers, data=payload)
        r = requests.request("GET", url, headers=headers)
        print(r.text)
        back_code = r.json()
        self.ip = back_code['data']['ip']
        self.port = int(back_code['data']['port'])
        print("设置代理........")
        socks.set_default_proxy(socks.SOCKS5, self.ip, self.port)
        socket.socket = socks.socksocket

    def get_911(self):
        self.ip = "127.0.0.1"
        self.port = 5001
        socks.set_default_proxy(socks.SOCKS5, self.ip, self.port)
        socket.socket = socks.socksocket

    def set_location_US(self):
        print("设置位置set_location_US.......")
        url = "http://ip-api.com/json/"
        # s = requests.Session()
        payload = {}
        headers = {
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': self.ua,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': self.language
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        # socket.close()
        print(response.json())
        self.state = response.json()['regionName']
        # self.state = "ENG"
        print(response.json()['regionName'])
        self.city = response.json()['city']
        print(response.json()['city'])
        self.postalCode = response.json()['zip']
        self.ip_check = self.postalCode
        self.fakeAddress_US()
        if self.postalCode == "":
            print("没有获取zip,跳出系统,程序终止执行......")
            sys.exit()
        # print(response.text)

    def set_location_GB(self):
        print("设置代理并且获取位置set_proxy_get_location...")
        url = "http://ip-api.com/json/"
        # s = requests.Session()
        payload = {}
        headers = {
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': self.ua,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': self.language
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        # socket.close()
        print(response.json())
        self.fakeAddress_GB()
        # self.state = "ENG"

    def refresh(self):
        print("进入refresh....获取captcha验证码...")
        url = "https://portal.aws.amazon.com/billing/signup/rest/v1.0/captcha/refresh?divaImgCaptchaLevel=" + self.divaImgCaptchaLevel + "&page=diva"
        payload = {}
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': self.ua,
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation',
            'Accept-Language': self.language,
        }
        response = self.sess.get(url, headers=headers, data=payload)
        print(response.json())
        print(response.json()['ces'])
        self.Cap_ces = response.json()['ces']
        print(response.json()['url'])
        self.Cap_url = response.json()['url']
        print(response.json()['guess'])
        self.Cap_guss = response.json()['guess']
        print("替换等级level.............")
        print(response.json()["level"])
        self.level = response.json()["level"]

    def refresh_create(self):
        url = "https://portal.aws.amazon.com/billing/signup/rest/v1.0/captcha/refresh?"
        payload = {}
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': self.ua,
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation',
            'Accept-Language': self.language,
            # 'Cookie': 'aws-session-id-fallback=5pBiAJ7qjSU8JCNaFkUj6Pwn6otMXEi7rAM8ow34_tU; aws-session-id=5pBiAJ7qjSU8JCNaFkUj6Pwn6otMXEi7rAM8ow34_tU; aws_sup_lang=en-us; JSESSIONID=FB640BB58762D25F34BA69E56B960406; awsccc=eyJlIjoxLCJwIjoxLCJmIjoxLCJhIjoxLCJpIjoiOTNjNTQzNjMtODA1ZC00MTExLTllODktNGQzOWY1NWRhYmNiIiwidiI6IjEifQ==; s_fid=3B7BC516B1E7A987-0242978B4E8BB5C0; regStatus=registering; s_cc=true; aws-ubid-main=983-7857540-0846457; s_sq=awsamazonallprod1%3D%2526pid%253DReg%252520Start%2526pidt%253D1%2526oid%253Dfunction%252528e%252529%25257Bif%252528s%252526%252526n.__isDisabled%252528%252529%252529returne.preventDefault%252528%252529%25253Bvart%25253De.button%25252Cr%25253De.ctrlKey%25252Ci%25253De.shiftKey%25252Co%2526oidt%253D2%2526ot%253DSUBMIT'
        }
        response = self.sess.get(url, headers=headers, data=payload)
        print(response.json())
        print(response.json()['ces'])
        self.Cap_ces = response.json()['ces']
        print(response.json()['url'])
        self.Cap_url = response.json()['url']
        print(response.json()['guess'])
        self.Cap_guss = response.json()['guess']
        print(response.json()["level"])
        self.level = response.json()["level"]

    def signup(self):
        url = "https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation"
        payload = {}
        headers = {
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': self.ua,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Accept-Language': self.language,
            # 'Cookie': 'aws-ubid-main=140-6180586-5122417'
        }
        response = self.sess.get(url, headers=headers, data=payload)
        soup = BeautifulSoup(response.content, "html.parser")
        xToken = soup.findAll(id="xsrfToken")[0]['value']
        self.xToken = xToken

    def denforcePI0(self):
        url = "https://portal.aws.amazon.com/billing/signup/rest/v1.0/steps/current?enforcePI=False&type"
        payload = {}
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': self.ua,
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation',
            'Accept-Language': self.language,
        }
        response = self.sess.get(url, headers=headers, data=payload)
        print(response.text)

    def all(self):
        import requests

        url = "https://portal.aws.amazon.com/billing/signup/rest/v1.0/steps/all"

        payload = {}
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': self.ua,
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation',
            'Accept-Language': self.language,
            # 'Cookie': 'aws-session-id-fallback=dNKTA1Xc6n6zoyeZpEt_PlcYiRdXzIPFkW0aWejPvQE; aws-session-id=dNKTA1Xc6n6zoyeZpEt_PlcYiRdXzIPFkW0aWejPvQE; aws_sup_lang=en-us; JSESSIONID=CA237B818B0F6641365B9541578A7C44'
        }
        response = self.sess.get(url, headers=headers, data=payload)
        print(response.text)

    def in_bs64_out_word(self):
        print("进入get_image...获取图片验证码....")
        url = self.Cap_url
        payload = {}
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': self.ua,
            'Accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
            # 'Accept-Encoding': 'gzip, deflate',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': 'https://portal.aws.amazon.com/',
            'Accept-Language': self.language
        }
        response = self.sess.get(url, headers=headers, data=payload)
        print("输出图片字节码...")
        base64_data = base64.b64encode(response.content)
        print("输出图片base64编码...")
        # self.base64_image = "data:image/gif;base64,"+str(base64_data, encoding="utf8");
        self.b64 = str(base64_data, encoding="utf8")
        # cap = Cap();

        word = self.return_word()
        if "timeout" in word:
            print("已经超时......")
            return "timeout"
        else:
            self.Cap_guss = word
            print(self.Cap_guss)
            return "sucess"

    def return_word(self):
        api_key = os.getenv('APIKEY_2CAPTCHA', 'dbaf18256978ffffb7e6cd214d6d08e5')
        solver = TwoCaptcha(api_key, defaultTimeout=45, pollingInterval=5)
        try:
            result = solver.canvas(self.b64, hintText='Draw around apple')
            return result['code']
        except Exception as e:
            print(str(e))
            return "timeout..."
            # sys.exit(e)
        else:
            print("其他问题日志记录.......")
            sys.exit('result: ' + str(result))

    def create(self):
        print("进入create")
        url = "https://portal.aws.amazon.com/billing/signup/rest/v1.0/identity/create"
        payload = json.dumps({
            "email": self.email,
            "fullName": self.fullName,
            "password": self.pwd,
            "rePassword": self.pwd,
            "showCaptcha": False,
            "browserFingerPrintMetadata": self.m1
        })
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': self.ua,
            'x-awsbc-xsrf-token': self.xToken,
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Origin': 'https://portal.aws.amazon.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation',
            'Accept-Language': self.language,
        }

        response = self.sess.post(url, headers=headers, data=payload)
        print(response.json())
        if "message" in response.json():
            if response.json()["message"] == "Parameters validation failed with CAPTCHA_REQUIRED":
                print("需要captcha验证....")
                print("message:" + json.dumps(response.json()))
                self.create_capTcha()

    def create_capTcha(self):
        self.refresh_create()
        identifi = self.in_bs64_out_word()
        for index in range(3):
            if "sucess" == identifi:
                break;
            else:
                self.refresh_create()
                identifi = self.in_bs64_out_word()
        if "error" == identifi:
            print("验证码问题......！")
            sys.exit()
        url = "https://portal.aws.amazon.com/billing/signup/rest/v1.0/identity/create"
        payload = json.dumps({
            "email": self.email,
            "fullName": self.fullName,
            "password": self.pwd,
            "rePassword": self.pwd,
            "showCaptcha": True,
            "captcha": {
                "ces": self.Cap_ces,
                "guess": self.Cap_guss,
                "url": self.Cap_url,
                "type": "CLASSIC_IMAGE",
                "level": self.level
            },
            "browserFingerPrintMetadata": self.m1
        })
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': self.ua,
            'x-awsbc-xsrf-token': self.xToken,
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Origin': 'https://portal.aws.amazon.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation',
            'Accept-Language': self.language,
        }
        # headers['x-awsbc-xsrf-token'] = self.xToken
        # headers['Cookie'] = 'aws-session-id-fallback=' + self.asif + '; aws-session-id=' + self.asi + '; JSESSIONID=' + self.j
        response = self.sess.post(url, headers=headers, data=payload)
        print(response.text)
        if ("message" in response.json()):
            if response.json()["message"] == "Parameters validation failed with CAPTCHA_REQUIRED":
                for index in range(3):
                    if response.json()["message"] == "Parameters validation failed with CAPTCHA_REQUIRED":
                        print("需要captcha验证....")
                        print("message:" + json.dumps(response.json()))
                        self.create_capTcha()
                if response.json()["message"] == "Parameters validation failed with CAPTCHA_REQUIRED":
                    print("验证码错误次数过多....退出程序...")
                    sys.exit()

    def account(self):
        print("进入account")
        url = "https://portal.aws.amazon.com/billing/signup/rest/v1.0/account"
        payload = json.dumps({
            "address": {
                "addressLine1": self.add1,
                "addressLine2": "",
                "city": self.city,
                "state": self.state,
                "countryCode": self.countryCode,
                "postalCode": self.postalCode,
                "fullName": self.fullName,
                "phoneNumber": '+1' + self.number[1:]
            },
            "clientInfo": {
                "languageSettings": self.languageSettings
            },
            "customerAgreement": True,
            "browserFingerPrintMetadata": self.m1
        })

        show = {
            "address": {
                "addressLine1": self.add1,
                "addressLine2": "",
                "city": self.city,
                "state": self.state,
                "countryCode": self.countryCode,
                "postalCode": self.postalCode,
                "fullName": self.fullName,
                "phoneNumber": '+1' + self.number[1:]
            },
            "clientInfo": {
                "languageSettings": self.languageSettings
            },
            "customerAgreement": True,
            # "browserFingerPrintMetadata": self.m1
        }
        print(show)
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': self.ua,
            'x-awsbc-xsrf-token': self.xToken,
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Origin': 'https://portal.aws.amazon.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation',
            'Accept-Language': self.language,
            # 'Cookie': 'aws-session-id-fallback=wlpYUy5Yuzll_1TZT4mkal_NMFRI80nTIh6qZw6t2n8; aws-session-id=wlpYUy5Yuzll_1TZT4mkal_NMFRI80nTIh6qZw6t2n8; aws_sup_lang=en-us; JSESSIONID=91CA1451931C83EBC74451FA0C72EE73; awsccc=eyJlIjoxLCJwIjoxLCJmIjoxLCJhIjoxLCJpIjoiODVkMzdjMjQtOTg4Ni00MDNhLWIxNGQtYTExNDk2MTZiZThlIiwidiI6IjEifQ==; s_fid=4260FF99BDDA027E-16DF26C1F26271CA; s_cc=true; regStatus=registering; aws-ubid-main=142-1532517-7440385; aws-das-fallback="AAAAAAAAAAHU_4lseUwUgVC6r5WDWshZkl2DbxCJr4ymZ1ktZ_uftgrP7oT1YqCHO38XtyNe3G3KiHjvs8R3tQxNK--Dju0P-tFbgPPYHmWXa5mQWsX3Hh8r0SjepfhOTJG541m0mZRfdX_UC2Iz0vqWzXEQc8njXkRtqDvd3nmjHdnN5zKs2ONzRvkEMxhkn0NFFrqO13cCvjPjCUvEi7_syWiF56dAny4_26AJnQxoFCns0dvUMLZSrB_Yky4U3AE="; aws-das=AAAAAAAAAAHU_4lseUwUgVC6r5WDWshZkl2DbxCJr4ymZ1ktZ_uftgrP7oT1YqCHO38XtyNe3G3KiHjvs8R3tQxNK--Dju0P-tFbgPPYHmWXa5mQWsX3Hh8r0SjepfhOTJG541m0mZRfdX_UC2Iz0vqWzXEQc8njXkRtqDvd3nmjHdnN5zKs2ONzRvkEMxhkn0NFFrqO13cCvjPjCUvEi7_syWiF56dAny4_26AJnQxoFCns0dvUMLZSrB_Yky4U3AE=; s_sq=awsamazonallprod1%3D%2526pid%253DSignup%2526pidt%253D1%2526oid%253Dfunction%252528e%252529%25257Bif%252528s%252526%252526n.__isDisabled%252528%252529%252529returne.preventDefault%252528%252529%25253Bvart%25253De.button%25252Cr%25253De.ctrlKey%25252Ci%25253De.shiftKey%25252Co%2526oidt%253D2%2526ot%253DSUBMIT'
        }

        response = self.sess.post(url, headers=headers, data=payload)
        print(response.json())
        if "message" in response.json():
            if response.json()["message"] == "Failed to create account":
                sys.exit()

    def creditcards(self):
        # self.get_m1()
        url = "https://portal.aws.amazon.com/billing/signup/rest/v1.0/creditcards"

        payload = {'address[addressLine1]': self.add1,
                   'address[addressLine2]': '',
                   'address[city]': self.city,
                   'address[state]': self.state,
                   'address[countryCode]': self.countryCode,
                   'address[postalCode]': self.postalCode,
                   'address[company]': '',
                   'address[fullName]': self.fullName,
                   'address[phoneNumber]': '+1' + self.number[1:],
                   'accountHolderName': self.fullName,
                   'addCreditCardNumber': self.card_code,
                   'expirationMonth': self.card_month,
                   'expirationYear': self.card_year,
                   'enforcePI': 'False',
                   'xsrfToken': self.xToken,
                   'browserFingerPrintMetadata': self.m1}
        show = {'address[addressLine1]': self.add1,
                'address[addressLine2]': '',
                'address[city]': self.city,
                'address[state]': self.state,
                'address[countryCode]': self.countryCode,
                'address[postalCode]': self.postalCode,
                'address[company]': '',
                'address[fullName]': self.fullName,
                'address[phoneNumber]': '+1' + self.number[1:],
                'accountHolderName': self.fullName,
                'addCreditCardNumber': self.card_code,
                'expirationMonth': self.card_month,
                'expirationYear': self.card_year,
                'enforcePI': 'False',
                'xsrfToken': self.xToken, }
        print(show)
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': self.ua,
            'x-awsbc-xsrf-token': self.xToken,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': '*/*',
            'Origin': 'https://portal.aws.amazon.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation',
            'Accept-Language': self.language,
        }
        payload = parse.urlencode(payload)
        # print(payload)
        # self.set_proxy_get_location_second()
        response = self.sess.post(url, headers=headers, data=payload)
        print(response.text)
        # self.create_capTcha()

    def startSMS(self):
        self.refresh()
        identifi = self.in_bs64_out_word()
        for index in range(3):
            if "sucess" == identifi:
                break;
            else:
                self.refresh()
                identifi = self.in_bs64_out_word()
        if "error" == identifi:
            print("验证码问题......！")
            sys.exit()
        # self.get_m1()
        url = "https://portal.aws.amazon.com/billing/signup/rest/v1.0/diva/startSMS"
        payload = json.dumps({
            "phoneNumber": "+1 " + self.number[1:],
            "language": "en-us",
            "captchaCES": self.Cap_ces,
            "captchaType": "CLASSIC_IMAGE",
            "captchaGuess": self.Cap_guss,
            "countryCode": "+1",
            "checkCaptcha": "true",
            "enforcePI": "False",
            "divaImgCaptchaLevel": self.divaImgCaptchaLevel,
            "country": "US",
            "browserFingerPrintMetadata": self.m1
        })
        show = json.dumps({
            "phoneNumber": "+1 " + self.number[1:],
            "language": "en-us",
            "captchaCES": self.Cap_ces,
            "captchaType": "CLASSIC_IMAGE",
            "captchaGuess": self.Cap_guss,
            "countryCode": "+1",
            "checkCaptcha": "true",
            "enforcePI": "False",
            "divaImgCaptchaLevel": self.divaImgCaptchaLevel,
            "country": "US",
        })
        print(show)

        headers = {
            'Connection': 'keep-alive',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'x-awsbc-xsrf-token': self.xToken,
            'sec-ch-ua-mobile': '?0',
            'User-Agent': self.ua,
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Origin': 'https://portal.aws.amazon.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://portal.aws.amazon.com/billing/signup?refid=em_127222&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation',
            'Accept-Language': self.language,
        }
        response = self.sess.post(url, headers=headers, data=payload)
        print(response.json())

        if ("errorCode" in response.json()):
            SmsCode = response.json()["errorCode"]
            while (SmsCode == "Captcha_Verification_Failed" or SmsCode == "CAPTCHA_LEVEL_ERROR"):
                if (SmsCode == "Captcha_Verification_Failed"):
                    print("captcha验证码不对,也需要变级别,变为hard.......")
                    aa.divaImgCaptchaLevel = "ImgHardCaptcha"
                    aa.level = "hard"
                    return 0  # 验证码错误状态码0
                elif SmsCode == "CAPTCHA_LEVEL_ERROR":
                    print("等级错误,变级为hard...")
                    # print("变级hard...")
                    aa.divaImgCaptchaLevel = "ImgHardCaptcha"
                    aa.level = "hard"
                    return 1  # 等级错误状态码1
            if SmsCode == "_Credit_Card_Vet_Check_Failed_":
                print("虚拟卡作废......")
                return 2  # 虚拟卡作废状态码2
        elif ("nextStep" in response.json()):
            return 3  # 短信发送成功状态码3
        else:
            print("收集未知错误信息" + response.json() + "......")
            print("未知...退出程序")
            sys.exit()

    def enforcePi(self):
        import requests
        url = "https://portal.aws.amazon.com/billing/signup/rest/v1.0/steps/current?enforcePI=False&type"
        payload = {}
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': self.ua,
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation',
            'Accept-Language': self.language,
        }
        response = self.sess.get(url, headers=headers, data=payload)
        print(response.json())
        print(response.json()["properties"]["divaImgCaptchaLevel"])
        if "properties" in response.json():
            self.divaImgCaptchaLevel = response.json()["properties"]["divaImgCaptchaLevel"]
            # self.divaImgCaptchaLevel = "ImgHardCaptcha"
            return True
        else:
            print("enforcePI响应值为空,图片验证码等级为默认........")
            return False

    def verifySMS(self):
        print("发送验证码")
        url = "https://portal.aws.amazon.com/billing/signup/rest/v1.0/diva/verifySMS"
        payload = json.dumps({
            "country": "US",
            "phoneNumber": "+1 " + self.number[1:],
            "enforcePI": "False",
            "smsPin": self.smsPin
        })
        headers = {
            'Connection': 'keep-alive',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'x-awsbc-xsrf-token': self.xToken,
            'sec-ch-ua-mobile': '?0',
            'User-Agent': self.ua,
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Origin': 'https://portal.aws.amazon.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://portal.aws.amazon.com/billing/signup?refid=em_127222&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation',
            'Accept-Language': self.language,
        }
        response = self.sess.post(url, headers=headers, data=payload)
        print(response.text)

    def support(self):
        url = "https://portal.aws.amazon.com/billing/signup/rest/v1.0/subscribe/support"
        payload = json.dumps({
            "product": "AWSSupportBasic"
        })
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': self.ua,
            'x-awsbc-xsrf-token': self.xToken,
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Origin': 'https://portal.aws.amazon.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation',
            'Accept-Language': self.language,
        }
        response = self.sess.post(url, headers=headers, data=payload)

        print(response.text)

    def urp(self):
        import requests
        import json

        url = "https://portal.aws.amazon.com/billing/signup/rest/v1.0/subscribe/urp"

        payload = json.dumps({
            "type": None
        })
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': self.ua,
            'x-awsbc-xsrf-token': self.xToken,
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Origin': 'https://portal.aws.amazon.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation',
            'Accept-Language': self.language,
            # 'Cookie': 'aws-session-id-fallback=nhyClfSJHTUX_OmIC738f4m9pSq-A4MAr9wNdXpAkVw; aws-session-id=nhyClfSJHTUX_OmIC738f4m9pSq-A4MAr9wNdXpAkVw; aws_sup_lang=en-us; JSESSIONID=BA01AF6FEDB60C61B8E3822DE427FEE1; awsccc=eyJlIjoxLCJwIjoxLCJmIjoxLCJhIjoxLCJpIjoiNjc2MTg4NzAtZGVjZi00MWIwLTllNGQtNTQ5OTIxYzM2MGM2IiwidiI6IjEifQ==; s_fid=4EAE1C853DCA0B29-24A86E2DAF0B1F9C; regStatus=registering; s_cc=true; aws-ubid-main=362-3646210-0306283; aws-das-fallback="AAAAAAAAAAHiJwH657ZY2KtrLvq9UOMSfoL33nEftHu2HP7XZbryxviQOexT-rJrvibQeK5yXOcDP4Tjgo_dSSnE_AghJaHCUM07cdTTbvmvsJ4mkJIh3Vo8VjVgXH3r1LY5_iX3MFs3x0gr5Q-ELxWWU4-B6Ou15Elea3f2pagIxgmPM0ywS5k1MbOUuPsZPdJHDjEAk_m2zeDPKObuWXv4VRIgZkAFSXdJg5QNIt3-1hooYH8bSjxY2A0jwEGjJX4="; aws-das=AAAAAAAAAAHiJwH657ZY2KtrLvq9UOMSfoL33nEftHu2HP7XZbryxviQOexT-rJrvibQeK5yXOcDP4Tjgo_dSSnE_AghJaHCUM07cdTTbvmvsJ4mkJIh3Vo8VjVgXH3r1LY5_iX3MFs3x0gr5Q-ELxWWU4-B6Ou15Elea3f2pagIxgmPM0ywS5k1MbOUuPsZPdJHDjEAk_m2zeDPKObuWXv4VRIgZkAFSXdJg5QNIt3-1hooYH8bSjxY2A0jwEGjJX4=; aws-reg-aid=604739845399; aws-reg-guid=0965eea997c310d172f68ca6a2a374acb75861580ec313cb5ff9b47de7d55565; s_sq=awsamazonallprod1%3D%2526pid%253DSupport%2526pidt%253D1%2526oid%253Dfunction%252528e%252529%25257Bif%252528s%252526%252526n.__isDisabled%252528%252529%252529returne.preventDefault%252528%252529%25253Bvart%25253De.button%25252Cr%25253De.ctrlKey%25252Ci%25253De.shiftKey%25252Co%2526oidt%253D2%2526ot%253DSUBMIT'
        }

        response = self.sess.post(url, headers=headers, data=payload)

        print(response.text)

    def regconf(self):
        import requests

        url = "https://aws.amazon.com/registration-confirmation"

        payload = {}
        headers = {
            'authority': 'aws.amazon.com',
            'upgrade-insecure-requests': '1',
            'user-agent': self.ua,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation',
            'accept-language': self.language,
            # 'cookie': 'awsccc=eyJlIjoxLCJwIjoxLCJmIjoxLCJhIjoxLCJpIjoiNjc2MTg4NzAtZGVjZi00MWIwLTllNGQtNTQ5OTIxYzM2MGM2IiwidiI6IjEifQ==; s_fid=4EAE1C853DCA0B29-24A86E2DAF0B1F9C; regStatus=registering; s_cc=true; aws-ubid-main=362-3646210-0306283; aws-reg-aid=604739845399; aws-reg-guid=0965eea997c310d172f68ca6a2a374acb75861580ec313cb5ff9b47de7d55565; s_sq=awsamazonallprod1%3D%2526pid%253DSupport%2526pidt%253D1%2526oid%253Dfunction%252528e%252529%25257Bif%252528s%252526%252526n.__isDisabled%252528%252529%252529returne.preventDefault%252528%252529%25253Bvart%25253De.button%25252Cr%25253De.ctrlKey%25252Ci%25253De.shiftKey%25252Co%2526oidt%253D2%2526ot%253DSUBMIT'
        }
        response = self.sess.get(url, headers=headers, data=payload)

        # print(response.text)

    def regconf1(self):
        import requests
        url = "https://aws.amazon.com/registration-confirmation"
        payload = {}
        headers = {
            'authority': 'aws.amazon.com',
            'upgrade-insecure-requests': '1',
            'user-agent': self.ua,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation',
            'accept-language': self.language,
            # 'cookie': 'awsccc=eyJlIjoxLCJwIjoxLCJmIjoxLCJhIjoxLCJpIjoiNjc2MTg4NzAtZGVjZi00MWIwLTllNGQtNTQ5OTIxYzM2MGM2IiwidiI6IjEifQ==; s_fid=4EAE1C853DCA0B29-24A86E2DAF0B1F9C; regStatus=registering; s_cc=true; aws-ubid-main=362-3646210-0306283; aws-reg-aid=604739845399; aws-reg-guid=0965eea997c310d172f68ca6a2a374acb75861580ec313cb5ff9b47de7d55565; s_sq=awsamazonallprod1%3D%2526pid%253DSupport%2526pidt%253D1%2526oid%253Dfunction%252528e%252529%25257Bif%252528s%252526%252526n.__isDisabled%252528%252529%252529returne.preventDefault%252528%252529%25253Bvart%25253De.button%25252Cr%25253De.ctrlKey%25252Ci%25253De.shiftKey%25252Co%2526oidt%253D2%2526ot%253DSUBMIT'
        }
        response = self.sess.get(url, headers=headers, data=payload)
        # print(response.text)

    def slp(self):
        sleep(self.wait)
        print("等待" + str(self.wait) + "秒......")


try:
    t1 = time.time()
    # fake1 = Faker()
    pwd = 'M' + str(int(random() * 1000)) + 's' + str(int(random() * 10000)) + 'gs3#'
    aa = AwsAuto("fakneyslt@hotmail.com", pwd, '4085440102554555', "2022", "07")
    # aa.get_number_test(36,"am")
    aa.get_number(36, "am")
    aa.get_proxy()
    # aa.get_911()
    aa.set_location_US()
    aa.get_m1()
    aa.signup()
    aa.denforcePI0()
    aa.all()
    aa.slp()
    aa.create()
    aa.get_m1()
    aa.slp()
    aa.account()
    aa.get_m1()
    aa.slp()
except Exception as e:
    print("输出异常信息......")
    print(e.args)
    print("------")
    print(traceback.format_exc())
    print("出现异常终止程序....卡可以继续使用.....需要更换换邮箱")
    # return "emailIsLost......"
    sys.exit()
try:
    aa.creditcards()
    # aa.get_m1()
    aa.enforcePi()
    i = 0
    l = 0
    sms = 0
    # print("变级medium...")
    aa.divaImgCaptchaLevel = "ImgMediumCaptcha"
    aa.level = "medium"
    status_sms = aa.startSMS()

    # if status_sms == 0

    while (status_sms == 0 or status_sms == 1):
        sleep(5)
        status_sms = aa.startSMS()
    if status_sms == 2:
        print("...")
        sys.exit()
    else:
        # print()
        # c = aa.get_code()
        if aa.get_code() == True:
            aa.verifySMS()
            sleep(5)
            aa.support()
            aa.urp()
            # aa.regconf()
            # aa.regconf1()
            t2 = time.time()
            print("注册用时:")
            print(t2 - t1)
            print("_____________________")
            print("输出账号密码")
            print(pwd)
            print(aa.email)
            print("_____________________")
            print(aa.card_code)
            print("_____________________")
        else:
            print("等待到最后依旧没有获取到验证码,建议用此卡再尝试一次......")
except:
    print("此次注册失败，已经伤卡,建议不要再次使用......")
