"""
定义一个bool类型的变量，用于开启和关闭装饰器
    on：
        True：使用装饰器
        False：不用
"""
on = True


def strong(fun):

    if on:  # 如果on的值，是True，表示开启装饰器
        def new_hello():
            print("新增功能。。。")
            fun()
            print("新增功能。。")

        return new_hello
    else:
        return fun  # 不开启装饰器



@strong
def hello():
    print("我是hello，你是二狗么。。")


# hello = strong(hello)  # hello= new _hello,, hello = hello
# hello()
hello()
