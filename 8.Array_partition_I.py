class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum_of_pairs = 0
        for i in range(len(nums)):
            if i%2 == 0:
                sum_of_pairs += nums[i]
        return sum_of_pairs
