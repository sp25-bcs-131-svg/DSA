import heapq

graph = {
    'S' : {'B':1,'A':3,'C':2},
    'B' : {'E':5,'G':10},
    'A' : {'D':4,'E':1},
    'C' : {'E':2},
    'D' : {'G':8},
    'E' : {'H':1},
    'H' : {'G':1},
    'G' : {}
}

def ucs(graph,start,goal):
    queue = [(0,start,[start])]
    visited = set()

    while queue:
        cost , node , path = heapq.heappop(queue)

        if node == goal:
            print("Goal Reached")
            print("Path","-->".join(path))
            print("Total cost:",cost)
            return

        if node not in visited:
            visited.add(node)

            for neighbour , weight in graph[node].items():
                if neighbour not in visited:
                    new_cost = cost + weight
                    new_path = path + [neighbour]
                    heapq.heappush(queue,(new_cost,neighbour,new_path))

print("Following is the Uniform Cost Search")
ucs(graph,'S','G')
