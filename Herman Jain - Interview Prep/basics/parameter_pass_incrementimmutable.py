def increment(newvar):
    newvar += 1

def main():
    var = 10
    print(f"Value before increment {var}")
    
    increment(var)
    print(f"Value after increment {var}")

main()