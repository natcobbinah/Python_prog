import sys

class ParameterPass:

    def __init__(self):
        A = 1
        self.Change(A)
        print(A)

    def Change(self,B):
        B = 2

p = ParameterPass()

