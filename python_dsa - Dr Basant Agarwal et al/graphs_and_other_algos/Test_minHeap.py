from min_heap import Heap

h = Heap()

for i in (4, 8, 7, 2, 9, 10, 5, 1, 3, 6):
    h.insert(i)
    print(h.heap)
##[0, 1, 2, 5, 3, 6, 10, 7, 8, 4, 9]

print()
# popping elements off the heap
for i in range(10):
    n = h.pop()
    print(n)
    print(h.heap)
