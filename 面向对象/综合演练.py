class Game(object):
    top_score = 0  # 类属性

    def __init__(self, player_name):
        self.player_name = player_name  # 实例属性

    @staticmethod
    def show_help():
        print("显示帮助信息：让僵尸进入大门。")  # 静态方法

    @classmethod
    def show_top(cls):
        print("历史最高分是{}".format(cls.top_score))  # 类方法

    def start_game(self):
        print("{} 开始游戏啦！".format(self.player_name))  # 实例方法


#  1.显示游戏帮助信息
Game.show_help()
#  2. 显示历史最高分
Game.show_top()

#  3.创建对象，并开始游戏
xiaoming = Game("小明")
xiaoming.start_game()
