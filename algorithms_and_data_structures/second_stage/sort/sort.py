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


class AbstractHeap:
    def __init__(self, size=0, my_operator=None):
        self.size = size
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
    __default_capacity = 10

    def __init__(self, elements=None, my_compator=None):
        super(BinaryHeap, self).__init__(my_compator)
        if elements is None or len(elements) == 0:
            self.elements = [None] * self.__default_capacity
        else:
            self.size = len(elements)
            capacity = max(self.__default_capacity, self.size)
            self.elements = [None] * capacity
            i = 0
            while i < len(elements):
                self.elements[i] = elements[i]
                i = i + 1
            self.elements = elements

    def clear(self):
        self.elements = []
        self.size = 0

    def add(self, element):
        self.__element_not_none_check(element)
        self.__ensure_capacity(self.size + 1)
        self.size = self.size + 1
        self.elements[self.size] = element
        self.__sift_up(self.size - 1)

    def get(self):
        self.__empty_check()
        return self.elements[0]

    def remove(self):
        self.__empty_check()
        last_index = self.size
        self.size = self.size - 1
        root = self.elements[0]
        self.elements[0] = self.elements(last_index)
        self.elements[last_index] = None
        self.__sift_down(0)
        return root

    def replace(self, element):
        self.__element_not_none_check(element)
        root = None
        if self.size == 0:
            self.elements[0] = element
            self.size = self.size + 1
        else:
            root = self.elements[0]
            self.elements[0] = element
            self.__sift_down(0)
        return root

    # 批量建堆
    def heapify(self):
        # 自上而下的上滤 每次向最后插入元素 上滤
        """
        i = 1
        while i < self.size:
            self.__sift_up(i)
            i = i + 1
        """
        i = self.size >> 1
        while i >= 0:
            self.__sift_down(i)
            i = i - 1

    # 从这个元素开始上滤
    def __sift_up(self, index):
        element = self.elements[index]
        while index > 0:
            parent_index = (index - 1) >> 1  # 完全二叉树性质 float((n-1)/2)
            parent = self.elements[parent_index]
            if self.compare(element, parent) <= 0:  # 大堆
                # if self.compare(parent, element) <= 0:  # 小堆
                break
            self.elements[index] = parent
            index = parent_index
        element[index] = element

    # 从这个元素开始下滤
    def __sift_down(self, index):
        element = self.elements[index]
        # 小于第一个叶子的索引(即非叶子节点的数量)
        # 必须保证index位置不是叶子节点
        half = self.size >> 1
        while index < half:
            # index 的节点有两种情况
            # 1.只有左子节点
            # 2.同时有左右子节点
            child_index = (index << 1) + 1
            child = self.elements[child_index]
            right_index = child_index + 1
            # 不能在此处直接取右子节点 可能为空 索引越界  self.elements[right_index]
            # 如果有右子节点 并且右子节点比左子节点大 那么选择 大的右子节点去和父节点比较
            # 选出左右子节点最大的那个
            if right_index < self.size and self.compare(self.elements[right_index], child) > 0:  # 大堆 就要挑大的去比价
                child_index = right_index
                child = self.elements[child_index]
            if self.compare(element, child) >= 0:  # 大堆
                break
            # 将子节点存放到index位置
            self.elements[index] = child
            # 重新设置index
            index = child_index
        self.elements[index] = element

    def __empty_check(self):
        if self.size == 0:
            raise Exception("Heap is empty")

    @staticmethod
    def __element_not_none_check(element):
        if element is None:
            raise Exception("element must not be None")

    def __ensure_capacity(self, capacity):
        old_capacity = len(self.elements)
        if old_capacity >= capacity:
            return
        new_capacity = old_capacity + (old_capacity >> 1)  # 扩大1.5倍
        new_elements = [None] * new_capacity
        self.elements = new_elements
        print("扩容为%d" % new_capacity)


class HeapSort(AbstractSort):

    def __init__(self, __heap_size=0):
        super(HeapSort, self).__init__()
        self.__heap_size = __heap_size

    def sort(self):
        # 原地建最大堆
        self.__heap_size = len(self.array)
        for i in range((self.__heap_size >> 1) - 1, -1, -1):
            self.__sift_down(i)
        # 次取出堆的最大值 即array[0] 放到数组后面 然后剩下的重建堆 拿到数组
        while self.__heap_size > 1:
            self.__heap_size -= 1
            self.swap(0, self.__heap_size)
            # 对0的位置进行sift_down 恢复堆的性质
            self.__sift_down(0)

    def __sift_down(self, index):
        element = self.array[index]
        # 小于第一个叶子的索引(即非叶子节点的数量)
        # 必须保证index位置不是叶子节点
        while index < self.__heap_size >> 1:
            # index 的节点有两种情况
            # 1.只有左子节点
            # 2.同时有左右子节点
            child_index = (index << 1) + 1
            child = self.array[child_index]
            right_index = child_index + 1
            # 不能在此处直接取右子节点 可能为空 索引越界  self.elements[right_index]
            # 如果有右子节点 并且右子节点比左子节点大 那么选择 大的右子节点去和父节点比较
            # 选出左右子节点最大的那个
            if right_index < self.__heap_size and self.cmp_element(self.array[right_index], child) > 0:  # 大堆 就要挑大的去比价
                child_index = right_index
                child = self.array[child_index]
            if self.cmp_element(element, child) >= 0:  # 大堆
                break
            # 将子节点存放到index位置
            self.array[index] = child
            # 重新设置index
            index = child_index
        self.array[index] = element


class InsertSort(AbstractSort):
    def sort(self):
        begin = 1
        while begin < len(self.array):
            cur = begin
            # while cur > 0 and self.cmp(cur, cur - 1) < 0:
            while cur > 0 and not self.cmp(cur, cur - 1) >= 0:
                self.swap(cur, cur - 1)
                cur -= 1
            begin += 1
