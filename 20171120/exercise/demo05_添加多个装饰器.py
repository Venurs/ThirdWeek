"""
装饰器：
    定义一个装饰函数(原始函数)
        内层函数：增强原始函数的功能。return 内层函数

添加多个：
"""
def strong1(fun):
    def new_hello():
        print("装饰器1，新增功能。。。")
        fun()

    return new_hello


def strong2(fun):
    def new_hello2():
        print("装饰器2，新增功能，巴拉巴拉。。。")
        fun()

    return new_hello2


# @strong2
# @strong1
def hello():
    print("原始 函数：hello。。")

# hello()

print("-------")
hello = strong1(hello)   # hello = new_hello1
hello = strong2(hello)  # hello = new_hello2
hello()


# hello = strong2(strong1(hello))