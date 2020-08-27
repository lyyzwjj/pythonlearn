# 深拷贝:
a = [11, 22, 33]
b = a
# b仅仅是复制指向地址
# 浅拷贝:
import copy

# 深拷贝 指向的不是同一个地址 而是完完全全复制属性 指向另外一个空间
c = copy.copy(a)
c = copy.deepcopy(a)  # 内层的引用也完全深拷贝
print(id(a))
print(id(c))
druid = (1, 2)
# 元组是不可变类型  怎么拷贝都只有一个 copy可以判断类型是不是不可变得
d = copy.copy(druid)
d = copy.deepcopy(druid)
print(id(druid))
print(id(d))
