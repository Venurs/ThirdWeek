"""
.读取english.txt文件中的数据，并打印输出
"""

english = open("english.txt", mode="r")
print(english.read())
english.close()
