import time
import datetime
import threading


class Times:
    str_format1 = "%Y-%m-%d %H:%M:%S.%f"
    str_format2 = "%H:%M:%S"
    str_format3 = "%H:%M:%S.%f"

    @classmethod
    def format_time(cls, format_type=None, now=None):
        if now is None:
            now = datetime.datetime.now()
        if format_type == 1:
            format_time_str = now.strftime(Times.str_format1)
        elif format_type == 2:
            format_time_str = now.strftime(Times.str_format2)
        elif format_type == 3:
            format_time_str = now.strftime(Times.str_format3)
        else:
            format_time_str = now.strftime(Times.str_format1)
        return format_time_str

    @classmethod
    def test(cls, title, target, *args):
        if target is None:
            return
        title = "" if title is None else ("【" + title + "】")
        print(title)
        print("开始: " + Times.format_time(3))
        begin = time.time()
        task = threading.Thread(target=target, args=args)
        task.start()
        task.join()
        end = time.time()
        # print("耗时: " + str(end - begin) + "秒")
        print("耗时: %.3f秒" % (end - begin))
        print("-------------------------------------")
