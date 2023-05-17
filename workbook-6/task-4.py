import csv


class Graph:
    def __init__(self, filename=None, matrix=False):
        self.graph = {}
        self.matrix = matrix
        if filename:
            self._load_from_file(filename, matrix)

    def _load_from_file(self, filename, matrix):
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter=' ')
            num_vertices = int(next(reader)[0])
            for i in range(num_vertices):
                self.graph[i] = {}
            if matrix:
                for i, row in enumerate(reader):
                    for j, weight in enumerate(row):
                        if float(weight) != 0:
                            self.graph[i][j] = float(weight)
            else:
                for i, row in enumerate(reader):
                    for j in range(0, len(row), 2):
                        self.graph[int(row[j])][int(row[j + 1])] = float(row[j + 2])

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = {}
        self.graph[u][v] = weight

    def remove_edge(self, u, v):
        if u in self.graph and v in self.graph[u]:
            del self.graph[u][v]

    def print_graph(self):
        for vertex, edges in self.graph.items():
            print(f'{vertex}: {edges}')

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            writer = csv.writer(file, delimiter=' ')
            writer.writerow([len(self.graph)])
            if self.matrix:
                for i in range(len(self.graph)):
                    row = []
                    for j in range(len(self.graph)):
                        row.append(self.graph[i].get(j, 0))
                    writer.writerow(row)
            else:
                for vertex, edges in self.graph.items():
                    for neighbor, weight in edges.items():
                        writer.writerow([vertex, neighbor, weight])


# Constructor A
graphA = Graph(filename='graphA.txt')
graphA.print_graph()

# Constructor B
graphB = Graph(filename='graphB.txt')
graphB.print_graph()

# Constructor C
graphC = Graph(filename='graphC.txt', matrix=True)
graphC.print_graph()
