def sandwich_toppings(*toppings):
    for topping in toppings:
        print(f"- {topping}")

sandwich_toppings("meat","beef","sausage")
sandwich_toppings("pretts")
sandwich_toppings("tuna","sardine","eggs")