import heapq

ucs_graph = {
    'S': [('A', 1), ('B', 5), ('C', 15)],
    'A': [('G', 10)],
    'B': [('G', 5)],
    'C': [('G', 5)],
    'G': []
}

def uniform_cost_search(graph,start,goal):
    pq = [(0,start,[start])]
    visited = {}

    while pq:
        cost , node , path = heapq.heappop(pq)

        if node == goal:
            return path, cost

        if node not in visited or cost < visited[node]:
            visited[node] = cost
            for neighbour , step_cost in graph.get(node , []):
                new_cost = cost + step_cost
                heapq.heappush(pq , (new_cost , neighbour , path + [neighbour  ]))

    return None , float('inf')

path , cost = uniform_cost_search(ucs_graph , 'S' , 'G')
print(f"Optimal Path: {path}")
print(f"Total Cost: {cost}")