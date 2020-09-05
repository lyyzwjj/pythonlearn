def test():
    i = 0
    while i < 5:
        if i == 0:
            temp = yield i
        else:
            temp = yield i
        print(temp)
        i += 1


t = test()
# print(t.send("haha"))  //报错
# 第一种解决方法
# print(t.__next__())
# print(t.send("haha"))
# 第二种
print(t.send(None))
print(t.send("哈哈"))
print(t.send("哈哈"))
# print()
