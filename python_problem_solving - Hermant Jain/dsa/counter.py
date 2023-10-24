from collections import Counter 

class MyCounter:

    @classmethod
    def main(cls,args):
        seq = [1,1,2,2,3,3,4,4,4,4]

        mycounter = Counter(seq)

        print(mycounter)
        print(mycounter.get(3))
       
        mycounter.pop(4)
        print(4 in mycounter)

        mycounter[5] += 1
        mycounter[5] += 1

        print(mycounter)

if __name__ == '__main__':
    import sys
    MyCounter.main(sys.argv)
