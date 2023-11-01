from node import Node

class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self,data):
        new_node = Node(data)

        if self.top:
            new_node.next = self.top 
            self.top = new_node
        else:
            self.top = new_node
        self.size += 1

    def pop(self):
        if self.top:
            data = self.top.data 
            self.size -= 1
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            return None
        
    def peek(self):
        if self.top:
            return self.top.data 
        else:
            return None