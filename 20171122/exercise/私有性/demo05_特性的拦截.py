"""
特性的用法二：
    用法一：类中定义特性：
        特性名 = property(getxx,setxx)
    用法二：特性的拦截
        A：@property
            def 特性名(self)
                return 特性值

            当外部：通过对象.特性名，表示要获取特性的数值。那么自动执行到此处
        B：@特性名.setter
            def 特姓名(self, 参数)--->set_xxx()
                self._特信命= 参数。表示赋值

            当外部：通过对象.特性名= 数值，表示要对特性进行赋值。那么自动执行此处

        额外增加：
        C：@特姓名.getter
            功能也是获取特性的数值
        D：@特姓名.deleter
            功能是：外部 通过del 对象.特性 时，自动执行此处。


类：
    属性：
        类属性
        实例属性
    方法
        实例方法
        类方法
        静态方法

一：属性
    对象.属性名= 数值---->对属性进行赋值
    对象.属性名---->获取属性值


二：属性私有
        属性私有：__age
            不允许外部直接访问：如何赋值和取值？

            类：提供set_age(),get_age()

            赋值：
                对象.属性 = 数值
                    --->对象.set_age(数值)

            取值：
                对象.属性
                    --->对象.get_age()

三：特性：对应了某一个方法
    本质：类中的实例方法

    用法：同类中的属性相同

    对象.特性---->同对象.属性
        区别：
            对象.属性
                对象.属性= 数值
                对象.属性

            对象.特性
                对象.特性 = 数值
                    --->执行对应setxxx()
                对象.特性
                    --->执行对应getxxx()
    方法一：
        特姓名= property(参数1，参数2)
            参数1：必须get_age
            参数2：必须set_age

    方法二：
        @property
        def 特性名(self):
            获取数值
        @特性名.setter
        def 特姓名(self, 参数):
            进行赋值

        @特姓名.getter
        def 特姓名(self):
            获取数值
        @特性名.deleter
        def 特性名(self):
            删除特性：del self.特性名

"""
class Person:

    def __init__(self, name):
        self.name = name  # 定义实例属性

    @property  # 定义一个特性,注意点：self._特性名
    def age(self):
        print("特性的访问。。")
        return self._age

    # 设置，特性的拦截器：语法@特性名.setter
    # 功能：当使用对象.特性名= 数值。本意是要进行赋值操作。那么会自动执行此处
    @age.setter
    def age(self, age):
        print("age.setter....赋值的方法。。")
        self._age = age

    # 使用@特性名.getter
    # 功能：当外部：对象.特性--->获取特性的数值，那么执行此处。如果没有设置@特性名.getter，那么就执行@property
    @age.getter
    def age(self):
        print("age.getter...获取数值")
        return self._age

    # 使用@age.delete,表示删除某一个特性
    # 功能：外部通过调用：del  对象.特性，自动 执行此处
    @age.deleter
    def age(self):
        print("删除特性。。。。")
        # del self._age


p1 = Person("王二狗")
# p1.age  # 对象.属性-->获取数值。对象.属性= 数值

p1.age = 30  # 对象.特性 = 数值--->相当于执行setxxx进行赋值，自动调用
print(p1.age)  # 对象.特性，相当于获取特性的结果。自动调用 定义特性的方法

del p1.name  # 删除对象的属性，普通的属性
# print(p1.name)



# del p1.age  # AttributeError: can't delete attribute
del p1.age  # 就会自动的执行@特姓名.delete
print(p1.age)



# del,删除， 被删除的内容，在内存中销毁。
# 列表：pop(index), remove(元素),del 列表名[index]
# 字典：无序的名值对的组合：{}。del 字典名["key"]
# 对象 del 对象名