"""
继承中的init()方法
    1.如果子类没有手动的调用__init__()，那么会自动调用父类的__init__()
    2.如果子类自己手动的调用__init__(),那么不会自动调用父类，需要自己也手动调用。

惯性写法：
    父类中：__init__()
                self.父类的属性
    子类中：__init__()
            super().__init__(),创建父类的属性
            self.子类属性= 数值


如果子类中没有新增的属性，那么子类不用手动添加__init__(),会自动调用父类的
如果子类中有新增的属性，子类中手动添加__init__(),里面手动调用父类的__init__()
"""
class Person:

    def __init__(self, name, age):
        print("父类的init方法。。")
        self.name = name
        self.age = age

class Student(Person):

    def __init__(self, name, age, school):
        print("子类的init方法。。。")
        # name，age其实已经抽象到父类的声明中。需要手动的调用父类的init(),
        super().__init__(name, age)
        # Person.__init__(self, name, age)
        self.school = school


# p1 = Person()  # 父类对象
# s1 = Student()  # TypeError: __init__() missing 2 required positional arguments: 'name' and 'age'
s2 = Student("王二狗", 18, "蓝翔技校")
print(s2.name)  # 访问父类属性
print(s2.age)  # 访问父类属性
print(s2.school)  # 访问子类的属性