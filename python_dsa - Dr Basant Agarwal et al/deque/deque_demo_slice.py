from  collections import deque
import itertools

dq = deque('abc') # creates deque(['a','b','c'])
dq.append('d') # creates deque(['a','b','c','d'])
dq.appendleft('z')  # creates deque(['z','a','b','c','d'])
dq.extend('efg')  # creates deque(['z','a','b','c','d','e','f','g'])
dq.extendleft('yxw') # creates deque(['w','x','y','z','a','b','c','d','e','f','g'])

print(list(itertools.islice(dq,3,9))) # queues cannot be sliced directly so we use itertools