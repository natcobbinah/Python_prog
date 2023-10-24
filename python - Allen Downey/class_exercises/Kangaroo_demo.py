class Kangaroo:
    
    def __init__(self, contents = None):

        if contents == None:
            contents = []
        self.pouch_contents = contents

    def put_in_pouch(self,item):
        self.pouch_contents.append(item)

    def __str__(self):
        res = []
        for x in self.pouch_contents:
            if isinstance(x,Kangaroo):
                for attr in vars(x):
                    res.append(getattr(x,attr))
            else:
                 res.append(x)
        return str(res)

kanga = Kangaroo()
roo = Kangaroo(['rice','meat','beef'])
kanga.put_in_pouch(roo)
kanga.put_in_pouch(['jollof'])

print(kanga)
print(roo)