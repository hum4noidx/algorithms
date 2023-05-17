from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend(
                neighbor for neighbor in range(len(graph)) if graph[node][neighbor] and neighbor not in visited)

    return visited


def connectivity_number_adjacency(graph):
    components = []
    unvisited = set(range(len(graph)))

    while unvisited:
        start = unvisited.pop()
        component = bfs(graph, start)
        components.append(component)
        unvisited -= component

    return len(components)


# Graph with 7 vertices using the adjacency matrix
graph_adjacency = [
    [0, 1, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0]
]

conn_number_adjacency = connectivity_number_adjacency(graph_adjacency)
print(f"Connectivity number (adjacency matrix): {conn_number_adjacency}")
