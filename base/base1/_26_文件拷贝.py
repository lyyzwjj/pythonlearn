"""
#小文件拷贝
file_source = open("/Users/wjj/Desktop/测试专用.txt")
file_target = open("/Users/wjj/Desktop/测试专用copy.txt","w")
txt = file_source.read()
file_target.write(txt)
file_source.close()
file_target.close()
"""
# 大文件拷贝
file_source = open("/Users/wjj/Desktop/测试专用.txt")
file_target = open("/Users/wjj/Desktop/测试专用copy.txt","w")
while True:
    text = file_source.readline()
    if not text:
        break
    file_target.write(text)

file_source.close()
file_target.close()
