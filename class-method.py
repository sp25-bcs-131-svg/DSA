class Graph:

    def __init__(self , graph_dict):
        self.graph = graph_dict

    def bfs(self,start_node):
        visited = []
        queue = []

        visited.append(start_node)
        queue.append(start_node)

        print("Following is the Breadth-First Search")

        while queue:
            m = queue.pop(0)
            print(m, end = " " )

            for neighbour in self.graph[m]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

graph_data = {
    'A' : ['B','E','C'],
    'B' : ['A','D','E'],
    'C' : ['F','G','A'],
    'D' : ['B','E','F'],
    'E' : ['A','B','D','F'],
    'F' : ['E','C','D'],
    'G' : ['C'] 
}

graph = Graph(graph_data)
graph.bfs('A')
