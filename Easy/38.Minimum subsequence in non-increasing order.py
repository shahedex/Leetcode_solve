class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        nums.sort(reverse=True)
        ret = nums
        for i in range(len(nums)):
            if sum(nums[:i]) > sum(nums[i:]):
                return nums[:i]
        return ret
