class TreeNode():
    def  __init__(self,key) -> None:
          self.left = None
          self.right = None
          self.value = key
          self.height = 1
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

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1 and key< node.left.value:
            return self.right_rotate(node)
        if balance < -1 and key > node.left.value:
            return self.left_rotate(node)
        if balance > 1 and key > node.left.value:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and key < node.left.value:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def right_rotate(self, z):
        y = z.left
        x = y.right

        y.right = z
        z.left = x

        z.height = 1+max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1+max(self.get_height(y.left), self.get_height(y.right)) 


        return y
    
    def left_rotate(self, z):
        y = z.right
        x = y.left

        y.left = z
        z.right = x

        z.height = 1+max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1+max(self.get_height(y.left), self.get_height(y.right)) 


        return y    

    def get_height(self,node):
        if not node:
            return 0
        return node.height

    def get_balance(self,node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

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