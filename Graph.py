class Graph:
    def __init__(self) -> None:
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self , vertex1, vertex2):
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)
        
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            for adjacent in list(self.graph[vertex]):
                self.graph[adjacent].remove(vertex)
            del self.graph[vertex]

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph[vertex1]:
            self.graph[vertex1].remove(vertex2)
        if vertex2 in self.graph and vertex1 in self.graph[vertex2]:
            self.graph[vertex2].remove(vertex1)

    def get_vertices(self):
        return list(self.graph.keys())
    
    def get_edges(self):
        edges = []
        for vertex in self.graph:
            for adjecent in self.graph[vertex]:
                if {vertex, adjecent} not in edges:
                    edges.append({vertex, adjecent})
        return edges

    def __str__(self) -> str:
        return str(self.graph)

g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_edge("A", "B")
g.add_edge("A", "D")
g.add_edge("B", "C")
g.add_edge("B", "E")
g.add_edge("D", "E")

print("Graph:", g)
print("Vertices:", g.get_vertices())
print("Edges:", g.get_edges())

g.remove_edge("A", "B")
print("Graph after removing edge A-B:", g)

g.remove_vertex("A")
print("Graph after removing vertex A:", g)