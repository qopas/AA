class PrimGraph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]
        self.INF = float('inf')

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    def prims_algorithm(self):
        selected = [False] * self.V
        selected[0] = True  # Start with the first vertex
        no_edge = 0
        print("Edge : Weight\n")

        while no_edge < self.V - 1:
            minimum = self.INF
            x = y = 0
            for i in range(self.V):
                if selected[i]:
                    for j in range(self.V):
                        if not selected[j] and self.graph[i][j]:
                            if self.graph[i][j] < minimum:
                                minimum = self.graph[i][j]
                                x, y = i, j
            print(f"{x}-{y}: {self.graph[x][y]}")
            selected[y] = True
            no_edge += 1