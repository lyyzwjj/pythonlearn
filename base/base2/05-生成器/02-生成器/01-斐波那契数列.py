def creatNum():
    print("------start----")
    a, b = 0, 1
    for i in range(5):
        # 只要加了yield的函数就变成了生成器  不能像普通函数一样执行
        # print("xx")
        yield b  # 到了此处会执行print(next(a))
        # print("yy")
        a, b = b, a + b
        # print(b)
    print("------stop----")


a = creatNum()  # 生成器对象
print(a)
for n in a:
    print(n)
# print(next(a))
# 上下两种方式相等
# print(a.__next__())
