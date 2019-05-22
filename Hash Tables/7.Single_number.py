class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        number_count = collections.Counter(nums)
        number = [num for num in number_count if number_count[num] == 1][0]
        return number
