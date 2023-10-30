from BidirectionalNode import BidirectionalNode

class DoublyLinkedList:

    def __init__(self):
        self.head = None 
        self.tail = None 
        self.size = 0

    def append(self, data): #O(1)
        """Append an item to the list"""

        new_node = BidirectionalNode(data,None,None)

        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail 
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1
    
    def delete(self,data): # O(n)
        """Delete a node from the list"""
        current = self.head 
        node_deleted = False

        if current == None: #item to be deleted is not found in the list
            node_deleted = False 
        elif current.data == data: # item to be deleted is found at starting of the list
            self.head = current.next 
            self.head.prev = None 
            node_deleted = True
        elif self.tail.data == data: #item to be deleted is found at the end of the list
            self.tail = self.tail.prev
            self.tail.next = None 
            node_deleted = True 
        else:  # item to be deleted is in_between head and tail
            while current: # search item to be deleted and delete that node
                if current.data == data:
                    current.prev.next = current.next 
                    current.next.prev = current.prev 
                    node_deleted = True 
                current = current.next
        
        if node_deleted:
            self.size -= 1

    def iter(self):
        current = self.head 
        while current:
            val = current.data 
            current = current.next 
            yield val
    
    def contain(self,data):
        for node_data in self.iter():
            if data == node_data:
                return True 
        return False

    def print(self):
        current = self.head 
        while current:
            print(current.data)
            current = current.next
    
    