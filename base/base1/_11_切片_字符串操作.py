str = "0123456789"  # 最后一个表示 -1  -2 即是8
#         0  1  2  3  4  5  6  7  8  9
# 正索引   0  1  2  3  4  5  6  7  8  9
# 负索引 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

# -1代表最后一个不取 不写代表最后
var = str[::2]  # 02468    // 开始(包含) 结束(不包含) 步长
print(var)
var = str[::-3]  # 9630
print(var)
var = str[2:5:1]  # 234
print(var)
var = str[-1:6:-2]  # 97 反着切开始索引要大些
print(var)
var = str[-2:6:-2]  # 8 反着切开始索引要大些
print(var)
var = str[-2:6:-3]  # 8 反着切开始索引要大些
print(var)

var = str[-1:]
print(var)  # 9
list = [1, 2, 3, 4][1:4]  # 2 3 4
print(list)
tuple = (1, 2, 3, 4)[:0:-2]  # -2  从右往左开始 不写就是-1 即4  4 2
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
