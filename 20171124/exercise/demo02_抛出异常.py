"""
异常：
    程序执行过程中，不正常：python解释器创建了这种类型异常的对象：
        异常 的对象。

异常类型：class
Exception
ValueError
。。

抛出异常：raise
    程序中主动抛出一个异常对象。

    需求：接收用户输入的密码，长度至少为8。否则抛异常
1.接收用户输入
2.密码判断长度
3.少于8，主动抛出一个异常对象
    创建对象
"""
# 定义一个函数，用于接收用户输入的密码
def input_password():
    # 1.接收用户的输入
    pwd = input("请输入密码：")
    # 2.判断密码长度是否小于8
    if len(pwd) >= 8:
        return pwd

    # 3.否则，产生异常对象并抛出
    print("主动抛出异常。。")
    # 创建异常对象
    e1 = Exception("密码长度不够")
    # 抛出异常对象
    raise e1

# 测试
try:
    res = input_password()
    print("得到的数据：%s" % res)
except Exception as result:
    print("报错啦。。%s " % str(result))

