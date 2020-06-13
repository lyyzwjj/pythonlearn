import threading
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
    thread_list = []
    print("all is start")
    for i in range(lenth):
        # threading.Thread 就是用线程来执行我们的功能
        t = threading.Thread(target=loop, args=(i, sleep_list[i]))  # 按照列表长度和列表内容调用函数
        thread_list.append(t)  # 将生成的线程添加到列表里
    for t in thread_list:
        t.start()  # 开始执行线程
    for t in thread_list:
        t.join()  # 挂起线程，到所有线程结束  不加join 主进程就直接执行了到了all is down
    print("all is down")


if __name__ == '__main__':
    main()
