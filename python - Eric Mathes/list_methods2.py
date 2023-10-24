motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

# del  to remove an element from a list, but the value can not be used
del motorcycles[0]
print(motorcycles)

# pop() method to remove an element from the list and use it#
motorcycles2 = ['harley davidson','bel-air', 'ganji']
print(motorcycles2)

popped_motorcycle = motorcycles2.pop()
print(motorcycles2)
print(popped_motorcycle)

# popping from a specific position
first_owned = motorcycles2.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}")
print(motorcycles2)

# removing by value
motorcycles3 = ["Kawasaki", "Aprilia", "Cagiva","Benelli", "Keeway"]
print(motorcycles3)
motorcycles3.remove("Kawasaki")
print(motorcycles3)

too_expensive = "Cagiva"
motorcycles3.remove(too_expensive)
print(motorcycles3)
print(f"\nA {too_expensive.title()} is too expensive for me")