"""
装饰器：如果一个函数的定义已经完成。需要在不修改该函数的情况下，进行功能的扩展。
    使用装饰器

函数式编程：函数的功能强大：函数可以看成变量，作为参数，作为返回值。。高阶函数，闭包。。。

耦合性：藕断丝连
    低耦合：降低程序的耦合性。

设计程序：开放，封闭
    封闭：对于已经实现好了的功能进行封闭。
    开放：对扩展开放

思路步骤：
step1：定义一个原始函数：hello()

step2：定义一个装饰器函数：应用闭包
def strong(fun):
    def new_xxx():
        # 新增功能。。。
        fun()

    return new_xxx


分析原理：hello = strong(hello)

使用：在原始函数上添加：@装饰器函数名即可

"""
# 2.定义装饰器函数
def strong(fun):

    # 定义一个内层函数，用于增强fun函数的功能
    def new_hello():
        print("我是装饰器中的新增功能，，before。。")
        fun()  #hello()，调用原来的功能，(可以根据需求可有可无)。
            # 如果有，就相当于在原功能上扩展，如果没有，将原功能重新实现
        print("我是装饰器中的新增功能，，after。。")

    return new_hello

# 1.先定义一个函数
@strong  # 理解为strong(hello)
def hello():
    print("hello，王二狗。。这是hello函数中的代码")


# hello = strong(hello)  # hello = new_hello
# hello()

hello()

@strong  # 理解为strong(test)
def test():
    print("另一个函数。。。")


test()