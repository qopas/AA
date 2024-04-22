def floyd_warshall(graph):
    num_vertices = len(graph)
    dist = [[float('inf')] * num_vertices for _ in range(num_vertices)]

    # Initialize distances based on the graph's edge weights
    for u in range(num_vertices):
        dist[u][u] = 0
        for v, weight in graph[u].items():
            dist[u][v] = weight

    # Update distances using intermediate vertices
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist