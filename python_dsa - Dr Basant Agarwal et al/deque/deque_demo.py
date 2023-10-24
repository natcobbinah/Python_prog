from  collections import deque

dq = deque('abc') # creates deque(['a','b','c'])
print(dq)

print()

dq.append('d') # creates deque(['a','b','c','d'])
dq.appendleft('z')  # creates deque(['z','a','b','c','d'])
dq.extend('efg')  # creates deque(['z','a','b','c','d','e','f','g'])
dq.extendleft('yxw') # creates deque(['w','x','y','z','a','b','c','d','e','f','g'])

print(dq)