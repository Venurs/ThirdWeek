"""
复制一个文本
"""
english = open("english.txt", mode="r+")
english_copy = open("english_copy.txt", mode="w+")
content = english.read()
english_copy.write(content)
english.close()
english_copy.close()

