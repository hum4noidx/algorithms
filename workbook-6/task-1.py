import heapq


def prim(graph):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    min_tree = []
    edge_candidates = []

    # Start with the first vertex (index 0)
    visited[0] = True

    # Add all edges from the first vertex to the heap
    for j in range(1, num_vertices):
        if graph[0][j] != 0:
            heapq.heappush(edge_candidates, (graph[0][j], 0, j))

    while edge_candidates:
        weight, u, v = heapq.heappop(edge_candidates)

        if not visited[v]:
            visited[v] = True
            min_tree.append((u, v, weight))

            # Add all edges from the visited vertex to the heap
            for j in range(num_vertices):
                if graph[v][j] != 0 and not visited[j]:
                    heapq.heappush(edge_candidates, (graph[v][j], v, j))

    return min_tree


# Distance matrix for RTU MIREA campuses
graph = [
    [0, 1.97, 21.6, 10.7, 22.3, 10.4],
    [1.97, 0, 22.3, 11.4, 23, 11.1],
    [21.6, 22.3, 0, 11.5, 5.2, 12],
    [10.7, 11.4, 11.5, 0, 13.4, 0.68],
    [22.3, 23, 5.2, 13.4, 0, 13.8],
    [10.4, 11.1, 12, 0.68, 13.8, 0]
]

result = prim(graph)

print("Minimum spanning tree edges:")
for u, v, weight in result:
    print(f"({u}, {v}): {weight}")

total_length = sum(weight for _, _, weight in result)
print(f"Total length: {total_length} km")
