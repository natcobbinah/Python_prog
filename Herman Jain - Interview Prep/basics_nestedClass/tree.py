class Tree:
    class Node:
        def __init__(self, v, l=None, r=None):
            self.value = v
            self.lChild = l
            self.rChild = r

    def __init__(self):
        self.root = None
