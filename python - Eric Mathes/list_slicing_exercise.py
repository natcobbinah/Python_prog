names = ['Alice','Hugo','Bruno', 'Marc', 'Paulsen', 'Peter']
print(f"The first three items in the list are {names[0:3]}")
print(f"Three items from the middle of the list are {names[2:5]}")
print(f"The last three items in the list are {names[-3:]}")

# print last three items in names using for loop
for name in names[-3:]:
    print(name)

print("------------------------")
my_pizza = ["Verroni", "Chili", "Broily", "Chicken"]
friend_pizzas =  my_pizza[:]

my_pizza.append("Sausages")
friend_pizzas.append("Rabbit")

print(f"My favorite pizzas are {my_pizza}")
print(f"My friends favorite pizzas are {friend_pizzas}")