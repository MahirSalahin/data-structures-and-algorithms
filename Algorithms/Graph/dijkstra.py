from heapq import *
from math import inf


class Dijkstra:
    def __init__(self, n, edges) -> None:
        self.adj = [[] for _ in range(n + 1)]
        self.parent = [-1] * (n + 1)
        self.min_distance = [inf] * (n + 1)
        for source, destination, weight in edges:
            self.adj[source].append((destination, weight))

    def minimum_distance(self, source, destination=-1):
        self.min_distance[source] = 0
        min_heap = [(0, source)]
        while min_heap:
            cur_distance, cur_node = heappop(min_heap)
            if cur_distance > self.min_distance[cur_node]:
                continue

            for neighbor, distance in self.adj[cur_node]:
                total_distance = cur_distance + distance
                if total_distance < self.min_distance[neighbor]:
                    self.min_distance[neighbor] = total_distance
                    self.parent[neighbor] = cur_node
                    heappush(min_heap, (total_distance, neighbor))

            if cur_node == destination:
                break

        return self.min_distance[destination] if destination != -1 else inf

    def shortest_path(self, source, destination):
        if self.parent.count(-1) == len(self.parent):
            self.minimum_distance(source, destination)
        path = []
        while destination != -1:
            path.append(destination)
            destination = self.parent[destination]
        path.reverse()
        return path if path[0] == source else [-1]


if __name__ == '__main__':
    edges = [(1, 2, 10), (1, 3, 3), (2, 3, 4),
             (2, 4, 1), (3, 4, 4), (3, 5, 4), (4, 5, 2)]
    graph = Dijkstra(5, edges)
    print(graph.minimum_distance(1, 5))  # Output: 7
    print(graph.shortest_path(1, 5))  # Output: [1, 3, 5]