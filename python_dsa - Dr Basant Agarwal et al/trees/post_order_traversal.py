def postorder(root_node):
    current = root_node
    if current == None:
        return
    postorder(current.left_child)
    postorder(current.right_child)
    print(current.data)