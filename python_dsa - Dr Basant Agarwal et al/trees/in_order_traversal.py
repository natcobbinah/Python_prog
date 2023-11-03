def inorder(root_node):
    current = root_node
    if current == None:
        return 
    inorder(current.left_child)
    print(current.data)
    inorder(current.right_child)