import heapq

def dijkstra(graph, start):
    # Initialize distances to all nodes as infinity, except the start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        # Ignore outdated entries in the priority queue
        if current_dist > distances[current_node]:
            continue

        # Visit neighbors and update distances if shorter path found
        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances