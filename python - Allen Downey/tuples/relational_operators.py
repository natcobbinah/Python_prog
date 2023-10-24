# relational operators work on tuples by comparing each first element
# in the corresponding tuple, and increments the index for the others as well
# eg
tuple1 = (0,1,4)
tuple2 = (0,3,4)
print(tuple1 < tuple2) 
# if an element in one is less than the other being compared,
# other comparisons are terminated and the result is returned

tuple3 = (0,1,2000000)
tuple4 = (0,3,4)
print(tuple3 < tuple4)