from bi_directionalNode import BidirectionalNode

class Queue:

    def __init__(self):
        self.head = None 
        self.tail = None 
        self.count = 0

    def enqueue(self,data):
        new_node = BidirectionalNode(data)
        if self.head:
            new_node.prev = self.tail 
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

        self.count += 1

    def dequeue(self):
        current = self.head 
        
        if self.count == 1:
            self.count -= 1
            self.head = None 
            self.tail = None 
        elif self.count > 1:
            self.head = self.head.next
            self.head.prev = None 
            self.count -= 1
        return current.data