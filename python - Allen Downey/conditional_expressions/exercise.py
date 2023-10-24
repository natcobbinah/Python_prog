def binomial_coeff(n,k):
    if k == 0:
        return 1
    if n == 0:
        return 0
    
    res = binomial_coeff(n - 1,k) + binomial_coeff(n - 1, k - 1)
    return res

def binomial_coeff2(n,k):
    return 1 if k == 0 else 0 if n == 0 else  binomial_coeff(n - 1,k) + binomial_coeff(n - 1, k - 1)

print(binomial_coeff(5,2))
print(binomial_coeff2(5,2))