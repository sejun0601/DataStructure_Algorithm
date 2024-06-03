class Graph:
    def __init__(self):
        # 그래프를 딕셔너리로 저장. 키는 노드, 값은 해당 노드로부터 나가는 간선들을 저장한 리스트
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, from_node, to_node):
        if from_node not in self.graph:
            self.graph[from_node] = []
        self.graph[from_node].append(to_node)

    def remove_edge(self, from_node, to_node):
        if from_node in self.graph:
            if to_node in self.graph[from_node]:
                self.graph[from_node].remove(to_node)

    def remove_node(self, node):
        if node in self.graph:
            del self.graph[node]
        for edges in self.graph.values():
            if node in edges:
                edges.remove(node)

    def has_edge(self, from_node, to_node):
        return from_node in self.graph and to_node in self.graph[from_node]

    def get_neighbors(self, node):
        return self.graph.get(node, [])

    def __str__(self):
        return str(self.graph)
    
    
# 그래프 객체 생성
g = Graph()

# 노드 추가
g.add_node('A')
g.add_node('B')
g.add_node('C')

# 간선 추가
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'C')

# 그래프 출력
print("Graph:")
print(g)

# 특정 노드의 이웃 확인
print("\nNeighbors of A:")
print(g.get_neighbors('A'))

# 간선 존재 여부 확인
print("\nDoes an edge exist from A to B?")
print(g.has_edge('A', 'B'))

# 간선 제거
g.remove_edge('A', 'B')
print("\nGraph after removing edge from A to B:")
print(g)

# 노드 제거
g.remove_node('C')
print("\nGraph after removing node C:")
print(g)
