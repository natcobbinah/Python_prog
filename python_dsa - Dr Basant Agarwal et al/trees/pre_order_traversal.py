def preorder(root_node):
    current = root_node
    if current == None:
        return
    print(current.data)
    preorder(current.left_child)
    preorder(current.right_child)