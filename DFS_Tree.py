class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

def dfs(root):
    visited = []
    stack = []
    stack.append(root)

    while stack:
        cur = stack[-1]
        visited.append(cur)
        if cur.children:
            choosed = choose_children(cur.children, visited)
            if choosed != None:
                stack.append(choosed)
            else:
                stack.pop()
        else:
            stack.pop()
            
    return visited

def choose_children(children, visited) -> TreeNode:

    for child in children:
        if child not in visited:
            return child
        else:
            continue
    return None





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
visited = dfs(root)
for i in visited:
    print(i.value)