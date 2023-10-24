class VariableType(object):

    @classmethod
    def main(cls,args):
        maxInt = sys.maxsize

        print(f"type of maxint {type(maxInt)} {maxInt}")

if __name__ == '__main__':
    import sys
    VariableType.main(sys.argv)
