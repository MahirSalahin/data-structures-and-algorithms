def floyd_warshall(graph):
    n = len(graph)
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u in range(n):
        for v in range(n):
            if graph[u][v] != 0:
                dist[u][v] = graph[u][v]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


if __name__ == '__main__':
    graph = [[0, 5, 0, 10],
             [0, 0, 3, 0],
             [0, 0, 0, 1],
             [0, 0, 0, 0]]
    print(floyd_warshall(graph))
    # Output: [[0, 5, 8, 9], [inf, 0, 3, 4], [inf, inf, 0, 1], [inf, inf, inf, 0]]
