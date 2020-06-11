class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lo = c = 0
        hi = len(nums) - 1
        
        while lo <= hi:
            if nums[lo] == 0:
                nums[lo], nums[c] = nums[c], nums[lo]
                lo += 1
                c += 1
            elif nums[lo] == 2:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                hi -= 1
            else:
                lo += 1


        
#         c = 0
#         for i in range(2):
#             for j in range(c, len(nums)):
#                 if nums[j] == i:
#                     nums[c], nums[j] = nums[j], nums[c]
#                     c += 1
