class Graph:
    def __init__(self) -> None:
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self, vertex) -> bool:
        if vertex in self.adj_list:
            return False
        self.adj_list[vertex] = []
        return True

    def add_edge(self, vertex1, vertex2) -> bool:
        if vertex1 not in self.adj_list.keys() or vertex2 not in self.adj_list.keys():
            return False
        self.adj_list[vertex1].append(vertex2)
        self.adj_list[vertex2].append(vertex1)
        return True

    def remove_edge(self, vertex1, vertex2) -> bool:
        if vertex1 not in self.adj_list.keys() or vertex2 not in self.adj_list.keys():
            return False
        self.adj_list[vertex1].remove(vertex2)
        self.adj_list[vertex2].remove(vertex1)
        return True

    def remove_vertex(self, vertex) -> bool:
        if vertex not in self.adj_list.keys():
            return False
        for v in self.adj_list[vertex]:
            self.adj_list[v].remove(vertex)
        del self.adj_list[vertex]
        return True


my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'C')
my_graph.add_edge('A', 'D')
my_graph.add_edge('B', 'D')
my_graph.add_edge('C', 'D')


print('Graph before remove_vertex():')
my_graph.print_graph()


my_graph.remove_vertex('D')


print('\nGraph after remove_vertex():')
my_graph.print_graph()

"""
EXPECTED OUTPUT:
----------------
    Graph before remove_vertex():
    A : ['B', 'C', 'D']
    B : ['A', 'D']
    C : ['A', 'D']
    D : ['A', 'B', 'C']

    Graph after remove_vertex():
    A : ['B', 'C']
    B : ['A']
    C : ['A']

"""