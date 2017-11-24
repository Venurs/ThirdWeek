"""
复制一个图片
"""
picture = open("图片2.jpeg", mode="rb")
picture_copy = open("复制2.jpeg", mode="wb")
while True:
    content = picture.readline()
    if not content:
        break
    picture_copy.write(content)

picture.close()
picture_copy.close()


