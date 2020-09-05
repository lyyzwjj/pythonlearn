from multiprocessing import Pool, Manager
import os

enumerate


def copy_file_task(name, old_folder_name, new_folder_name, queue):
    fr = open(old_folder_name + "/" + name)
    fw = open(new_folder_name + "/" + name, "w")
    contend = fr.read()
    fw.write(contend)
    fr.close()
    fw.close()
    queue.put(name)
    # print("存进了%s" % name)


def main():
    old_folder_name = input("请输入文件夹的名字:")
    new_folder_name = old_folder_name + ".复件"
    os.mkdir(new_folder_name)
    file_names = os.listdir(old_folder_name)
    print(file_names)
    pool = Pool(2)
    queue = Manager().Queue()

    for name in file_names:
        pool.apply_async(copy_file_task, args=(name, old_folder_name, new_folder_name, queue))

    num = 0
    all_num = len(file_names)
    while num < all_num:
        queue.get()
        print("取出来%s" % str(queue.get()))
        num += 1
        copy_rate = num / all_num
        print("\rcopy的进度是:%.2f%%" % (copy_rate * 100))

    print("已完成copy.....")
    # pool.close()
    # pool.join()


if __name__ == '__main__':
    main()
