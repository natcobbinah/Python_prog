from collections import OrderedDict

od1 = OrderedDict([('one',1), ('two',2)])
print(od1)

od2 = OrderedDict([('two',2), ('one',1)])
print(od2)

#comparision btwn orderedDict uses keys as well as ordered of insertion
print(od1 == od2) # False