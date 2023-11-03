from node import Node

class Tree:

    def __init__(self):         # the rootNode is all that is needed to 
        self.root_node = None   # maintain the state of a bst tree

    def find_min(self): # runtime O(h) where h is the height of the tree
        current = self.root_node
        while current.left_child:
            current = current.left_child
        return current
    
    def find_max(self): # runtime O(h) where h is the height of the tree
        current = self.root_node
        while current.right_child:
            current = current.right_child 
        return current
    
    def insert(self, data):
        node = Node(data)
        if self.root_node == None:
            self.root_node = node 
        else:
            current = self.root_node
            parent = None 
        while True:
            parent = current
            if node.data < parent.data:
                current = current.left_child
                if current == None:
                    parent.left_child = node 
                    return
                else:
                    current = current.right_child
                    if current == None:
                        parent.right_child = node 
                        return
        