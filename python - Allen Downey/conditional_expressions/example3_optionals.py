class GoodKangaroo:

    def __init__(self, name, content = None):
        self.name = name
        if content == None: 
            content = []
        else:
            self.pouch_contents = content

class GoodKangaroo2:

    def __init__(self, name, content = None):
        self.name = name 
        self.pouch_contents = [] if content == None else content