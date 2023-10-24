import heapq

class MyHeap:

    @classmethod
    def main(cls, args):
        myheap = [19,1,18] # creates heap from list
        heapq._heapify_max(myheap)
        print(myheap)

        heapq.heappush(myheap, 17)
        heapq.heappush(myheap, 9)
        heapq.heappush(myheap, 12)
        heapq.heappush(myheap, 15)

        heapq._heapify_max(myheap)
        print(myheap)

        print(heapq._heappop_max(myheap))


if __name__ == '__main__':
    import sys
    MyHeap.main(sys.argv)