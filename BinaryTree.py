class TreeNode():
    def  __init__(self,key) -> None:
          self.left = None
          self.right = None
          self.value = key
class BinaryTree:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)
    
    def _insert(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left,key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right,key)

    def inorder_traversal(self, node , result = None):
        if result is None:
            result = []
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)
        return result
    
    def postorder_traversal(self, node, result = None):
        if result is None:
            result = []
        
        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.value)
        return result
    
    def preorder_traversal(self, node, result = None):
        if result is None:
            result = []
        
        if node:
            result.append(node.value)
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            
        return result
    
    def search(self, node, value):
        if value < node.value:
            return self.search(node.left,value)
        elif value == node.value:
            return node.value
        else:
            return self.search(node.right, value) 


bt = BinaryTree()
bt.insert(10)
bt.insert(5)
bt.insert(15)
bt.insert(3)
bt.insert(7)
bt.insert(12)
bt.insert(18)

print(bt.search(bt.root, 5))

print("Inorder traversal:", bt.inorder_traversal(bt.root))
print("Preorder traversal:", bt.preorder_traversal(bt.root))
print("Postorder traversal:", bt.postorder_traversal(bt.root))