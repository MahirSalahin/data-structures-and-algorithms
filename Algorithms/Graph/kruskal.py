from heapq import *
from union_find import UnionFind


class Kruskal:
    def __init__(self, n, edges) -> None:
        self.n = n
        self.min_heap = []
        for node1, node2, weight in edges:
            heappush(self.min_heap, (weight, node1, node2))

    def minimum_spanning_tree(self):
        union_find = UnionFind(self.n)
        MST = []
        while len(MST) < self.n - 1:
            weight, node1, node2 = heappop(self.min_heap)
            if not union_find.union(node1, node2):
                continue
            MST.append([node1, node2])

        return MST


if __name__ == '__main__':
    edges = [(1, 2, 10), (1, 3, 3), (2, 3, 4),
             (2, 4, 1), (3, 4, 4), (3, 5, 4), (4, 5, 2)]
    kruskal = Kruskal(5, edges)
    print(kruskal.minimum_spanning_tree())
