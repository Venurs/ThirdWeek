"""
写出数据：

aaa.txt中写数据。
    io.UnsupportedOperation: not writable。没有写的权限。
open(filename，mode，encoding="gbk")
mode：文件打开的模式
    默认：rt：read，text-->只读文本模式打开

write(字符串)，写出数据
writelines(参数)，参数-->字符串，写出数据
"""
# file = open(r"C:\Ruby\pro\aaa.txt", mode="w")  # 打开文件，光标在文件开头，覆盖之前的数据
# file.write("hello")
# file.write("abcd")
# file.close()
#
# file2 = open(r"C:\Ruby\pro\aaaa.txt", mode="a")  # append，追加。打开文件，光标在文件的末尾，追加写入数据，不覆盖
# file2.write("hello")
# file2.write("world")
# nums = ("a","b","c","d")
# # file2.write(nums)  # TypeError: must be str, not tuple
# # 方法一：遍历元组
# # 方法二：str()
# str1 = str(nums)
# print(str1)
# file2.write(str1)
# # 方法三：writeline(参数)-->合并为一个字符串，再写出
# file2.writelines(nums)
# file2.write("\n")
# file2.write("memeda")
# file2.close()

"""
练习1：通过写出的方法：写出26个字母。
练习2：写出一首诗。
今古河山无定据，画角声中，牧马频来去。满目荒凉谁可语？西风吹老丹枫树。
从来幽怨应无数？铁马金戈，青冢黄昏路。一往情深深几许？深山夕照深秋雨。
练习3：对比：
    r，w，a
    r+，w+，a+
"""

file = open("demo2.txt", mode="w+")
for i in range(97, 123):
    file.write(chr(i))
file.write("\r蝶恋花.出塞\r")
file.write("今古河山无定据，画角声中，牧马频来去。\n")
file.write("满目荒凉谁可语？西风吹老丹枫树。\n")
file.write("从来幽怨应无数？铁马金戈，青冢黄昏路。\n")
file.write("一往情深深几许？深山夕照深秋雨。\n")

# file.close()
# file = open("demo2.txt", mode="r")
while True:
    content = file.readline()
    if not content:
        break
    print(content, end="")

file.close()


