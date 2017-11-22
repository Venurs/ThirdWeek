"""
私有方法：
    不让外部直接调用

    注意点
        1.如果本类中有一个公有方法，该公有方法中，可以访问私有属性和私有方法。
"""
class Woman:

    def __init__(self, name):
        self.name = name
        self.__age = 18

    # 私有方法：不允许外部调用
    def __secret(self):
        print("偷偷的告诉你一个小秘密：%s，的年龄是%d" % (self.name, self.__age))

    # 定义类中的公有方法，因为是本类中，既可以访问私有属性，也可以访问私有方法。
    def test(self):
        print("我是类中的一个非私有的方法(公有方法)，姓名：%s，年龄：%d" % (self.name, self.__age))
        self.__secret()


p1 = Woman("如花")
print(p1.name)
# print(p1.__age)  # 私有属性，不允许外部直接访问
# p1.__secret()  # 私有方法，不允许外部直接访问
p1.test()

# 扩展：python没有真正的私有。
# 私有化的处理：将属性名，或者方法名，进行处理，导致外部无法访问。处理方式：_类名
print(p1._Woman__age)  # 强烈不建议使用
