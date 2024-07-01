class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_at_tail(self,value):
        node = Node(value)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
    
    def add_at_head(self,value):
        node = Node(value)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head  = node
        self.size += 1

    def display_linked_list(self):
        trav_node = self.head
        while trav_node != None:
            print(trav_node.data)
            trav_node = trav_node.next
        
    def display_linked_list_reverse(self):
        trav_node = self.head
        stack = []
        while trav_node != None:
            stack.append(trav_node.data)
            trav_node = trav_node.next
        while stack:
            print(stack.pop())
    
    def inplace_reverse(self):
        prev = None
        current = self.head
        while current != None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        self.display_linked_list()

    def get(self,index):
        trav_node = self.head
        count = 0
        while trav_node != None:
            if count == index:
                return trav_node.data
            trav_node = trav_node.next
            count += 1


ll = LinkedList()
ll.add_at_tail(1)
ll.add_at_tail(2)
ll.add_at_tail(3)
ll.add_at_tail(4)
ll.add_at_tail(5)
ll.add_at_head(0)
ll.add_at_head(-1)
print("Displaying linked list")
ll.display_linked_list()
print("Displaying linked list in reverse")
ll.inplace_reverse()
print("Displaying linked list")
ll.display_linked_list()
print("Displaying linked list in reverse")
ll.inplace_reverse()
print("Displaying item at index 2")
print(ll.get(2))