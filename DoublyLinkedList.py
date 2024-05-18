class ListNode:
    def __init__(self, data):
        self.val = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def append(self, data):

        newnode = ListNode(data)
        if self.head == None:
            self.head = newnode
            return
        
        cur = self.head

        while cur.next != None:
            cur = cur.next
        cur.next = newnode
        newnode.prev = cur

    def prepend(self,data):
        newnode = ListNode(data)
        if self.head ==None:
            self.head = newnode
            return

        cur = self.head
        newnode.next = cur
        cur.prev = newnode
        self.head = newnode

    def delete(self, index):
        if self.head == None:
            print("the list is empty")
            return

        cur = self.head
        for i in range(index):
            cur = cur.next

        p = cur.prev
        n = cur.next
        if p == None:
            self.head = n
            return
        if n == None:
            p.next = None
            return
        p.next = n
        n.prev = p

    def print_list(self):

        if self.head ==None:
            print("list is empty")

        cur = self.head
        while cur != None:
            print(f"{cur.val} -> ", end="")
            cur = cur.next

dlist = DoublyLinkedList()
dlist.append(1)
dlist.append(2)
dlist.prepend(0)
dlist.delete(2)
dlist.print_list()