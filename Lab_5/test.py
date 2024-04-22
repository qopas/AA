import networkx as nx
import matplotlib.pyplot as plt
import time
import tracemalloc
from bfs import bfs
from dfs import dfs
def generate_graph(num_vertices, num_edges):
    return nx.gnm_random_graph(num_vertices, num_edges)

def benchmark_algorithm(func, *args):
    tracemalloc.start()
    start_time = time.time()
    func(*args)
    elapsed_time = time.time() - start_time
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return elapsed_time, current / 1024**2

def main():
    graph_sizes = [10, 50, 100, 500, 1000]  # Change as needed
    results_bfs = {'time': [], 'memory': []}
    results_dfs = {'time': [], 'memory': []}

    for size in graph_sizes:
        graph = generate_graph(size, size * 2)  # Adjust edges for density
        start_node = list(graph.nodes)[0]  # Start from the first node for simplicity

        # BFS
        time_bfs, memory_bfs = benchmark_algorithm(bfs, graph, start_node)
        results_bfs['time'].append(time_bfs)
        results_bfs['memory'].append(memory_bfs)

        # DFS
        time_dfs, memory_dfs = benchmark_algorithm(dfs, graph, start_node)
        results_dfs['time'].append(time_dfs)
        results_dfs['memory'].append(memory_dfs)

    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(graph_sizes, results_bfs['time'], label='BFS Time')
    plt.plot(graph_sizes, results_dfs['time'], label='DFS Time')
    plt.xlabel('Graph Size (Number of Vertices)')
    plt.ylabel('Time (seconds)')
    plt.title('Time Complexity: BFS vs DFS')
    plt.legend()
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.plot(graph_sizes, results_bfs['memory'], label='BFS Memory Usage')
    plt.plot(graph_sizes, results_dfs['memory'], label='DFS Memory Usage')
    plt.xlabel('Graph Size (Number of Vertices)')
    plt.ylabel('Memory Usage (MB)')
    plt.title('Memory Usage: BFS vs DFS')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()