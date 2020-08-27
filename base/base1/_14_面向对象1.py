class person:
    def eat(self):
        print("正在吃饭")

    def sleep(self):
        print("静态方法")


xiaoxiao = person()
xiaoxiao.eat()
xiaoxiao.sleep()

#临时价格属性
xiaoxiao.name="xiaoxiao"
print(xiaoxiao.name)

print(xiaoxiao)
# %d  10进制打印
# %X  16进制打印
print("%x" % (id(xiaoxiao)))


