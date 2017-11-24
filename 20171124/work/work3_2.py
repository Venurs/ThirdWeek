"""
模拟聊天记录
循环读取键盘输入，保存到本地文件中。小明，小红
"""
chat = open("wechat.txt", mode="w")
sign = True
while True:
    if sign:
        wechat = input("小明：")
        wechat = "小明：" + wechat + "\n"
    else:
        wechat = input("小红：")
        wechat = "小红：" + wechat + "\n"
    sign = not sign
    if wechat.endswith("。。。\n"):
        chat.write(wechat)
        print("对方不想和你聊天，即将退出。。。")
        break
    chat.write(wechat)
chat.close()
