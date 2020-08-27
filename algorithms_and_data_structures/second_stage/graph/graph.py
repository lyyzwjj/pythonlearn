import abc
from queue import Queue


class AbstractGraph:
    @abc.abstractmethod
    def edges_size(self):
        pass

    @abc.abstractmethod
    def vertices(self):
        pass

    @abc.abstractmethod
    def add_vertex(self, v):
        pass

    @abc.abstractmethod
    def add_edge_no_weight(self, ori, dest):
        pass

    @abc.abstractmethod
    def add_edge(self, ori, dest, weight):
        pass

    @abc.abstractmethod
    def remove_vertex(self, v):
        pass

    @abc.abstractmethod
    def remove_edge(self, ori, dest):
        pass

    @abc.abstractmethod
    def bfs(self, begin):
        pass

    @abc.abstractmethod
    def dfs(self, begin):
        pass


class ListGraph(AbstractGraph):
    def __init__(self):
        self.__vertices = {}
        self.__edges = set()

    def edges_size(self):
        return len(self.__edges)

    def vertices(self):
        return self.__vertices

    def add_vertex(self, v):
        if not self.__vertices.__contains__(v):
            self.__vertices[v] = ListGraph.__Vertex(v)

    def add_edge_no_weight(self, ori, dest):
        self.add_edge(ori, dest, None)

    def add_edge(self, ori, dest, weight):
        ori_vertex = self.__vertices.get(ori)
        if ori_vertex is None:
            ori_vertex = ListGraph.__Vertex(ori)
            self.__vertices[ori] = ori_vertex
        dest_vertex = self.__vertices.get(dest)
        if dest_vertex is None:
            dest_vertex = ListGraph.__Vertex(dest)
            self.__vertices[dest] = dest_vertex
        edge = ListGraph.__Edge(ori_vertex, dest_vertex, weight)
        ori_vertex.out_edges.discard(edge)
        dest_vertex.in_edges.discard(edge)
        self.__edges.discard(edge)
        ori_vertex.out_edges.add(edge)
        dest_vertex.in_edges.add(edge)
        self.__edges.add(edge)

    def remove_vertex(self, v):
        vertex = self.__vertices.pop(v, None)
        if vertex is not None:
            for edge in ListGraph.__set_sort(vertex.out_edges):
                edge.dest.in_edges.remove(edge)
                self.__edges.discard(edge)

            for edge in ListGraph.__set_sort(vertex.in_edges):
                edge.ori.out_edges.remove(edge)
                self.__edges.discard(edge)

    def remove_edge(self, ori, dest):
        ori_vertex = self.__vertices.get(ori)
        if ori_vertex is None:
            return
        dest_vertex = self.__vertices.get(dest)
        if dest_vertex is None:
            return
        edge = ListGraph.__Edge(ori_vertex, dest_vertex)
        ori_vertex.out_edges.discard(edge)
        dest_vertex.in_edges.discard(edge)
        self.__edges.discard(edge)

    def bfs(self, begin):
        begin_vertex = self.__vertices.get(begin)
        if begin_vertex is None:
            return
        visited_vertices = set()
        visited_vertices.add(begin_vertex)
        queue = Queue()
        queue.put(begin_vertex)
        while not queue.empty():
            vertex = queue.get()
            print(vertex.value)
            for edge in ListGraph.__set_sort(vertex.out_edges):
                if not visited_vertices.__contains__(edge.dest):
                    queue.put(edge.dest)
                    visited_vertices.add(edge.dest)

    def dfs(self, begin):
        begin_vertex = self.__vertices.get(begin)
        if begin_vertex is None:
            return
        self.dfs_recursion(begin_vertex, set())

    def dfs_recursion(self, vertex, visited_vertices):
        print(vertex.value)
        visited_vertices.add(vertex)
        for edge in ListGraph.__set_sort(vertex.out_edges):
            if not visited_vertices.__contains__(edge.dest):
                self.dfs_recursion(edge.dest, visited_vertices)

    def print(self):
        print("vertices==================================================")
        # print(lambda v, vertex: (
        #     print(v),
        #     print("in---------------------"),
        #     print(vertex.in_edges),
        #     print("out---------------------"),
        #     print(vertex.in_edges)
        # ), self.__vertices)
        for v, vertex in self.__vertices.items():
            print(v)
            print("in---------------------")
            # print(vertex.in_edges)
            ListGraph.__print_set_edges(vertex.in_edges)
            print("out---------------------")
            # print(vertex.out_edges)
            ListGraph.__print_set_edges(vertex.out_edges)
        print("\n" + "edges==================================================")
        # print(lambda edge: print(edge), self.__edges)
        for edge in self.__edges:
            print(edge)

    @staticmethod
    def __print_set_edges(edges):
        string = "["
        for edge in edges:
            string += str(edge)
            string += ","
        string = string.rstrip(",")
        string += "]"

        print(string)

    @staticmethod
    def __set_sort(edges):
        """
        强制给edges set排序
        :param edges:
        :return:
        """
        edges_list = list(edges)
        # TODO  edges set排序规则待优化
        edges_list.sort(key=lambda edge: edge.ori.value + edge.dest.value)
        return edges_list

    class __Vertex:
        def __init__(self, value):
            self.value = value
            self.in_edges = set()
            self.out_edges = set()

        def __hash__(self):
            return hash(self.value) if self.value is not None else 0

        def __eq__(self, other):
            if type(other) == self.__class__:
                return self.value == other.value
            else:
                return False

        def __str__(self):
            return self.value if self.value is not None else "None"

    class __Edge:
        def __init__(self, ori, dest, weight=None):
            self.ori = ori
            self.dest = dest
            self.weight = weight

        def __hash__(self):
            return hash(self.ori) + 31 * hash(self.dest)

        def __eq__(self, other):
            if type(other) == self.__class__:
                return self.ori == other.ori and self.dest == other.dest
            else:
                return False

        def __str__(self):
            return "Edge {ori=" + str(self.ori) + ", dest=" + str(self.dest) + ", weight=" + str(self.weight) + '}'
