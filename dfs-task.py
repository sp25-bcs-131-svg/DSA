graph = {
    'S' : ['C','B','A'],
    'A' : ['D','E'],
    'B' : ['E','G'],
    'C' : ['E'],
    'D' : ['G'],
    'E' : ['H'],
    'H' : ['G'],
    'G' : []
}

visited = set()

def dfs(visited,graph,node,goal):

    if node not in visited:
        print(node , end=' ')
        visited.add(node)

        if node == goal:
            print("\nGoal Reached")
            return True

        for neighbour in graph[node]:
            if dfs(visited,graph,neighbour,goal):
                return True

    return False

print("Following is the Depth-First Search")
dfs(visited,graph,'S','G')

