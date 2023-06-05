class Admin:
    def __init__(self):
        self.adminU = "admin"
        self.adpwd = 123456

    def printAdminView(self):
        print("="*20)
        print("欢迎使用银行管理系统")
        print("="*20)

    def printFunctionView(self):
        print("""
        """)

    def adminOption(self):
        pass


class ATM:
    def __init__(self, alluser):
        self.alluser = alluser

    def randomiCardId(self):
        pass

    def creatUser(self):
        pass

    def checkpwg(self):
        pass

    def lockCard(self):
        pass

    def searchUser(self):
        pass

    def getMoney(self):
        pass

    def saveMoney(self):
        pass

    def transferMoney(self):
        pass

    def unlockCard(self):
        pass


class Card:
    def __init__(self, cardid, cardpwd, money, cardlock):
        self.cardID = cardid
        self.cardPwd = cardpwd
        self.money = money
        self.cardLock = cardlock


class User:
    def __init__(self, name, userid, phone, card):
        self.name = name
        self.id = userid
        self.phone = phone
        self.card = card


class HomePage:
    def __init__(self, alluserd, atm, admin):
        self.allUserD = alluserd
        self.atm = atm
        self.admin = admin

    def saveUser(self):
        pass

    def main(self):
        pass

