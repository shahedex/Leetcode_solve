import random

class Solution:
    def __init__(self, w: List[int]):
        self.vals = []
        self.sums = 0
        for n in w:
            self.sums += n
            self.vals.append(self.sums)
            
    def pickIndex(self) -> int:
        rand = random.randint(1, self.sums)
        return self.find_rand(rand)

    def find_rand(self, rand) -> int:
        lo = 0
        hi = len(self.vals) - 1
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self.vals[mid] < rand:
                lo = mid + 1
            else:
                hi = mid
        return lo
    
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()