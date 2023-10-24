age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")

# else is not required, so the above could be written as this
age2 = 12

if age2 < 4:
    price2 = 0
elif age2 < 18:
    price2 = 25
elif age2 < 65:
    price2 = 40
elif age2 >= 65:
    price = 20

print(f"Your admission cost is ${price}.")
