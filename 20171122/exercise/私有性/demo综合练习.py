"""
1.设计一个Game类："连连看"
	2.属性
		定义一个类属性：top_score,记录游戏的历史最高分
		定义一个实例属性：player_name，记录当前游戏的玩家姓名
	3.方法
		静态方法：show_help显示游戏帮助信息
		类方法：show_top_score，显示历史最高分
		实例方法：start_game，开始当前玩家的游戏
	4.主程序的步骤
		1) 查看帮助信息
		2) 查看历史最高分
		3) 创建游戏对象，调用方法
"""
class Game:

    # 定义类属性，描述该游戏的最高分
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    # 定义静态方法
    @staticmethod
    def show_help():
        print("显示帮助信息：玩的好就玩的好，玩不好，就再来，不行重启机器。。")

    # 定义类方法
    @classmethod
    def show_top_score(cls):
        print("本游戏的最高分是：%d" % cls.top_score)

    # 定义实例方法
    def start_game(self):
        print("%s，可以开始游戏啦。。。" % self.player_name)


Game.show_help()
Game.show_top_score()
player1 = Game("王二狗")
player1.start_game()  # 相当于player1.start_game(player1)