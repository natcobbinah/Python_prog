from collections import deque

class Stack:

    def __init__(self):
        self.elements = deque([])
    
    def push(self,data):
        self.elements.append(data)
    
    def pop(self):
        return self.elements.pop()
    
    def peek(self):
        if self.elements:
            return self.elements[-1]
        else:
            return None
        
    def isEmpty(self):
       return len(self.elements) == 0
    
    def size(self):
        return len(self.elements)
