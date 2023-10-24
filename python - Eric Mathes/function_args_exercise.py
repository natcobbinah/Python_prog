def make_shirt(size = "L", text = "I love Python"):
    print(f"The size of this shirt is {size}")
    print(f"It has the message {text} on it")

make_shirt("M")
make_shirt()
make_shirt("S", "I love Python 3.7")

print()

def describe_city(name,country="France"):
    print(f"{name} is in {country}")

describe_city("Paris")
describe_city("Lyon")
describe_city("Amsterdam","Netherlands")