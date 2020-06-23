name_list = ['你好', 33, '小刘', 33, 33]
# 增加
name_list.append('你好')
name_list.insert(0, '2333')
name_list.extend(['小小', '大大'])
# 删除
name_list.remove('小小')
# name_list.clear()
# 变量从内存中删除
del name_list[2]
name_list.pop()
# 长度
print(len(name_list))
# 统计
print(name_list.count(33))

name_list[1] = 'cc'
index = name_list.index('cc')
print(name_list)
print(index)
for item in name_list:
    print(item)

name_list = ['你好', 33, '小刘', 33, 33]
list1 = [1, 2, 3]
#append会将整个list1当一个参数加进列表
name_list.append(list1)
print(name_list)


#遍历方法
colours = ["red","green","blue"]
for colour in colours:
    print(colour)

for i in range(0, len(colours)):
    print(i, colour[i])

for i in range(len(list)):
    print(i, list[i])

for i in enumerate(colours):
    print(i)

for i in iter(colours):
    print(i)



