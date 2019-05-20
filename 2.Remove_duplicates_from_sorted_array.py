class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        noduplicate = list(set(nums))
        
        for i in range(len(noduplicate)):
            nums[i] = noduplicate[i]
        
        while(len(nums) != len(noduplicate)):
            del nums[len(noduplicate)]
        
        nums.sort()
        return len(nums)
