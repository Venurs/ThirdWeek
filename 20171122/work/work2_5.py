"""
多态的使用
有三种动物：狗、猫、猪，
父类：动物、
子类：狗、猫、猪
动物的属性：动物的名字
动物的方法是eat（就是打印自己的名字）
有一个饲养员：饲养员
饲养员的方法：feed_animal(需要饲养的动物)
函数的实现是（其实就是调用动物的eat方法）
"""


class Animal:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    name = property(get_name, set_name)

    def eat(self):
        print("动物")


class Feeder:

    @staticmethod
    def feed_animal(cls):
        print("要养的动物是%s" % cls.name)


class Dog(Animal):

    def eat(self):
        print("狗")


class Cat(Animal):

    def eat(self):
        print("猫")


class Pig(Animal):

    def eat(self):
        print("猪")


animal = Animal("动物")
print(animal.eat())

dog = Dog("狗")
print(dog.eat())

Feeder.feed_animal(dog)



