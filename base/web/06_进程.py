import threading
import time
import multiprocessing

g_num = 0


def test1():
    while True:
        print("----- in test1 -----")
        time.sleep(1)


def test2():
    while True:
        print("----- in test2 -----")
        time.sleep(1)


def main():
    p1 = multiprocessing.Process(target=test1)
    p2 = multiprocessing.Process(target=test2)
    p1.start()
    p2.start()


# t1 = threading.Thread(target=test1)
# t2 = threading.Thread(target=test2)
# t1.start()
# t2.start()


if __name__ == '__main__':
    main()
