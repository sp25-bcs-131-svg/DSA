graph = {
    'A' : ['B','E','C'],
    'B' : ['A','D','E'],
    'C' : ['F','G','A'],
    'D' : ['B','E','F'],
    'E' : ['A','B','D','F'],
    'F' : ['E','C','D'],
    'G' : ['C'] 
}

visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end = " " )
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("Following is the Breadth-First Search")
bfs(visited, graph, 'A')
