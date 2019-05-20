class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            index_of_target = 0
            for value in nums:
                if value < target:
                    continue
                else:
                    return nums.index(value)
            else:
                return len(nums)
