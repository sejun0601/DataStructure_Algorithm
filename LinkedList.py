class ListNode:
    def __init__(self, val = 0 , next = None):
        self.val = val
        self.next = next
    def print_node(self):
        print(self.val)
    


class LinkedList:
    def __init__(self, data):
        self.head = ListNode(data)
    
    def append(self, data):
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = ListNode(data)

    def print_list(self):
        cur = self.head
        while cur != None:
            print(f"{cur.val} -> ", end="")
            cur = cur.next
        print("")

    def get_node(self, index):
        cur = self.head
        for i in range(index):
            if(cur.next == None):
                print("this node doesn't exist")
                return None
            else:
                cur = cur.next
        return cur
    
    def get_size(self):
        size = 0
        cur = self.head
        while cur != None:
            size += 1
            cur = cur.next
        return size

    def add_node(self, index, val):
        size = self.get_size()

        if(index >= size):
            print("use append method")
        else:
            cur = self.get_node(index)
            newnode = ListNode(val, None) 
            if(cur == self.head):
                newnode.next = self.head
                self.head = newnode
            else:
                prev = self.get_node(index - 1)
                prev.next = newnode
                newnode.next = cur      
    
    def delete_node(self, index):
        size = self.get_size()

        if(index >= size):
            print("can't delete a non existing node")
        else:
            cur = self.get_node(index)
            if(cur == self.head):
                self.head = self.head.next
            else:
                prev = self.get_node(index-1)
                prev.next = cur.next



llist = LinkedList(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.print_list()
llist.add_node(3, 100)
llist.print_list()
llist.delete_node(0)
llist.print_list()
llist.print_list()