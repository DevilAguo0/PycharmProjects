import time  # 导入time module


def sing():
    for i in range(3):
        print("唱歌..")
        time.sleep(0.5)


def dance():
    for i in range(3):
        print("跳舞..")
        time.sleep(0.5)


sing()
dance()
