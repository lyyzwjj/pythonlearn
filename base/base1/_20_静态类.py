class Tool:
    count = 0

    def __init__(self):
        Tool.count += 1

    @classmethod
    def haha(cls):
        print(cls.count)

    @staticmethod
    def static():
        print("静态方法")


tool1 = Tool()
print(Tool.count)
tool2 = Tool()
print(Tool.count)
tool3 = Tool()
print(Tool.count)
Tool.haha()
Tool.static()


def haha():
    print("哈哈")
