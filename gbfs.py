graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'C': ['E', 'F'],
    'D': ['F'],
    'E': ['G', 'F'],
    'F': ['I', 'H'],
    'G': ['I'],
    'H': ['I'],
    'I': []
}

h = {
    'A': 10,
    'B': 8,
    'C': 2,
    'D': 1,
    'E': 2,
    'F': 6,
    'G': 3,
    'H': 4,
    'I': 0
}

current = 'A'
goal = 'I'
path = [current]

while current != goal:
    neighbors = graph[current]
    best_node = neighbors[0]

    for node in neighbors:
        if h[node] < h[best_node]:
            best_node = node

    current = best_node
    path = path + [current]

print("Path:", path)