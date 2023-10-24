class MyStack:

    @classmethod
    def main(cls,args):
        a = []
        a.append(1)
        a.append(2)
        a.append(3)
        a.append(4)
        print(a)
        print(len(a))
        print(a.pop())
        print(a)

if __name__ == "__main__":
    import sys
    MyStack.main(sys.argv)