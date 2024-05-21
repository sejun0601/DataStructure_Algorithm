from collections import deque

class Queue:
    def __init__(self) -> None:
        self.queue = deque()

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        item = self.queue.popleft()
        print(f"Dequeued: {item}")
        return item
    
    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[0]

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(f"Peek: {q.peek()}")
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()