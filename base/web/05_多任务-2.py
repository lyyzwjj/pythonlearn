import threading
import time

g_num = 100
g_nums = [11, 22]


def test1(temp):
    # global g_num
    # g_num += 1
    # print("----- in test1 g_num=%d" % g_num)
    temp.append(33)
    print("----- in test1 temp=%s" % str(temp))


def test2(temp):
    # nums.append(33)
    # nums += [100, 200]
    # print("----- in test2 g_num=%d" % g_num)
    print("----- in test2 temp=%s" % str(temp))


def main():
    t1 = threading.Thread(target=test1, args=(g_nums,))
    t2 = threading.Thread(target=test2, args=(g_nums,))
    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)
    # print("----- in main g_num=%d" % g_num)
    print("----- in main g_nums=%s" % str(g_nums))


if __name__ == '__main__':
    main()
