from list_based_queue import ListQueue

queue = ListQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

print(queue.size)

print()
queue.dequeue()

print()
print(queue.size)