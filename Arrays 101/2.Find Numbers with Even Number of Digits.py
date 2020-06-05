class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_counter = 0
        for n in nums:
            digits = 0
            while n != 0:
                n = n // 10
                digits += 1
            if digits % 2 == 0:
                even_counter += 1
        return even_counter
