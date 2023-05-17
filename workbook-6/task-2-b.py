from collections import deque


def adjacency_from_incidence(incidence_matrix):
    num_vertices = len(incidence_matrix)
    num_edges = len(incidence_matrix[0])
    adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    for j in range(num_edges):
        vertices = [i for i in range(num_vertices) if incidence_matrix[i][j]]
        adjacency_matrix[vertices[0]][vertices[1]] = 1
        adjacency_matrix[vertices[1]][vertices[0]] = 1

    return adjacency_matrix


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


# Graph with 7 vertices using the incidence matrix
graph_incidence = [
    [1, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 1]
]

graph_adjacency_from_incidence = adjacency_from_incidence(graph_incidence)
conn_number_incidence = connectivity_number_adjacency(graph_adjacency_from_incidence)
print(f"Connectivity number (incidence matrix): {conn_number_incidence}")
