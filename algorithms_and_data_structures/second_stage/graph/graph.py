import abc


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
        ori_vertex.outEdges.discard(edge)
        dest_vertex.inEdges.discard(edge)
        self.__edges.discard(edge)
        ori_vertex.outEdges.add(edge)
        dest_vertex.inEdges.add(edge)
        self.__edges.add(edge)

    def remove_vertex(self, v):
        vertex = self.__vertices.pop(v, None)
        if vertex is not None:
            for edge in vertex.outEdges:
                edge.dest.inEdges.remove(edge)
                self.__edges.discard(edge)

            for edge in vertex.inEdges:
                edge.ori.outEdges.remove(edge)
                self.__edges.discard(edge)

    def remove_edge(self, ori, dest):
        ori_vertex = self.__vertices.get(ori)
        if ori_vertex is None:
            return
        dest_vertex = self.__vertices.get(dest)
        if dest_vertex is None:
            return
        edge = ListGraph.__Edge(ori_vertex, dest_vertex)
        ori_vertex.outEdges.discard(edge)
        dest_vertex.inEdges.discard(edge)
        self.__edges.discard(edge)

    def bfs(self, begin):
        pass

    def dfs(self, begin):
        pass

    def print(self):
        print("vertices==================================================")
        # print(lambda v, vertex: (
        #     print(v),
        #     print("in---------------------"),
        #     print(vertex.inEdges),
        #     print("out---------------------"),
        #     print(vertex.inEdges)
        # ), self.__vertices)
        for v, vertex in self.__vertices.items():
            print(v)
            print("in---------------------")
            # print(vertex.inEdges)
            ListGraph.__print_set_edges(vertex.inEdges)
            print("out---------------------")
            # print(vertex.outEdges)
            ListGraph.__print_set_edges(vertex.outEdges)
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

    class __Vertex:
        def __init__(self, value):
            self.value = value
            self.inEdges = set()
            self.outEdges = set()

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
