def dfs(graph, start):
    visited = set()
    stack = [start]
    order_of_visits = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            order_of_visits.append(vertex)
            stack.extend(set(graph.neighbors(vertex)) - visited)  # Use graph.neighbors to get adjacent vertices

    return order_of_visits
