常数时间插入、删除和获取随机元素
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = set()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        len1 = len(self.s)
        self.s.add(val)
        if len1 == len(self.s):
            return False
        else:
            return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        try:
            self.s.remove(val)
            return True
        except:
            return False
            

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        import random
        return random.choice(list(self.s))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
