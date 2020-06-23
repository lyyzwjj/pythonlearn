str = "0123456789"
# -1代表最后一个不取 不写代表最后
var = str[::2]  # 02468
var = str[::-3]  # 9630
var = str[2:5:1]  # 234
var = str[-1:6:-2]  # 97 反着切开始索引要大些
var = str[-1:]
print(var)
list = [1, 2, 3, 4][1:4]
print(list)
tuple = (1, 2, 3, 4)[:0:-2]
print(tuple)
list_repeat = [1, 2] * 5
print(list_repeat)
tuple_repeat = (1, 2) * 5
print(tuple_repeat)
print(list + list_repeat)  # 生成一个新的列表对象
print(tuple + tuple_repeat)
print(list)
list.extend([1, 2])  # 追加进原来的列表[2, 3, 4, 1, 2]
print(list)
list.append([3, 4])  # 将列表作为一个元素添加进原来的列表[2, 3, 4, 1, 2, [3, 4]]
print(list)
print(1 in list)
dict = {"1": "cc", "2": "bb"}
print("6" not in dict)
