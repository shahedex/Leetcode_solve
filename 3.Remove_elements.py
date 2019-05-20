class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while(val in nums):
            index_of_val = nums.index(val)
            del nums[index_of_val]
            
        return len(nums)
