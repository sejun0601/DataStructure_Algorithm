class ListNode:
    def __init__(self, val = 0 , next = None):
        self.val = val
        self.next = next

class CircularLinkedList:
    def __init__(self) :
        self.head = None

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False
    
    def append(self, data):

        newnode = ListNode(data, None)
        
        if self.head:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = newnode
            newnode.next = self.head
        else:
            self.head = newnode
            newnode.next = self.head
    
    def remove(self, data):

        if self.is_empty():
            print("the list is empty")
            return
        
        cur = self.head
        while True:

            if cur.next.val == data:
                temp = cur.next.next
                cur.next = temp
                return
            cur = cur.next
            if cur == self.head:
                break


    def print_list(self):
        if self.head:
            cur = self.head
            while True:
                print(f"{cur.val} -> ", end="")
                cur = cur.next
                if cur == self.head:
                    break
        else:
            print("no nodes in the list")

    

clist = CircularLinkedList()
clist.append(1)
clist.append(2)
clist.append(3)
clist.append(4)
clist.append(5)
clist.remove(4)
clist.print_list()