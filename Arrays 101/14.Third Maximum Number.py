class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        maxx = nums[0]
        counter = 1
        for i in range(1, len(nums)):
            if maxx > nums[i]:
                maxx = nums[i]
                counter += 1
            if counter == 3:
                break
        if counter < 3:
            return nums[0]
        else:
            return maxx
