from Circular_SinglyLinkedList import CircularSinglyLinkedList

c = CircularSinglyLinkedList()
c.append('ham')
c.append('spam')
c.append('dam')

print(c.size)

print()

#c.delete('ham')
print(c.size)

print()

counter = 0
for word in c.iter():
    print(word)
    counter += 1
    if counter >= c.size:
        break
