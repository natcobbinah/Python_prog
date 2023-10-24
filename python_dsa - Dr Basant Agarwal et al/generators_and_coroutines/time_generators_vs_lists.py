#compare the running time of a list compared to a generator
import time

# generator function creates an iterator of odd numbers between n and m
def oddGen(n,m):
    while n < m:
        yield n
        n += 2

# build a list of odd numbers between n and m
def oddLst(n,m):
    lst = []
    while n < m:
        lst.append(n)
        n += 2
    return lst

t1 = time.time()
sum(oddLst(1,1000000))
print(f"Time to sum a list: {(time.time() - t1)}")


t1 = time.time()
sum(oddGen(1,1000000))
print(f"Time to sum an iterator: {(time.time() - t1)}")

