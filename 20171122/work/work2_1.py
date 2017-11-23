"""
.西游记:3个徒弟

类：父类：唐僧的徒弟
name，age，吃饭，取经，

子类：
孙悟空：name，age，武器，吃饭，取经，除妖。。。

猪八戒：name，age，属性：字符串媳妇，吃饭，取经，牵马。。

沙和尚：name，age，属性：流沙河，吃饭，取经，挑行李。。。
"""


#  唐僧徒弟类
class TPrantice:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    def eat(self):
        print("吃饭")

    def buddhist_scriptures(self):
        print("取经")


#  孙悟空类
class Monkey(TPrantice):

    def __init__(self, name, age, weapon):
        super(Monkey, self).__init__(name, age)
        self.__weapon = weapon

    @property
    def weapon(self):
        return self.__weapon

    @weapon.setter
    def weapon(self, weapon):
        self.__weapon = weapon

    def kill_monster(self):
        print("孙悟空杀妖", end=" ")


#  猪八戒类
class Pig(TPrantice):

    def __init__(self, name, age, girlfriend):
        super(Pig, self).__init__(name, age)
        self.__girlfiend = girlfriend

    @property
    def girlfriend(self):
        return self.__girlfiend

    @girlfriend.setter
    def girlfriend(self, girlfriend):
        self.__girlfriend = girlfriend

    def lead_horse(self):
        print("八戒牵马", end=" ")


#  沙僧类
class MonkSha(TPrantice):

    def __init__(self, name, age, river):
        super(MonkSha, self).__init__(name, age)
        self.__river = river

    @property
    def river(self):
        return self.__river

    @river.setter
    def river(self, river):
        self.__river = river

    def boot(self):
        print("沙僧挑行李", end=" ")


tp = TPrantice("唐僧的徒弟", 800)
tp.name = 200
print(tp.name)

monkey = Monkey("猴子", 800, "棍子")
print(monkey.weapon, monkey.kill_monster())


pig = Pig("猪", 800, "高小兰")
print(pig.girlfriend, pig.lead_horse())


monksha = MonkSha("沙僧", 800, "流沙河")
print(monksha.river, monksha.boot())

