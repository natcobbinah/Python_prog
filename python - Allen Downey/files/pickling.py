import pickle
# a limitation of (dbm) is that the (keys and values) have to be 
# (strings or bytes). If you try to use any other type, you get an error

# It translates almost any type of object into a string suitable for 
# storage in a database, and then translates string back into objects

# pickle.dumps takes an object and returns a string
# pickle.loads takes a string and returns the object

t1 = [1,2,3]
s =  pickle.dumps(t1)
t2 = pickle.loads(s)
print(f"string format {s}")
print(f"reversed string to object format {t2}")