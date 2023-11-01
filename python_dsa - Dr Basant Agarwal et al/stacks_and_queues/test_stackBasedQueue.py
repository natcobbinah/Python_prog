from stack_based_queue import Queue

queue = Queue()
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)

print(queue.inbound_stack)  # [5,6,7]
print(queue.dequeue())      # [7,6] as first element will be popped-out = 5
print(queue.inbound_stack)  # []
print(queue.outbound_stack) # [7,6]
print(queue.dequeue())      # 6 popped out
print(queue.outbound_stack) # [7]
