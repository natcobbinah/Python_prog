import heapq

data = [-2,-4,-5,-2,-3,-4]
heapq.heapify(data)

while len(data):
    print(-1 * heapq.heappop(data))