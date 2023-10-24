# instead of using x/y and then x%y to have quotient and remainder
# the divmod fxn returns a tuple of both quotient and remainder eg:
t = divmod(7,3)
print(t)

# or tuple assignment can be used to store each value separately
quot, rem = divmod(3,5)
print(f"quotient = {quot} remainder = {rem}")

# A fxn normally returns a single result, but it can be made
# to return a tuple
def min_max(*t):
    return min(t), max(t)

min, max = min_max(9,2)
print(f"min = {min} max = {max}")

def sumall(*args):
    return sum(args)

print(f"Sum = {sumall(1,2,3)}")