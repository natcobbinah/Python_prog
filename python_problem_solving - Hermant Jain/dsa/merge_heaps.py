import heapq

list_1 = [12,42,15,25]
list_2 = [1,4,5,2,5,2]

list_3 = heapq.merge(list_1,list_2)
print(list(list_3))