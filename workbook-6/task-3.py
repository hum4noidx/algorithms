import sys

def nearest_neighbor(graph, start_vertex):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    visited[start_vertex] = True

    path = [start_vertex]
    total_weight = 0

    current_vertex = start_vertex
    for _ in range(num_vertices - 1):
        min_distance = sys.maxsize
        next_vertex = -1

        for neighbor, weight in enumerate(graph[current_vertex]):
            if not visited[neighbor] and weight and weight < min_distance:
                min_distance = weight
                next_vertex = neighbor

        visited[next_vertex] = True
        path.append(next_vertex)
        total_weight += min_distance
        current_vertex = next_vertex

    # Connect the last vertex to the start vertex
    total_weight += graph[current_vertex][start_vertex]
    path.append(start_vertex)

    return path, total_weight

# Weighted graph using the adjacency matrix (7 vertices, weight range: 0-10)
graph = [
    [0, 2, 0, 8, 0, 0, 7],
    [2, 0, 3, 0, 0, 0, 0],
    [0, 3, 0, 0, 4, 9, 0],
    [8, 0, 0, 0, 0, 5, 0],
    [0, 0, 4, 0, 0, 0, 6],
    [0, 0, 9, 5, 0, 0, 1],
    [7, 0, 0, 0, 6, 1, 0]
]

start_vertex = 0
path, total_weight = nearest_neighbor(graph, start_vertex)
print(f"Path: {path}")
print(f"Total weight: {total_weight}")