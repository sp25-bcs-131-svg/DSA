graph = {
    'A': [('B', 3), ('C', 5), ('D', 2)],
    'B': [('E', 4)],
    'C': [('E', 2), ('F', 6)],
    'D': [('F', 7)],
    'E': [('G', 3), ('F', 5)],
    'F': [('I', 8), ('H', 2)],
    'G': [('I', 4)],
    'H': [('I', 3)],
    'I': []
}

heuristic = {
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


def greedy_best_first(graph, heuristic, start, goal):
    path = [start]
    distances = [0]
    visited = {start}

    while path:
        current = path[-1]

        if current == goal:
            print("Goal found!")
            print("Path:", " -> ".join(path))
            print("Total distance:", distances[-1])
            return

        neighbours = [(n, d) for n, d in graph[current] if n not in visited]

        if not neighbours:
            path.pop()
            distances.pop()
            continue

        best, distance = min(neighbours, key=lambda item: heuristic[item[0]])
        visited.add(best)
        path.append(best)
        distances.append(distances[-1] + distance)

    print("Goal not reachable")

greedy_best_first(graph, heuristic, 'A', 'I')