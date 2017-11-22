"""
多继承：
    子类，具有多个父类的情况。子类有多个父类的功能。

    注意点：有些语言只允许单继承(子类只能有一个父类。多层继承)

python：
    支持多继承：多个爹
    也支持多层继承(继承的传递)：爹，爷爷，太爷爷。。。。祖宗
"""
class A:
    def fun1(self):
        print("A类的fun1方法。。")

class B(A):
    def fun2(self):
        print("B类的fun2 方法。。")

    def fun1(self):  # 重写
        print("B类重写A类的fun1方法。。")

class C(B):
    def fun3(self):
        print("c类的fun3方法。。")


a = A()
a.fun1()
print("--------")
b = B()
b.fun1()
b.fun2()

print("------")
c = C()
c.fun1()  # 访问爷爷的方法
c.fun2()  # 访问父类的方法
c.fun3()  # 访问子类新增的方法

print("-" * 50)
# 多继承：
