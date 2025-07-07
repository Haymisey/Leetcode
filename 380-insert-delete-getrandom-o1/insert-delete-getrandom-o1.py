class RandomizedSet:

    def __init__(self):
        self.data=[]
        self.map={}

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val]=len(self.data)
        self.data.append(val)
        return True
    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        index=self.map[val]
        last_val=self.data[-1]

        self.data[index]=last_val
        self.map[last_val]=index

        self.data.pop()
        del self.map[val]    
        return True                
    def getRandom(self) -> int:
        x=random.randint(0,len(self.data)-1)
        return self.data[x]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()