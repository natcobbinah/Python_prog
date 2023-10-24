prompt = "Enter your age to determine your ticket price: "

active = True
while active:
    age = input(prompt)
    age = int(age)

    if age < 3:
        print("Ticket is free")
    elif age <= 12:
        print("Ticket cost is $10")
    elif age > 12:
        print("Ticket is $15")
    
    active = False