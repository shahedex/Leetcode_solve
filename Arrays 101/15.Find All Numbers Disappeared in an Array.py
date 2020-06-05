class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ret = []
        for i in range(len(nums)):
            x = abs(nums[i]) - 1
            nums[x] = abs(nums[x]) * -1
        for i in range(len(nums)):
            if nums[i] > 0:
                ret.append(i+1)
        return ret
