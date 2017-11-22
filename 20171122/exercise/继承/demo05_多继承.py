"""
多继承：
    子类可以同时拥有多个父类的功能

    注意点：不要在两个父类中使用同名的方法。
    __mro__属性：(method resolution order),子类访问某个方法的时候，搜索的顺序,C3算法。
"""


class A:
    def fun1(self):
        print("A类的fun1.。")

    def test1(self):
        print("A类的test1方法。。")


class B:
    def test1(self):
        print("B类的test1方法。。")


class C(A, B):
    pass


c = C()
c.fun1()  # 访问父类A的方法
c.test1()  # 访问父类B的方法

print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

