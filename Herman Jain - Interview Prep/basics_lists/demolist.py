mylist = list(range(5))
mylist2 = [5,6]

print(mylist) # 0 1 2 3 4
print(len(mylist)) # 5
print(mylist + mylist2) # 0 1 2 3 4 5 6
print(mylist*2) # 0 1 2 3 4 0 1 2 3 4
print(mylist[0]) # 0
print(mylist[1:4]) # 1 2 3

mylist[1] = 100
print(mylist) # 0 100 2 3 4
mylist.append(5)
print(mylist) # 0 100 2 3 4 5
mylist.pop()
print(mylist) # 0 100 2 3 4
mylist.reverse()
print(mylist) # 4 3 2 100 0
mylist.sort()
print(mylist) # 0 2 3 4 100