def increment(cls,newvar):
    newvar += 1

def main(cls,args):
    var = 10
    print(f"var {var}")
    cls.increment(var)
    print(f"var after increment {var}")

