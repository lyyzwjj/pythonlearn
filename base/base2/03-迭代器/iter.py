# 判断是否可迭代
from collections import Iterable, Iterator


def test():
    yield None
    print("迭代器")


print(isinstance([], Iterable))
print(isinstance([], Iterator))
# iter 把列表编程迭代器 可迭代的东西转成迭代对象
print(isinstance(iter([]), Iterator))
print(isinstance(test(), Iterator))
# 可迭代的(Iterable)不一定能迭代(Iterator) 可迭代的对象不一定是迭代对象
# 生成器对象一定是迭代对象 可迭代的东西转成迭代对象
# 人有游泳的能力 但不是游泳创建出来的对象
