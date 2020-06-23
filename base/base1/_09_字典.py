dict1 = {'姓名': '小明', 'age': 18}
dict2 = {'性别': '男'}
dict1.update(dict2)
print(len(dict1))
print(dict1)
for key in dict1:
    print('%s-%s' % (key, dict1[key]))
