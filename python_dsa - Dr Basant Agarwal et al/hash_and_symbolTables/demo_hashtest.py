hash_str1 = sum(map(ord, 'hello world'))
print(f"ordinal of hello world =  {hash_str1}") # 1116

hash_str2 = sum(map(ord, 'world hello')) 
print(f"ordinal of world hello =  {hash_str2}") # 1116

hash_str3 = sum(map(ord, 'gello xorld')) #1116
print(f"ordinal of gello xorld =  {hash_str3}") # 1116

# In the above strings, summing up the ordinal value of the 
# characters produces the same results and thus, there'll
# be collisions if used as a hashing fxn

print("\nTesting out hash fxn\n")

#Let's try and multiply each value by an increasing numeric
#constant 
def myhash(s):
    mult = 1
    hv = 0
    for ch in s:
        hv += mult * ord(ch)
        mult += 1
    return hv

print(f"ordinal of hello world =  {myhash('hello world')}") #6736
print(f"ordinal of world hello =  {myhash('world hello')}") #6616
print(f"ordinal of gello xorld =  {myhash('gello xorld')}") #6742

# seems to work fine,but testing out the ff,result in the same hash value
print(f"ordinal of ad = {myhash('ad')}") # 297
print(f"ordinal of ga = {myhash('ga')}") # 297