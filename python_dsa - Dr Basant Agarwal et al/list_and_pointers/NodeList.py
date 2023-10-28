from Node import Node

n1 = Node('eggs')
n2 = Node('ham')
n3 = Node('spam')

# link nodes together to form a chain
n1.next = n2 
n2.next = n3

#traversing through the nodes
current = n1
while current:
    print(current.data)
    current = current.next