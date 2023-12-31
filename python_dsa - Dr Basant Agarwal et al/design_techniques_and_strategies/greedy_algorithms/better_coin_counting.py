def optimal_small_change(denom, total_amount):
    sorted_denominations = sorted(denom, reverse=True)

    series = []
    for j in range(len(sorted_denominations)):
        term = sorted_denominations[j:]

        number_of_denoms = []
        local_total = total_amount
        for i in term:
            div = local_total // i 
            local_total = local_total % i 
            if div > 0:
                number_of_denoms.append((i,div))
        series.append(number_of_denoms)

    return series

coins = [8,5,1]
coin_total = 12
print(optimal_small_change(coins,coin_total))