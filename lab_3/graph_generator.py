import random

def generate_weighted_graph(num_vertices, density=0.5):
    graph = [[0]*num_vertices for _ in range(num_vertices)]
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if random.random() < density:
                weight = random.randint(1, 100)
                graph[i][j] = weight
                graph[j][i] = weight
    return graph
