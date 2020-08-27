from time import sleep


def loop(num, sleeptime):
    """
    当前函数作为功能函数
    :param num: 函数的编号
    :param sleeptime:  睡眠的时间
    """
    print("loop %s is start" % num)
    sleep(sleeptime)
    print("loop %s is done" % num)


def main():
    sleep_list = [3, 2]  # 睡眠时间
    lenth = len(sleep_list)  # 获取列表长度
    print("all is start")
    for i in range(lenth):
        loop(i, sleep_list[i])  # 按照列表长度和列表内容调用函数
    print("all is down")


if __name__ == "__main__":
    main()
