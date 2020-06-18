class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ret = []
        for i in nums:
            c = 0
            for j in nums:
                if i > j:
                    c += 1
            ret.append(c)
        return ret
