import math
x = 7

if x > 0:
    y = math.log(x)
else:
    y = float('nan')

print(y)

# written using conditional-expression
y1 = math.log(x) if x > 0 else float('nan')
print(y1)