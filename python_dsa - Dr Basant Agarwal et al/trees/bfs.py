from collections import deque

def breadth_first_traversal(root_node):
    list_of_nodes = [] # to keep track of visited nodes
    traversal_queue = deque([root_node])

    while len(traversal_queue) > 0:
        node = traversal_queue.popleft()

        list_of_nodes.append(node.data)
        if node.left_child:
            traversal_queue.append(node.left_child)
            
        if node.right_child:
            traversal_queue.append(node.right_child)
    return list_of_nodes