"""
创建一个车类，提供属性：颜色，速度。方法：移动()。停止()。
创建两个子类：自行车，跑车。
分别新增属性和方法。
创建对象，进行测试。
"""


class Capport:

    def __init__(self, color, speed):
        self.__color = color
        self.__speed = speed

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed

    color = property(get_color, set_color)
    speed = property(get_speed, set_speed)

    def move(self):
        print("车子移动。。。。")

    def stop(self):
        print("车子停止")


class Bicy(Capport):

    def __init__(self, color, speed, weight):
        super(Bicy, self).__init__(color, speed)
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight

    weight = property(get_weight, set_weight)

    def tui(self):
        print("自行车是可以推得吧")


class SportCar(Capport):

    def __init__(self, color, speed, price):
        super(SportCar, self).__init__(color, speed)
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    price = property(get_price, set_price)

    def run_fast(self):
        print("跑得快")


b = Bicy("黑色", 20, 100)
b.speed = 30
print(b.speed)

s = SportCar("黄的", 300, "贼贵")
s.price = "更贵"
print(s.price)
