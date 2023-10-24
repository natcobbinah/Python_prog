import heapq

class MyHeap:

    @classmethod
    def main(cls, args):
        myheap = [19,1,18] # creates heap from list
        heapq.heapify(myheap)
        print(myheap)

        heapq.heappush(myheap, 5)
        heapq.heappush(myheap, 3)
        heapq.heappush(myheap, 8)
        heapq.heappush(myheap, 2)
        print(myheap)

        print(heapq.heappop(myheap)) # pops the smallest item from the heap
        print(myheap)
        print(myheap[0]) # peek the smallest element from the heap
        print(len(myheap))

if __name__ == '__main__':
    import sys
    MyHeap.main(sys.argv)