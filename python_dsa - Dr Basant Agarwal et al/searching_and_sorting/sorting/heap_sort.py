from min_heap import Heap

h = Heap()
unsorted_list = [15,12,67,45,19,18,34,27,98,5,3]

for i in unsorted_list:
    h.insert(i)

print(f"Unsorted list: {unsorted_list}")
print(f"Heap Structure: {h.heap}")

#heap-sort
def heap_sort():
    sorted_list = []
    for node in range(len(unsorted_list)):
        n = h.pop()
        sorted_list.append(n)    

    return sorted_list

print(f"Heap sort: {heap_sort()}")
