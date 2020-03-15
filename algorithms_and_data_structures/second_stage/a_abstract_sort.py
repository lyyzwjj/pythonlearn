import abc
import time


class AbstractSort:
    def __init__(self, array=None, cmp_count=0, swap_count=0, sort_time=None):
        self.array = array
        self.cmp_count = cmp_count
        self.swap_count = swap_count
        self.sort_time = sort_time

    def compare_to(self, abstract_sort):
        result = self.sort_time - abstract_sort.time
        if result != 0:
            return result
        result = self.cmp_count - abstract_sort.cmp_count
        if result != 0:
            return result
        return self.swap_count - abstract_sort.swap_cout

    @abc.abstractmethod
    def sort(self):
        pass

    def p_sort(self, array):
        if array is None or len(array) < 2:
            return
        self.array = array
        begin = time.time_ns()
        self.sort()
        self.sort_time = time.time_ns() - begin

    def cmp(self, index1, index2):
        self.cmp_count += 1
        return self.array[index1] - self.array[index2]

    def cmp_element(self, element1, element2):
        self.cmp_count += 1
        return element1 - element2

    def swap(self, index1, index2):
        self.swap_count += 1
        tmp = self.array[index1]
        self.array[index1] = self.array[index2]
        self.array[index2] = tmp

    @classmethod
    def number_string(cls, number):
        if number < 10000:
            return str(number)
        if number < 100000000:
            return "{:.2f}".format(number / 10000.0) + "万"
        return "{:.2f}".format(number / 100000000.0) + "亿"

    def __str__(self):
        time_str = "耗时：" + str((self.sort_time / 1000000000.0)) + "s(" + str(self.sort_time / 1000000.0) + "ms)"
        compare_count_str = "比较：" + AbstractSort.number_string(self.cmp_count)
        swap_count_str = "交换：" + AbstractSort.number_string(self.swap_count)
        return "【" + self.__class__.__name__ + "】\n" + time_str + " \t" + compare_count_str + "\t " + swap_count_str \
               + "\n" + "------------------------------------------------------------------"
