# 自定义的异常
class MyException(Exception):
    def __init__(self):
        self.args = ("统一的异常",)


#raise MyException()


def main():
    try:
        raise MyException()
    except MyException as mine:
        print("%s" % mine)


main()
