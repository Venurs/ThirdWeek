"""
单例模式：目的，让一个类在内存中只能产生一个对象
    核心：对象的创建过程
        step1：开辟内存，创建对象--->new
        step2：自动执行init方法，用于初始化实例变量

    单例的操作步骤：
        1.重写new方法
            A：在类中添加类属性__instance，用于控制对象的的产生
                如果__instance为空，创建对象：object类的new：object.__new__(cls)，并且将值返回给__instance
                如果不为空，直接返回__instance

            B：让init，初始化实例变量时，仅依次
                定义一个类属性：__first_init = False
                如果__first_init 为False，证明没有初始化属性，那么就执行，修改为True
                如果__first_init 为True，直接return。
"""


class MusicPlayer:

    # 定义一个类属性：
    __instance = None
    # 定义一个类属性：用于控制init是否是初次执行
    __first_init = False

    # 重写new方法
    def __new__(cls, *args, **kwargs):
        # 1.判断类属性是否是None，证明内存中没有创建过，那么就创建
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        # 2.返回
        return cls.__instance

    def __init__(self, name):
        if MusicPlayer.__first_init:
            return

        print("init方法。。。")

        self.name = name

        MusicPlayer.__first_init = True


player1 = MusicPlayer("网易云")
player2 = MusicPlayer("网易云")
print(player1)
print(player2)