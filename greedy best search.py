graph = {
    'A' : ['B','C','D'],
    'B' : ['E'],
    'C' : ['E','F'],
    'D' : ['F'],
    'E' : ['G','F'],
    'F' : ['H','I'],
    'G' : ['I'],
    'H' : ['I'],
    'I' : []
}

heuristic = {
    'A' : 10,
    'B' : 8,
    'C' : 7,
    'D' : 9,
    'E' : 5,
    'F' : 6,
    'G' : 3,
    'H' : 4,
    'I' : 0 
}

def greedy_best_first(graph,heuristic,start,goal):

    frontier = [start]
    visited = set()

    while frontier:

        current = min(frontier,key=lambda node: heuristic[node])
        frontier.remove(current)

        print(current)

        if current == goal:
            print("Goal Found")
            return

        visited.add(current)

        for neighbour in graph[current]:
            if neighbour not in visited and neighbour not in frontier:
                frontier.append(neighbour)

greedy_best_first(graph,heuristic,'A','I')
