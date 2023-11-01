from node_based_queue import Queue

queue = Queue()
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
queue.enqueue(8)

print(queue.count)
print()
print(queue.dequeue())
print()
print(queue.dequeue())