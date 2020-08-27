from time import sleep


# 通过这个例子我们来看计算机正常情况下的执行顺序 从左往右，从上到下
def loop0():
    print("loop 0 is start")
    sleep(3)
    print("loop 0 is down")


def loop1():
    print("loop 1 is start")
    sleep(2)
    print("loop 1 is down")


def main():
    print("all is start")
    loop0()
    loop1()
    print("all is down")


if __name__ == "__main__":
    main()
