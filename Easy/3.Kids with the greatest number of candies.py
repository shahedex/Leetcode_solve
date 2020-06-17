class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ret = []
        m = max(candies)
        for i in candies:
            ret.append(True if i+extraCandies >= m else False)
        return ret
