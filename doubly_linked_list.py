class Node:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val

class MyLinkedList:   
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        print(f"performing get at index {index}\n")
        count = 0
        trav_node = self.head
        while trav_node != None:
            #print(trav_node.val)
            if count == index: 
                return trav_node.val
            trav_node = trav_node.next
            count = count + 1
        return -1

    def addAtHead(self, val: int) -> None:
        print(f"performing add at head {val}\n")
        node = Node(val)
        node.next = self.head
        node.prev = None
        if self.head == None:
            self.tail = node
        self.head = node
        self.head.prev = None
        self.size += 1
        self.display_list()
        #print(self.head.val)
        #print(self.tail.val)
        #print('\n')

    def addAtTail(self, val: int) -> None:
        print(f"performing add at Tail {val}\n")
        #print(self.tail.val)
        node = Node(val)
        node.next = None
        node.prev = self.tail
        if self.size == 0:
            self.head = node
            self.tail = node
            self.size += 1
            self.display_list()
        else:
            trav_node = self.head
            while trav_node.next != None:
                trav_node = trav_node.next
            self.tail = node
            trav_node.next = node
            self.size += 1
            self.display_list()


    def deleteAtTail(self) -> None:
        print(f"performing delete at Tail\n")
        self.tail.prev.next = None
        self.size -= 1
        self.display_list() 
        
    def addAtIndex(self, index: int, val: int) -> None:
        print(f"performing add at index {index} {val}\n")
        count = 0
        trav_node = self.head
        if index == 0:
            self.addAtHead(val)
            return
        while trav_node != None:
            if count == index-1:
                print(f'count : {count}')
                print(f'index : {index}')
                print(f'self.size : {self.size}')
                if count == (self.size - 1) and index != 1:
                    print("inside count")
                    self.addAtTail(val)
                    self.display_list()
                else:
                    node = Node(val)
                    node.next = trav_node.next
                    node.prev = trav_node
                    trav_node.next = node
                    trav_node.next.prev = node
                    self.size += 1
                    self.display_list()
                    return
            trav_node = trav_node.next
            count = count + 1
        return -1
    
    def deleteAtIndex(self, index: int) -> None:
        print(f"performing delete at index {index}\n")
        #self.display_list()
        trav_node = self.head
        count = 0
        if index == 0 and self.size == 1:
            self.head = None
            self.size -= 1
            self.display_list()
            return
        elif index == 0 and self.size > 1:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
            self.display_list()
            return
        elif index >= self.size:
            return -1
            self.display_list()
        while trav_node :
            self.display_list()
            if count == index - 1:
                if count == self.size - 2:
                    print('inside count')
                    trav_node.next = None
                    self.size -= 1
                    self.display_list()
                    return
                #print(f'trav_node.val : {trav_node.val}')
                #print(trav_node.next.val)
                #print(trav_node.next.next.val)
                trav_node.next = trav_node.next.next
                trav_node.next.prev = trav_node
                self.size -= 1
                self.display_list()
                return
            trav_node = trav_node.next
            count = count + 1
        return -1

    def display_list(self):
        trav_node = self.head
        print(f"size : {self.size}\n")
        #print(f"self.tail : {self.tail}\n")
        print(f'self.tail : {self.tail.val}\n')
        while trav_node:
            print(trav_node.val)
            trav_node = trav_node.next
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(38)
obj.addAtTail(66)
obj.addAtTail(61)
obj.addAtTail(76)
obj.addAtTail(26)
obj.addAtTail(37)
obj.addAtTail(8)
obj.deleteAtIndex(5)
obj.addAtHead(4)
obj.addAtHead(45)
obj.get(4)
obj.addAtTail(85)
obj.addAtHead(37)
obj.get(5)
obj.addAtTail(93)
obj.addAtIndex(10,23)
obj.addAtTail(21)
obj.addAtHead(52)
obj.addAtHead(15)
obj.addAtHead(47)
obj.get(12)
obj.addAtIndex(6,24)
obj.addAtHead(64)
obj.get(4)
obj.addAtHead(31)
obj.deleteAtIndex(6)
obj.addAtHead(40)
obj.addAtTail(17)
obj.addAtTail(15)
obj.addAtIndex(19,2)
obj.addAtTail(11)
obj.addAtHead(86)
obj.get(17)
obj.addAtTail(55)
obj.deleteAtIndex(15)
obj.addAtIndex(14,95)
obj.deleteAtIndex(22)
obj.addAtHead(66)
obj.addAtTail(95)
obj.addAtHead(8)
obj.addAtHead(47)
obj.addAtTail(23)
obj.addAtTail(39)
obj.get(30)
obj.get(27)
obj.addAtHead(0)
obj.addAtTail(99)
obj.addAtTail(45)
obj.addAtTail(4)
obj.addAtIndex(9,11)
obj.get(6)
obj.addAtHead(81)
obj.addAtIndex(18,32)
obj.addAtHead(20)
obj.addAtTail(13)
obj.addAtTail(42)
obj.addAtIndex(37,91)
obj.deleteAtIndex(36)
obj.addAtIndex(10,37)
obj.addAtHead(96)
obj.addAtHead(57)
obj.deleteAtIndex(20)
obj.addAtTail(89)
obj.deleteAtIndex(18)
obj.addAtIndex(41,5)
obj.addAtTail(23)
obj.addAtHead(75)
obj.get(7)
obj.addAtIndex(25,51)
obj.addAtTail(48)
obj.addAtHead(46)
obj.addAtHead(29)
obj.addAtHead(85)
obj.addAtHead(82)
obj.addAtHead(6)
obj.addAtHead(38)
obj.deleteAtIndex(14)
obj.get(1)
obj.get(12)
obj.addAtHead(42)
obj.get(42)
obj.addAtTail(83)
obj.addAtTail(13)
obj.addAtIndex(14,20)
obj.addAtIndex(17,34)
obj.addAtHead(36)
obj.addAtTail(58)
obj.addAtTail(2)
obj.get(38)
obj.addAtIndex(33,59)
obj.addAtHead(37)
obj.deleteAtIndex(15)
obj.addAtTail(64)
obj.get(56)
obj.addAtHead(0)
obj.get(40)
obj.addAtHead(92)
obj.deleteAtIndex(63)
obj.get(35)
obj.addAtTail(62)
obj.addAtTail(32)