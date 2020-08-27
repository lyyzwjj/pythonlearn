arr = [x * 2 for x in range(10)]
print(arr)
# 需要一个非常大的列表 但是又不希望占用太大内存空间
# 生成器第一种
arr = (x * 2 for x in range(10))
print(arr)
"""
要一个生成一个
print(next(arr))
print(next(arr))
print(next(arr))
"""


def creatNum():
    a, b = 0, 1
    for i in range(5):
        print(b)
        a, b = b, a + b


creatNum()
