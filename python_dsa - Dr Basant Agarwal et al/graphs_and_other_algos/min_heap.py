class Heap:

    def __init__(self):
        self.heap = [0] # dummy first element to make the maths easier by using 2n for left-child and 2n+1 for right-child
        self.size = 0

    def arrange(self,k):
        while k // 2 > 0: # integer floor division
            if self.heap[k] < self.heap[k//2]:
                self.heap[k], self.heap[k//2] = self.heap[k//2], self.heap[k]
            k //= 2
    
    def insert(self,item):
        self.heap.append(item)
        self.size += 1
        self.arrange(self.size)
    
    def minIndex(self,k):
        # we may get beyond the list, if we do, then we return the index of the left child
        if k * 2 + 1 > self.size:
            return k * 2
        # otherwise, we simply return the index of the lesser of the two children
        elif self.heap[k*2] < self.heap[k*2 + 1]:
            return k * 2
        else:
            return k * 2 + 1
    
    def sink(self,k):
        while k * 2 <= self.size:
            mi = self.minIndex(k) # which of the children (left or right) to compare against

            # now we compare parent with the child to see if a swap should occur
            if self.heap[k] > self.heap[mi]:
                self.heap[k], self.heap[mi] = self.heap[mi], self.heap[k]
            
            # we need to move down the tree so we don't get stuck in a loop
            k = mi

    def pop(self):
        item = self.heap[1] # removing the root element from the heap
        self.heap[1] = self.heap[self.size] # assign the last element to the root node
        self.size -= 1
        self.heap.pop()
        self.sink(1) # compare the root node to its children and place it at where it needs to be
        return item # return root element
