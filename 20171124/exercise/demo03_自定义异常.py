"""
自己定义异常：自己定义一个类，继承Exception或Error。具有了异常类的功能
    异常类：产生的对象，异常对象，能够通过raise关键字抛出，并且打断程序的执行

异常类：Exception

普通类：Person

自定义类：

"""
# 定义一个函数，接收用户的密码，密码长度小于10，抛出异常：要求的长度，接收的数据的长度
# 1.定义异常类
class ShortInputException(Exception):

    def __init__(self, length, at_least):
        self.lenght = length  # 定义异常类的属性，表示接收到的数据的长度
        self.at_least = at_least  # 定义异常类的属性，表示要求的长度

def input_password():
    pwd = input("请输入密码：")

    at_least = 10

    if len(pwd) >= at_least:
        return pwd

    # 主动抛出异常的对象
    e1 = ShortInputException(len(pwd), at_least)
    raise e1

try:
    res = input_password()
    print("密码是：%s" % res)
except ShortInputException as result:  # rsult封装产生异常的信息：e1
    print("报错啦。。ShortInputException：输入的长度：%d，要求的长度：%d" % (result.lenght, result.at_least))
