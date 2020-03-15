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


class Asserts:
    @classmethod
    def test(cls, value):
        try:
            if not value:
                raise Exception("测试未通过")
        except Exception as result:
            print("%s" % result)
