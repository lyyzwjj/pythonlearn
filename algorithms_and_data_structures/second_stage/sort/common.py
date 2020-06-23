import random
import copy


class Integers:
    @classmethod
    def random(cls, count, arg_min, arg_max):
        if count <= 0 or arg_min > arg_max:
            return None
        array = []
        for i in range(count):
            array.append(random.randint(arg_min, arg_max))
        return array

    @classmethod
    def copy(cls, array):
        return copy.deepcopy(array)

    @classmethod
    def print_ln(cls, array):
        if array is None or len(array) == 0:
            return
        array_str = ""
        for index, element in enumerate(array):
            if index != 0:
                array_str += "_"
            array_str += element
        print(array_str)

    @classmethod
    def is_asc_order(cls, array):
        if array is None or len(array) == 0:
            return False
        for index, element in enumerate(array):
            if index != 0:
                if element < array[index - 1]:
                    return False
        return True


class Entity:
    def __init__(self, score, age):
        self.score = score
        self.age = age

    def __eq__(self, other):
        return self.score == other.score

    def __ne__(self, other):
        return self.score != other.score

    def __gt__(self, other):  # 大于函数
        result = 1 if self.score > other.score else 0
        return result

    def __ge__(self, other):  # 大于等于
        result = 1 if self.score >= other.score else 0
        return result

    def __lt__(self, other):  # 小于
        result = 1 if self.score < other.score else 0
        return result

    def __le__(self, other):  # 小于等于
        result = 1 if self.score <= other.score else 0
        return result

    def __sub__(self, other):
        result = 0 if self.score != other.score else 1 if self.score < other.score else -1
        return result
