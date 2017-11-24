"""
异常的传递：当函数中产生异常，函数本身可以处理。如果没有处理，异常对象传递给了调用处。
    调用处应该进行处理，如果调用处没有处理。主函数也没有处理，打断程序的执行。

1.fun1（）
    产生异常

2.调用处：
    如果方法中产生异常，没有处理。交给调用处进行处理。

    fun2()-->

    主函数
"""
# # 1.定义一个函数
# def fun1():
#     num1 = int(input("请输入一个整数："))  # 阻塞式：
#     return num1
#
# def fun2():
#     return fun1()
#
#
# try:
#     res = fun2()  # res = num1
#     print("输出结果：%d" % res )
# except Exception as result:
#     print("报错啦，，%s" % str(result))


"""
练习1：设计一个函数：foo()
    可能产生异常：
    
设计一个函数：test1():
    尝试调用foo()
    
主函数中：调用test1()
    对异常进行处理：try。。except
    
    
练习2：针对于以上情况
    foo()中，异常进行处理。。
"""


def foo():
    num1 = int(input())
    num2 = int(input())
    return num1, num2


def test1():
    num1, num2 = foo()
    print(num1 / num2)


if  __name__ == '__main__':
    try:

        fun = test1()

    except Exception as result:
        print("出错了", result)



