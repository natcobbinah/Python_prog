def towersOfHanoi(n, fOf1, fNminus1, fN):
    if n == 1:
        print("Move disk 1 from rod", fOf1, "to rod", fNminus1)
        return
    towersOfHanoi(n-1, fOf1, fN, fNminus1)
    print("Move disk", n, "from rod", fOf1, "to rod", fNminus1)
    towersOfHanoi(n-1, fN, fNminus1, fOf1)


towersOfHanoi(4, 'A', 'C', 'B')
