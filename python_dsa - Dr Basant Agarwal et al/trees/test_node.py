from node import Node
from in_order_traversal import inorder
from post_order_traversal import postorder
from pre_order_traversal import preorder
from bfs import breadth_first_traversal

n1 = Node("4 rootNode")
n2 = Node("2 leftChild node")
n3 = Node("8 rightChild node")
n4 = Node("1 leftChild-leftGrandchild node")
n5 = Node("3 leftChild-rightGrandchild node")
n6 = Node("5 rightChild-leftGrandchild node")
n7 = Node("10 rightChild-rightGrandchild node")

n1.left_child = n2
n1.right_child = n3 
n2.left_child = n4
n2.right_child = n5 
n3.left_child = n6 
n3.right_child = n7

current = n1 # rootNode

# traversing the left-sub tree
""" current = n1
while current:
    print(current.data)
    current = current.left_child """

print("Inorder ------------------")
# using in-order traversal in DFS
inorder(current)

print("Preorder -----------------")
# using pre-order traversal in DFS
preorder(current)

print("Postorder -----------------")
# using post-order traversal in DFS
postorder(current)

print("BFS -----------------------")
#using breadth-first search traversal
print(breadth_first_traversal(current))