from algorithms_and_data_structures.second_stage.graph.graph import *


def test_graph():
    test1()


def test1():
    graph = ListGraph()
    graph.add_edge("V1", "V0", 9)
    graph.add_edge("V1", "V2", 3)
    graph.add_edge("V2", "V0", 2)
    graph.add_edge("V2", "V3", 5)
    graph.add_edge("V3", "V4", 1)
    graph.add_edge("V0", "V4", 6)
    graph.remove_edge("V0", "V4")
    # graph.remove_vertex("V0")

    graph.print()


if __name__ == '__main__':
    test_graph()
