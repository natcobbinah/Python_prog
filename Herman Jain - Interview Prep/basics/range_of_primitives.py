import sys

class VariableType:

    @classmethod
    def main(cls,args):
        maxInt = sys.maxsize
        longStart = maxInt + 1
        floatValue = 9.1
        stringValue = "hello, world"
        
        print("type of maxInt", type(maxInt), "value: ", maxInt)
        print("type of longStart", type(longStart), "value: ", longStart)
        print("type of floatValue", type(floatValue), "value: ", floatValue)
        print("type of stringValue", type(stringValue), "value: ", stringValue)

if __name__ == "__main__":
    VariableType.main(sys.argv)