"""
需求：
    如花和自己的宠物花花(小猫)玩
    如梦和自己的宠物啸天(狗狗)玩
    如歌和自己的宠物，兔子(玉兔)

分析：
定义女孩类，
    name属性
    play_with_pet(宠物),和自己的宠物玩

定义父类：Pet类
    name属性：
定义子类：Cat类，Dog类
"""


class Girl:

    def __init__(self, name):
        self.name = name

    def play_with_pet(self, pet):
        print("%s,和自己的宠物%s，在玩。。" % (self.name, pet.name))
        pet.eat()
        pet.sleep()
        if isinstance(pet, Dog):
            pet.look_door()


class Pet:  # 宠物的父类

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("%s,开始吃东西啦。" % self.name)

    def sleep(self):
        print("%s,玩累了，休息一下。。" % self.name)


class Cat(Pet):

    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def eat(self):  # 重写方法
        print("%s,小猫吃鱼。。" % self.name)


class Dog(Pet):

    def look_door(self):
        print("%s,小狗看门。。" % self.name)


g1 = Girl("如花")
c1 = Cat("花花", "白色")
g1.play_with_pet(c1)

g2 = Girl("如梦")
d1 = Dog("啸天")
g2.play_with_pet(d1)

