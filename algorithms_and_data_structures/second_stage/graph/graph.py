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
    def add_edge(self, ori, dest):
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
            self.__vertices[v] = ListGraph.Vertex(v)

    def add_edge(self, ori, dest):
        pass

    def remove_vertex(self, v):
        pass

    def remove_edge(self, ori, dest):
        pass

    def bfs(self, begin):
        pass

    def dfs(self, begin):
        pass

    class Vertex:
        def __init__(self, value):
            self.value = value
            self.inEdges = set()
            self.outEdges = set()

    class Edge:
        def __init__(self, ori, dest, weight=None):
            self.ori = ori
            self.dest = dest
            self.weight = weight
