class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        k=0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k],nums[i] = nums[i],nums[k]
                k += 1

#===================================                
#         le = len(nums)
#         for i in range(le-1, -1, -1):
#             if nums[i] == 0:
#                 for j in range(i, le):
#                     if j+1 == le:
#                         nums[j] = 0
#                     else:
#                         nums[j] = nums[j+1]
        
#===================================
# zero_count = nums.count(0)
# for i in range(zero_count):
#     zero_index = nums.index(0)
#     nums.pop(zero_index)
#     nums.append(0)
