import abc
import time
import operator

from algorithms_and_data_structures.second_stage.sort.common import Entity


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

    def is_stable(self):
        # entities = (Entity(score * 10, 10) for score in range(20))
        entities = [Entity(score * 10, 10) for score in range(20)]
        self.p_sort(entities)
        index = 1
        while index < 20:
            score = entities[index].score
            pre_score = entities[index - 1].score
            if score != pre_score + 10:
                return False
            index += 1
        return True

    def __str__(self):
        time_str = "耗时：" + str((self.sort_time / 1000000000.0)) + "s(" + str(self.sort_time / 1000000.0) + "ms)"
        compare_count_str = "比较：" + AbstractSort.number_string(self.cmp_count)
        swap_count_str = "交换：" + AbstractSort.number_string(self.swap_count)
        stable_str = "稳定性: " + str(self.is_stable())
        return "【" + self.__class__.__name__ + "】\n" + stable_str + " \t" + time_str + " \t" + compare_count_str + "\t " + swap_count_str \
               + "\n" + "------------------------------------------------------------------"


class BubbleSort(AbstractSort):
    def sort(self):
        self.sort3()

    def sort1(self):
        end = len(self.array) - 1
        while end > 0:
            begin = 1
            while begin <= end:
                if self.cmp(begin, begin - 1) < 0:
                    self.swap(begin, begin - 1)
                begin += 1
            end -= 1

    def sort2(self):
        end = len(self.array) - 1
        array_sorted = True
        while end > 0:
            begin = 1
            while begin <= end:
                if self.cmp(begin, begin - 1) < 0:
                    self.swap(begin, begin - 1)
                    array_sorted = False
                begin += 1
            if array_sorted:
                break
            end -= 1

    def sort3(self):
        end = len(self.array) - 1

        array_sorted = True  # 优化一 记录列表一开始是否就已经有序
        while end > 0:
            begin = 1
            sorted_index = 1
            while begin <= end:
                if self.cmp(begin, begin - 1) < 0:
                    self.swap(begin, begin - 1)
                    array_sorted = False
                    sorted_index = begin
                begin += 1
            if array_sorted:
                break
            end = sorted_index - 1  # 每次冒泡判断终止位置应该是最后一次交换位置，而非最后一位每次减一


class SelectSort(AbstractSort):
    def sort(self):
        end = len(self.array) - 1
        while end > 0:
            max_index = 0
            begin = 1
            while begin <= end:
                if self.cmp(max_index, begin) <= 0:
                    max_index = begin
                begin += 1
            self.swap(max_index, end)
            end -= 1


class AbstractHeap():
    def __init__(self, my_operator=None):
        if my_operator is not None:
            self.operator = my_operator
        else:
            self.operator = operator

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    @abc.abstractmethod
    def clear(self):
        pass

    @abc.abstractmethod
    def add(self, element):
        pass

    @abc.abstractmethod
    def get(self):
        pass

    @abc.abstractmethod
    def remove(self):
        pass

    @abc.abstractmethod
    def replace(self, element):
        pass

    @staticmethod
    def compare(e1, e2):
        if operator.lt(e1, e2):
            return -1
        elif operator.gt(e1, e2):
            return 1
        else:
            return 0


class BinaryHeap(AbstractHeap):

    def __init__(self, elements=None, my_compator=None):
        super(BinaryHeap, self).__init__(my_compator)
        if elements is None:
            self.elements = []
        else:
            self.size = len(elements)

    def clear(self):

    def add(self, element):
        pass

    def get(self):
        pass

    def remove(self):
        pass

    def replace(self, element):
        pass


class HeapSort(AbstractSort):

    def sort(self):


class InsertSort(AbstractSort):
    def sort(self):
        begin = 1
        while begin < len(self.array):
            cur = begin
            while cur > 0 and self.cmp(cur, cur - 1) < 0:
                self.swap(cur, cur - 1)
                cur -= 1
            begin += 1
