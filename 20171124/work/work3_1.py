"""
读取message.txt。世界杯的信息。键盘上输入年份，输出对应的举办地和冠军国。如果没有举办，就输出没有举办
思路：读取本地文件的数据：
[],{}
"""

# 这个撒懒，结果判断不了没有举办


# def product_list():
#     file = open("message.txt", mode="r")
#     list2 = []
#     while True:
#         content = file.readline()
#         if not content:
#             break
#         list2.append(str(content).split("|", 3))
#     file.close()
#     return list2

#
# list2 = product_list()
# while True:
#     year = input("请输入查询年份：")
#     for li in list2:
#         if li[0] == year:
#             print("举办国家是%s 冠军国家是%s" % (li[1], li[2]))


def product_list():
    file = open("message.txt", mode="r")
    list2 = []
    while True:
        content = file.readline()
        if not content:
            break
        list2.append(str(content).split("|", 1))
    file.close()
    return list2


list2 = product_list()
dict1 = dict()
for li in list2:
    dict1[li[0]] = li[1]
while True:
    year = input("请输入年份：")
    if year in dict1.keys():
        list1 = dict1.get(year).strip("\n").split("|")
        print("举办国家是%s 冠军国家是%s" % (list1[0], list1[1]))
        # break
    else:
        print("这一年未举办")






