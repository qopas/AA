import numpy as np
import time
import tracemalloc
from dijkstra import dijkstra
from floyd_warshall import floyd_warshall
import matplotlib.pyplot as plt

def generate_random_graph(num_vertices, density=0.5, max_weight=10):
    graph = {}
    for u in range(num_vertices):
        graph[u] = {}
        for v in range(num_vertices):
            if u != v and np.random.rand() < density:
                graph[u][v] = np.random.randint(1, max_weight)
    return graph

def benchmark_algorithm(func, *args):
    tracemalloc.start()
    start_time = time.time()
    func(*args)
    elapsed_time = time.time() - start_time
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return elapsed_time, current / 1024**2

def main():
    graph_sizes = [10, 50, 100,200]  # Change as needed
    density = 0.5  # Adjust density of edges
    max_weight = 10  # Adjust maximum edge weight

    results_dijkstra = {'time': [], 'memory': []}
    results_floyd_warshall = {'time': [], 'memory': []}

    for size in graph_sizes:
        graph = generate_random_graph(size, density, max_weight)

        # Benchmark Dijkstra's algorithm
        start_node = 0  # Start node for Dijkstra's algorithm
        time_dijkstra, memory_dijkstra = benchmark_algorithm(dijkstra, graph, start_node)
        results_dijkstra['time'].append(time_dijkstra)
        results_dijkstra['memory'].append(memory_dijkstra)

        # Benchmark Floyd-Warshall algorithm
        time_floyd_warshall, memory_floyd_warshall = benchmark_algorithm(floyd_warshall, graph)
        results_floyd_warshall['time'].append(time_floyd_warshall)
        results_floyd_warshall['memory'].append(memory_floyd_warshall)

    # Plotting results
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.plot(graph_sizes, results_dijkstra['time'], marker='o', label="Dijkstra's Algorithm")
    plt.plot(graph_sizes, results_floyd_warshall['time'], marker='o', label="Floyd-Warshall Algorithm")
    plt.xlabel('Graph Size')
    plt.ylabel('Time (seconds)')
    plt.title('Execution Time Comparison')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(graph_sizes, results_dijkstra['memory'], marker='o', label="Dijkstra's Algorithm")
    plt.plot(graph_sizes, results_floyd_warshall['memory'], marker='o', label="Floyd-Warshall Algorithm")
    plt.xlabel('Graph Size')
    plt.ylabel('Memory Usage (MB)')
    plt.title('Memory Usage Comparison')
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()