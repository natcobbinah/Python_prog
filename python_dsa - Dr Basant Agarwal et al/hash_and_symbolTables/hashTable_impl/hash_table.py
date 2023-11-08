from hash_item import HashItem

class HashTable:

    def __init__(self):
        self.size  = 256
        self.slots = [None for i in range(self.size)]
        self.count = 0

    #the assumption is key are strings for now
    def _hash(self,key):
        mult = 1
        hv = 0
        for ch in key:
            hv += mult * ord(ch)
            mult += 1
        return hv % self.size
    
    def put(self, key, value):
        item = HashItem(key,value)
        h = self._hash(key)

        while self.slots[h] is not None:
            if self.slots[h] == key:
                break 
            h = (h + 1) % self.size
        
        if self.slots[h] is None: 
            self.count += 1
        self.slots[h] = item

    def get(self, key):
        h = self._hash(key) #computer hash for the given key
        while self.slots[h] is not None:
            if self.slots[h].key == key:
                return self.slots[h].value
            h = (h + 1) % self.size 
        return None

    # using [] with the hashTable
    def __setitem__(self,key,value):
        self.put(key,value)
    
    def __getitem__(self,key):
        return self.get(key)

