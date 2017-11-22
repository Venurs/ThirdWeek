"""
父类的私有属性和方法
    私有的属性和方法：不允许外部直接访问。
        注意点：通过类的公有方法可以偷偷的访问私有属性和私有方法。


    子类继承父类：
        子类中不允许直接的访问父类的私有属性和私有方法。
        只允许访问公有的属性和方法。
        注意点：如果父类的公有方法中，有私有属性和私有方法，其实也可以访问。
"""
class A:

    def __init__(self):
        self.num1 = 100  # 定义一个公有属性
        self.__num2 = 200  # 定义一个私有属性，本类中使用

    def __test1(self):
        print("父类中的私有方法。。访问父类的属性：num1 = %d，num2 = %d" %( self.num1, self.__num2))

    def test2(self):
        print("父类的公有方法。。")

    def test3(self):
        print("父类的私有属性：%d" % self.__num2)
        self.__test1()


a = A()  # num1，num2，  num2私有，外部不让访问，类里能访问
a.test3()


class B(A):

    def fun(self):
        # 1.能否访问父类的私有属性：不能
        # print("尝试访问父类的私有属性：%d " % self.__num2 )

        # 2.能否访问父类的公有属性：能
        # print("尝试访问父类的公有属性：%d" % self.num1)

        # 3.能否访问父类的私有方法：不能
        # self.__test1()

        # 4.能够访问父类的公有方法
        # self.test2()
        self.test3()


b = B()
b.fun()







