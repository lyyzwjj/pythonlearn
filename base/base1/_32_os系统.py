import os
import shutil

# 1.返回操作系统类型 ：posix 是linux操作系统，nt 是windows操作系统
print(os.name)
print('Linux' if os.name == 'posix' else 'Windows')

# 2.操作系统的详细信息
info = os.uname()
print(info)
print(info.sysname)
print(info.nodename)

# 3.系统的环境变量
print(os.environ)
print(os.environ.get('PATH'))  # 通过key值获取环境变量对应的value值

# 4.判断是否是绝对路径
print(os.path.isabs('/tmp/ffff'))
print(os.path.isabs('hello.jog'))

# 5.获取当前路径
print(os.getcwd())

# 6.生成绝对路径的三种方式
print(os.path.abspath('hello.png'))
print(os.path.join(os.path.abspath('.'), 'hello.jpg'))  # .表示当前路径
print(os.path.join('/home/kiosk', 'hello.jpg'))

# 7.获取目录或文件名
filename = '/Users/wjj/PycharmProjects/pythonlearn/readme.md'
print(os.path.basename(filename))
print(os.path.dirname(filename))

# 8.返回指定目录下的所有文件名和目录名 ，返回的是一个列表
print(os.listdir('/Users/wjj/PycharmProjects/pythonlearn/'))

# 9.分离后缀名和文件名
print(os.path.splitext('readme.md'))

# 10.将目录名和文件名分离
print(os.path.split('/Users/wjj/PycharmProjects/pythonlearn/readme.md'))

# 11.创建目录【 mkdir / mkdir -p】
# os.mkdir('/Users/wjj/Desktop/mp3')
# os.makedirs('/Users/wjj/Desktop/mp3/japanese/one')

# 不能递归删除目录，一层一层删
# os.rmdir('/Users/wjj/Desktop/mp3/japanese/one')

# 12.可以删除多层递归的空目录，若目录中有文件则无法删除
# os.removedirs('/Users/wjj/Desktop/mp3/japanese')
# os.remove('/Users/wjj/Desktop/mp3/japanese')  # Operation not permitted
# os.system("rm -rf /Users/wjj/Desktop/mp3")  # 可以删除

# 13.创建文件 删除文件
os.mknod('/Users/wjj/Desktop/mp3/japanese/one/aaa.txt')
os.remove('/Users/wjj/Desktop/mp3/japanese/one/aaa.txt')

# 14.文件重命名
os.rename('data.txt', 'data1.txt')

# 15.判断文件或目录是否存在
print(os.path.exists('ips.txtyyyy'))
print(os.path.exists('/home/kiosk/PycharmProjects/2019python/ips.txt'))

# 16.判断是否是文件或者目录
print(os.path.isfile('ips.txt'))
print(os.path.isdir('img'))

# 17. 改变当前目录到指定目录中
print(os.getcwd())
path = '/tmp'
os.chdir(path)
print(os.getcwd())

# 18.文件信息
'''
Access:文件最近一次被访问的时间；当编辑器打开文件时，使用cat,more,less,grep,sed读取文件内容将会刷新 
【 Access的时间，使用ls -lu可以读取当前的Access时间】

Modify:文件内容最近一次被修改的时间；当修改文件内容时Modify的时间将会刷新
【使用ls -l命令显示的是最近一次Modify时间】

Change:文件属性最近一次被修改的时间，对一个文件或则目录执行mv,chmod,chgrp命令，将会刷新Change 的时间
【使用ls -lc可以查看最近一次Change的时间】

'''
# getatime()    返回最近访问时间  （浮点型秒数）
# getctime()    返回文件创建时间
# getmtime()    返回最近文件修改时间
# getsize()    返回文件大小 （字节为单位）
