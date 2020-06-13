from random import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ds = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.ds:
            return False
        self.ds[val] = 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.ds:
            return False
        del self.ds[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        pix = int(random() * len(self.ds))
        lst = list(self.ds.keys())
        return lst[pix]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()