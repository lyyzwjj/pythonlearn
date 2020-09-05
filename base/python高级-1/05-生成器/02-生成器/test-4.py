def test():
    i = 0
    while i < 5:
        temp = yield i
        print(temp)
        i += 1


t = test()
print(t.__next__())
print(t.__next__())
# next 和send 都可以让生成器往下走一步  不过send 可以带个参数 赋值给yield
t.send("haha")
# 第一次不能用send() 第一次智能用next
# 或者 t.send(None) 第一次send 空的 send(None) 等效next()
