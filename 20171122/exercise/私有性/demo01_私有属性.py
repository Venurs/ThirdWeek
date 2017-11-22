"""
私有： 只能在类中使用，类的外部不能使用
    语法：属性或方法，前边加双下划线，就是表示私有的。

    私有属性：__属性名。
        只能本类中使用
"""
class Person:

    def __init__(self, name):
        self.name = name
        self.__age = 0  # 私有的，本类中使用

    # 为私有属性进行赋值
    def set_age(self, age):
        if age < 0 or age > 200:
            print("年龄不合法，无法赋值")
            return
        else:
            self.__age = age

    # 提供获取私有属性数值的方法
    def get_age(self):
        return self.__age


p1 = Person("王二狗")
print(p1.name)

p1.set_age(-30)
print(p1.get_age())
