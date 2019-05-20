class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        sorted_non_decreasing_order_array = [i*i for i in A]
        return sorted(sorted_non_decreasing_order_array)
