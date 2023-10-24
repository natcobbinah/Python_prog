class ParameterPass2:

    def __init__(self):
        A = [1,2]
        self.Change(A)
        print(A)
    
    def Change(self,B):
        B.append(3)

p = ParameterPass2()
print(p)