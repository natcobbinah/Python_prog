class MyDictionary:

    @classmethod
    def main(cls,args):
        a = {}
        a["apple"] = 40
        a["banana"] = 10
        a["mango"] = 20
        
        print(a)
        print(a["mango"])
        print(a.get("mango"))
        print("apple" in a)

if __name__ == '__main__':
    import sys
    MyDictionary.main(sys.argv)