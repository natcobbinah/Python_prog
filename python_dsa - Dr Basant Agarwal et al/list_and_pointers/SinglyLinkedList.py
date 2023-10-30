from Node import Node

class SinglyLinkedList:

    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def appendCostyOp(self,data): # O(n) operation node too desirable
        #Encapsulate the data in a node
        node = Node(data)

        if self.tail :
            current = self.tail #=  node(data, next)
            while current.next:
                current = current.next 
            current.next = node
        else:
             self.tail = node # = node (data, next)

    # fast append O(1)
    def append(self,data):
        self.size += 1 # the the linkedList size after each append operation in O(1) time

        node = Node(data)
        if self.head:
            self.head.next = node 
            self.head = node
        else:
            self.tail = node 
            self.head = node

    #delete op   O(n)
    def delete(self,data):
        current = self.tail 
        prev = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next 
                else:
                    prev.next = current.next 
                self.size -= 1 # keeping track of the size
                return
            prev = current
            current = current.next

    
    # getting the size of the list by traversing(costy operation O(n))
    def sizeCostyOp(self):
        count = 0
        current = self.tail
        while current:
            count += 1
            current = current.next
        return count

    # iterate through list
    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next 
            yield val

    # search through list
    def search(self,data):
        for node in self.iter():
            if node == data:
                return True 
        return False
    
    # clear entire list
    def clear(self):
        """Clear entire list"""
        self.tail = None 
        self.head = None
    
    # print list content
    def print(self):
        current = self.tail
        while current:
            print(current.data)
            current = current.next