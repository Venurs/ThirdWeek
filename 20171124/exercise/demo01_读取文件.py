"""
step1：打开文件
    表示和文件建立连接

step2：读取数据，写出数据

step3：关闭文件
    断开连接
"""
# 1.打开文件
# open("demo1.txt")  # 相对路径：当前程序本身。
# file1 = open("C:\Ruby\pro\demo1.txt")
#
# # 2.读取文件的内容
# content = file1.read()
#
# print(content)
#
# # 3.关闭文件
# file1.close()

"""
读取文件：
    绝对路径的文件
    相对路径的文件
"""


file1 = open("test.txt")
content = file1.read()
print(content)
file1.close()

