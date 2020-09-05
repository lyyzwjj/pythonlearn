import types


class Person(object):
    # __slots__ = ("name", "age") 限制类中的属性  外部就不能随便加属性了

    def __init__(self, newName, newAge):
        self.name = newName
        self.age = newAge

    def eat(self):
        print("-----%s正在吃----" % self.name)


def run(self):
    print("-----%s正在跑----" % self.name)


@staticmethod
def run_static():
    print("-----%静态方法----")


@classmethod
def run_class(cls):
    print("-----%类方法----")


Person.run_static = run_static
Person.run_class = run_class
p1 = Person("p1", 10)
p1.eat()
# p1.run = run  这样做不行
p1.run = types.MethodType(run, p1)
p1.run()  # 虽然p1对象中 run属性已经指向了10行的函数,,,但是这句代码还不正确
# 因为run属性指向的函数 是后来添加的,几p1.run()的时候,并没有把p1当做第
# 1个参数,导致了第10行的函数调用的时候, 出现缺少参数的问题
xxx = p1.run
xxx()  # 类似闭包  之前给了p1对象当参数传入的
Person.run_static()
Person.run_class()
p1.run_class()
p1.run_static()
