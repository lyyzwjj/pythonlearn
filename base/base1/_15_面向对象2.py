class person:
    def __init__(self, name, age):
        print("init方法执行")
        self.name = name
        self.age = age

    def __del__(self):
        print("%s销毁了" % self.name)

    def eat(self):
        print("正在吃饭")

    def sleep(self):
        print("静态方法")

    def __str__(self):
        return "我名字: %s" % self.name + "     年领: %d" % self.age


person1 = person("小小", 15)
person1.eat()
person1.sleep()
print(person1)
print(person1.name)
print(person1.age)
