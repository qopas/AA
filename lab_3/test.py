import time
import tracemalloc
from prims import PrimGraph
from kruksal import Graph as KruskalGraph
from graph_generator import generate_weighted_graph
import matplotlib.pyplot as plt


def benchmark_algorithm(func, *args):
    tracemalloc.start()
    start_time = time.time()
    func(*args)
    elapsed_time = time.time() - start_time
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return elapsed_time, current / 1024 ** 2, peak / 1024 ** 2


def main():
    num_vertices = range(5, 51, 5)  # Test with graphs from 5 to 50 vertices
    times_kruskal, times_prim = [], []
    memory_kruskal, memory_prim = [], []

    for v in num_vertices:
        graph = generate_weighted_graph(v, density=0.4)

        # Kruskal's Algorithm
        kruskal_graph = KruskalGraph(vertices=v)
        for i in range(v):
            for j in range(i + 1, v):
                if graph[i][j] != 0:
                    kruskal_graph.add_edge(i, j, graph[i][j])

        # Prim's Algorithm
        prim_graph = PrimGraph(v)
        for i in range(v):
            for j in range(i + 1, v):
                if graph[i][j] != 0:
                    prim_graph.add_edge(i, j, graph[i][j])

        time_k, mem_k, _ = benchmark_algorithm(kruskal_graph.kruskal_algo)
        time_p, mem_p, _ = benchmark_algorithm(prim_graph.prims_algorithm)

        times_kruskal.append(time_k)
        times_prim.append(time_p)
        memory_kruskal.append(mem_k)
        memory_prim.append(mem_p)

    plt.figure(figsize=(10, 5))
    plt.plot(num_vertices, times_kruskal, label='Kruskal\'s Time')
    plt.plot(num_vertices, times_prim, label='Prim\'s Time')
    plt.xlabel('Number of Vertices')
    plt.ylabel('Time (seconds)')
    plt.title('Time Complexity')
    plt.legend()

    plt.figure(figsize=(10, 5))
    plt.plot(num_vertices, memory_kruskal, label='Kruskal\'s Memory Usage')
    plt.plot(num_vertices, memory_prim, label='Prim\'s Memory Usage')
    plt.xlabel('Number of Vertices')
    plt.ylabel('Memory (MB)')
    plt.title('Memory Usage')
    plt.legend()

    plt.show()


if __name__ == "__main__":
    main()