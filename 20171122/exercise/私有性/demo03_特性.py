"""
特性：property，词义"性质，性能"
属性：attribute，词义"属性；特质"
    类的属性特征，类的变量

    语法：
    @property，内置的装饰器，将一个方法变成一个特性。

    定义特性和定义方法类似。上边使用@property

    特性的访问和实例变量的方法相同，不需要加()
"""


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property  # 将area()，方法变为特性area。特性名：area
    def area(self):
        area = self.length * self.width
        return area


r1 = Rectangle(20, 10)
# print("面积为：", r1.area())  # 对象调用方法
print(r1.area)
