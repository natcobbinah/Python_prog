prompt = "Enter your desired pizza toppings: "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(f"{message} will be added  to topping of your pizza")