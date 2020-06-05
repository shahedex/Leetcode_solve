class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        else:
            for i in range(len(nums)-1):
                if nums[i+1] != nums[i]:
                    nums[j] = nums[i]
                    j += 1
            nums[j] = nums[len(nums)-1]
            while len(nums) != j+1:
                nums.pop()
