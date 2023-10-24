sandwich_orders = ['Chicken Sandwich', 'Egg Sandwich', 'Seafood Sandwich']
finished_sandwiches = []

while sandwich_orders:
    available_sandwich = sandwich_orders.pop()

    print(f"I made your {available_sandwich}")
    finished_sandwiches.append(available_sandwich)

for sandwich in finished_sandwiches:
    print(f"This {sandwich} order has been completed")

