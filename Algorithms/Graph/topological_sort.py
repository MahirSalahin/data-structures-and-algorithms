from collections import deque


class TopologicalSort:
    def __init__(self, n: int, edges: list[int]) -> None:
        self.n = n
        self.adj = [[] for _ in range(n + 1)]
        self.indegree = [0] * (n + 1)
        self.topological_order = []

        for cur_node, neighbor in edges:
            self.adj[cur_node].append(neighbor)
            self.indegree[neighbor] += 1

    def bfs(self):
        self.topological_order = []
        queue = deque()
        for i in range(1, self.n + 1):
            if self.indegree[i] == 0:
                queue.append(i)

        while queue:
            cur_node = queue.popleft()
            self.topological_order.append(cur_node)
            for neighbor in self.adj[cur_node]:
                self.indegree[neighbor] -= 1
                if self.indegree[neighbor] == 0:
                    queue.append(neighbor)

        return self.topological_order

    def _dfs(self, source, visited):
        if visited[source]:
            return True
        visited[source] = True

        for neighbor in self.adj[source]:
            self._dfs(neighbor, visited)
        self.topological_order.append(source)

    def dfs(self):
        self.topological_order = []
        visited = [False] * (self.n + 1)
        for i in range(1, self.n):
            self._dfs(i, visited)
        self.topological_order.reverse()
        return self.topological_order


edges = [[1, 2], [2, 3], [1, 5], [4, 2]]
top_sort = TopologicalSort(5, edges)
print(top_sort.bfs())
print(top_sort.dfs())
