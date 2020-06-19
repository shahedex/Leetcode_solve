class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ret = []
        i = 0
        while i+1 < len(nums):
            ret += [nums[i+1]]*nums[i]
            i += 2
        return ret
