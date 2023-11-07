from hash_table import HashTable

ht = HashTable()
ht.put("good","eggs")
ht.put("better","ham")
ht.put("best","spam")
ht.put("ad", "do not")
ht.put("ga", "collide")

for key in ("good","better","best","worst","ad","ga"):
    v = ht.get(key)
    print(v)
