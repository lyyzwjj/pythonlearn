def say():
    print("hello python")


# 测试模块
if __name__ == "__main__":
    print(__name__)
    print("别人开发的模块")
    say()

import hm_message

hm_message.send_message.send("你好啊")
txt = hm_message.receive_message.receive()
print(txt)
