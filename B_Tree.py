class BTreeNode:
    def __init__(self, leaf = True) -> None:
        self.leaf = leaf
        self.keys = []
        self.children = []
    
    def display(self, level = 0):
        print(f"level {level} : {self.keys}")
        if not self.leaf:
            for child in self.children:
                child.display(level + 1)

class BTree:
    def __init__(self, t) -> None:
        self.root = BTreeNode(True)
        self.t = t