from DoublyLinkedList import DoublyLinkedList

d = DoublyLinkedList()
d.append("chicken")
d.append("egg")
d.append("farmer")

print(d.contain("chicken")) # True
print(d.contain("rice")) # False

print()

# print content of list using iter method
for  content in d.iter():
    print(content)

print()
# print content of list using in_built print method
d.print()

print(d.size) # 2, bcos count starts from 0 and 3 items = (2)

d.delete("farmer")

print(d.size) # 1, after deletion items left = (1)
