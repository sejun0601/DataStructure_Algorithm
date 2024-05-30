class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

from collections import deque

def bfs(root):
    if root is None:
        return []

    visited = []
    queue = deque([root])

    while queue:
        current_node = queue.popleft()
        visited.append(current_node.value)
        
        for child in current_node.children:
            queue.append(child)

    return visited

# 트리 노드 생성
root = TreeNode('A')
b_node = TreeNode('B')
c_node = TreeNode('C')
d_node = TreeNode('D')
e_node = TreeNode('E')
f_node = TreeNode('F')
g_node = TreeNode('G')
h_node = TreeNode('H')

# 트리 구성
root.add_child(b_node)
root.add_child(c_node)
b_node.add_child(d_node)
b_node.add_child(e_node)
c_node.add_child(f_node)
c_node.add_child(g_node)
e_node.add_child(h_node)

# BFS 실행
print("BFS 탐색 순서:", bfs(root))
