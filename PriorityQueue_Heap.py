class MinHeap:
    def __init__(self) -> None:
        self.heap  = []
    
    def insert(self,key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) -1)

    def _heapify_up(self, index):
        parent_index = (index - 1)//2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index] , self.heap[index]
            self._heapify_up(parent_index)
        
    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_down(self, index):
        smallest = index
        left_child = 2*index + 1
        right_child = 2*index + 2

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child
        
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    
class PriorityQueue:
    def __init__(self) -> None:
        self.min_heap = MinHeap()
    
    def push(self, key):
        self.min_heap.insert(key)
    
    def pop(self):
        return self.min_heap.extract_min()
    
    def peek(self):
        return self.min_heap.heap[0] if self.min_heap.heap else None

pq = PriorityQueue()
pq.push(3)
pq.push(1)
pq.push(5)
pq.push(2)

print("Min element:", pq.pop())  # 출력: 1
print("Min element:", pq.pop())  # 출력: 2
print("Min element:", pq.pop())  # 출력: 3
print("Min element:", pq.pop())  # 출력: 5