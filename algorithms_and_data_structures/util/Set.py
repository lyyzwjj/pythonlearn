import abc


class Set:
    @abc.abstractmethod
    def add(self, v):
        pass

    @abc.abstractmethod
    def remove(self, v):
        pass


class HashSet(Set):
    def __init__(self):
        self.idict = {}

    def add(self, v):
        self.idict[v] = None

    def remove(self, v):
        self.idict.pop(v)

    def __len__(self):
        return len(self.idict.keys())
