class ParameterPass:

    def __init__(self):
        A = 1
        self.Change(A)
        print(A)
    
    def Change(self,B):
        B = 2

if __name__ == '__main__':
 p = ParameterPass()
 print(p)
