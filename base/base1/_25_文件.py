# read 一次性读取所有文件内容
file = open("/Users/wjj/Desktop/测试专用.txt")
txt = file.read()
print(txt)
file.close()
# 一行一行读
file = open("/Users/wjj/Desktop/测试专用.txt")
while True:
    text = file.readline()
    if not text:
        break
    print(text)
file.close()

