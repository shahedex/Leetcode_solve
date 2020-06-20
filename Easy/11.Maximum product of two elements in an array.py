class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxed = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                check = (nums[i]-1)*(nums[j]-1)
                if check > maxed:
                    maxed = check
        return maxed
