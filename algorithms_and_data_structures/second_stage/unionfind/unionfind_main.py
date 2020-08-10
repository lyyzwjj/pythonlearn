from algorithms_and_data_structures.second_stage.unionfind.unionfind import *
from algorithms_and_data_structures.util.Times import *
from algorithms_and_data_structures.util.Asserts import *

# count = 100000
count = 100000


def execute_method(uf):
    for c in range(count):
        uf.union(random.randint(0, count - 1), random.randint(0, count - 1))
    for c in range(count):
        uf.is_same(random.randint(0, count - 1), random.randint(0, count - 1))


def test_time(uf):
    uf.union(0, 1)
    uf.union(0, 3)
    uf.union(0, 4)
    uf.union(2, 3)
    uf.union(2, 5)

    uf.union(6, 7)

    uf.union(8, 10)
    uf.union(9, 10)
    uf.union(9, 11)

    Asserts.test(not uf.is_same(2, 7))

    uf.union(4, 6)

    Asserts.test(uf.is_same(2, 7))

    Times.test(uf.__class__.__name__, execute_method, uf)


def test_union_find():
    # test_time(UnionFindQF(count))
    # test_time(UnionFindQU(count))
    test_time(UnionFindQUS(count))
    test_time(UnionFindQUR(count))
    test_time(UnionFindQURPC(count))
    test_time(UnionFindQURPH(count))
    test_time(UnionFindQURPS(count))
    guf = GenericUnionFind()
    for i in range(count):
        guf.make_set(i)
    test_time(guf)


if __name__ == '__main__':
    test_union_find()
