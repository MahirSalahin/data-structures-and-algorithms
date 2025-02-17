def bellman_ford(graph, source, v):
    """
    Find the shortest path from a source vertex to all other vertices in a weighted graph.

    Args:
        graph (list(list(tuples))): Adjacency list representation of the graph. Each tuple contains
            (neighbor_vertex, edge_weight).
        source (int): The source vertex from which to compute shortest paths.
        v (int): The total number of vertices in the graph.

    Returns:
        list(int): A list of shortest distances from the source vertex to all other vertices.
        If the graph contains a negative weight cycle, returns None.

    Time Complexity: O(V * E), where V is the number of vertices and E is the number of edges.\n
    Space Complexity: O(V), where V is the number of vertices.
    """
    dist = [float('inf')] * v
    dist[source] = 0

    for _ in range(v - 1):
        for u in range(v):
            for neighbor, weight in graph[u]:
                if dist[u] + weight < dist[neighbor]:
                    dist[neighbor] = dist[u] + weight

    for u in range(v):
        for neighbor, weight in graph[u]:
            if dist[u] + weight < dist[neighbor]:
                return None

    return dist


if __name__ == '__main__':
    graph = [[(1, 5), (3, 10)],
             [(2, 3)],
             [(3, 1)],
             []]
    source = 0
    v = 4
    print(bellman_ford(graph, source, v))
    # Output: [0, 5, 8, 9]
