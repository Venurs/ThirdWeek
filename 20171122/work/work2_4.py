"""
创建Person类。属性：姓名，年龄。方法：显示信息。
创建两个子类：学生和工人。分别新增属性成绩和工资。
"""


class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    name = property(get_name, set_name)
    age = property(get_age, set_age)

    def show(self):
        print(self.__name, self.__age, end=" ")


class Student(Person):

    def __init__(self, name, age, school):
        super(Student, self).__init__(name, age)
        self.__school = school

    def get_school(self):
        return self.__school

    def set_school(self, school):
        self.__school = school

    school = property(get_school, set_school)

    def show(self):
        super(Student, self).show()
        print(self.__school)


class Worker(Person):

    def __init__(self, name, age, factory):
        super(Worker, self).__init__(name, age)
        self.__factory = factory

    def get_factory(self):
        return self.__factory

    def set_factory(self, factory):
        self.__factory = factory

    factory = property(get_factory, set_factory)

    def show(self):
        super(Worker, self).show()
        print(self.__factory)


stu = Student("小沫沫", 20, "中北")
stu.show()

wor = Worker("明明", 25, "搬砖")
wor.show()
