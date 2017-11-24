"""
复制一个大视频：循环
"""
video = open(r"D:\python文档\20171121(面向对象视频)\day12_01_面向对象的概念&类和对象.wmv", mode="rb")
video1 = open(r"D:\python文档\20171121(面向对象视频)\复制版day12_01_面向对象的概念&类和对象.wmv", mode="ab")
for vid in video:
    video1.write(vid)
video.close()
video1.close()


