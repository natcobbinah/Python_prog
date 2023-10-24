from collections import ChainMap

dict1 = {'a':1, 'b':2, 'c':3}
dict2 = {'d':4,'e':5}

chain_map = ChainMap(dict1,dict2) # linking two dictionaries
print(chain_map)
print(chain_map.maps)
print(chain_map.values)

print()
print(chain_map['b']) #accessing values
print(chain_map['e'])