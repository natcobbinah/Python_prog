sandwich_orders = ['Chicken Sandwich', 'Egg Sandwich', 'Seafood Sandwich',
                   'pastrami', 'pastrami','pastrami']

print(f"Deli has run out of pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)