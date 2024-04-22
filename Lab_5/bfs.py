import collections

def bfs(graph, root):
    visited, queue = set(), collections.deque([root])
    visited.add(root)
    order_of_visits = []

    while queue:
        vertex = queue.popleft()
        order_of_visits.append(vertex)

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return order_of_visits