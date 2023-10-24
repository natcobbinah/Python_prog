from collections import OrderedDict

od1 = OrderedDict([('one',1),('two',2),('three',3)])

new_kvPairs = [('three',3),('four',4),('five',5)]
od1.update(new_kvPairs)

print(od1)

print()
for k,v in od1.items():
    print(k,v)