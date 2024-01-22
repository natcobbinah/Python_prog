import sys

class ParameterPass:

    def __init__(self):
        A = [1,2]
        self.Change(A)
        print(A)

    def Change(self,B):
        B = [3,4]

p = ParameterPass()

