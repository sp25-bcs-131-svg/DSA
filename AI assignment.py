from collections import deque

def bfs(graph,start,goal):

    if start == goal:
        return [start], 0

    queue = deque([start])
    visited = set([start])
    parent = {start: None}
    expanded_count = 0

    while queue:
        current = queue.popleft()
        expanded_count += 1

        for next in sorted(graph.get(current, [])):
            if next not in visited:
                visited.add(next)
                parent[next] = current

                if next == goal:
                    path = []
                    node = next
                    while node is not None:
                        path.append(node)
                        node = parent[node]
                    return path[::-1],expanded_count
                
                queue.append(next)

    return None,expanded_count

romania_graph = {
    'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
    'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J'],
    'F': ['K'],
    'G': ['L', 'M'],
    'I': ['N'],
    'K': ['O']
}

path_01 , node_expanded_01 = bfs(romania_graph,'Arad','Bucharest')
print("BFS on Romania Graph (Arad to Bucharest) ")
print(f"Path: {' -> '.join(path_01)}")
print(f"Nodes Expanded : {node_expanded_01}\n")

path_02 , node_expanded_02 = bfs(tree,'A','K')
print("BFS on Tree (A to K)")
print(f"Path: {' -> '.join(path_02)}")
print(f"Nodes Expanded : {node_expanded_02}")