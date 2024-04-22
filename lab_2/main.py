import numpy as np
import time
import pandas as pd
import matplotlib.pyplot as plt
from quickSort import quicksort  # Ensure this is correctly imported
from mergeSort import mergeSort  # Ensure this is correctly imported
from heapSort import heapSort  # Ensure this is correctly imported
from gnomeSort import gnomeSort  # Ensure this is correctly imported
import sys

sys.setrecursionlimit(10**6)



def generate_datasets(size):
    random_data_set = np.random.uniform(-1000000.0, 10000000.0, size=size).tolist()
    sorted_data_set = sorted(random_data_set)
    reverse_sorted_data_set = sorted_data_set[::-1]
    alternating_large_small_data_set = [None] * size
    for i in range(size // 2):
        alternating_large_small_data_set[2*i] = i + 10000000
        alternating_large_small_data_set[2*i + 1] = size*10000.0 - i
    return {
        'Random': random_data_set,
        'Sorted': sorted_data_set,
        'Reversed': reverse_sorted_data_set,
        'Alternating': alternating_large_small_data_set
    }

sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 10000]



execution_times = {name: [] for name in ['Random', 'Sorted', 'Reversed', 'Alternating']}

# Measure execution times
for size in sizes:
    datasets = generate_datasets(size)
    for name, dataset in datasets.items():
        start_time = time.perf_counter()
        #quicksort(dataset, 0, len(dataset) - 1)
        #heapSort(dataset)
        gnomeSort(dataset)
        #mergeSort(dataset)
        end_time = time.perf_counter()
        execution_times[name].append(end_time - start_time)

# Print the execution times
print("EXECUTION TIMES FOR GNOMESORT")

print(f"{'Size':<10}", end="")
for name in execution_times:
    print(f"{name:<15}", end="")
print()

# Print the execution times for each size
for i, size in enumerate(sizes):
    print(f"{size:<10}", end="")
    for name in execution_times:
        print(f"{execution_times[name][i]:<15.0e}", end="")
    print()


# # Plotting
plt.figure(figsize=(10, 6))
for name, times in execution_times.items():
    plt.plot(sizes, times, marker='o', label=name)

plt.xlabel('Dataset Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Heap Sort Performance Across Different Datasets')
plt.legend()
plt.grid(True)
plt.show()