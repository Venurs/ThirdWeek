"""
捕获异常：异常的一种处理方式。程序正常的执行结束了。

语法：
try:
    有可能产生问题的代码
except 异常的类型1:
    对异常进行处理
except 异常的类型2：
    处理
except (异常类型3，异常类型4)：
    处理。。
"""
# str1 = input("请输入一个整数：")
# try:
#     num1 = int(str1) # 产生问题了：ValueError
#     sum = 10 + num1
#     res = 10 / num1  # 产生问题了： ZeroDivisionError
#     print(sum)
#     print(res)
# except ValueError:  # 问题类型
#     # 程序产生错误，会进入此处执行
#     print("输入的数据有误，无法计算。。")
#
# except ZeroDivisionError:
#     print("除数不能为零，无法计算。。")
#
# print("over..")


"""
练习1：设计一段代码：有可能产生异常。。。
"""

str1 = "hello"
try:
    for i in str1:
        print(i, end=" ")
except IndexError:
    print("下标越界了。。。")

