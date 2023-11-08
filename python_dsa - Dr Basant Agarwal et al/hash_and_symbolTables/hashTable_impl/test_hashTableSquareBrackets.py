from hash_table import HashTable

ht = HashTable()

ht["good"] = "eggs"
ht["better"] = "ham"
ht["best"] = "spam"
ht["ad"] = "do not"
ht["ga"] = "collide"

for key in ("good","better", "best","worst","ad","ga"):
    v = ht[key]
    print(v)

print(f"The number of elements is {ht.count}")