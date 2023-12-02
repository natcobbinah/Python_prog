def basic_small_change(denom, total_amount):
    sorted_denominations = sorted(denom, reverse=True)

    number_of_denoms = []

    for i in sorted_denominations:
        div = total_amount // i 
        total_amount = total_amount % i 
        if div > 0:
            number_of_denoms.append((i,div))
    
    return number_of_denoms

currencies = [1,5,8]
total_amt = 12
print(basic_small_change(currencies,total_amt))