class HashTable:
    def __init__(self, size=10) -> None:
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hash_index = self._hash(key)

        for pair in self.table[hash_index]:
            if pair[0] == key:
                pair[1] = value
                return
        
        self.table[hash_index].append([key, value])
    
    def remove(self, key):
        hash_index = self._hash(key)
        for i, pair in enumerate(self.table[hash_index]):
            if pair[0] == key:
                del self.table[hash_index][i]
                return
        raise KeyError(f"key {key} not found")
    
    def search(self, key):
        hash_index = self._hash(key)
        for pair in self.table[hash_index]:
            if pair[0] == key:
                return pair[1]
        raise KeyError(f"key {key} not found")
    
    def __str__(self) -> str:
        return str(self.table)
    
ht = HashTable()

# 삽입
ht.insert("apple", 1)
ht.insert("banana", 2)
ht.insert("orange", 3)

# 검색
print("apple:", ht.search("apple"))  # 출력: 1
print("banana:", ht.search("banana"))  # 출력: 2

# 업데이트
ht.insert("apple", 10)
print("updated apple:", ht.search("apple"))  # 출력: 10

# 삭제
ht.remove("banana")
# ht.search("banana")  # KeyError 발생

# 해시 테이블 출력
print(ht)