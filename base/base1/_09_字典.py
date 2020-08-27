dict1 = {'姓名': '小明', 'age': 18}
dict2 = {'性别': '男'}
dict1.update(dict2)
print(len(dict1))
print(dict1)
print(dict1.__contains__('姓名'))
for key in dict1:
    print('%s-%s' % (key, dict1[key]))

for key, value in dict1.items():
    print('%s-%s' % (key, value))
dict1.pop('姓名1')  # 报错
re = dict1.pop('姓名1', None)  # 删除不报错
print(dict1)
