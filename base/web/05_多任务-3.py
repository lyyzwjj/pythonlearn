import threading
import time

g_num = 0


def test1(num):
    global g_num
    # 请求上锁 如果之前没有被上锁 那么上锁
    # 如果之前上了锁,那么在此处等待 直到锁被解开
    mutex.acquire()
    print("test1加锁")
    for i in range(num):
        g_num += 1
    mutex.release()
    print("test1解锁")
    print("----- in test1 temp=%d -----" % g_num)


def test2(num):
    global g_num
    mutex.acquire()
    print("test2加锁")
    for i in range(num):
        g_num += 1
    mutex.release()
    print("test2解锁")
    print("----- in test2 temp=%d -----" % g_num)


# 创建一个互斥锁
mutex = threading.Lock()


def main():
    t1 = threading.Thread(target=test1, args=(100000,))
    t2 = threading.Thread(target=test2, args=(100000,))
    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)
    print("----- in main g_num=%d ------" % g_num)


if __name__ == '__main__':
    main()
