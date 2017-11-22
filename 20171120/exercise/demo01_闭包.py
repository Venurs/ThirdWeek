"""
什么是闭包？
    外层函数嵌套里层函数，在里层函数中如果访问了外部函数的局部变量，那么该局部变量和里层函数统一称为闭包。
        里层函数也叫作闭包函数

    1.闭包函数可以访问外层函数的局部变量。即使外层函数调用已经结束，对于闭包函数，依然可以访问外层函数的局部变量。
    2.闭包函数在访问外层函数的局部变量时，总是访问该变量的最新值。
"""

def outer1():
    # 外层函数的局部变量
    x = 20

    # 定义一个里层函数
    def inner1():
        # 添加一个标记，标记x是外层函数的变量。
        nonlocal x
        x = x + 10
        return x

    return inner1  # 返回的整个里层函数对象，在外部可以继续调用该返回值所表示的内层函数。
    # return inner1()  # 这个返回的是里层函数调用后的结果数值。

res = outer1()
print(res)
print(type(res))  # <class 'function'>,是一个函数
# 第一次调用res函数，其实就是调用outer1的内层函数inner1
num1 = res()
print(num1)  # 打印输出内层函数的return值：x= 30

# 第二次调用res函数，表示再次执行内层函数，inner1
num2 = res()
print(num2)  # 打印内层函数的return值，x = 40
print(res())
print(outer1())


# resu = outer1()
# print(resu())
# print(resu())
# print(resu())


