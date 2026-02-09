class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key)%self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        # If key exists in the bucket, update its value
        for i, (k, _) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        # Otherwise append the new key-value pair
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        # Search the bucket for the key; return value if found
        for k, v in self.table[index]:
            if k == key:
                return v
        # Not found
        return None
        

def test():
    h = HashTable()
    h.insert("Apple", 10)
    h.insert("Banana", 20)
    h.insert("Grape", 30)
    print("Value for 'Banana' : ", h.get("Banana"))
if __name__ == '__main__':
    test()