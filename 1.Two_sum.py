class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_length = len(nums)
        for i in range(nums_length):
            for j in range(i+1,nums_length):
                if((nums[i] + nums[j]) == target):
                    return list([i,j])
