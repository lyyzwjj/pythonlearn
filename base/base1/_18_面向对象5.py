# 私有属性和私有方法 加上__
class Woman:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        print("%s年龄是%d" % (self.name, self.__age))

    def secret(self):
        self.__secret()


lily = Woman("Lily")
#  lily.__secret() __secret()方法是私有的
lily.secret()
print(lily.name)
# 私有属性不能外界被直接访问  print(lily.__age)
# 没有绝对的私有
# print(lily._Women__age)
lily._Women__secret()







