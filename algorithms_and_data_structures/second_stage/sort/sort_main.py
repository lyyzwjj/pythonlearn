import json
from functools import cmp_to_key
from algorithms_and_data_structures.second_stage.sort.common import *
from algorithms_and_data_structures.second_stage.sort.sort import *
from algorithms_and_data_structures.util.Asserts import Asserts


def test_sort(array, sorts):
    for sort in sorts:
        new_array = Integers.copy(array)
        sort.p_sort(new_array)
        print(new_array)
        Asserts.test(Integers.is_asc_order(new_array))

    # python3 实现类自定义排序
    sorts = sorted(sorts, key=cmp_to_key(AbstractSort.compare_sort()))
    for sort in sorts:
        print(sort)


if __name__ == '__main__':
    proto_array = Integers.random(1000, 1, 2000)
    # json.dump(proto_array, open('../../resources/array.json', 'w'))
    # proto_array = json.load(open('../../../resources/array.json', 'r'))
    # test_sort(proto_array, [BubbleSort(), SelectSort(), InsertSort()])
    # test_sort(proto_array, [BBubbleSort(), CSelectSort(), DHeapSort(), EInsertSort(), FMergeSort(), GQuickSort()])
    # test_sort(proto_array, [DHeapSort(), FMergeSort(), GQuickSort(), HShellSort(), ICountSort()])
    # test_sort(proto_array, [ICountSort()])
    test_sort(proto_array, [ICountSort(), JRadixSort()])
