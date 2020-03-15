from algorithms_and_data_structures.second_stage.a_common import Integers, Asserts
from algorithms_and_data_structures.second_stage.b_bubble_sort import BubbleSort
import json


def test_sort(array, sorts):
    for sort in sorts:
        new_array = Integers.copy(array)
        sort.p_sort(new_array)
        print(new_array)
        Asserts.test(Integers.is_asc_order(new_array))

    for sort in sorts:
        print(sort)


if __name__ == '__main__':
    # proto_array = Integers.random(10000, 1, 20000)
    # json.dump(proto_array, open('../../resources/array.json', 'w'))
    proto_array = json.load(open('../../resources/array.json', 'r'))
    test_sort(proto_array, [BubbleSort()])
