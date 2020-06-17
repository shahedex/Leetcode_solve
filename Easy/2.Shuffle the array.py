class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        out = []
        lo = 0
        hi = n
        for i in range(n):
            out.append(nums[lo])
            out.append(nums[hi])
            lo += 1
            hi += 1
        return out
