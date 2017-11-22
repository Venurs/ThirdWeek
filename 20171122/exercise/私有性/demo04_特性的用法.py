"""
特性的用法：
    方法一：对私有属性的操作
        将私有属性设置为特性
            使用：定义一个特性
                特性名= property(getxxx,setxxx)

            对象.特性名 = 数值。意味着要为特性进行赋值。那么会自动调用setxxx
            对象.特性名，意味着是获取特性的数值，那么自动调用getxxx
"""


class Person:

    def __init__(self, name):
        self.name = name
        self.__age = 0  # 私有属性

    def set_age(self, age):
        print("set_age()..被执行了。。")
        self.__age = age

    def get_age(self):
        print("get_age()...被执行了。。。")
        return self.__age

    # 设置age为特性
    # 特性名= property(get,set)
    age = property(get_age, set_age)


p1 = Person("王二狗")
# 对于私有属性的操作，需要调用方法：set_age(),get_age(),
# 为age进行赋值：p1.age = 数值
# p1.set_age(30)
# 获取age的数值：print(p1.age)
# print(p1.get_age())

p1.age = 40  # 自动的执行set_age()
print(p1.age)  # 自动调用get_age
