class Stack:
    def __init__(self) -> None:
        self.items = []
    
    def is_empty(self) : 
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):

        pop_object = None
        if self.is_empty():
            print("stack is empty")
        else:
            pop_object = self.items.pop()

        return pop_object
    
    def top(self):
        top_object = None
        if self.is_empty():
            print("stack is empty")
        else:
            top_object = self.items[-1]
        return top_object
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.top())
print(stack.pop())
