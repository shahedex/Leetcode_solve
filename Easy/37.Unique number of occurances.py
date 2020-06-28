from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        u = dict(Counter(arr))
        if len(u) == len(set(u.values())):
            return True
        return False
