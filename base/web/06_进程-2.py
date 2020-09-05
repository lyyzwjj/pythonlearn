import multiprocessing


def download_form_web(q):
    # 模拟从网下下载的数据
    data = [11, 22, 33, 44]
    # 向队列中写入数据
    for temp in data:
        q.put(temp)
        print("已缓存数据%s" % str(temp))
    print("---下载器已经下载完了数据并且存到了队列中---")


def analysis_data(q):
    # 数据处理
    waiting_ananlysis_data = list()
    while True:
        data = q.get()
        waiting_ananlysis_data.append(data)
        print("已存数据%s" % dir(data))
        if q.empty():
            break
    print(waiting_ananlysis_data)


def main():
    # 创建一个队列
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=download_form_web, args=(q,))
    p2 = multiprocessing.Process(target=analysis_data, args=(q,))
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()
