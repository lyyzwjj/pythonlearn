import json
from algorithms_and_data_structures.second_stage.sort.common import *
from algorithms_and_data_structures.second_stage.sort.sort import *


def test_sort(array, sorts):
    for sort in sorts:
        new_array = Integers.copy(array)
        sort.p_sort(new_array)
        print(new_array)
        Asserts.test(Integers.is_asc_order(new_array))

    for sort in sorts:
        print(sort)


if __name__ == '__main__':
    proto_array = Integers.random(1000, 1, 2000)
    # json.dump(proto_array, open('../../resources/array.json', 'w'))
    # proto_array = json.load(open('../../resources/array.json', 'r'))
    test_sort(proto_array, [BubbleSort(), SelectSort(), InsertSort()])
