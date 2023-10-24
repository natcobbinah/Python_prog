from collections import deque

class MyQueue:

    @classmethod
    def main(cls, args):
        a = deque([])
        a.append(5)
        a.append(4)
        a.append(3)
        a.append(2)
        a.append(1)
        a.append(0)

        print(a)
        print(a.popleft())
        print(a)

if __name__ == '__main__':
    import sys
    MyQueue.main(sys.argv)
