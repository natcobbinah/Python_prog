from collections import OrderedDict

class MyOrderedDict:

    @classmethod
    def main(cls,args):
        b = OrderedDict()
        b["apple"] = 40
        b["banana"] = 10
        b["mango"] = 20

        print(b)
        print(b["mango"])
        print(b.get("mango"))
        print("banana" in b)

if __name__ == '__main__':
    import sys
    MyOrderedDict.main(sys.argv)