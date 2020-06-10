class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)-1
        if nums[hi] < target:
            return hi + 1
        while lo < hi:
            mid = lo + (hi-lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo
