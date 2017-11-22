"""
士兵突击
1.士兵许三多有一把AK47
2.士兵可以开火
3.枪能够发射子弹
4.枪装填子弹，增加子弹数量
士兵：类
姓名
开火()

许三多：对象

枪：类
ak47：对象
发射子弹()
装子弹()
"""


class Solider:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def fire(self):
        print("开火")


class Gun:

    def __init__(self, name):
        self.__name = name

    def send(self):
        print("发射")

    def push(self):
        print("装填")
