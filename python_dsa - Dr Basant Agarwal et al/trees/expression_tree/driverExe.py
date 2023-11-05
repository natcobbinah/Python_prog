from collections import deque
from treeNode import TreeNode

expr = "4 5 + 5 3 - *".split()

stack = deque([])

for term in expr:
    if term in "+-*/":
        node = TreeNode(term)
        node.right = stack.pop()
        node.left = stack.pop()
    else:
        node = TreeNode(int(term))
        stack.append(node)