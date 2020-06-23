class Parent:
    def __init__(self):
        print("父类构造开始")

    def say(self):
        print("开始说:哈哈")

    def say1(self):
        print("开始说:哈哈")
        
    def say2(self):
        print("super开始说:哈哈")


# 只需要子类中(父类) 就能继承了
class Son(Parent):
    def __init__(self):
        print("子类构造开始")

    def hop(self):
        print("开始跳跳啊跳")

    def say1(self):
        print("儿子叫")
        
    def say2(self):
        super().say2()
        print("son super开始说:哈哈")


son = Son()
son.hop()
son.say()
son.say1()
son.say2()


#############多继承问题##############

class A:
    def test(self):
        print("A的test方法开始了")

    def demo(self):
        print("A的demo方法开始了")


class B:
    def test(self):
        print("B的test方法开始了")

    def demo(self):
        print("B的demo方法开始了")


class C(B,A):
    pass


c = C()
c.demo()
c.test()


##python的MRO查看调用类的循序方法搜索循序
print(C.__mro__)
