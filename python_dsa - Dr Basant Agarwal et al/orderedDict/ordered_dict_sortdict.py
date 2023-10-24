from collections import OrderedDict

odt = OrderedDict([('one',1),('two',2),('three',3),('four',4),('five',5)])

odt_sorted = sorted(odt.items(), key = lambda t: (t[1]))
print(odt_sorted)