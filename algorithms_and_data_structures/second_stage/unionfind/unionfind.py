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


class GenericUnionFind:
    def __init__(self):
        # key: v  value: Node
        self.nodes = {}

    class Node:
        def __init__(self, value):
            self.value = value
            self.parent = self
            self.rank = 1

    def make_set(self, v):
        if not self.nodes.__contains__(v):
            self.nodes[v] = self.Node(v)

    def union(self, v1, v2):
        """ 合并v1、v2所属集合
        :param v1:
        :param v2:
        :return:
        """
        p1 = self.find_node(v1)
        p2 = self.find_node(v2)
        if p1 is None or p2 is None or p1 == p2:
            return
        # 树矮的挂到树高的下面
        if p1.rank < p2.rank:
            p1.parent = p2
        elif p1.rank > p2.rank:
            p2.parent = p1
        else:
            p1.parent = p2
            p2.rank += 1

    def find_node(self, v):
        """ 查找v所属集合(根节点)
        :param v:
        :return:
        """
        node = self.nodes.get(v)
        if node is None:
            return None
        while node.value != node.parent.value:
            node.parent = node.parent.parent
            node = node.parent
        return node

    def find(self, v):
        node = self.find_node(v)
        return None if node is None else node.value

    def is_same(self, v1, v2):
        """ 检查v1、v2是否属于同一个集合
        :param v1:
        :param v2:
        :return:
        """
        return self.find(v1) == self.find(v2)