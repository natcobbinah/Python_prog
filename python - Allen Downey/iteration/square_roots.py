#y = (x + a/x)/2
def newtons_square_roots(x,a):
    epsilon = 0.0000001
    while True:
        print(x)
        y = (x + a /x) / 2
        if abs(y - x) < epsilon:
            break
        x = y

newtons_square_roots(3,4)