from heapq import *
from math import inf


class Prim:
    def __init__(self, n, edges) -> None:
        self.adj = [[] for _ in range(n + 1)]
        for source, destination, weight in edges:
            self.adj[source].append((destination, weight))
            self.adj[destination].append((source, weight))

    def minimum_spanning_tree(self, source=1):
        min_heap = []
        for neighbor, weight in self.adj[source]:
            heappush(min_heap, (weight, source, neighbor))

        MST = []
        vis = set([source])
        while min_heap:
            cur_weight, prev_node, cur_node = heappop(min_heap)
            if cur_node in vis:
                continue

            vis.add(cur_node)
            MST.append([prev_node, cur_node])
            for neighbor, weight in self.adj[cur_node]:
                if neighbor not in vis:
                    heappush(min_heap, (weight, cur_node, neighbor))

        return MST

if __name__ == '__main__':
    edges = [(1, 2, 10), (1, 3, 3), (2, 3, 4),
            (2, 4, 1), (3, 4, 4), (3, 5, 4), (4, 5, 2)]
    prim = Prim(5, edges)
    print(prim.minimum_spanning_tree())