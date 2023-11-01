class ListQueue:

    def __init__(self):
        self.items = []
        self.size = 0

    # not very efficient as all elements are shifted by one space,
    # which will make the process slow for very large lists
    def enqueue(self,data):
        self.items.insert(0,data) # always insert items at index 0
        self.size += 1            # increment the size of the queue by 1

    def dequeue(self):
        data = self.items.pop() # delete the topmost item from the queue
        self.size -= 1          # decrement the size of the queue by 1
        return data 