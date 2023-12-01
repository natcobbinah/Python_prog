def factorial(n):
    results = [1,1]

    for i in range(2,n):
        results.append(results[i-1] * i)
        print(results)
    return results[-1] * n #latest computed value

print(factorial(5))
