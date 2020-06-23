try:
    num = int(input("请输入一个数字"))
    num = 1 / 0
except ZeroDivisionError:
    print("请输入数字")
except ValueError:
    print("请输入正确格式")
except Exception as result:  # 未知异常所有的错误
    print("%s" % result)
else:
    print("没有错误的时候执行的代码")
finally:
    print("无论任何是否出现异常都会执行的代码")


def raise_exception():
    ex = Exception("密码长度不够")
    raise ex


try:
    raise_exception()
except Exception as result:
    print("%s" % result)
