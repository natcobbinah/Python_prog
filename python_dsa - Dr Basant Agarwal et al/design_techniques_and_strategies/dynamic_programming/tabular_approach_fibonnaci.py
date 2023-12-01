
def fib(n):
    results = [1,1]

    for i in range(2,n):
        results.append(results[i-1] + results[i-2])
    return results[-1] #latest computed result


print(fib(20))