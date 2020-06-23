import abc
import random
from algorithms_and_data_structures.util.Times import *
from algorithms_and_data_structures.util.Asserts import *


class UnionFind:
    def __init__(self, capacity):
        if capacity < 0:
            raise Exception("capacity must be >=1")
        self.parents = [i for i in range(capacity)]

    @abc.abstractmethod
    def union(self, v1, v2):
        """ 合并v1、v2所属集合
        :param v1:
        :param v2:
        :return:
        """
        pass

    @abc.abstractmethod
    def find(self, v):
        """ 查找v所属集合(根节点)
        :param v:
        :return:
        """
        pass

    def is_same(self, v1, v2):
        """ 检查v1、v2是否属于同一个集合
        :param v1:
        :param v2:
        :return:
        """
        return self.find(v1) == self.find(v2)

    def range_check(self, v):
        if v < 0 or v >= len(self.parents):
            raise Exception("v is out of bounds")


class UnionFindQF(UnionFind):
    def union(self, v1, v2):
        p1 = self.find(v1)
        p2 = self.find(v2)
        if p1 == p2:
            return
        # 让和v1值一样的都与v2的根节点值一样
        for i in range(len(self.parents)):
            if p1 == self.find(self.parents[i]):
                self.parents[i] = p2

    def find(self, v):
        self.range_check(v)
        return self.parents[v]


class UnionFindQU(UnionFind):
    def union(self, v1, v2):
        p1 = self.find(v1)
        p2 = self.find(v2)
        if p1 == p2:
            return
        self.parents[p1] = p2

    def find(self, v):
        self.range_check(v)
        while v != self.parents[v]:
            v = self.parents[v]
        return v


class UnionFindQUS(UnionFindQU):
    def __init__(self, capacity):
        super().__init__(capacity)
        # self.sizes = [1] * capacity
        self.sizes = [1 for _ in range(capacity)]

    def union(self, v1, v2):
        p1 = self.find(v1)
        p2 = self.find(v2)
        if p1 == p2:
            return
        if self.sizes[p1] < self.sizes[p2]:
            self.parents[p1] = p2
            self.sizes[p2] += self.sizes[p1]
        else:
            self.parents[p2] = p1
            self.sizes[p1] += self.sizes[p2]


class UnionFindQUR(UnionFindQU):
    def __init__(self, capacity):
        super().__init__(capacity)
        # self.sizes = [1] * capacity
        self.ranks = [1 for _ in range(capacity)]

    def union(self, v1, v2):
        p1 = self.find(v1)
        p2 = self.find(v2)
        if p1 == p2:
            return
        if self.ranks[p1] < self.ranks[p2]:
            self.parents[p1] = p2
        elif self.ranks[p1] > self.ranks[p2]:
            self.parents[p2] = p1
        else:
            self.parents[p1] = p2
            self.ranks[p2] += 1


class UnionFindQURPC(UnionFindQUR):
    def find(self, v):
        self.range_check(v)
        if v != self.parents[v]:
            self.parents[v] = self.find(self.parents[v])
        return self.parents[v]


# 使路径上的每隔一个节点就指向其祖父节点
class UnionFindQURPH(UnionFindQUR):
    def find(self, v):
        self.range_check(v)
        while v != self.parents[v]:
            self.parents[v] = self.parents[self.parents[v]]
            v = self.parents[v]
        return v


# 使路径上的所有节点都指其祖父节点
class UnionFindQURPS(UnionFindQUR):
    def find(self, v):
        self.range_check(v)
        while v != self.parents[v]:
            parent = self.parents[v]
            self.parents[v] = self.parents[self.parents[v]]
            v = parent
        return v


def execute_method(uf):
    for c in range(UnionMain.count):
        uf.union(random.randint(0, UnionMain.count - 1), random.randint(0, UnionMain.count - 1))
    for c in range(UnionMain.count):
        uf.is_same(random.randint(0, UnionMain.count - 1), random.randint(0, UnionMain.count - 1))


class UnionMain:
    # count = 100000
    count = 100000

    @classmethod
    def main(cls):
        # UnionMain.test_time(UnionFindQF(UnionMain.count))
        # UnionMain.test_time(UnionFindQU(UnionMain.count))
        UnionMain.test_time(UnionFindQUS(UnionMain.count))
        UnionMain.test_time(UnionFindQUR(UnionMain.count))
        UnionMain.test_time(UnionFindQURPC(UnionMain.count))
        UnionMain.test_time(UnionFindQURPH(UnionMain.count))
        UnionMain.test_time(UnionFindQURPS(UnionMain.count))

    @classmethod
    def test_time(cls, uf):
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


if __name__ == '__main__':
    UnionMain.main()
