"""
面向对象：
    编程思想：核心：类-->对象

    三大特征：java，python，c#。。。
        封装性：
            "打包","包裹"
                电脑，电机
            面向对象编程的第一步：讲究将方法(行为功能)和属性(变量),封装到一个抽象的类中
                对象.属性
                对象.方法

            函数，方法
                将方法的细节，属性等，封装到了一个类的内部。
        继承性：
            爸爸，儿子
            类(父类，基类，超类，superclass)，类(子类，扩展类，派生类，subclass)
                存在了继承关系：子类继承父类。那么子类就可以使用父类的内容(属性，方法)

            子类是一个特殊的父类：子类 is  a  特殊的父类

            意义：
                1.提高代码的重用性.(避免重复的代码)。从子类的角度。
                2.扩展类的功能。从父类的角度。
            父类：人类：name，age，eat(),sleep()
            子类：学生类：name，age，学校名，eat(),sleep(),study()

            猫类：名字，年龄，eat(),run()，爬树()
            狗类：名字，年龄，eat(),run(),看家()

            动物类：名字，年龄，eat(),run()
            子类：猫类，狗类
        多态性


继承性：
    一个子类继承了一个父类：
    A：子类对象可以访问父类的属性和方法。(避免重复代码)
    B：子类中可以新增自己的属性和方法。(扩展子类的功能)
    C：子类还可以重写(override)父类已有的方法。(扩展子类的功能)
"""
# 1.定义一个父类
# class Person:
#
#     # 1.吃
#     def eat(self):
#         print("吃窝窝头。。")
#
#     # 2. 睡觉
#     def sleep(self):
#         print("睡觉啦。。")
#
# # 2.定义子类
# class Student(Person):  # Student类，继承自Person类。
#
#     # 1.新增方法学习
#     def study(self):
#         print("学习啦。。把你爸乐坏了。。")
#
#     # 2.重写的方法：该功能父类中已经有了，但是无法满足子类的需求。那么子类可以重新实现，就是重写。保证和父类中方法的声明一样。
#     def eat(self):
#         print("子类重写，吃炸鸡，喝啤酒。。")
#
#     # 3.重写：需要在父类的功能上进行扩展。
#     def sleep(self):
#         print("学生，睡觉之前玩手机。。。")
#         # 执行父类的sleep()
#         # 子类中表示父类：python2.x版本：父类名.父类的方法(self)
#         # python3.x版本：super().父类的方法()
#         # Person.sleep(self)
#         super().sleep()
#         print("学生，睡着了做梦也玩手机。。。")



# p1 = Person()
# p1.eat()  # 父类中的方法
# p1.sleep()
#
# print("-" * 50)
# s1 = Student()
# s1.study()  # 子类对象，访问子类新增的方法
# s1.eat()  # 子类对象，访问父类的方法
# s1.sleep()  # 子类重写方法

"""
1.创建动物类作为父类：
    eat(),sleep()
2.创建猫类作为动物类的子类
    新增方法,抓老鼠catch_mouse(),
    重写父类eat(),
3.创建狗类作为动物类的子类
    新增方法,看家look_door()
"""


class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("这是一个动物,在吃饭")

    def sleep(self):
        print("这是一个动物，在睡觉")




class Cat(Animal):

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def catch_mouse(self):
        print("这是一只猫，会抓老鼠")

    def eat(self):
        print("这是一只猫，喜欢吃鱼")


class Dog(Animal):

    def look_door(self):
        print("这是一只狗，可以看门")


a = Animal("动物", 12)
a.eat()
a.sleep()

c = Cat("猫", 2, "白色")
c.catch_mouse()
c.sleep()
c.eat()

d = Dog("狗子", 3)
d.eat()
d.sleep()
d.look_door()

