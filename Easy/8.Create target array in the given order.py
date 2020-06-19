class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ret = []
        for i,j in zip(index,nums):
            ret.insert(i, j)
        return ret
