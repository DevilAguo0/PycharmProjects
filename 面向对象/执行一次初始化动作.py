class MusicPlayer(object):
    instance = None
    init_flag = False  # 定义一个类属性作标记，记录一下是否进行过初始化

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    #  目的：执行一次初始化动作
    def __init__(self):
        #  判断是否执行过初始化动作
        if MusicPlayer.init_flag:  # 注意这里,MusicPlayer 默认为True
            return
        #  如果没有执行过，再执行初始化
        print("初始化音乐播放器")

        #  修改类属性的标记
        MusicPlayer.init_flag = True


mucic1 = MusicPlayer()
print(mucic1)
music2 = MusicPlayer()
print(music2)
