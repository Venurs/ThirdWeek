"""
1.read()-->读取文件中的所有的数据。并返回。
2.read(num)-->num表示要读取的数据量个数。
3.readline(),读取一行
4.readlines()，按照行读取数据，存入一个列表中，返回该列表。
5.for循环，效率更高
"""
# file1 = open(r"C:\Ruby\pro\demo1.txt")
#
# content = file1.read(10)  # 读取10个数据
# print(content)
#
# content = file1.read(20)  # 接着读取20个数据
# print(content)
#
# content = file1.read()  # 读取剩余所有
# print(content)
#
# content = file1.read()  # content = ""
# print("-->", content)
#
# file1.close()
# print("-" * 50)
# """
# 读取一个文件，每次读取10个数据。循环读取，直到读取完毕。关闭文件。
# """
# file2 = open(r"C:\Ruby\pro\demo1.txt")
# while True:
#     content = file2.read(10)
#
#     # if content == "":
#     if not content:
#         break
#
#
#     print(content)
# file2.close()
#
# """
# ord(a)-->97
# chr(97)-->a
# """
#
# print("-" * 50)
# file3 = open(r"C:\Ruby\pro\demo1.txt")
# line = file3.readline()
# print(line)
# line = file3.readline()
# print(line)
# line = file3.readline()
# print("-->", line)
# file3.close()

"""
练习2：使用readline()读取一行。循环读取完毕。
练习3：使用readllines(),读取一个列表。
练习4：使用for。。in循环读取
"""

# file4 = open(r"C:\Ruby\pro\demo1.txt")
# list1 = file4.readlines()
# print(list1)
#
# file5 = open(r"C:\Ruby\pro\demo1.txt")
# for line in file5:  # 原理：对于file5对应的文件demo1.txt。每次循环都是读取一行。
#     print(line)
# file5.close()


file = open("demo1.txt")
# while True:
#     line = file.readline()
#     if not line:
#         break
#     print(line)


list1 = file.readlines()
print(list1)


# while True:
#     list = file.readlines(1)
#     if not list:
#         break
#     print(list)

# for line in file:
#     print(line, end="")


file.close()


